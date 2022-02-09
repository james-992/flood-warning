from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

stations = build_station_list()

radius = 10

centre_coord = (52.2053, 0.1218)

stations_in_radius = stations_within_radius(stations, centre_coord, radius)

def test_list_types():
    
    for station in stations_in_radius:
        assert type(station) == str