import unittest
import mai
class TestMain(unittest.TestCase):
  def test(self):
    test_param=10
    result=mai.do_stuff(test_param)
    self.assertEqual(result,15)

  def test1(self):
    test_param='gjdjh'
    result=mai.do_stuff(test_param)
    self.assertIsInstance(result,ValueError)

  def test1(self):
    test_param=None
    result=mai.do_stuff(test_param)
    self.assertIsInstance(result,ValueError)

unittest.main()