## `data`
This directory houses all small (< 100 MB) data sets that are a result of individual experiments and/or simulations. Depending on the type of data collected, you may want to split them up based on file type. Data larger than 
100 MB can be stored using [Git LFS](https://git-lfs.github.com/), though I personally try to avoid saving large files under version control and have them 
redundantly backed up elsewhere.

If possible, data sets from individual experiments should be compiled in a long-form tidy format. This is important not only for your analysis, but for others who wish to reproduce your work. While you may have an intimate knowledge of your data and experimental structure, it may not be obvious to anyone else. It is much easier if you can combine the individual data sets into as few files as possible so only one or two files have to be read to perform the analysis and generate the figures. 

This is **not** a place to store all of your large (> 1000 MB) data files, such as images. For accessibility of these large data sets, there are myriad online data repositories such as [Zenodo](https://zenodo.org) which provide free storage and DOI generation. In addition, you should have all of your data backed up locally with redundancy.