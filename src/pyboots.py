# -*- coding: utf-8 -*-
#! /usr/bin/env python3

"""
bootstrap-python --- Bootstrapper for Python projects.

Created on 08 March 2022.

@author: Marco Wegner
@copyright: Copyright 2022 Marco Wegner
@license: MIT
"""

__author__ = "Marco Wegner"
__copyright__ = "Copyright 2022, Marco Wegner"
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Marco Wegner"
__status__ = "Development"


import sys
from argparse import ArgumentParser, Namespace

from bootstrap.processor import Processor, ProcessorParameters

LAST_UPDATED = "2022-11-27"

# Return Codes
RC_SUCCESS = 0


def main() -> int:
    """ The main function. """

    args = _get_command_line_args()

    params: ProcessorParameters = {
        "project_name": args.bootstrap_project,
        "enable_linting": args.bootstrap_linting,
        "enabled_unit_testing": args.bootstrap_testing,
        "enabled_test_coverage": args.bootstrap_coverage,
    }

    processor = Processor(params)
    processor.run()

    return RC_SUCCESS


def _get_command_line_args() -> Namespace:
    parser = ArgumentParser()

    parser.add_argument("bootstrap_project", help="the name of the Python project to bootstrap")

    parser.add_argument("--disable-linting", dest="bootstrap_linting",
                        action="store_false", default=True, help="disable linting by default")
    parser.add_argument("--disable-testing", dest="bootstrap_testing",
                        action="store_false", default=True, help="disable testing by default")
    parser.add_argument("--disable-coverage", dest="bootstrap_coverage", action="store_false",
                        default=True, help="disable unit test coverage by default")

    parser.add_argument("--version", action="version", version=_get_version_message(True))

    return parser.parse_args()


def _get_version_message(short: bool = False) -> str:
    name = "pyboots"
    template = "{name} v{version} ({updated})" if short else "This is {name} version {version} (last updated {updated})"
    return template.format(name=name, version=__version__, updated=LAST_UPDATED)


if __name__ == "__main__":
    sys.exit(main())
