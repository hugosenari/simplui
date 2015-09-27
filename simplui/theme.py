# ----------------------------------------------------------------------
# Copyright (c) 2009 Tristam MacDonald
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions 
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright 
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of DarkCoda nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------

from .ninepatch import NinePatch
from .icons import add_fontawesome, FONT_NAME
from .pyglet_utils import my_path
from pyglet.resource import Loader

try:
	import json
except ImportError:
	try:
		import simplejson as json
	except ImportError:
		import sys
		print('\nsimplui requires json support. upgrade to python 2.6 or install the simplejson module.\n')
		sys.exit(0)

		
class BaseTheme(dict):
	def __init__(self, arg, image):
		for k, v in arg.items():
			if isinstance(v, dict):
				temp = {}
				
				for k2, v2 in v.items():
					if k2.startswith('image'):
						temp[k2] = NinePatch( image.get_region(*v2) )
					else:
						temp[k2] = v2
				
				self[k] = temp
			else:
				self[k] = v

		self['image'] = image
		
		if FONT_NAME == self.get('icon', None):
			add_fontawesome() 


class Theme(BaseTheme):
	def __init__(self, path):
		loader = Loader(path=path)
		
		with open(path +'theme.json') as theme_file:
			info = json.loads( theme_file.read() )
			image = loader.texture( info['image'] )
			BaseTheme.__init__(self, info, image) 


def pywidget_theme():
	return Theme(my_path("pywidget"))

def macos_theme():
	return Theme(my_path("macos"))
