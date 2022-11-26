# -*- coding: utf-8 -*-

"""
State module for the Python Boostrapper.

@author: Marco Wegner
@contact: devel@marcowegner.de
@copyright: 2022 Marco Wegner. All rights reserved.
@license: MIT
"""


from typing import Dict, Optional


class State:
    """ The underlying application state. """

    @property
    def requirements(self) -> Dict[str, str | None]:
        """ The project requirements. """
        return self.__requirements

    @property
    def is_testing_enabled(self) -> bool:
        """ Whether or not testing is enabled. """
        return self.__testing_enabled

    @is_testing_enabled.setter
    def is_testing_enabled(self, enabled: bool) -> None:
        self.__testing_enabled = enabled
        self.__coverage_enabled = self.is_coverage_enabled if enabled else False

    @property
    def is_coverage_enabled(self) -> bool:
        """ Whether or not coverage is enabled. """
        return self.__coverage_enabled

    @is_coverage_enabled.setter
    def is_coverage_enabled(self, enabled: bool) -> None:
        self.__coverage_enabled = enabled

    @property
    def is_linting_enabled(self) -> bool:
        """ Whether or not linting is enabled. """
        return self.__linting_enabled

    @is_linting_enabled.setter
    def is_linting_enabled(self, enabled: bool):
        self.__linting_enabled = enabled

    def __init__(self) -> None:
        self.__requirements: Dict[str, str | None] = {}
        self.__testing_enabled: bool = True
        self.__coverage_enabled: bool = True
        self.__linting_enabled: bool = True

    def add_requirement(self, module: str, version: Optional[str] = None) -> None:
        """ Adds a single requirement. """
        self.requirements[module] = version

    def get_requirement_version(self, module: str) -> str | None:
        """
        Returns the version the specified requirement.

        Returns None if the version was not specified.

        Throws an error if the requirement is not stored in the state.
        """
        if module not in self.requirements:
            raise ValueError(f"Module {module} is not stored in the requirements.")

        return self.requirements[module]
