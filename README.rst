===================
README for pydirect
===================

DIRECT is a method to solve global bound constraint optimization problems and
was originally developed by D. R. Jones, C. D. Perttunen and B. E. Stuckmann.

`pydirect` is a python wrapper around DIRECT. It enables using DIRECT from the
comfort of the great Python scripting language.

The `pydirect` package uses the fortan implementation of DIRECT written by
Joerg.M.Gablonsky, DIRECT Version 2.0.4. More information on the DIRECT
algorithm can be found in Gablonsky's
`thesis <http://repository.lib.ncsu.edu/ir/bitstream/1840.16/3920/1/etd.pdf>`_.

Installing
==========

Use ``setup.py``::

   python setup.py install


Reading the docs
================

After installing::

   cd doc
   make html

Then, direct your browser to ``build/html/index.html``.


Testing
=======

To run the tests with the interpreter available as ``python``, use::

   cd test
   python test_direct.py


Conditions for use
==================

pydirect is open-source code released under the `MIT <http://opensource.org/licenses/MIT>`_ License.


Contributing
============

For bug reports use the Bitbucket issue tracker.
You can also send wishes, comments, patches, etc. to amitibo@tx.technion.ac.il


Acknowledgement
===============

Thank-you to the people at <http://wingware.com/> for their policy of **free licenses for non-commercial open source developers**.

.. image:: http://wingware.com/images/wingware-logo-180x58.png
