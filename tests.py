import logging
from unittest import TestCase

from list_manager import add_to_list, display_list, remove_from_list


example_list = [
    "~/test/file",
    "~/test/subdir/file",
    "~/test/subdir/other_file",
    "~/test/subdir/subdir/file",
    "~/test/subdir/subdir/other_other_file",
    "~/test/subdir2",
]


class AddTestCase(TestCase):
    def setUp(self):
        logging.disable(logging.CRITICAL)
        self.initial_list = [*example_list]

    def test_add_no_entries(self):
        add_to_list(self.initial_list, [])
        self.assertEqual(self.initial_list, example_list)

    def test_add_invalid(self):
        add_to_list(self.initial_list, ["~/test//file/x"])
        self.assertEqual(self.initial_list, example_list)

    def test_add_duplicates(self):
        add_to_list(self.initial_list, ["~/test/file", "~/test/subdir/file"])
        self.assertEqual(self.initial_list, example_list)

    def test_add_already_contained(self):
        add_to_list(
            self.initial_list, ["~/test/subdir2/file", "~/test/subdir2/other_subdir2"]
        )
        self.assertEqual(self.initial_list, example_list)

    def test_add_parent(self):
        add_to_list(self.initial_list, ["~/test/subdir/"])
        self.assertEqual(
            self.initial_list, ["~/test/file", "~/test/subdir", "~/test/subdir2"]
        )

    def test_add_regular_entries(self):
        add_to_list(
            self.initial_list,
            ["~/test/file2", "~/test/subdir/file3", "~/test/subdir/subdir/file4"],
        )
        self.assertEqual(
            self.initial_list,
            [
                "~/test/file",
                "~/test/file2",
                "~/test/subdir/file",
                "~/test/subdir/file3",
                "~/test/subdir/other_file",
                "~/test/subdir/subdir/file",
                "~/test/subdir/subdir/file4",
                "~/test/subdir/subdir/other_other_file",
                "~/test/subdir2",
            ],
        )


class RemoveTestCase(TestCase):
    def setUp(self):
        logging.disable(logging.CRITICAL)
        self.initial_list = [*example_list]

    def test_remove_no_entries(self):
        remove_from_list(self.initial_list, [])
        self.assertEqual(self.initial_list, example_list)

    def test_remove_invalid(self):
        remove_from_list(self.initial_list, ["~/test//file/x"])
        self.assertEqual(self.initial_list, example_list)

    def test_remove_not_present(self):
        remove_from_list(self.initial_list, ["~/test/file2", "~/test/subdir/file3"])
        self.assertEqual(self.initial_list, example_list)

    def test_remove_regular_entries(self):
        remove_from_list(
            self.initial_list,
            ["~/test/file", "~/test/subdir/file", "~/test/subdir/subdir/file"],
        )
        self.assertEqual(
            self.initial_list,
            [
                "~/test/subdir/other_file",
                "~/test/subdir/subdir/other_other_file",
                "~/test/subdir2",
            ],
        )


class DisplayTestCase(TestCase):
    def setUp(self):
        self.regular_list = [*example_list]

    def test_display_empty_list(self):
        self.assertEqual(display_list([]), "")
        self.assertEqual(display_list([], concatenate=True), "")

    def test_regular_list(self):
        self.assertEqual(
            display_list(self.regular_list),
            "~/test/file\n~/test/subdir/file\n~/test/subdir/other_file\n~/test/subdir/subdir/file\n~/test/subdir/subdir/other_other_file\n~/test/subdir2",
        )

    def test_regular_list_concatenated(self):
        self.assertEqual(
            display_list(self.regular_list, concatenate=True),
            "~/test/file ~/test/subdir/file ~/test/subdir/other_file ~/test/subdir/subdir/file ~/test/subdir/subdir/other_other_file ~/test/subdir2",
        )
