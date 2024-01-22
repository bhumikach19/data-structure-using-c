import unittest
import mai1
class TestMain(unittest.TestCase):
  def test(self):
    test_param=10
    result=mai1.do_stuff(test_param)
    self.assertEqual(result,15)

  def test1(self):
    test_param='gjdjh'
    result=mai1.do_stuff(test_param)
    self.assertIsInstance(result,ValueError)

  def test1(self):
    test_param=None
    result=mai1.do_stuff(test_param)
    self.assertIsInstance(result,ValueError)

unittest.main()