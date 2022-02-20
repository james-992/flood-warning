from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels

def run():

    #   build and update the lsit of stations
    stations = build_station_list()
    update_water_levels(stations)

    #   set variable N
    N = 5

    #   Print out stations as the questions requests
    for station in stations_highest_rel_level(stations, N):
        print(station)
    


if __name__ == "__main__":
    "Running Task2C..."
    run()