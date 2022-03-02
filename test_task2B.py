from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_over_threshold


def test_extreme_cases():
    stations = build_station_list()
    #   check for any erroneous data
    assert len(stations_over_threshold(stations, 1000)) == 0
    #   check there is data coming in
    assert len(stations_over_threshold(stations, 0)) >= 1

def test_tuple_types():
    stations = build_station_list()
    for station in stations_over_threshold(stations, 0):
        assert type(station[0]) == str
        assert type(station[1]) == float