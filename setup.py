"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
    
# Get current version
with open(path.join(here, 'VERSION')) as version_file:
    #version = version_file.read().strip()
    #version = version_file.read().strip().split("-")[0].split()[1]
    #version = "1.9.9"
    version = "1.9.20"
    #version = "2.0.0"

setup(
    name='tnseq-transit',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=version,

    description='TRANSIT is a tool for the analysis of Tn-Seq data. It provides an easy to use graphical interface and access to three different analysis methods that allow the user to determine essentiality in a single condition as well as between conditions.',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/mad-lab/transit',
    download_url='https://github.com/mad-lab/transit',
    
    # Author details
    author='Michael A. DeJesus',
    author_email='mad@cs.tamu.edu',

    # Choose your license
    license='GNU GPL',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        #'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 2.7',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ],

    # What does your project relate to?
    keywords=['tnseq', 'analysis', 'biology', 'genome'],
    
    #package_dir = {'tnseq-transit': 'src/pytransit'},

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages = find_packages('src', exclude=['contrib', 'tests']),
    #packages = ['pytransit'],
    package_dir = {'pytransit': 'src/pytransit',  'pytpp': 'src/pytpp'},
    include_package_data=True,
    #py_modules = ['tpp'],

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['setuptools', 'numpy', 'scipy', 'pillow', 'matplotlib>1.2.0,<1.5.0'],
    
    #dependency_links = [
    #	"git+https://github.com/wxWidgets/wxPython.git#egg=wxPython"
	#],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    #extras_require={
    #    'dev': ['check-manifest'],
    #    'test': ['coverage'],
    #},

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data={
        'pytransit': ['pytransit/data/*', 'pytransit/doc/*.*', 'pytransit/doc/images/*', 'pytransit/genomes/*']
    },
    
    #scripts=['src/tpp.py', 'src/transit.py'],

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    #data_files=[('transitdata', ['package_data.dat'])],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'transit=pytransit.__main__:main',
            'tpp=pytpp.__main__:main',
        ],
    },
)

