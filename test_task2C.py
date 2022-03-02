from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels

def test_list_characteristics():
    stations = build_station_list()
    update_water_levels(stations)

    for n in range (1, 15):
        assert len(stations_highest_rel_level(stations, n)) == n
        assert type(stations_highest_rel_level(stations, n)) == tuple
        assert type(stations_highest_rel_level(stations, n)[0]) == str
        assert type(stations_highest_rel_level(stations, n)[1]) == float
    
