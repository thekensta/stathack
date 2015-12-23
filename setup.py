from setuptools import setup

# http://python-packaging.readthedocs.org/en/latest/minimal.html
setup(name="stathacks",
      packages=["stathacks"],
      version="0.1",
      license="MIT", 
      url="https://github.com/thekensta/stathacks",
      install_requires=["numpy>=1.6", "scipy>=0.16"], 
      scripts=["bin/ab-test"]
     )

