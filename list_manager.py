import argparse
import logging
import sys


logging.basicConfig(format="%(asctime)s - [%(levelname)s] - %(message)s")
logger = logging.getLogger()


def setup_args(parser):
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
        "-r",
        "--remove",
        help="remove a single file/directory path",
        action="store_true",
    )
    group.add_argument(
        "-R",
        "--remove-multiple",
        help="remove multiple, new-line separated, file/directory paths",
        action="store_true",
    )
    group.add_argument(
        "-d",
        "--display",
        help="display the current list in the file",
        action="store_true",
    )
    group.add_argument(
        "-c",
        "--concatenate",
        help="display the current list in the file with the lines concatenated and joined by a space",
        action="store_true",
    )


def load_from_file(file):
    """Load the files/directories list from the supplied file."""
    try:
        with open(file, encoding="utf-8") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        logger.critical("File '%s' could not found, exiting.", file)
        sys.exit(1)
    except PermissionError:
        logger.critical("No permission to read file '%s', exiting.", file)
        sys.exit(1)


def save_to_file(file_dir_list, file):
    pass


def display_list(file_dir_list, concatenate=False):
    """Return the files/directories list to be displayed in stdout."""
    return (" " if concatenate else "\n").join(file_dir_list)


def main():
    parser = argparse.ArgumentParser()
    setup_args(parser)

    args = parser.parse_args()

    file_dir_list = load_from_file(args.file)

    if args.add:
        pass
    elif args.add_multiple:
        pass
    elif args.remove:
        pass
    elif args.remove_multiple:
        pass
    elif args.display:
        print(display_list(file_dir_list))
    elif args.concatenate:
        print(display_list(file_dir_list, concatenate=True))


if __name__ == "__main__":
    main()
