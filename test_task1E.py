from floodsystem.stationdata import build_station_list
from floodsystem.geo import *


def test_list_types():
    stations = build_station_list()
    samplelist = rivers_by_station_number(stations, 40) 

    assert type(samplelist) == list
    assert type(samplelist[0]) == tuple
    
def test_list_length_check():
    stations = build_station_list()
    samplelist = rivers_by_station_number(stations, 40) 

    assert len(rivers_by_station_number(stations, 40)) == 47
    assert len(rivers_by_station_number(stations, 20)) < len(samplelist)
    assert len(rivers_by_station_number(stations, 13)) == len(rivers_by_station_number(stations, 14))