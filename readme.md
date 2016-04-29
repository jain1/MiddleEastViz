# Visualization for conflicts in the Middle East (Centering around Syria) 


## Project Description
The aim of the project is to visualization the relationship between countries
(all caps) and organization (lowercase) involved in primarily in the Syrian conflict.
We wanted to be able to encode the kind of relationship (positive or negative)
as well as the strength of the relationship between these organization and countries.

The relationships span the duration of the year 2015. This is the most recent
complete year for the civil war. The choice of this year was also to do with our
data being used. In order to generate the relationship, we used GDELT's event
database and filtered events that took place in Syria and involve either the
Syrian Governement or Syrian Opposition. We further filtered by the number of
sources for that events (essentially the number of newspaper organization that
reported on the event) to filter out the important events. 2015 was chosen
because many events contained a SOURCEURL where we could find an article covering
that event. However, for the year 2014 and earlier, most of these SOURCEURL's are
broken because the webpages have been taken down. 2015 also have some broken
SOURCEURL's but there is a much better functional percentage of them.

The visualization has 2 primary graphs. One of the graphs shows an overview, an
average, or the relationships between all the involved countries. The second graph
shows the events that took place for a given day (which can be chosen though a slider).
Along with the event being shown, we also see the actual headlines generated from the
SOURCEURL for those events in the Headlines section. These headlines are hyperlinked
to the actual SOURCEURL, allowing you to access the actual article.


## Reconstruction
Instructions to run visualization on local server:
1) Clone repository or, download repository as zip file and extract contents
2) On command line, navigate to the directory containing index.html
3) Run a local server and access contents from browser by entering the local server's address and port number
For eg.
To run Python server:

In Python 2 execute command:
```
python -m SimpleHTTPServer
```

In Python 3 execute command:
```
python3 -m http.server
```

This gives console output like:
```
Serving HTTP on 0.0.0.0 port 8000 ...
```

Open Browser and go to: **0.0.0.0:8000**


The visualization will automatically be loaded.
