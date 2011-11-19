import os
import sys
import time
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

requirements = ['httplib2', 'argparse', 'prettytable']
if sys.version_info < (2, 6):
    requirements.append('simplejson')

TOPDIR = os.path.abspath(os.path.dirname(__file__))
VFILE  = os.path.join(TOPDIR, 'version.py')

args = filter(lambda x: x[0] != '-', sys.argv)
command = args[1] if len(args) > 1 else ''

if command == 'sdist':
    PISTON_VERSION = os.environ['PISTON_VERSION']
    with file(VFILE, 'w') as f:
        f.write('''#!/usr/bin/env python\nVERSION = '%s'\n''' % PISTON_VERSION)
elif command == 'develop':
    PISTON_VERSION = time.strftime('9999.0.%Y%m%d%H%M%S', time.localtime())
    with file(VFILE, 'w') as f:
        f.write('''#!/usr/bin/env python\nVERSION = '%s'\n''' % PISTON_VERSION)
elif command is None:
    PISTON_VERSION = '9999999999-You_did_not_set_a_version'
else:
    assert os.path.exists(VFILE), 'version.py does not exist, please set PISTON_VERSION (or run make_version.py for dev purposes)'
    import version as pistonversion
    PISTON_VERSION = pistonversion.VERSION

setup(
    name = "python-novaclient",
    version = PISTON_VERSION,
    description = "Client library for OpenStack Nova API",
    long_description = read('README.rst'),
    url = 'https://github.com/rackspace/python-novaclient',
    license = 'Apache',
    author = 'Rackspace, based on work by Jacob Kaplan-Moss',
    author_email = 'github@racklabs.com',
    packages = find_packages(exclude=['tests', 'tests.*']),
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    install_requires = requirements,

    tests_require = ["nose", "mock"],
    test_suite = "nose.collector",

    entry_points = {
        'console_scripts': ['nova = novaclient.shell:main']
    }
)
