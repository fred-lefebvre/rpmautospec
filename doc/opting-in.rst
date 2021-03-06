Opting into using `rpmautospec`
===============================

To opt into using `rpmautospec` you need to use the two macros as explained
here below:

Use the ``%autorelease`` macro
------------------------------

Basically, in the spec file you replace the manually set release, e.g.:

::

    Release:    7{%dist}

with the ``%autorelease`` macro, such as:

::

    Release:    %autorelease

There are different options you can associate with this macro which are
documented in: :ref:`using-autorelease`.


Use the ``%autochangelog`` macro
--------------------------------

For new packages
^^^^^^^^^^^^^^^^

If you use this macro in a brand-new package without git history, you can
simply put the following two lines at the end of your spec file:

::

    %changelog
    %autochangelog

From this point on, the build system will insert into your spec file an
automatically generated changelog using the information from the git commit
history of the package.


For existing packages
^^^^^^^^^^^^^^^^^^^^^

Existing packages will already have a ``%changelog`` section with content, you can copy that into a
file ``changelog`` that needs to be added to the git repository of the package.  You can then remove
the content of the ``%changelog`` section of your spec file and simply have it be:

::

    %changelog
    %autochangelog

Once these two changes are done, commit them in a *single commit* for both
files. If the same commit contains other changes that would require
a changelog entry, add it to the top of the ``changelog`` file.

From now on, the changelog will be automatically generated from the commit
history of your git repository up until the most recent commit found that
changes the ``changelog`` file.

More explanations on how the ``%autochangelog`` macro works can be found
in :ref:`using-autochangelog`.


.. note::
    Congratulations for opting into `rpmautospec`. You may now want to have a
    look at the :ref:`peculiarities`.
