from setuptools import setup, find_packages

setup(name='EPass',
      version='0.1.0',
      packages=find_packages(include=['EPass', 'EPass.*']),
      install_requires=[],
      entry_points={
          'console_scripts': ['epass=EPass.__main__:main',
                              'epass-help=EPass.__main__:help']
      })
