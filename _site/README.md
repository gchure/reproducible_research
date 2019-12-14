# Reproducible Research Website Template
This repository is a bare-bones template website for publishing of your work as
an interactive website. It's tailored for easy inclusion of data files, plots,
and interactive figures. It is a heavily modified form of the Jekyll template
[Flexible Jekyll](https://artemsheludko.github.io/flexible-jekyll/) by
[`@artemsheludko`](https://github.com/artemsheludko). It is originally published
under the [GNU General Public License
v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html) and is distributed here
under the same license terms.

This repository is designed to be hosted as a website on GitHub using the
[GitHub Pages]() hosting service. This service is based on the Ruby framework
[Jekyll]() which is tailored for blog management. I've made several
modifications to the structure to be amenable for scientific publications. 

## How Do I Use This?
Full documentation of how to use this repository as either a standalone website
or as a branch in another repository can be found on the [GitHub Wiki page](https://github.com/gchure/reproducible_website/wiki)
for this repository. 

## Software requirements 
To deploy locally, you must have a [Ruby development environment]() installed as
well as [Jekyll](). You can install Jekyll via 

```
gem install jekyll bundler
```

Once you have Jekyll installed, you can install of the Ruby requirements for
this website by running the following in the command line from the template directory:

```
bundle install
```

The build and preview the website locally, execute the following:
```
bundle exec jekyll serve --watch
```

This will build the website and serve it up at the address:
[http://127.0.0.1:4000](http://127.0.0.1:4000).


## License
This template is a heavily modified version of [Flexible
Jekyll](https://artemsheludko.github.io/flexible-jekyll/) under a GNU General
Public License Version 3.0. This template is provided with the same license.
All writing, logo, and other creative works provided with this template are
issued with a [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).


```
Copyright (C) 2019  Griffin Chure 

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
```
