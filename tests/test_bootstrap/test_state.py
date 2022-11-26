"""
Tests for the state module.
"""


import pytest

from bootstrap.state import State


@pytest.fixture(name="state")
def fixture_state() -> State:
    """ Fixture for state. """

    return State()


def test_coverage_disabled(state: State):
    """ Verifies that disabling testing automatically disables test coverage. """

    # in the initial state everything should be enabled
    assert state.is_testing_enabled is True
    assert state.is_coverage_enabled is True

    state.is_testing_enabled = False

    assert state.is_testing_enabled is False
    assert state.is_coverage_enabled is False


def test_add_requiremenents(state: State) -> None:
    """ Verifies that setting requirements works. """

    assert "pylint" not in state.requirements

    state.add_requirement("pylint")

    assert "pylint" in state.requirements


def test_get_requirement_version_01(state: State) -> None:
    """ Verifies that not setting a requirement's version correctly returns None when queried. """

    assert "pylint" not in state.requirements

    state.add_requirement("pylint")

    assert state.get_requirement_version("pylint") is None


def test_get_requirement_version_02(state: State) -> None:
    """ Verifies that the requirement's version is correctly returned when set. """

    assert "pylint" not in state.requirements

    state.add_requirement("pylint", "2.12.2")

    assert state.get_requirement_version("pylint") == "2.12.2"


def test_get_requirement_version_error(state: State) -> None:
    """ Verifies trying to get the version for a non-existent requirement correctly raises an error. """

    assert "pylint" not in state.requirements

    with pytest.raises(ValueError) as ex_info:
        state.get_requirement_version("pylint")

    assert str(ex_info.value) == "Module pylint is not stored in the requirements."
