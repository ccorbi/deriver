from setuptools import setup
from setuptools import find_packages

setup(name='deriver',
      description='Deriver: for all your molecule generation needs.',
      long_description='A software tool for the generation of novel chemical entities.',
      version='1.0.0',
      url='https://gitlab.com/cyclicainc/deriver',
      license='All Rights Reserved Cyclica Inc.',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      zip_safe=False,
      install_requires=["selfies>=0.2.2"]
      )