# file-list-manager

Very simple Python command-line tool to manage lists of files/directories.

## Use Cases

I developed this tool to use on a personal backup script, and, given that it
manages lists of files/directories, backup-related operations are most likely
the main use cases.

But there might be other things for which a tool like this could be useful; if
you come across some let me know and I'll add it in this section!

## Usage

To use this tool, first clone the repository or download its contents.

Then, the tool can be run with Python 3 using:

    python3 path/to/list_manager.py [options] file

Where `options` denotes the options specified below and `file` is the path
to the file where the list is/will be stored.

### Options

The tool can be run with the following options:

* `-h`, `--help`: shows a help dialog explaining all the options and arguments
* `-a`, `--add`: adds a single file/directory path
* `-A`, `--add-multiple`: adds multiple, new-line separated, file/directory
paths
* `-r`, `--remove`: removes a single file/directory path
* `-R`, `--remove-multiple`: removes multiple, new-line separated,
file/directory paths
* `-d`, `--display`: displays the current list in the file
* `-c`, `--concatenate`: displays the current list in the file with the lines
concatenated and joined by a space

## Contributing

If you wish to contribute with new ideas/bug fixes/etc. feel free to
do it and create a Pull Request! I'll review it as soon as I can.

## Development

The functionalities are all in the `list_manager.py` file. Python 3 is used.
The tests can be run with:

    python3 -m unittest tests.py
