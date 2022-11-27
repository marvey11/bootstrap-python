# -*- coding: utf-8 -*-
#! /usr/bin/env python3

"""
bootstrap-python --- Bootstrapper for Python projects.

Created on 08 March 2022.

@author: Marco Wegner
@contact: devel@marcowegner.de
@copyright: 2022 Marco Wegner. All rights reserved.
@license: MIT
"""

import sys
from argparse import ArgumentParser, Namespace

__author__ = "Marco Wegner"
__version__ = "0.1.0"
__date__ = "2022-03-08"
__updated__ = "2022-11-27"
__license__ = "MIT"

# Return Codes
RC_SUCCESS = 0


def main() -> int:
    """ The main function. """

    args = _get_command_line_args()

    print(args)

    return RC_SUCCESS


def _get_command_line_args() -> Namespace:
    parser = ArgumentParser()

    parser.add_argument("project_name", help="the name of the Python project to create")

    parser.add_argument("--disable-linting", dest="bootstrap_linting",
                        action="store_false", default=True, help="disable linting")
    parser.add_argument("--disable-testing", dest="bootstrap_testing",
                        action="store_false", default=True, help="disable testing")
    parser.add_argument("--disable-coverage", dest="bootstrap_coverage", action="store_false",
                        default=True, help="disable unit test coverage")

    parser.add_argument("--version", action="version", version=_get_version_message(True))

    return parser.parse_args()


def _get_version_message(short: bool = False) -> str:
    name = "pyboots"
    template = "{name} v{version} ({updated})" if short else "This is {name} version {version} (last updated {updated})"
    return template.format(name=name, version=__version__, updated=__updated__)


if __name__ == "__main__":
    sys.exit(main())
