========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor|
        | |coveralls|
    * - package
      - |version| |downloads| |wheel| |supported-versions| |supported-implementations|
    * - chat
      - | |chat|

.. |docs| image:: https://readthedocs.org/projects/nadist/badge/?style=flat
    :target: https://readthedocs.org/projects/nadist
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/midnighter/nadist.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/midnighter/nadist

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/midnighter/nadist?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/midnighter/nadist

.. |coveralls| image:: https://coveralls.io/repos/midnighter/nadist/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/midnighter/nadist

.. |version| image:: https://img.shields.io/pypi/v/nadist.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/nadist

.. |downloads| image:: https://img.shields.io/pypi/dm/nadist.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/nadist

.. |wheel| image:: https://img.shields.io/pypi/wheel/nadist.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/nadist

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/nadist.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/nadist

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/nadist.svg?style=flat
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/nadist

.. |chat| image:: https://badges.gitter.im/Midnighter/nadist.svg
    :alt: Gitter
    :target: https://gitter.im/Midnighter/nadist

.. end-badges

Compute distance metrics between vectors with missing values.

The name `nadist` was inspired by R which has built-in support for missing
values using the symbol `NA` (not available).

* Free software: BSD 3-clause license

Installation
============

::

    pip install nadist

Documentation
=============

https://nadist.readthedocs.org/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox


.. image:: https://badges.gitter.im/Midnighter/nadist.svg
   :alt: Join the chat at https://gitter.im/Midnighter/nadist
   :target: https://gitter.im/Midnighter/nadist?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge