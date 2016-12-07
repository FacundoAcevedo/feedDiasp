# coding=utf-8

from setuptools import setup

setup(name='feeddiasp',
      version='0.1',
      description='Feed Diaspora with RSS-Feeds or Facebook',
      url='https://github.com/Debakel/feedDiasp/',
      author='Moritz Duchêne',
      author_email='',
      license='GPL',
      packages=['feeddiasp'],
      install_requires=['facepy', 'argparse', 'diaspy', 'feedparser', 'html2text', 'pypandoc'])