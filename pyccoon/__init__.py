# -*- coding: utf-8 -*-

"""
![Pyccoon](pyccoon.svg)

"**Pyccoon**" is a side-to-side documentation generating system.

It descended from [Pyccoon](https://github.com/fitzgen/pyccoon) - a Python port of\
[Docco](http://jashkenas.github.com/docco/):\
the original quick-and-dirty, hundred-line-long, literate-programming-style\
documentation generator. It produces HTML that displays your comments\
alongside your code. Comments are passed through \
[Markdown](http://daringfireball.net/projects/markdown/syntax), while code is\
passed through [Pygments](http://pygments.org/) for syntax highlighting. \
[PyStache](https://github.com/defunkt/pystache) is used for page templating.

**This website is the result of running Pyccoon against its source.**

Pyccoon generates the documentation folder structured correspondingly to the code. To create \
documentation `docs` for the project in `src` folder, run the following:

    pyccoon -s src -d docs

[Pyccoon](https://github.com/ckald/pyccoon) is released on GitHub under the MIT license.
"""

__author__ = 'Andrii Magalich'
__email__ = 'andrew.magalich@gmail.com'
__version__ = '0.1.0'

from .pyccoon import Pyccoon
