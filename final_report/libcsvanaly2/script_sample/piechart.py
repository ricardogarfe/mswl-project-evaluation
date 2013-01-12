# Copyright (C) 2007-2011  GSyC/LibreSoft, Universidad Rey Juan Carlos
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
# Authors:
#      Daniel Izquierdo Cortazar <dizquierdo@libresoft.es>


import matplotlib as mpl
from pylab import *

import matplotlib.pyplot as plt

# make a square figure and axes
figure(1, figsize=(10,10))
ax = axes([0.1, 0.1, 0.8, 0.8])

labels = 'Initial Analysis', 'Functionality', 'Usability', 'Robustness', 'Development', 'Community', 'Documentation' 
fracs = [13.00, 12.00, 14.00, 17.00, 15.00, 19.00, 10.00]
explode=(0.05, 0.05, 0.05, 0.1, 0.1, 0.1, 0)

pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)

title('Weight defined for each Category', bbox={'facecolor':'0.8', 'pad':5})

savefig("vcs-scm-weight-analysis-piechart.png")
