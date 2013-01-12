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
import MySQLdb
import sys
import datetime as dt

def connect(database):
   user = 'root'
   password = 'admin'
   host = 'localhost'

   dbaux = database
   try:
      db =  MySQLdb.connect(host,user,password,dbaux)
      return db.cursor()
   except:
      print("Database connection error")


def get_dates_commits(dates_commits):

   dates = []
   commits = []
   total_commits = 0
   for date_commit in dates_commits:
      year = int(date_commit[0])
      month = int(date_commit[1])
      day = int(date_commit[2])

      num_commits = int(date_commit[3])
      dates.append(dt.date(year, month, day))
      commits.append(num_commits)
      total_commits = total_commits + num_commits


   return dates, commits, total_commits



def main(database):

   #Commits per committer limited to the 30 first with the highest accumulated activity
   query = "select year(date), month(date), day(date), count(*) from scmlog where year(date) = 2012 group by year(date), month(date), day(date)"

   #Connecting to the data base and retrieving data
   connector = connect(database)
   results = int(connector.execute(query))
   if results > 0:
      results_aux = connector.fetchall()
   else:
      print("Error when retrieving data")
      return

   dates, commits, total_commits = get_dates_commits(results_aux)


   #Creating the final boxplot
   fig = plt.figure()
   plt.title('Evolution of Commits')
   plt.plot(dates, commits)
   fig.autofmt_xdate()
   plt.savefig('basic_timeseries.png')


if __name__ == "__main__":main(sys.argv[1])


