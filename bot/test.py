import unittest
import doctest

docSuite = doctest.DocFileSuite("interfaces.txt")
unittest.TextTestRunner(verbosity=3).run(docSuite)
