These scripts are used to generate the JSON files from the GDELT data required by the
d3 visualization.

Run the below Python scripts in the given order. Skip any as desired (if file already generated)

1_extractlinks.py 
pings the GDELT database and extracts and temporarily save the .csv files containing event data for 2015.
These are parsed to generate .tsv files

2_generate2015json.py
generates 2015.json which contains all required events with required attributes for 2015

3_normalize2015json.py
generates 2015normalized.json which contains 1 Actor name instead of below shown variations

4_create_alldaysjson.py
generates alldays.json which contains overall data for year 2015. 
this json is used by the first visualization

5_createtime_interm.py
generates intermediate file for timeline data -  contains events ordered by dates as keys

6_newscrape.py
generates urltitle.json which contains all title tags related the url per event to generate headlines
deadlinks and other errors give empty string as title

7_combineurl.py
modifies timeline_interm.json to include scraped headlines

8_generatetimelinejson.py
generates timeline.json to use in 2nd visualization. It contains event data grouped by date