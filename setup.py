"""
    :copyright: 2010 Lee Olayvar.
    :license: MIT, see LICENSE.txt for more details.
"""
from setuptools import setup


setup(
    name = 'Injaection',
    version = '0.0.1',
    license = 'MIT',
    url = '',
    description = ('Allows custom code hooks to be run directly after
                   'the development server starts by physically modifying
                   'the sdk itself.'),
    long_description = __doc__,
    author = 'Lee Olayvar',
    author_email = 'leeolayvar@gmail.com',
    zip_safe = False,
    packages = [],
    install_requires = [
        'zc.recipe.egg >= 1.2.2',
    ],
    entry_points = {
        'zc.buildout': [
            'default = volatilemonk.injaection.recipes:Recipe',
            ],
        },
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
