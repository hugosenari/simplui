#! /usr/bin/env python
from setuptools import setup, find_packages

setup(
	name = 'simplui',
	version = '1.0.4',
	author = 'Tristam MacDonald',
	author_email = 'swiftcoder@gmail.com',
	description = 'Light-weight GUI toolkit for pyglet',
	url = 'https://github.com/swiftcoder/simplui',
	platforms = ['all'],
	license = 'BSD',
	classifiers = [
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: BSD License',
		'Natural Language :: English',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 3',
		'Topic :: Scientific/Engineering :: Human Machine Interfaces',
		'Topic :: Software Development :: User Interfaces',
	],
	
	packages = find_packages(),
	package_dir={'simplui': 'simplui'},
	package_data={'simplui': ['themes/*/*']},
	install_requires = ['simplejson >= 2.0', 'pyglet >= 1.1']
)
