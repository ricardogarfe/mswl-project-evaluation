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
#this avoid the use of the $DISPLAY value for the charts
mpl.use('Agg')
import matplotlib.pyplot as plt



# make a square figure and axes
plt.figure(1, figsize=(6,6))
ax = plt.axes([0.1, 0.1, 0.8, 0.8])

labels = 'JavaScript', 'C/C++ Header', 'ActionScript', 'C++', 'C', 'Shell' 
fracs = [18.97, 14.21, 12.7, 47.69, 4.74, 1.96]

plt.pie(fracs, labels=labels, autopct='%1.1f%%', shadow=False)

plt.title('Number of Files')

plt.savefig("basic_piechart.eps")

