from floodsystem.stationdata import build_station_list


stations = build_station_list()

def rivers_with_station(stations):

    #creates a blank set for the towns to be added to
    alltowns = set()

    #gets town name and only adds it to the set, which does not contain duplicates
    for station in stations:
        alltowns.add(station.town)

    return alltowns

print(rivers_with_station(stations))

def stations_by_river(stations):
    #creates a blank dictionary 
    objectsbyriver = {}
    

