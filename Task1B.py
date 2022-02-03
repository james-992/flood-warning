from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list


def run():
    """requirement for task 1b"""
    
    #   build list of stations from stationdata module
    stations = build_station_list()

    #   create coordinate p used for sorting
    p = (52.2053, 0.1218)

    #   create list of every sorted station
    stations_sorted = stations_by_distance(stations ,p)

    #   create new list for the 10 closest and 10 farthest stations
    stations_closest = stations_sorted[:10]
    stations_farthest =  stations_sorted[-10:]
    
    return stations_closest, stations_farthest

