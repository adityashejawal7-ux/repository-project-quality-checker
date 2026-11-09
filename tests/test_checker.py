import unittest
import os

class TestRepositoryChecker(unittest.TestCase):

    def test_project_folders_exist(self):
        folders = ["src", "tests", "reports", "docs", "evidence"]

        for folder in folders:
            self.assertTrue(os.path.isdir(folder))

    def test_checker_file_exists(self):
        self.assertTrue(os.path.isfile("src/checker.py"))


if __name__ == "__main__":
    unittest.main()