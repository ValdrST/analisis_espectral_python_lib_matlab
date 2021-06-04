#!/usr/bin/env python
from pip._internal.req import parse_requirements
from setuptools import setup, find_packages

with open('readme.md', 'r', encoding='utf-8') as f:
    readme = f.read()

requirements = parse_requirements("./requirements.txt", session=False)

setup(name='analizador_web',
      version="0.1.0",
      description='',
      long_description=readme,
      long_description_content_type="text/markdown",
      author='Valdr Stiglitz',
      author_email='valdr.stiglitz@gmail.com',
      url='',
      packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
      include_package_data=True,
      install_requires=[i.strip() for i in open("./requirements.txt").readlines()],
      entry_points={
          'console_scripts': ['analizador_web = analizador_web:main','analizador_webWSGI = analizador_web:wsgi']
      },
      classifiers=[
          'Programming Language :: Python :: 3',
          "Operating System :: OS Independent",
      ])
