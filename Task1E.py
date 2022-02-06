from floodsystem.stationdata import build_station_list
from floodsystem.geo import *
#this isn't finished yet
stations = build_station_list()
"""
A function which determines the rivers with the greatest number of monitoring stations.
It returns a list of (river name, number of stations) tuples, 
sorted by the number of stations. In the case that there are more rivers
with the same number of stations as the N th entry, include these rivers in the list
"""

#def rivers_by_station_number(stations, N):


def stationsongivenriver(stations, river):
    stationsonriver = stations_by_river(stations)
    listedstations = stationsonriver[river] 
    stationnames = []
    for station in listedstations:
        stationnames.append(station.name) 
    
    return sorted(stationnames)

river = "River Thames"
print (stationsongivenriver(stationsonriver, river))

