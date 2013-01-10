library(RMySQL)

con = dbConnect(MySQL(), user='root', pass='admin', dbname='scm_svn_complete')

results = dbGetQuery(con, "select l.committer_id, count(*) from scmlog l, people p where year(date) = 2012 and p.id = l.committer_id group by l.committer_id order by count(*) desc")

jpeg("barplot_svn_2000.jpg")

barplot(log(results[,2]), names.arg = as.character(results[,1]), col = "blue")

dev.off()

# Archivos más actualizados.
# select f.file_name, count(*) from actions l, files f where f.file_name like '%.%' and l.file_id=f.id group by l.file_id order by count(*) desc limit 10;

# Commits del año 2012 ordenados por meses
# select year(date), month(date), count(*) from scmlog where year(date) = 2012 group by year(date), month(date) order by year(date), month(date);

# Agrupados los commits por años:
# select year(date), month(date), count(*) from scmlog group by year(date), month(date) order by year(date), month(date)

# El commiter máximo:
# select l.committer_id, p.name, count(*) from scmlog l, people p where year(l.date) = 2012 and p.id = l.committer_id group by l.committer_id order by count(*) desc;

# select year(l.date), month(l.date), l.committer_id, p.name, count(*) from scmlog l, people p where year(l.date) = 2012 and p.id = l.committer_id group by l.committer_id order by count(*) desc;

# Lista de committers máximos dado un año ordenados por meses.
# select year(l.date), month(l.date), l.committer_id, p.name, count(*) from scmlog l, people p where year(l.date) = 2012 and p.id = l.committer_id group by year(l.date), month(l.date), l.committer_id order by year(l.date), month(l.date), count(*) desc;

# Committers per month and commits
# select committer_id, count(*) from scmlog where year(date) = 2012 and month(date) = 1 group by committer_id order by count(*) desc;

