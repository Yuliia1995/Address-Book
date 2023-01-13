import unittest
from lab174 import add_item, look_up, change_item, del_item
from lab174 import read_unpickle
eof = False
address_book = read_unpickle(eof)
name = "Yuliia"



class MyTestCase(unittest.TestCase):
    def test_add_item(self):
        self.assertEqual(add_item(), "Name and address have been added.")

    def test_look_up_fail(self):
        # Enter 'someone' for a name to test that name is not in the book
        self.assertEqual(look_up(), "The specified name was not found")

    def test_change_item(self):
        self.assertEqual(change_item(), "Information has been updated.")

    def test_del_item(self):
        self.assertRaises(TypeError)


if __name__ == '__main__':
    unittest.main()
