from unittest import TestCase

from list_manager import display_list


class AddTestCase(TestCase):
    pass


class RemoveTestCase(TestCase):
    pass


class DisplayTestCase(TestCase):
    def setUp(self):
        self.regular_list = [
            "~/test/file",
            "~/test/dir/file",
            "~/test/dir/other_file",
            "~/test/dir/subdir/file",
            "~/test/dir/subdir/other_other_file",
        ]

    def test_display_empty_list(self):
        self.assertEqual(display_list([]), "")
        self.assertEqual(display_list([], concatenate=True), "")

    def test_regular_list(self):
        self.assertEqual(
            display_list(self.regular_list),
            "~/test/file\n~/test/dir/file\n~/test/dir/other_file\n~/test/dir/subdir/file\n~/test/dir/subdir/other_other_file",
        )

    def test_regular_list_concatenated(self):
        self.assertEqual(
            display_list(self.regular_list, concatenate=True),
            "~/test/file ~/test/dir/file ~/test/dir/other_file ~/test/dir/subdir/file ~/test/dir/subdir/other_other_file",
        )
