import unittest
import main

class TestMain(unittest.TestCase):
    def setUp(self):
        print('we are now running our test...')

    def tearDown(self):
        print('cleaning up...')

    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff_2(self):
        test_param = 'shkshks'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)
    
    def test_do_stuff_3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter a number')

    def test_do_stuff_4(self):
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter a number')

if __name__ == '__main__':
    unittest.main()