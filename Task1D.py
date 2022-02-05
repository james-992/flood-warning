from floodsystem.stationdata import build_station_list
from floodsystem.geo import *

stations = build_station_list()

"""
#check one, which print how many rivers have at least one monitoring station 
and prints the first 10 of these rivers in alphabetical order
"""


print("the number of rivers with at least one station is:")
listofrivers = rivers_with_station(stations)

sortedlist = sorted(listofrivers)
print (len(sortedlist))

print("the first 10 rivers in the list are:")
print (sortedlist[:10])


"""
Check two, where a list of the name of stations is printed for given rivers

"""
stationsonriver = stations_by_river(stations)

#a function which return a sorted list of the names of stations for a given river
def stationsongivenriver(stationsonriver, river):
    listedstations = stationsonriver[river] 
    stationnames = []
    for station in listedstations:
        stationnames.append(station.name) 
    
    return sorted(stationnames)

river = "River Thames"

print ("the stations on", river, " are:\n", stationsongivenriver(stationsonriver, river))
    

