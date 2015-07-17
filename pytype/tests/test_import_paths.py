"""Tests for import_paths.py."""


from pytype import import_paths
from pytype import utils
from pytype.tests import test_inference

import unittest


class ImportPathsTest(unittest.TestCase):
  """Tests for import_paths.py."""

  PYTHON_VERSION = (2, 7)

  def testBuiltinSys(self):
    ast = import_paths.module_name_to_pytd("sys", 0, self.PYTHON_VERSION)
    self.assertTrue(ast)
    self.assertTrue(ast.Lookup("exit"))

  def testUserDef(self):
    with utils.Tempdir() as d:
      d.create_file("path/to/some/module.pytd",
                    "def foo(x:int) -> str")
      ast = import_paths.module_name_to_pytd("path.to.some.module",
                                             0, self.PYTHON_VERSION,
                                             pythonpath=[d.path],
                                             pytd_import_ext=".pytd")
      self.assertTrue(ast)
      self.assertTrue(ast.Lookup("foo"))


if __name__ == "__main__":
  test_inference.main()
