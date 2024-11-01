from unittest.mock import Mock
from path import Path
import numpy.testing as npt


def test_compute_daily_standard_deviation_by_data():
    from inflammation.compute_data import compute_standard_deviation_by_data as csdd

    patient_1 = [0.0, 1.0, 0.0]
    patient_2 = [0.0, 2.0, 0.0]
    file_1 = [patient_1, patient_2]
    all_files = [file_1]
    print(all_files)
    standard_deviation = csdd(all_files)
    npt.assert_array_almost_equal(standard_deviation, [0, 0, 0])


test_compute_daily_standard_deviation_by_data()


def test_compute_data_mock_source():
    from inflammation.compute_data import analyse_data_from_data_source

    data_source = Mock()
    data_source.load_data.return_value = [[[0.0, 1.0, 0.0], [0.0, 2.0, 0.0]]]
    result = analyse_data_from_data_source(data_source)
    npt.assert_array_almost_equal(
        result["standard deviation by day"],
        [0, 0, 0],
    )


def test_analyse_data():
    from inflammation.compute_data import analyse_data

    path = Path.cwd() / "data"
    result = analyse_data(path)

    assert "standard deviation by day" in result
    result_array = result["standard deviation by day"]

    npt.assert_array_almost_equal(
        result_array,
        [
            0.0,
            0.22510286,
            0.18157299,
            0.1264423,
            0.9495481,
            0.27118211,
            0.25104719,
            0.22330897,
            0.89680503,
            0.21573875,
            1.24235548,
            0.63042094,
            1.57511696,
            2.18850242,
            0.3729574,
            0.69395538,
            2.52365162,
            0.3179312,
            1.22850657,
            1.63149639,
            2.45861227,
            1.55556052,
            2.8214853,
            0.92117578,
            0.76176979,
            2.18346188,
            0.55368435,
            1.78441632,
            0.26549221,
            1.43938417,
            0.78959769,
            0.64913879,
            1.16078544,
            0.42417995,
            0.36019114,
            0.80801707,
            0.50323031,
            0.47574665,
            0.45197398,
            0.22070227,
        ],
    )
