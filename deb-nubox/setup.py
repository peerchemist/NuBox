from setuptools import setup

setup(name='nubox',
      version='0.1',
      description='NuBox control scripts',
      url='https://github.com/peerchemist/NuBox',
      author='Peerchemist',
      author_email='peerchemist@protonmail.ch',
      license='GLP',
      packages=['nubox'],
      install_requires=["requests", "sh"],
      scripts=['bin/nubox'],
      zip_safe=False)
