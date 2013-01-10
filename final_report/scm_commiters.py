#!/usr/bin/env python

import sys
from storm.locals import *
from libcvsanaly2.Database import *
from libcvsanaly2.Graphs.PychaGraph import PychaGraph

# Create a DBOptionContext to parse database command line options
ctx = DBOptionContext ()
ctx.parse_options (sys.argv[1:])

# Create the database, it returns a storm object
db = ctx.create_database ()

# Create a store (database connection)
store = Store (db)

# Create an Horizontal Bar Graph using the pycha module
gfx = PychaGraph (PychaGraph.HORIZONTAL_BAR)

# Graphic look and feel
options = {
    'colorScheme': 'red',
    'background': {
        'chartColor': '#ffeeff',
        'baseColor': '#ffffff',
        'lineColor': '#444444'
    },
    'axis': {
        'x': {},
        'y': {
            'tickPrecision': 0
        }
    },
    'legend': {
        'hide': True
    },
    'padding': {
        'top': 20,
        'left': 70,
        'right': 20,
        'bottom': 20
    }
}

# The query to get the number of commits per committer
query = "select p.name, count(s.id) from scmlog s, people p " + \
        "where p.id = s.committer group by p.name order by 2 desc"

# Run the query, we use storm execute method in this case instead of Find
result = store.execute (query)
data = [item for item in result]

# Fill the structures needed by pycha to plot the graph
dataset = (("committers", [(i, l[1]) for i, l in enumerate (data)]),)
options['axis']['x']['ticks'] = [dict(v=i, label=d[0]) for i, d in enumerate (data)]
options['axis']['y']['ticksCount'] = len (dataset[0][1])
options['title'] = "Top committers"

# Render the graph into a png file of 500x400
gfx.render ("top-committers.png", 500, 400, dataset, options)
