var diameter = 600,
    radius = diameter / 2,
    innerRadius = radius - 90;

var cluster = d3.layout.cluster()
    .size([360, innerRadius])
    .sort(null)

var bundle = d3.layout.bundle();

var line = d3.svg.line.radial()
    .interpolate("bundle")
    .tension(.85)
    .radius(function(d) { return d.y; })
    .angle(function(d) { return d.x / 180 * Math.PI; });

var svgOverview = d3.select("#chart").append("svg")
    .attr("width", diameter)
    .attr("height", diameter)
    .append("g")
    .attr("transform", "translate(" + radius + "," + radius + ")");

var link = svgOverview.append("g").selectAll(".link"),
    node = svgOverview.append("g").selectAll(".node");

var data2,
    data3 = [],
    colorFlag = [],
    colorFlag2 = [],
    strokeFlag = [],
    titleList = [],
    participants = [],
    urlList = [];

//chart 2 variables
var clusterTimeline = d3.layout.cluster()
    .size([360, innerRadius])
    .sort(null)

var bundleTimeline = d3.layout.bundle();

var lineTimeline = d3.svg.line.radial()
    .interpolate("bundle")
    .tension(.85)
    .radius(function(d) { return d.y; })
    .angle(function(d) { return d.x / 180 * Math.PI; });

var svgTimelineChart = d3.select("#chart2").append("svg")
    .attr("width", diameter)
    .attr("height", diameter)
    .append("g")
    .attr("transform", "translate(" + radius + "," + radius + ")");

var linkTimeline = svgTimelineChart.append("g").selectAll(".link"),
    nodeTimeline = svgTimelineChart.append("g").selectAll(".node");

//adding the url links elements
var barHeight = 20;
var urlLinks = d3.select('#text').append('svg')
    .attr('width', 800)

//generate chart 1
d3.json("alldays2.json", function(error, classes) {
    if (error) throw error;

    data2 = generateData(classes);

    var nodes = cluster.nodes(packageHierarchy(data2)),
        links = packageImports(nodes);

    link = link
        .data(bundle(links))
        .enter().append("path")
        .each(function(d) {
            d.source = d[0], d.target = d[d.length - 1];
        })
        .attr("stroke-opacity", ".4")
        .attr("class", "link")
        .attr("stroke", function(d, i){
            if (colorFlag[i] == 1) return "#304FFE";
            return "#FF1744";
        })
        .attr("d", line)
        .attr('stroke-width', function(d, i){
            return strokeFlag[i] + 'px';
        })


    node = node
        .data(nodes.filter(function(n) { return !n.children; }))
        .enter().append("text")
        .attr("class", "node")
        .attr("dy", ".31em")
        .style('font-size', function(d, i){
            if (d.name === "Syria") {
                return '150%';
            }
        })
        .attr("transform", function(d) { return "rotate(" + (d.x - 90) + ")translate(" + (d.y + 8) + ",0)" + (d.x < 180 ? "" : "rotate(180)"); })
        .style("text-anchor", function(d) { return d.x < 180 ? "start" : "end"; })
        .text(function(d) {
            return d.name;
        })
        .on("mouseover", mouseovered)
        .on("mouseout", mouseouted);

    nodeTimeline = nodeTimeline
        .data(nodes.filter(function(n) { return !n.children; }))
        .enter().append("text")
        .attr("class", "node")
        .attr("dy", ".31em")
        .style()
        .style('font-size', function(d, i){
            if (d.name === "Syria") {
                return '150%';
            }
        })
        .attr("transform", function(d) { return "rotate(" + (d.x - 90) + ")translate(" + (d.y + 8) + ",0)" + (d.x < 180 ? "" : "rotate(180)"); })
        .style("text-anchor", function(d) { return d.x < 180 ? "start" : "end"; })
        .text(function(d) { return d.name; })
        //.on("mouseover", mouseovered)
        //.on("mouseout", mouseouted);
});

d3.select(self.frameElement).style("height", diameter + "px");

////***************************************************************************************************************
////*****************************************  Timeline Chart  ****************************************************
////***************************************************************************************************************

function generateTimelineGraph(key) {
    //get rid of all the link on the d3 chart

    d3.json("timeline2.json", function(error, dat) {
        if (error) throw error;
        svgTimelineChart.selectAll('.link').remove();

        console.log("generating links");

        var nodesTimeline = clusterTimeline.nodes(packageHierarchy(generateTimelineData(dat,key)));
        var linksTimeline = packageImports(nodesTimeline);

        console.log(data3);

        linkTimeline = linkTimeline
            .data(bundle(linksTimeline))
            .enter().append("path")
            .each(function(d) {
                d.source = d[0], d.target = d[d.length - 1];
            })
            .attr("stroke-opacity", ".4")
            .attr("class", "link")
            .attr("stroke", function(d, i){
                if (colorFlag2[i] > 0) return "#304FFE";
                return "#FF1744";
            })
            .attr("d", lineTimeline)
            .attr('stroke-width', function(d, i){
                return '2px';
            });

        //console.log("This is our data3")
        //console.log(data3);
        generateURL();


    });
}

//***************************************************************************************************************
//*****************************************      Slider      ****************************************************
//***************************************************************************************************************

formatDate = d3.time.format("%b %d");

// parameters
var margin = {
        top: 0,
        right: 50,
        bottom: 20,
        left: 50
    },
    width = 960 - margin.left - margin.right,
    height = 100 - margin.bottom - margin.top;


// scale function
var timeScale = d3.time.scale()
    .domain([new Date('2012-01-02'), new Date('2013-01-01')])
    .range([0, width])
    .clamp(true);


// initial value
var startValue = timeScale(new Date('2012-03-20'));
startingValue = new Date('2012-03-20');

// defines brush
var brush = d3.svg.brush()
    .x(timeScale)
    .extent([startingValue, startingValue])
    .on("brush", brushed)
    //.on('brushend', brushended)

var svg = d3.select("#slider").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    // classic transform to position g
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")")
    //append text

    svg.append('text')
        .attr("x", 400)
        .attr("y", 80)
        .style("fill", "white")
        .style("font-size", "12px")
        //.attr("dy", ".35em")
        .attr("text-anchor", "middle")
        .style("pointer-events", "none")
        .text('Dragging for too long may result in flashing lights');

svg.append("g")
    .attr("class", "x axis")
    // put in middle of screen
    .attr("transform", "translate(0," + height / 2 + ")")
    // inroduce axis
    .call(d3.svg.axis()
        .scale(timeScale)
        .orient("bottom")
        .tickFormat(function(d) {
            return formatDate(d);
        })
        .tickSize(0)
        .tickPadding(12)
        .tickValues([timeScale.domain()[0], timeScale.domain()[1]]))
    .select(".domain")
    .select(function() {
        //console.log(this);
        return this.parentNode.appendChild(this.cloneNode(true));
    })
    .attr("class", "halo");

var slider = svg.append("g")
    .attr("class", "slider")
    .call(brush);

slider.selectAll(".extent,.resize")
    .remove();

slider.select(".background")
    .attr("height", height);

var handle = slider.append("g")
    .attr("class", "handle")

handle.append("path")
    .attr("transform", "translate(0," + height / 2 + ")")
    .attr("d", "M 0 -20 V 20")

handle.append('text')
    .text(startingValue)
    .attr("transform", "translate(" + (-18) + " ," + (height / 2 - 25) + ")");

slider
    .call(brush.event)

//***************************************************************************************************************
//*****************************************      Links      *****************************************************
//***************************************************************************************************************

function generateURL(){
    //first remove all g elements
    urlLinks.selectAll('g').remove();
    urlLinks.attr('height', urlList.length * barHeight);

    //then add them
    var newLinks = urlLinks.selectAll("g")
        .data(urlList)
        .enter().append("g")
        .attr("transform", function(d, i) { return "translate(0," + i * barHeight + ")"; });

    newLinks.append('a')
        .attr("xlink:href", function(d){
            return d;
        })
        .append("rect")
        .attr("x", 2)
        .attr("y", 2)
        .attr("height", barHeight - 4)
        .attr("width", 800)
        .style("fill", "grey")

    newLinks.append("text")
        .attr("x", 400)
        .attr("y", 14)
        .style("fill", "white")
        .style("font-size", "12px")
        //.attr("dy", ".35em")
        .attr("text-anchor", "middle")
        .style("pointer-events", "none")
        .text(function(d, i){
            if (titleList[i] === ''){
                return participants[i] + ': ' + '<<LINK BROKEN>>'
            }
            return participants[i] + ': ' + titleList[i];
        });
}

//***************************************************************************************************************
//*****************************************      Legend      ****************************************************
//***************************************************************************************************************

var legend = d3.select("#legend").append("svg")
    .attr("width", 1200)
    .attr("height", 20)


var legend1 = legend.append('g')
    .attr('transform', 'translate(200,0)')

legend1
    .append("rect")
    .attr("x", 200)
    .attr("y", 0)
    .attr("height", 20)
    .attr("width", 200)
    .style("fill", "#FF1744")
    .style('opacity', 0.3)

legend1
    .append('text')
    .attr("x", 300)
    .attr("y", 14)
    .style("fill", "white")
    .style("font-size", "12px")
    //.attr("dy", ".35em")
    .attr("text-anchor", "middle")
    .style("pointer-events", "none")
    .text("negative relationships");

var legend2 = legend.append('g')
    .attr('transform', 'translate(200,0)')

legend2
    .append("rect")
    .attr("x", 400)
    .attr("y", 0)
    .attr("height", 20)
    .attr("width", 200)
    .style("fill", "#304FFE")
    .style('opacity', 0.3)


legend2
    .append('text')
    .attr("x", 500)
    .attr("y", 14)
    .style("fill", "white")
    .style("font-size", "12px")
    //.attr("dy", ".35em")
    .attr("text-anchor", "middle")
    .style("pointer-events", "none")
    .text("positive relationships");