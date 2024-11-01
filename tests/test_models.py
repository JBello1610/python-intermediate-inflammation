"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import os
import pytest


@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0, 0], [0, 0], [0, 0]], [0, 0]),
        ([[1, 2], [3, 4], [5, 6]], [3, 4]),
    ],
)
def test_daily_mean(test, expected):
    """Test mean function works for array of zeroes and positive integers."""
    from inflammation.models import daily_mean

    npt.assert_array_equal(daily_mean(np.array(test)), np.array(expected))


def test_load_from_json(tmpdir):
    from inflammation.models import load_json

    example_path = os.path.join(tmpdir, "example.json")
    with open(example_path, "w") as temp_json_file:
        temp_json_file.write('[{"observations":[1, 2, 3]},{"observations":[4, 5, 6]}]')
    result = load_json(example_path)
    npt.assert_array_equal(result, [[1, 2, 3], [4, 5, 6]])


@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0, 0], [0, 0], [0, 0]], [0, 0]),
        ([[1, 2], [3, 4], [5, 6]], [5, 6]),
    ],
)
def test_daily_max(test, expected):
    from inflammation.models import daily_max

    npt.assert_array_equal(daily_max(np.array(test)), np.array(expected))


@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0, 0], [0, 0], [0, 0]], [0, 0]),
        ([[1, 2], [3, 4], [5, 6]], [1, 2]),
    ],
)
def test_daily_min(test, expected):
    from inflammation.models import daily_min

    npt.assert_array_equal(daily_min(np.array(test)), np.array(expected))
