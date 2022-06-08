import numpy as np
import pandas as pd

from scipy import spatial


def calc_euclidean(series1, series2):
    return np.sqrt(np.sum((series1 - series2) ** 2))


def calc_mae(series1, series2):
    return np.mean(np.abs((series1 - series2)))


def calc_mape(series1, series2):
    return np.mean(np.abs((series1 - series2) / series1))


def calc_cosine(series1, series2):
    return 1 - spatial.distance.cosine(series1, series2)


def calc_correlation(series1, series2):
    a_diff = series1 - np.mean(series1)
    p_diff = series2 - np.mean(series2)
    numerator = np.sum(a_diff * p_diff)
    denominator = np.sqrt(np.sum(a_diff ** 2)) * np.sqrt(np.sum(p_diff ** 2))
    return numerator / denominator


