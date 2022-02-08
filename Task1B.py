from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list


def run():
    """requirement for task 1b -> list 10 closest and farthest stations from coordinate p"""

    #   build list of stations from stationdata module
    stations = build_station_list()

    #   create coordinate p used for sorting
    p = (52.2053, 0.1218)

    #   create list of every sorted station
    closest, farthest = stations_by_distance(stations ,p)

    print (closest)
    print()
    print (farthest)


    #   Assertions
    for station in closest:
        #   checking that types are correct
        assert type(station[0]) == str
        assert type(station[1]) == str
        assert type(station[2]) == float

    for station in farthest:
        assert type(station[0]) == str
        assert type(station[1]) == str
        assert type(station[2]) == float

    #   checking length of lists is correct
    assert len(closest) == 10
    assert len(farthest) == 10

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()

    
