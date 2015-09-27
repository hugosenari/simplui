#! /usr/bin/env python

#insert projet at path
import sys
from  os import path
my_dir = path.dirname(path.abspath(__file__))
sys.path = [my_dir + "/../"] + sys.path
# import pyglet, as usual
from pyglet.window import Window
from pyglet.app import run

# import simplui
from simplui.theme import pywidget_theme
from simplui.frame import Frame
from simplui.label import Label

# create a basic pyglet window
window = Window(200, 50, caption='Hello Window')

# create a frame to contain our gui
frame = Frame(
	pywidget_theme(),
	children=[
		Label('Hello World', x=18, y=25)
	]
)

# in the on_draw event, we just call frame.draw()
@window.event
def on_draw():
	window.clear()
	frame.draw()

run()
