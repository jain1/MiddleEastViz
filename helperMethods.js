////***************************************************************************************************************
////**************************************  d3 Helper Methods  ****************************************************
////***************************************************************************************************************
/**
 * On mouse hover method for the nodes of the overview bundling diagram.
 *
 * Changes the font size of the node text, and changes the opacity of
 * all links attached to this node to 1, while reducing the opacity of
 * all other links to 0.16
 */
function mouseovered(){
    d3.select(this)
        .style("font-size", "120%")

    var entity = d3.select(this).text(); //text of the current node
    var hoverFlag = []
    for (var i = 0; i < data2.length; i++){
        if (data2[i].name === entity){
            for (var j = 0; j < data2[i].imports.length; j++) {
                hoverFlag.push(1);
            }
        }
        else{
            for (var j = 0; j < data2[i].imports.length; j++){
                if (data2[i].imports[j] == entity){
                    hoverFlag.push(1);
                }
                else {
                    hoverFlag.push(0);
                }
            }
        }
    }

    d3.selectAll('.link')
        .attr('stroke-opacity', function(d, i){
            if (hoverFlag[i] == 1) return "1";
            else return "0.16";
        })
}

/**
 * On mouse out method for the nodes of the overview bundling diagram.
 *
 * Changes the font size of the node text and opacity of all links to default.
 */
function mouseouted(){
    d3.select(this)
        .style("font-size", "80%")

    d3.selectAll('.link')
        .attr('stroke-opacity', "0.4")

}

////***************************************************************************************************************
////**************************************  Data Helper Methods  **************************************************
////***************************************************************************************************************

/**
 * Generates the data for the overview edge bundling diagram
 *
 *
 *
 *
 * @param {JSON} classes: The JSON read by d3 containing processed GDELT data
 * @param {Array} data2: Array in which to stored further processed data
 *
 * @return {Array} data2: Processed data successfully entered into array
 */
function generateData(classes, data2){

    data2 = []; //initialize the data2 array
    var names = []; //keeps track of all the organizations added to the array
    for (var i = 0; i < classes.length; i++){
        data2[i] = new Object();        //create an object

        //add the values to the object
        data2[i].name = classes[i]['name'];
        data2[i].imports = classes[i]['imports'];
        data2[i].values = classes[i]['values'];
        data2[i].eventCount = classes[i]['eventCount'];

        //check to see if the name just added exists
        if (names.indexOf(data2[i].name) < 0){
            names.push(data2[i].name);
        }
    }

    //add the neighbors that arent there but have relationships through the main entities
    for (var i = 0; i < data2.length; i++){
        var currNeighbors = data2[i].imports;
        for (var j = 0; j < currNeighbors.length; j++){
            if (names.indexOf(currNeighbors[j]) < 0){
                //console.log(currNeighbors[j] + " does not exists!")
                var newObj = new Object();
                newObj.name = currNeighbors[j];
                newObj.imports = [];
                newObj.values = [];
                newObj.eventCount = [];
                //console.log("our new object is: " + newObj);
                data2.push(newObj);

                //remember to add this to the names array
                names.push(currNeighbors[j])
            }
        }
    }

    //switch position of Syrian Oppn for aesthetic appeal
    var temp = data2[1]; // current position
    data2[1] = data2[23];
    data2[23] = temp;

    //generates flags to determine what color the link is
    for (var i = 0; i < data2.length; i++){
        for (var j = 0; j < data2[i].values.length; j++){
            if (data2[i].values[j] > 0) colorFlag.push(1);
            else colorFlag.push(-1);
        }
    }

    //generates flags to determine the stroke value of the links
    for (var i = 0; i < data2.length; i++){
        for (var j = 0; j < data2[i].values.length; j++){
            if (data2[i].eventCount[j] < 25) strokeFlag.push(2);
            else strokeFlag.push(Math.min(18, Number(data2[i].eventCount[j]) / 12));
        }
    }

    //creates an empty data3 array, later to be used by second edge bundling chart
    return data2;
}

/**
 * Generates the data for the timeline edge bundling diagram
 *
 * The GDELT data organized in dat is organized as a dictionary, the key is the
 * SQL date value. The key has already been generated and is used to pull the events
 * of interest for a particular day.
 *
 *
 *
 *
 * @param {JSON} dat: The JSON read by d3 containing processed GDELT data
 * @param {Array} key: the key to determine what day's data to use
 *
 * @return {Array} data3: Processed data successfully entered into array
 */
function generateTimelineData(dat, key){
    //clear out the existing data3 array
    for (var i = 0; i < data2.length; i++){
        data3[i] = new Object();
        data3[i].name = data2[i].name;
        data3[i].imports = [];
        data3[i].eventCount = [];
        data3[i].values = [];
        data3[i].headlines = [];
        data3[i].sourceURL = [];
        data3[i].participants = [];
    }

    for (var k = 0; k < data3.length; k++){
        data3[k].imports = [];
        data3[k].eventCount = [];
        data3[k].values = [];
        data3[k].sourceURL = [];
        data3[k].headlines = [];
        data3[k].participants = [];
    }

    if (dat[key] != undefined){
        var events = dat[key];

        for (var i = 0; i < events.length; i++){
            var protagonistIndex;
            for (var j = 0; j < data2.length; j++){
                if (events[i].name == data2[j].name){
                    protagonistIndex = j;
                    break;
                }
            }
            //add the values to the object
            data3[protagonistIndex].name = events[i]['name'];
            data3[protagonistIndex].imports = events[i]['imports'];
            data3[protagonistIndex].values = events[i]['values'];
            data3[protagonistIndex].eventCount = events[i]['eventCounts'];
            data3[protagonistIndex].headlines = events[i]['titlelists'];
            data3[protagonistIndex].sourceURL = events[i]['urllists'];
        }

        colorFlag2 = [],
        participants = [],
        titleList = [],
        urlList = [];

        //color flag
        for (var i = 0; i < data3.length; i++){
            for (var j = 0; j < data3[i].values.length; j++){
                if (data3[i].values[j] > 0) colorFlag2.push(1);
                else colorFlag2.push(-1);
            }
        }

        //urlList for all the links
        for (var i = 0; i < data3.length; i++){
            for (var j = 0; j < data3[i].headlines.length; j++){
                for (var k = 0; k < data3[i].headlines[j].length; k++){
                    urlList.push(data3[i].sourceURL[j][k]);
                    titleList.push(data3[i].headlines[j][k]);
                    participants.push(data3[i].name + " and " + data3[i].imports[j])
                }
            }
        }
    }
    return data3;
}

/**
 * Generates the nodes to be used by the edge bundling diagram.
 *
 * Original source: https://bl.ocks.org/mbostock/7607999
 *
 *
 *
 *
 * @param {Array} classes: Processed GDELT data needed to generate the nodes
 */
// Lazily construct the package hierarchy from class names.
function packageHierarchy(classes) {
    var map = {};

    function find(name, data) {
        var node = map[name], i;
        if (!node) {
            node = map[name] = data || {name: name, children: []};
            if (name.length) {
                node.parent = find(name.substring(0, i = name.lastIndexOf(".")));
                node.parent.children.push(node);
                node.key = name.substring(i + 1);
            }
        }
        return node;
    }

    classes.forEach(function(d) {
        find(d.name, d);
    });

    return map[""];
}

/**
 * Generates the links to be used by the edge bundling diagram.
 * Uses the output nodes of packageHierarchy. It creates a 'source' and
 * 'target' attribute for each node
 *
 * Original source: https://bl.ocks.org/mbostock/7607999
 *
 *
 *
 *
 * @param {Array} nodes: output from the packageHierarchy method
 * @return {Array} import: links for all the nodes
 */
// Return a list of imports for the given array of nodes.
function packageImports(nodes) {
    var map = {},
        imports = [];

    // Compute a map from name to node.
    nodes.forEach(function(d) {
        map[d.name] = d;
    });

    // For each import, construct a link from the source to target node.
    nodes.forEach(function(d) {
        if (d.imports) d.imports.forEach(function(i) {
            imports.push({source: map[d.name], target: map[i]});
        });
    });

    return imports;
}

////***************************************************************************************************************
////****************************************  Slider Methods  *****************************************************
////***************************************************************************************************************

/**
 * On brush function that triggers the formulation of timeline data
 *
 * When brushed is triggered, it indicates that the user has changed the position
 * of the timeline, hereby requesting a new date to view events of. This function
 * takes generates the date value and uses generateTimelineGraph() to generate the
 * timeline edge bundling diagram.
 */
function brushed() {
    var value = brush.extent()[0];

    if (d3.event.sourceEvent) { // not a programmatic event
        value = timeScale.invert(d3.mouse(this)[0]);
        brush.extent([value, value]);
    }

    handle.attr("transform", "translate(" + timeScale(value) + ",0)");
    handle.select('text').text(formatDate(value));

    //clear out everything
    d3.select("#text").select('svg').selectAll('g').remove();
    urlList = [];
    titleList = [];
    participants = [];

    generateTimelineGraph(getDateValue(value));
}

/**
 * Converts the date value into an integer that can be used to generate the SQL date
 *
 *
 *
 *
 * @param {date} value: date object for selected date
 * @return {number}: integer value to be used as the key
 */
function getDateValue(value){
    var dateTokens = value.toString().split(' ');
    var month = dateTokens[1],
        day = Number(dateTokens[2]);

    if (month == 'Jan'){
        month = 0;
    }
    else if (month == 'Feb'){
        month = 31
    }
    else if (month == 'Mar'){
        month = 59
    }
    else if (month == 'Apr'){
        month = 90
    }
    else if (month == 'May'){
        month = 120
    }
    else if (month == 'Jun'){
        month = 151
    }
    else if (month == 'Jul'){
        month = 181
    }
    else if (month == 'Aug'){
        month = 212
    }
    else if (month == 'Sep'){
        month = 243
    }
    else if (month == 'Oct'){
        month = 273
    }
    else if (month == 'Nov'){
        month = 304
    }
    else if (month == 'Dec'){
        month = 334
    }

    var newValue = month + day;
    //console.log(getDate(newValue));
    return getDate(newValue);
}

/**
 * Converts the integer date value into the SQL date String that can be used as a key
 *
 *
 *
 *
 * @param {number} sliderNumber: integer date value
 * @return {String}: SQL date String that can be used as a string to access JSON data
 */
function getDate (sliderNumber){
    if (sliderNumber > 334) {
        if (sliderNumber - 334 < 10) return '2015120' + (sliderNumber - 334);
        return '201512' + (sliderNumber - 334);
    }
    else if (sliderNumber > 304) {
        if (sliderNumber - 304 < 10) return '2015110' + (sliderNumber - 304);
        return '201511' + (sliderNumber - 304);
    }
    else if (sliderNumber > 273) {
        if (sliderNumber - 273 < 10) return '2015100' + (sliderNumber - 273);
        return '201510' + (sliderNumber - 273);
    }
    else if (sliderNumber > 243) {
        if (sliderNumber - 243 < 10) return '2015090' + (sliderNumber - 243);
        return '201509' + (sliderNumber - 243);
    }
    else if (sliderNumber > 212) {
        if (sliderNumber - 212 < 10) return '2015080' + (sliderNumber - 212);
        return '201508' + (sliderNumber - 212);
    }
    else if (sliderNumber > 181) {
        if (sliderNumber - 181 < 10) return '2015070' + (sliderNumber - 181);
        return '201507' + (sliderNumber - 181);
    }
    else if (sliderNumber > 151) {
        if (sliderNumber - 151 < 10) return '2015060' + (sliderNumber - 151);
        return '201506' + (sliderNumber - 151);
    }
    else if (sliderNumber > 120) {
        if (sliderNumber - 120 < 10) return '2015050' + (sliderNumber - 120);
        return '201505' + (sliderNumber - 120);
    }
    else if (sliderNumber > 90) {
        if (sliderNumber - 90 < 10) return '2015040' + (sliderNumber - 90);
        return '201504' + (sliderNumber - 90);
    }
    else if (sliderNumber > 59) {
        if (sliderNumber - 59 < 10) return '2015030' + (sliderNumber - 59);
        return '201503' + (sliderNumber - 59);
    }
    else if (sliderNumber > 31) {
        if (sliderNumber - 31 < 10) return '2015020' + (sliderNumber - 31);
        return '201502' + (sliderNumber - 31);
    }
    else {
        if (sliderNumber < 10) return '2015010' + (sliderNumber);
        return '201501' + sliderNumber;
    }
}