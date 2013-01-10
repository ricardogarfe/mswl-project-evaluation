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


import numpy as np
import scipy as sp
import MySQLdb
import sys

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



def main(database):

   #Commits per committer limited to the 30 first with the highest accumulated activity
   query = "select count(*) from scmlog group by committer_id order by count(*) desc limit 40"

   #Connecting to the data base and retrieving data
   connector = connect(database)
   results = int(connector.execute(query))
   if results > 0:
      results_aux = connector.fetchall()
   else:
      print("Error when retrieving data")
      return

   #Moving data to a list
   commits = []
   for commit in results_aux[5:]:
#   for commits in results_aux:
      commits.append(int(commit[0]))

   #Calculating basic statistics
   print "max: " + str(sp.amax(commits))
   print "min: " + str(sp.amin(commits))
   print "mean: " + str(sp.mean(commits))
   print "median: " + str(sp.median(commits))
   print "std: " + str(sp.std(commits))
   print ".25 quartile: " + str(sp.percentile(commits, 25))
   print ".50 quartile: " + str(sp.percentile(commits, 50))
   print ".75 quartile: " + str(sp.percentile(commits, 75))
   

if __name__ == "__main__":main(sys.argv[1])


