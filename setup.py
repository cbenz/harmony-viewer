#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""Harmony Viewer"""

# sudo python setup.py develop --no-deps

from setuptools import setup, find_packages


doc_lines = __doc__.split('\n')


setup(
    author=u'Christophe Benz',
    author_email=u'cbenz@easter-eggs.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
        ],
    description=doc_lines[0],
    entry_points="""
        [paste.app_factory]
        main = harmony_viewer.application:make_app
        """,
    include_package_data=True,
    install_requires=[
        'Biryani1 >= 0.9dev',
        'WebError >= 0.10',
        'WebOb >= 1.1',
        ],
    keywords='harmony viewer osm shapefile gis',
    license=u'http://www.fsf.org/licensing/licenses/agpl-3.0.html',
    long_description='\n'.join(doc_lines[2:]),
    name=u'HarmonyViewer',
    packages=find_packages(),
    paster_plugins=['PasteScript'],
    setup_requires=['PasteScript >= 1.6.3'],
    url=u'https://github.com/cbenz/harmony-viewer',
    version='0.1',
    zip_safe=False,
    )
