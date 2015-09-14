'''
Created on Sep 14, 2015

@author: hugosenari
'''

# since this is not installed yet point to path where it is downloaded
import sys, os, inspect

def _example_path():
    sourcefile = inspect.getsourcefile(_example_path)
    abs_path = os.path.abspath(sourcefile)
    my_dir = os.path.dirname(abs_path)
    sys.path.append(my_dir + "/../")
    return my_dir
    
my_dir = _example_path()