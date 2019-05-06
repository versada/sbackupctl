from os import path
from setuptools import setup, find_packages

# Get the long description from the README file
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='versada_odoo_backups',
    description='A Utility for launching Odoo backups',
    long_description=long_description,
    long_description_content_type="text/markdown",
    use_scm_version=True,
    setup_requires=[
        'setuptools_scm',
        'pytest-runner',
    ],
    install_requires=[],
    tests_require=[
        'pytest',
        'mock',
        'coveralls',
    ],
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    classifiers=[
        'Development Status :: 2 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
    entry_points={
        'console_scripts': [
            'ctshed=versada_odoo_backups.cli:main'
        ]
    },
    url='https://github.com/versada/versada-odoo-backups.git',
)
