#! /usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'Dieter Vansteenwegen'
__email__ = 'dieter.vansteenwegen@vliz.be'
__project__ = 'Panthyr'
__project_link__ = 'https://waterhypernet.org/equipment/'
"""Functions to help getting the sun position calculation."""

from pysolar import solar
import datetime
import logging
import pytz
import warnings

log = logging.getLogger(f'__main__.{__name__}')


def get_sun_azimuth(lat: float, lon: float, timestamp: datetime.datetime):
    """Calculate the sun azimuth using pysolar.

    Check if timestamp is timezone aware, if not add UTC timezone. Get the sun azimuth.

    Args:
        lat (float): latitude (format xxx.yyyyyy)
        lon (float): longitude (format xxx.yyyyyy)
        timestamp (datetime.datetime): time for calculation.

    Returns:
        float: compass azimuth (0-360), rounded to 2 decimals
    """
    # check if timestamp is timezone aware (needed for PySolar >vxxx)
    timestamp = _make_tz_aware(timestamp)

    with warnings.catch_warnings():
        return float(round(solar.get_azimuth(lat, lon, timestamp), 2))


def get_sun_zenith(lat: float, lon: float, timestamp: datetime.datetime):
    """Calculate the sun zenith using pysolar.

    Check if timestamp is timezone aware, if not add UTC timezone. Get the sun zenith.
    Returned sun zenith is horizon referenced. 0 is at the horizon, +90 at zenith, -90 nadir.

    Args:
        lat (float): latitude (format xxx.yyyyyy)
        lon (float): longitude (format xxx.yyyyyy)
        timestamp (datetime.datetime): time for calculation.

    Returns:
        float: sun zenith (-90 , 90), rounded to 2 decimals
    """
    # check if timestamp is timezone aware (needed for PySolar >vxxx)
    timestamp = _make_tz_aware(timestamp)
    with warnings.catch_warnings():
        return float(round(solar.get_altitude(lat, lon, timestamp), 2))


def _make_tz_aware(timestamp: datetime.datetime):
    """Make sure timestamp is timezone aware.

    If timestamp is not aware, add UTC timezone

    Args:
        timestamp (datetime.datetime): timestamp to be checked

    Returns:
        datetime.datetime: aware timestamp
    """
    if not timestamp.tzname():
        log.info(f'timestamp {timestamp} is has no timezone information. Assuming UTC.')
        timestamp = timestamp.replace(tzinfo=pytz.UTC)
    return timestamp
