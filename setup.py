
#!/usr/bin/env python

import versioneer
versioneer.versionfile_source = '%project%/_version.py'
versioneer.versionfile_build = '%project%/_version.py'
versioneer.tag_prefix = ''
versioneer.parentdir_prefix = '%project%-'
import os
import sys

#from setuptools import setup
from distutils.core import setup

name = ""
description='<short description>'
package_name = ""


setup(name=name,
			version=versioneer.get_version(),
			cmdclass=versioneer.get_cmdclass(),
			description=description,
			author='<author>',
			author_email='<mail>',
			url='<url>',
			license='LICENSE',
			long_description=open('README').read(),
			packages = [%project%],
			py_modules = ['versioneer'],
			scripts=[name]
			)
