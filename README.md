# Git + GitHub As A Platform For Reproducible Research 
## Overview
This repository sets out the skeleton of an organizational structure used for scientific research. It loosely follows what I have used for several of my research projects and I hope it inspires you to conduct your research in an open, reproducible, and honest manner.

## Layout
a
The repository is split into 

### Directories
1. **`code`**:  Where all of the *executed* code lives. This includes pipelines, scripts, and figure files. 
    + **`processing`**: Any code used to *transform* the data into another type should live here. This can include everything from parsing of text data, image segmentation/filtering, or simulations.
    + **`analysis`**: Any code to to *draw conclusions* from an experiment or data set. This may include regression, dimensionality reduction, or calculation of various quantities.
    + **`exploratory`**: A sandbox where you keep a record of your different approaches to transformation, interpretation, cleaning, or generation of data.
    + **`figures`**: Any code used to generate figures for your finished work, presentations, or for any other use.
2. **`data`**: All raw data collected from your experiments as well as copies of the transformed data from your processing code. 
3. **`miscellaneous`**: Files that may not be code, but are important for reproducibility of your findings.
    + **`protocols`**: A well annotated and general description of your experiments. These protocols should be descriptive enough for someone to follow your experiments independently 
    + **`materials`**: Information regarding the materials used in your experiments or data generation. This could include manufacturer information, records of purity, and/or lot and catalog numbers.
    + **`software details`**: Information about your computational environment that are necessary for others to execute your code. This includes details about your operating system, software version and required packages.
5. **`tests`**: All test suites for your code. *Any custom code you've written should be thoroughly and adequately tested to make sure you know how it is working.*
6. **`software_module`**: Custom code you've written that is *not* executed directly, but is called from files in the `code` directory. If you've written your code in Python, for example, this can be the root folder for your custom software module or simply house a file with all of your functions. 
7. **`templates`**: Files that serve as blank templates that document the procedures taken for each experiment, simulation, or analysis routine. 


### Required Files

1. **`LICENSE`**: A legal protection of your work. *It is important to think deeply about the licensing of your work, and is not a decision to be made lightly. See [blah blah]() for more information about licensing and choosing the correct license for your project.*
2. **`README.md`**: A descriptive yet succinct description of your research project and information regarding the structure outlined below.

## A Pipeline for Reproducible Research 
1. 

# License
<p xmlns:dct="http://purl.org/dc/terms/">
<a rel="license" href="http://creativecommons.org/publicdomain/mark/1.0/">
<img src="http://i.creativecommons.org/p/mark/1.0/88x31.png"
     style="border-style: none;" alt="Public Domain Mark" />
</a>
<br />
This work (<span property="dct:title">A template for using git as a platform for reproducible scientific research</span>, by <a href="github.com/gchure/reproducible_research" rel="dct:creator"><span property="dct:title">Griffin Chure</span></a>), identified by <span resource="[_:publisher]" rel="dct:publisher"><span property="dct:title">Griffin Chure</span></span>, is free of known copyright restrictions.
</p>