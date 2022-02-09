# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""

from . import datafetcher



class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    def typical_range_consistent(self):
        """checks high/low range data for consistency"""

        #   check for inconsistent data
        if self.typical_range is None:
            return False
        elif self.typical_range[0] <= self.typical_range[1]:
            return True
        elif self.typical_range[0] > self.typical_range[1]:
            return False
        

def inconsistent_typical_range_stations(stations):
    """given list of stations, returns list of stations with inconsistent data"""

    #   set empty list to append to
    inconsistent_stations = []

    #   list for the data, purely for assertions
    inconsistent_data = []

    #   iterate over the stations in the list of all stations
    for station in stations:
        #   use typical_Range_consistent method to append the station name to the list of inconsistent stations if the data IS inconsistent
        if MonitoringStation.typical_range_consistent(station) is False:
            inconsistent_stations.append(station.name)
            inconsistent_data.append(station.typical_range)
        else:
            pass

    return inconsistent_stations, inconsistent_data
