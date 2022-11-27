# -*- coding: utf-8 -*-

"""
Processor module for the Bootstrapper.

@author: Marco Wegner
@copyright: Copyright 2022 Marco Wegner
@license: MIT
"""

from typing import TypedDict

from bootstrap.state import State


class ProcessorParameters(TypedDict):
    """ Processor parameters """

    # The name of the project to bootstrap.
    project_name: str

    # Whether or not linting will be enabled by default.
    enable_linting: bool

    # Whether or not unit testing will be enabled by default.
    enabled_unit_testing: bool

    # Whether or not unit test coverage will be enabled by default.
    enabled_test_coverage: bool


class Processor:
    """ The main processor class. """

    @property
    def state(self) -> State:
        """ This processor instance's state object. """
        return self.__state

    @property
    def processor_parameters(self) -> ProcessorParameters:
        """ This instance's processor parameters. """
        return self.__params

    def __init__(self, params: ProcessorParameters) -> None:
        self.__state = State()
        self.__params = params

    def run(self) -> None:
        """ Runs the main processor, flow is based on the parameters. """
