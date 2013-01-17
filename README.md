MWSL Project Evaluation
========================

Introduction
=============

Notes and Exercises for Project Evaluation Subject coursed in [Master on Libre Software (Master Universitario en Software libre](http://master.libresoft.es/) at [Universidad Rey juan Carlos](http://www.urjc.es/).

Requirements
=============

* LaTeX: to compile source code documentation files.

Documents Index
================

Main directory contains notes and exercises from the subject:

* 000-queries.txt: ``Queries for generated database using CVSAnaly.``
* 001-floss-projects-evaluation.tex: ``Describe 5 Mail client requirements``
* 001-metrics-analysis.tex: ``Source Code Management`` first metrics analysis and datasources.
* 002-floss-projects-evaluation.tex: ``Introduction to Quality in Libre Software``: Qualos and OpenBRR.
* 003-qualoss.tex: ``QuaLOSS; Quality of Libre Open Source Software``
* final_model.txt: ``Final model metrics values``.

Main directory
```
├── bbdd/
├── bbdd-pedro/
├── libcvsanalypatch/
├── final_report/
├── 000-queries.txt
├── 001-floss-projects-evaluation.tex
├── 001-metrics-analysis.tex
├── 002-floss-projects-evaluation.tex
├── 003-qualoss.tex
├── final_model.txt
├── mswl-project-evaluation.tex
├── README.md
└── scm-metrics.ods
```


Final Report
-------------

The most important file is 001-metrics-scm-svn.tex, final report: analysis bewteen tree scm; svn, git and cvs. Must read :) after compiling using LaTeX, of course.

*final_report* directory contains final report resources, documents and presentation:

* 001-metrics-scm-svn.tex: Metric analysis for choose VCS between SVN, Git and CVS.
* 001-beamer-metrics-scm-svn.tex: Presentation for the first part of the analysis, focused on SVN.
* scm-metrics.sxc: SXC file with all information related to SVN, Git and CVS based on created metrics to analyse these VCS.
* metrics_results: Metrics Documents from other CVS: CVS and Git.
* libcsvanaly2: charts and data generated with libcsvanaly2 tool. You can find, graphs, scripts from SCM analysis about; committers, commits, file actions and comparisons between the result score.
* images: Images used for final report and beamer.
* libcsvanaly2: Graphs rendered using libcvsanaly2.
* metrics_results: ods files form git and cvs analysis where is scm-metrics.sxc file. In this file you can see all raw results about scm analysis between SVN, Git and CVS.

Directory structure.
```
final_report/
├── images/
├── libcsvanaly2/
├── metrics_results/
├── 001-beamer-metrics-scm-svn.tex
├── 001-metrics-scm-svn.tex
├── 002-todo-final-report.rst
├── barplot_svn_2000.jpg
├── barplot_svn.jpg
├── metrics-scm-svn.lyx
├── scm_commiters.py
├── scm-metrics.ods
├── scm-metrics.sxc
├── scm_svn.R
└── Verzani-SimpleR.pdf
```

Libcvsanaly2 patches
---------------------

In this directory I have patches to run scripts from [libcvsanaly2 tool](http://git.libresoft.es/libcvsanaly2) using [CVSAnaly Data](https://github.com/MetricsGrimoire/CVSAnalY) from source code management tools (VCS) to extract data from commits.
```
libcvsanalypatch/
├── libcvsanaly2_color_scheme.patch
├── libcvsanaly2_fm3.patch
└── libcvsanaly2-full.patch
```

Apply *libcvsanaly2-full.patch* to project and run the scripts with database parameters. Sample to run generations script:

    python generations.py --db-output-user root --db-output-password admin --db-output-hostname localhost --db-output-database scm_svn_complete --db-driver mysql --db-user root --db-password admin --db-hostname localhost --db-database scm_svn_complete --db-driver mysql

License
========

<a href="http://creativecommons.org/licenses/by/3.0/" rel="Creative Commons Attribution 3.0">![Foo](http://i.creativecommons.org/l/by/3.0/88x31.png)</a>

This work is licensed under a [Creative Commons Attribution 3.0 Unported License](http://creativecommons.org/licenses/by/3.0/).

