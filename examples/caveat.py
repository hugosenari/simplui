'''
Created on Sep 14, 2015

@author: hugosenari
'''

# this solve problem that window blank after lost focus
# schedule an empty update function
# this forces the window to be refreshed regularly
from pyglet.clock import schedule
def update(dt):
    pass

schedule(update)