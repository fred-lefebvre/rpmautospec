.. _using-autorelease:

Using the ``%autorelease`` Macro
============================

Fedora's `Versioning Guidelines`_ define the different elements of which a
release field can consist. They are as follows:

::

    <pkgrel>[.<extraver>][.<snapinfo>]%{?dist}[.<minorbump>]

Each element in square brackets indicates an optional item.

The ``%autorelease`` macro accepts these parameters to allow packagers to specify
the different portions of the release field:

* ``-h <hotfix>``: Designates a hotfix release, i.e. enables bumping the
  ``minorbump`` portion in order to not overrun EVRs in later Fedora versions.
* ``-p <prerelease>``: Designates a pre-release, i.e. ``pkgrel`` will be prefixed
  with ``0.``.
* ``-e <extraver>``: Allows specifying the ``extraver`` portion of the release.
* ``-s <snapinfo>``: Allows specifying the ``snapinfo`` portion of the release.


.. warning::
    To date, only the normal release cadence is fully implemented. Please don't use the hotfix or
    pre-release parameters yet, attempting to build such packages will fail.


Some Examples:
--------------

.. _simple example:

The Simple Case
^^^^^^^^^^^^^^^

.. include:: examples/test-autorelease.spec
   :literal:

Will generate the following NEVR:

::

    test-autorelease-1.0-1.fc31.x86_64


.. _hotfix example:

The Hotfix Case
^^^^^^^^^^^^^^^

.. include:: examples/test-autorelease-hotfix.spec
   :literal:

Will generate the following NEVR:

::

    test-autorelease-hotfix-1.0-1.fc31.1.x86_64


.. _prerelease example:

The Pre-Release Case
^^^^^^^^^^^^^^^^^^^^

.. include:: examples/test-autorelease-prerelease.spec
   :literal:

Will generate the following NEVR:

::

    test-autorelease-prerelease-1.0-0.1.pre1.fc31.x86_64


.. _extraver case:

The Extraver Case
^^^^^^^^^^^^^^^^^

.. include:: examples/test-autorelease-extraver.spec
   :literal:

Will generate the following NEVR:

::

    test-autorelease-extraver-1.0-1.pre1.fc31.x86_64


.. _snapshot case:

The Snapshot Case
^^^^^^^^^^^^^^^^^

.. include:: examples/test-autorelease-snapshot.spec
   :literal:

Will generate the following NEVR:

::

    test-autorelease-snapshot-1.0-1.20200317git1234abcd.fc31.x86_64


.. _snapshot_and_extraver case:

The Snapshot and Extraver case
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: examples/test-autorelease-extraver-snapshot.spec
   :literal:

Will generate the following NEVR:

::

    test-autorelease-extraver-snapshot-1.0-1.pre1.20200317git1234abcd.fc31.x86_64


.. _Versioning Guidelines: https://docs.fedoraproject.org/en-US/packaging-guidelines/Versioning/#_more_complex_versioning