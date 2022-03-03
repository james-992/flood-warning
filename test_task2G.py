from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import *
from floodsystem.analysis import *
from floodsystem.flood import stations_highest_rel_level, stations_over_threshold
from floodsystem.plot import *
from floodsystem.datafetcher import *
import numpy
from floodsystem.stationdata import MonitoringStation


def test_2G():
    stations = build_station_list()
    update_water_levels(stations)

    
