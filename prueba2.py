# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 15:17:42 2016

@author: BrunoCheLeonB
"""

from bokeh.plotting import figure, output_file, show

output_file("test.html")
plot = figure()
plot.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], line_width=2)
show(plot)














