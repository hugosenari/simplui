'''
Created on Sep 27, 2015

@author: hugosenari
'''
from .widget import Widget
from .container import Container
from pyglet.window import Window


import os

class FilePicker(Window):
    '''
    File Picker component
    '''
    
    def __init__(self, path, action=None, **kwargs):
        self.action = action
        self.file_list = FileList(path, **kwargs)

    def on_close(self):
        self.close()
        
        if self.action:
            self.action(self.file_list.files)


class FileList(Container):
    '''
    File list component
    '''
    
    def __init__(self, path, action=None, match='.+', mult=False, **kwargs):
        Container.__init__(self, **kwargs)
        self.action=None
        self.path = path
        self.filter = match
        self.files = []
        self.file_list = []
        self.mutiple=mult
        
        self.update_path(path)
        
        
    def on_select(self, file_widget):
        file_widget.on_select()
        if self.mutiple:
            self.files.append(file_widget.file)
        else:
            self.files[0] = file_widget.file
            for _file_widget in self.file_list:
                if _file_widget != file_widget: 
                    _file_widget.on_deselect()

        if self.action:
            self.action(file_widget.file)
            
    def on_deselect(self, file_widget):
        file_widget.on_deselect()
        self.file_list = [fw for fw in self.file_list if fw != file_widget]
        
        
    def update_path(self, path):
        abs_path = os.path.abspath(path)
        self.file_list = []
        for root, dirs, files in os.walk(abs_path, topdown=False):
            for name in dirs:
                file = Dir(os.path.join(root, name))
                self.file_list.append(file) 
            for name in files:
                file = StdFile(os.path.join(root, name))
                self.file_list.append(file)


class File(Widget):

    def __init__(self, file, action=None, **kwargs):
        Widget.__init__(self, **kwargs)
        self.file = file
        self.action = action

    def on_mouse_release(self, x, y, button, modifiers):
        Widget.on_mouse_release(self, x, y, button, modifiers)


class Dir(File):
    pass

class StdFile(File):
    pass
