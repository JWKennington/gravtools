"""Utilities for filtering bulk strain timeseries
"""

from pycbc.types import TimeSeries
from lal import LIGOTimeGPS


LOW_PASS_BOUNDARY = 15 # Hz TODO investigate physical motivation for this value
ORDER_RATIO = 8


def centered_slice(ts: TimeSeries, time: LIGOTimeGPS, delta: int):
    """

    Args:
        ts:
        time:
        delta:

    Returns:

    """
    return ts.time_slice(start=time - delta, end=time + delta)


def low_pass(ts: TimeSeries, frequency: float = LOW_PASS_BOUNDARY, beta: float = 0.5):
    return ts.highpass_fir(frequency=frequency,
                           order=len(ts) // ORDER_RATIO,
                           beta=beta)
