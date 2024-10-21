Ansys Tools Omniverse
=====================
|pyansys| |ci| |pre-commit| |black| |isort| |bandit|

.. |pyansys| image:: https://img.shields.io/badge/Py-Ansys-ffc107.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAABDklEQVQ4jWNgoDfg5mD8vE7q/3bpVyskbW0sMRUwofHD7Dh5OBkZGBgW7/3W2tZpa2tLQEOyOzeEsfumlK2tbVpaGj4N6jIs1lpsDAwMJ278sveMY2BgCA0NFRISwqkhyQ1q/Nyd3zg4OBgYGNjZ2ePi4rB5loGBhZnhxTLJ/9ulv26Q4uVk1NXV/f///////69du4Zdg78lx//t0v+3S88rFISInD59GqIH2esIJ8G9O2/XVwhjzpw5EAam1xkkBJn/bJX+v1365hxxuCAfH9+3b9/+////48cPuNehNsS7cDEzMTAwMMzb+Q2u4dOnT2vWrMHu9ZtzxP9vl/69RVpCkBlZ3N7enoDXBwEAAA+YYitOilMVAAAAAElFTkSuQmCC
   :target: https://docs.pyansys.com/

.. |MIT| image:: https://img.shields.io/badge/License-MIT-yellow.svg
   :target: https://opensource.org/licenses/MIT

.. |black| image:: https://img.shields.io/badge/code_style-black-000000.svg
   :target: https://github.com/psf/black

.. |isort| image:: https://img.shields.io/badge/imports-isort-%231674b1.svg?style=flat&labelColor=ef8336
   :target: https://pycqa.github.io/isort/

.. |pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
   :target: https://github.com/pre-commit/pre-commit

.. |bandit| image:: https://img.shields.io/badge/security-bandit-yellow.svg
    :target: https://github.com/PyCQA/bandit
    :alt: Security Status

.. |ci| image:: https://github.com/ansys-internal/ansys-tools-omniverse/actions/workflows/ci.yml/badge.svg?branch=main
   :target: https://github.com/ansys-internal/ansys-tools-omniverse/actions?query=branch%3Amain

.. _PyEnSight: https://ensight.docs.pyansys.com/version/stable/

.. _EnSight: https://www.ansys.com/products/fluids/ansys-ensight

.. _PyAnsys: https://docs.pyansys.com/

Overview
--------

The Ansys Tools Omniverse extension is designed to let you interact
with Ansys applications via Omniverse, in order to display and post-process
results from Ansys simulations in the Omniverse environment.

The first product supported is Ansys EnSight_, a full-featured postprocessor
and general-purpose data visualization tool, that is capable of handling large simulation
datasets from a variety of physics and engineering disciplines.
It makes use of PyEnSight_, part of the PyAnsys_ ecosystem. PyEnSight is a Python module that
provides the ability to launch and control an EnSight instance from an external or remote
Python instance.

PyEnSight/Omniverse kit from an Omniverse Kit Application
---------------------------------------------------------

To install the service into an Omniverse application, one can install
it via the third party extensions dialog. Select the ``Extensions`` option
from the ``Window`` menu.  Select third party extensions and filter
by ``ANSYS``.  Enabling the extension will install the kit extension.
The kit extension will find the most recent Ansys install and use the
version of the pyensight found in the install to perform export
operations.

.. image:: https://ensight.docs.pyansys.com/version/stable/_images/omniverse_extension.png

The ``ansys.tools.omniverse.dsgui`` kit includes a GUI similar to the
EnSight 2025 R1 user-defined tool.  It allows one to select a
target directory and the details of a gRPC connection
to a running EnSight.  For example, if one launches EnSight with
``ensight.bat -grpc_server 2345``, then the uri:  ``grpc://127.0.0.1:2345``
can to used to request a locally running EnSight to push the current
scene to Omniverse.

.. note::

    If the ``ansys.tools.omniverse.core`` and ``ansys.tools.omniverse.dsgui``
    do not show up in the Community extensions list in Omniverse, then
    it can be added to the ``Extension Search Paths`` list as:
    ``git://github.com/ansys/pyensight.git?branch=main&dir=exts``.