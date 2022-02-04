from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

def run():
    """requirement for task 1C"""

    #   Request a list of the stations such that they can be manipulated
    stations = build_station_list()

    #   radius for function - in km
    radius = 10
    #   Centrepoint for the radius check
    centre_coord = (52.2053, 0.1218)

    print(stations_within_radius(stations, centre_coord, radius))


if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()