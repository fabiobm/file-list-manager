import argparse
import logging
import readline
import sys


logging.basicConfig(
    format="%(asctime)s - [%(levelname)s] - %(message)s", level=logging.INFO
)
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
        logger.critical("File '%s' could not found, exiting", file)
        sys.exit(1)
    except PermissionError:
        logger.critical("No permission to read file '%s', exiting", file)
        sys.exit(1)


def save_to_file(file_dir_list, file):
    """Write the files/directories list to the supplied file."""
    try:
        with open(file, "w", encoding="utf-8") as f:
            f.write(display_list(file_dir_list))
    except PermissionError:
        logger.critical("No permission to open or write to file '%s', exiting", file)
        sys.exit(1)


def get_input(multiple=False):
    """Get file/directory input from stdin."""
    readline.parse_and_bind("")

    lines = []
    print("Enter the " + ("files/directories" if multiple else "file/directory"))

    while True:
        try:
            lines.append(input())
            if not multiple:
                break
        except EOFError:
            break

    return lines


def add_to_list(file_dir_list, entries):
    """Add entries to the files/directories list."""
    modified = False

    for entry in entries:
        if entry.find("//") != -1:
            logger.info("New entry '%s' is not valid and will not be added", entry)
        elif entry in file_dir_list:
            logger.info("New entry '%s' is a duplicate and will not be added", entry)
        else:
            existing_children = [
                item
                for item in file_dir_list
                if item.startswith(entry + ("/" if entry[-1] != "/" else ""))
            ]
            for child in existing_children:
                logger.info(
                    "Removing entry '%s' as it is contained in new entry '%s'",
                    child,
                    entry,
                )
                file_dir_list.remove(child)

            possible_parents = [
                item
                for item in file_dir_list
                if entry.rstrip("/").startswith(item + "/")
            ]
            if len(possible_parents) > 0:
                logger.info(
                    "New entry '%s' will not be added since it is already contained in entry '%s'",
                    entry,
                    possible_parents[0],
                )
                continue

            file_dir_list.append(entry.rstrip("/"))
            modified = True

    if modified:
        file_dir_list.sort()


def remove_from_list(file_dir_list, entries):
    """Remove entries from the files/directories list."""
    modified = False

    for entry in entries:
        if entry.find("//") != -1:
            logger.info("Entry '%s' is not valid and will not be removed", entry)
        elif entry.rstrip("/") not in file_dir_list:
            logger.info("Entry '%s' is not in the list and will not be removed", entry)
        else:
            file_dir_list.remove(entry.rstrip("/"))
            modified = True

    if modified:
        file_dir_list.sort()


def display_list(file_dir_list, concatenate=False):
    """Return the files/directories list to be displayed in stdout."""
    return (" " if concatenate else "\n").join(file_dir_list)


def main():
    parser = argparse.ArgumentParser()
    setup_args(parser)

    args = parser.parse_args()

    file_dir_list = load_from_file(args.file)

    if args.add:
        add_to_list(file_dir_list, get_input())
        save_to_file(file_dir_list, args.file)
    elif args.add_multiple:
        add_to_list(file_dir_list, get_input(multiple=True))
        save_to_file(file_dir_list, args.file)
    elif args.remove:
        remove_from_list(file_dir_list, get_input())
        save_to_file(file_dir_list, args.file)
    elif args.remove_multiple:
        remove_from_list(file_dir_list, get_input(multiple=True))
        save_to_file(file_dir_list, args.file)
    elif args.display:
        print(display_list(file_dir_list))
    elif args.concatenate:
        print(display_list(file_dir_list, concatenate=True))


if __name__ == "__main__":
    main()
