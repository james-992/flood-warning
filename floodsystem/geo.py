# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from haversine import haversine, Unit

from .utils import sorted_by_key  # noqa


def stations_by_distance(stations, p):
    """sorts stations by distance using haversine formula, then returns the closest and farthest 10"""

    #   sort the station list by distance using haversine formula
    stations_sorted = sorted(stations, key=lambda station: haversine(p, station.coord))

    #   empty list that will eventually contain [stations_sorted] but with name, town, distance
    stations_ordered = []
    
    print(stations_sorted)

    #   iterate over the sorted stations
    for station in stations_sorted:
        #   append tuples with required data into empty list
        stations_ordered.append((station.name, station.town, haversine(p, station.coord)))

    #   slice the array 
    closest_ten_stations = stations_ordered[:10]
    farthest_ten_stations = stations_ordered[-10:]

    return closest_ten_stations, farthest_ten_stations


def stations_within_radius(stations, centre, r):
    """returns stations within radius r if centrepoint"""

    #   creating empty list to append to
    stations_in_radius = []

    #   iterate over the complete list of stations
    for station in stations:
        #   compare distance of station to radius r
        if haversine(centre, station.coord) < r:
            #   append stations to empty list
            stations_in_radius.append(station.name)
        else:
            pass
    

    #   sort the final list of stations within radius alphabetically
    return sorted(stations_in_radius)
