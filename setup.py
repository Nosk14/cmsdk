#!/usr/bin/env python

from distutils.core import setup
from cmsdk import __version__

setup(name='cmsdk',
      version=__version__,
      description='Card Market SDK',
      author='Carlos Lucas',
      author_email='nosk14@gmail.com',
      url='https://github.com/Nosk14/cmsdk',
      packages=['cmsdk'],
      install_requires=["requests>=2.19.1"]
      )
