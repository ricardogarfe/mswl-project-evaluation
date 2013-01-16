# Copyright(c) 2013 by Ricardo Garcia Fernandez <ricardogarfe@gmail.com>
#
# This file is part of SCMAnalay.
#
# PyCha is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyCha is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with PyCha.  If not, see <http://www.gnu.org/licenses/>.
import cairo
import pycha.bar
import pycha.line
import sys
import pycha.pie
import pycha.stackedbar

def optionsAndMetrics():

    metric_list = ('Initial Analysis', 'Functionality', 'Usability', 'Robustness', 'Development', 'Community', 'Documentation')

    options = {
        'legend': {'hide': False},
        'colorScheme': {
            'name': 'gradient',
            'args': {
                'initialColor': 'blue',
            },
        },
        'axis': {
            'x': {
                'ticks': [dict(v=i, label=l) for i, l in enumerate(metric_list)],
                'label': 'Metrics',
            },
            'y': {
                'tickCount': 4,
                'label': 'Score',
            }
        },
        'padding': {
            'top': 20,
            'left': 40,
            'right': 20,
            'bottom': 40
        }
    }

    return options

def renderMetricsWeight():

    lines = (
        ('Initial Analysis', 13),
        ('Functionality', 12),
        ('Usability', 14),
        ('Robustness', 17),
        ('Development', 15),
        ('Community', 19),
        ('Documentation', 10),
    )

    dataSet = [(line[0], [[0, line[1]]]) for line in lines]

    options = optionsAndMetrics()

    pieChart('metrics-piechart.png', dataSet, options)    


def renderWeightedGraph():

    scm_punctuation = (
      ('Subversion', [[0,4.06], [1,4.37], [2,4.67], [3,4.61], [4,4.47], [5,3.65], [6,4.4]]),
      ('Git', [[0,3.12], [1,4.7], [2,3.53], [3,4.73], [4,4.67], [5,4.1], [6,5]]),
      ('CVS', [[0,4.06], [1,3.81], [2,3.93], [3,3.03], [4,3.78], [5,1.96], [6,3.3]]),
    )

    scm_weigthed_punctuation = (
      ('Subversion', [[0,0.53], [1,0.52], [2,0.65], [3,0.78], [4,0.67], [5,0.69], [6,0.44]]),
      ('Git', [[0,0.41], [1,0.56], [2,0.49], [3,0.8], [4,0.7], [5,0.78], [6,0.5]]),
      ('CVS', [[0,0.53], [1,0.46], [2,0.55], [3,0.52], [4,0.57], [5,0.37], [6,0.33]]),
    )


    options = optionsAndMetrics()

    verticalChart('metrics-vertical-chart.png', scm_weigthed_punctuation, options)

def renderTotalsGraph():

    scm_over_100 = (
      ('Subversion', [[0,85.87]]),
      ('Git', [[0,84.95]]),
      ('CVS', [[0,66.4]]),
    )

    options = optionsAndMetrics()

    verticalChart('metrics-total-over100-chart.png', scm_over_100, options)


def lineChart(ouput, dataSet, options):

    width, height = (800, 400)
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)

    chart = pycha.line.LineChart(surface, options)

    chart.addDataset(scm_punctuation)
    chart.render()

    surface.write_to_png('metrics-line-chart.png')

def verticalChart(ouput, dataSet, options):

    width, height = (800, 400)
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)

    chart = pycha.bar.VerticalBarChart(surface, options)
    chart.addDataset(dataSet)
    chart.render()

    surface.write_to_png(ouput)

def stackedBarChart(ouput, dataSet, options):

    width, height = (800, 600)
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)

    chart = pycha.stackedbar.StackedVerticalBarChart(surface, options)

    chart.addDataset(dataSet)
    chart.render()

    surface.write_to_png('metrics-satcked-bar-chart.png')

def pieChart(output, dataSet, options):

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 800, 800)

    chart = pycha.pie.PieChart(surface, options)

    chart.addDataset(dataSet)
    chart.render()

    surface.write_to_png(output)

if __name__ == '__main__':

    if len(sys.argv) > 1:
        output = sys.argv[1]
    else:
        output = 'metrics-linechart.png'

    renderMetricsWeight()

