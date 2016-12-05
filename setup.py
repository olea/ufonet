#!/usr/bin/env python
import sys


if sys.version_info[0] != 2:
    sys.exit("Sorry, ufonet requires Python 2.7")
    
from distutils.core import setup

setup(
    name='ufonet',
    version='0.8b',
    license='GPLv3+',
    author_email='epsylon@riseup.net',
    author='Psy',
    description='Open Redirect DDoS WebAbuse Botnet Manager',
    url='http://ufonet.03c8.net/',
    long_description=open('docs/README.txt').read(),
    packages=['botnet', 'core', 'server'],
    requires=['geoip (>=0.3.2)', 'requests', 'pycrypto', 'pycurl'],
    data_files=[
      'maps/GeoIPASNum.dat', 'maps/GeoLiteCity.dat', 
      'docs/blackhole.txt', 'docs/LEEME.txt', 'docs/manifesto.txt', 'docs/README.txt'
      'botnet/aliens.txt', 'botnet/dorks.txt', 'botnet/droids.txt', 'botnet/rpcs.txt', 'botnet/ucavs.txt', 'botnet/zombies.txt'
      ],
    scripts=['ufonet'],
    keywords='DDoS DoS botnet WebAbuse UFONet',
    classifiers=[
        "Environment :: Web Environment",
        "Environment :: Console", 
        "Intended Audience :: System Administrators",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet", 
        "Topic :: Security", 
        "Topic :: System :: Networking",
      ],
)
