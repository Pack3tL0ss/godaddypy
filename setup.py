#!/usr/bin/env python

from setuptools import setup


setup(name='GoDaddyPy',
      version='0.1.1r',
      description='A very simple python client used to update the IP address in A records for GoDaddy managed domains.',
      author='Julian Coy',
      author_email='julian.calvin.coy@gmail.com',
      url='https://github.com/eXamadeus',
      packages=['godaddypy'],
      install_requires=[
          'requests>=2.4'
      ],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Topic :: Internet :: Name Service (DNS)',
          'License :: OSI Approved :: BSD License',
          'Natural Language :: English',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3 :: Only'
      ])
