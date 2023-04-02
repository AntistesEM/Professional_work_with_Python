import unittest
from unittest import TestCase

from task_2 import YandexFolder


class TestTask2(TestCase):
    folder = YandexFolder()

    def test_add_folder(self):
        return self.assertEqual(self.folder.add_folder("test"), 201)

    @unittest.expectedFailure
    def test_folder_exists(self):
        return self.assertEqual(self.folder.add_folder("test"), 409)

    @unittest.expectedFailure
    def test_auth(self):
        return self.assertEqual(self.folder.add_folder("test"), 401)

    def tearDown(self):
        self.folder.delete_folder("test")


if __name__ == "__main__":
    unittest.main()
