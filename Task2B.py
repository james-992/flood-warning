from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_over_threshold



def run():
    """Requirement for task 2B"""

    #   create station list
    stations = build_station_list()

    #   tolerance variable
    tol = 3

    #   produce list of stations with river levels above the tolerance
    stations_above_threshold = stations_over_threshold(stations, tol)

    #   print out these stations in required format
    for station in stations_above_threshold:
        print(station)



if __name__ == "__main__":
    print("Task 2B Running...")
    run()
