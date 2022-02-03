from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list


def run():
    """requirement for task 1b"""

    #   build list of stations from stationdata module
    stations = build_station_list()

    #   create coordinate p used for sorting
    p = (52.2053, 0.1218)

    #   create list of every sorted station
    closest, farthest = stations_by_distance(stations ,p)

    print (closest)
    print()
    print (farthest)


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()