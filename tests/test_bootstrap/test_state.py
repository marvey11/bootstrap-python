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

    assert state.is_testing_enabled is True
    assert state.is_coverage_enabled is True

    state.is_testing_enabled = False

    assert state.is_testing_enabled is False
    assert state.is_coverage_enabled is False
