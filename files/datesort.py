#
# The MIT License
#
# Copyright (c) 2009 Matthew Maravillas
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

import sys
import os
import shutil
import fnmatch
from datetime import datetime
import optparse


def main(options, args):
    for directory in args:
        basedir = os.path.abspath(options.destination or os.path.split(directory)[0])

        if options.recurse:
            for dirpath, dirnames, filenames in os.walk(directory):
                for file in fnmatch.filter(filenames, options.pattern):
                    sort_file(basedir, dirpath, file)

        else:
            for file in fnmatch.filter(os.listdir(directory), options.pattern):
                sort_file(basedir, directory, file)


def sort_file(basedir, directory, file):
    path = os.path.abspath(os.path.join(directory, file))

    date = None

    if not date:
        date = get_modification_date(path)

    new_directory = os.path.join(basedir,
                                 str(date.year),
                                 str(date.year) + "-%02d" % date.month,
                                 str(date.year) + "-%02d-%02d" % (date.month, date.day))

    if not options.pretend:
        if not os.access(new_directory, os.F_OK):
            os.makedirs(new_directory)

        shutil.move(path, os.path.join(new_directory, file))

    if options.verbose or options.pretend:
        print(path, "->", new_directory)


def get_modification_date(path):
    """Return the modification date & time of the file at path."""
    return datetime.fromtimestamp(os.stat(path).st_mtime)


if __name__ == "__main__":
    parser = optparse.OptionParser("Usage: %prog [options] directory ...")

    parser.add_option("-p", "--pattern", dest="pattern",
                      help="file pattern to match")
    parser.add_option("-r", "--recurse", dest="recurse",
                      action="store_true", help="recurse into subdirectories")
    parser.add_option("-d", "--destination", dest="destination",
                      help="directory that will contain sorted files")
    parser.add_option("-v", "--verbose", dest="verbose",
                      action="store_true", help="show verbose output")
    parser.add_option("-P", "--pretend", dest="pretend",
                      action="store_true", help="don't actually move files")

    parser.set_defaults(pattern="*.*",
                        recurse=False,
                        destination=None,
                        verbose=False,
                        pretend=False)

    (options, args) = parser.parse_args()

    if len(args) < 1:
        parser.error("Missing path argument")

    if options.verbose:
        print("File pattern:", options.pattern)

        if options.recurse:
            print("Recursing into subdirectories")

        print("Destination directory: %s" % (options.destination or "Default"))

    main(options, args)
