#!/usr/bin/python
# -*- coding:utf-8 -*-
from distutils.core import setup

version = '0.0'

setup(name = 'tomatopie',
      version = version,
      description = 'Tomatopie',
      author = 'YoungLee',
      author_email = 'YoungLeeNENU@gmail.com',
      url = 'https://github.com/YoungLeeNENU/tomato-timer.git',
      # packages=['doubanfm', 'doubanfm.source'],
      # package_data={'doubanfm': ['*.conf']},
      # scripts=['fm'],
      license = 'GPL-3+',
      requires = ['pyaudio','pygtk'],
      )
