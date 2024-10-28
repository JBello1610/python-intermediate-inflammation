"""Module containing mechanism for calculating standard deviation between datasets."""

import glob
import os
from inflammation.csv_data_source import CSVDataSource
import numpy as np

from inflammation import models, views


def compute_standard_deviation_by_data(data):
    means_by_day = map(models.daily_mean, data)
    means_by_day_matrix = np.stack(list(means_by_day))
    daily_standard_deviation = np.std(means_by_day_matrix, axis=0)

    return daily_standard_deviation


def load_inflammation_data(data_dir):
    data_file_paths = glob.glob(os.path.join(data_dir, "inflammation*.csv"))
    if len(data_file_paths) == 0:
        raise ValueError(f"No inflammation csv's found in path {data_dir}")
    data = map(models.load_csv, data_file_paths)

    return data


def analyse_data_from_data_source(data_source):
    """Calculate the standard deviation by day between datasets

    Gets all the inflammation csvs within a directory, works out the mean
    inflammation value for each day across all datasets, then graphs the
    standard deviation of these means."""

    data = data_source.load_data()
    daily_standard_deviation = compute_standard_deviation_by_data(data)

    graph_data = {
        "standard deviation by day": daily_standard_deviation,
    }
    # views.visualize(graph_data)
    return graph_data


def analyse_data(data_dir):
    """Calculate the standard deviation by day between datasets

    Gets all the inflammation csvs within a directory, works out the mean
    inflammation value for each day across all datasets, then graphs the
    standard deviation of these means."""

    data_source = CSVDataSource(data_dir)

    return analyse_data_from_data_source(data_source)
