import argparse


parser = argparse.ArgumentParser()
parser.add_argument(
    "file", help="the path to the file where the file list will be stored"
)

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument(
    "-a", "--add", help="add a single file/directory path", action="store_true"
)
group.add_argument(
    "-A",
    "--add-multiple",
    help="add multiple, new-line separated, file/directory paths",
    action="store_true",
)
group.add_argument(
    "-r", "--remove", help="remove a single file/directory path", action="store_true"
)
group.add_argument(
    "-R",
    "--remove-multiple",
    help="remove multiple, new-line separated, file/directory paths",
    action="store_true",
)
group.add_argument(
    "-d", "--display", help="display the current list in the file", action="store_true"
)
group.add_argument(
    "-c",
    "--concatenate",
    help="display the current list in the file with the lines concatenated and joined by a space",
    action="store_true",
)

args = parser.parse_args()
