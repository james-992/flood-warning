

from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations


def run():
    """requirement for task 1F"""

    stations = build_station_list()

    #   call function from .station submodule to use built list of stations and also sort them alphabetically 
    inconsistent_stations, inconsistent_data = inconsistent_typical_range_stations(stations)

    inconsistent_stations.sort()

    print(inconsistent_stations)

    #   Assertions
    assert len(inconsistent_data) == len(inconsistent_stations)
    


if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()