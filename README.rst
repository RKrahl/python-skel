A skeleton for a Python package
===============================

This repository provides a skeleton of a Python package.  It is useful
as a starting point to create a new package.

After using this template to create a new package, run the following
command to adapt the package name::

     $ python3 init.py <name>


System requirements
-------------------

Python:

+ Python 3.6 or newer.

Required library packages:

+ `setuptools`_

Optional library packages:

+ `git-props`_

  This package is used to extract some metadata such as the version
  number out of git, the version control system.  All releases embed
  that metadata in the distribution.  So this package is only needed
  to build out of the plain development source tree as cloned from
  GitHub, but not to build a release distribution.

+ `pytest`_ >= 3.0

  Only needed to run the test suite.

+ `distutils-pytest`_

  Only needed to run the test suite.


Copyright and License
---------------------

Copyright 2019–2025 Rolf Krahl

Licensed under the `Apache License`_, Version 2.0 (the "License"); you
may not use this package except in compliance with the License.

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
implied.  See the License for the specific language governing
permissions and limitations under the License.


.. _setuptools: https://github.com/pypa/setuptools/
.. _git-props: https://github.com/RKrahl/git-props
.. _pytest: https://pytest.org/
.. _distutils-pytest: https://github.com/RKrahl/distutils-pytest
.. _Apache License: https://www.apache.org/licenses/LICENSE-2.0
