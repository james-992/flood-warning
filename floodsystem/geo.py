# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from haversine import haversine, Unit

from .utils import sorted_by_key  # noqa


def stations_by_distance(stations, p):
    """sorts stations by distance using haversine formula, then returns the closest and farthest 10"""

    #   sort the station list by distance using haversine formula
    stations_sorted = sorted(stations, key=lambda station: haversine(p, station.coord))

    #   empty list that will eventually contain [stations_sorted] but with name, town, distance
    stations_ordered = []
    
    #print(stations_sorted)

    #   iterate over the sorted stations
    for station in stations_sorted:
        #   append tuples with required data into empty list
        stations_ordered.append((station.name, station.town, haversine(p, station.coord)))

    #   slice the array 
    closest_ten_stations = stations_ordered[:10]
    farthest_ten_stations = stations_ordered[-10:]

    return closest_ten_stations, farthest_ten_stations


def stations_within_radius(stations, centre, r):
    """returns stations within radius r if centrepoint"""

    #   creating empty list to append to
    stations_in_radius = []

    #   iterate over the complete list of stations
    for station in stations:
        #   compare distance of station to radius r
        if haversine(centre, station.coord, unit=Unit.KILOMETERS) < r:
            #   append stations to empty list
            stations_in_radius.append(station.name)
        else:
            pass
    

    #   sort the final list of stations within radius alphabetically
    return sorted(stations_in_radius)



def rivers_with_station(stations):

    #creates a blank set for the names of rivers to be added to
    allrivers = set()

    #gets town name and only adds it to the set, which does not contain duplicates
    for station in stations:
        allrivers.add(station.river)

    return allrivers




#creates a dictionary which links a river name to all stations on that river, and the data included
def stations_by_river(stations):
    #creates a blank dictionary 
    stationsbyriver = {}


    for station in stations:
        #checks to see if this river is allready in the dictionary 
        #(this may be redundant, and could be made more efficiant)
        if station.river in stationsbyriver:
            #adds the new station to the river in the dictionary 
            existingstations = stationsbyriver[station.river]
            existingstations.append(station)
    
            stationsbyriver[station.river] = existingstations

        
        else:
            #creates the new river in the dictionary, with the station

            stationsbyriver[station.river] = [station]             

    return stationsbyriver


"""
Task E
A function which determines the rivers with the greatest number of monitoring stations.
It returns a list of (river name, number of stations) tuples, 
sorted by the number of stations. In the case that there are more rivers
with the same number of stations as the N th entry, include these rivers in the list
"""



# cycles through the list of river names generated previously fed into a function which returns the 
# names of stations on the river.  
def rivers_by_station_number(stations, N):

    def stationsongivenriver(stations, river):
        stationsonriver = stations_by_river(stations)
        listedstations = stationsonriver[river] 
        stationnames = []
        for station in listedstations:
            stationnames.append(station.name) 
    
        return sorted(stationnames)

    allrivers = rivers_with_station(stations)
    riverswithstationno = []
    for river in allrivers:
        noofstations = len(stationsongivenriver(stations, river))
        #makes a tuple with river name and number of stations and adds it to the list

        riverwithstationno = (river, noofstations)
        riverswithstationno.append(riverwithstationno)
    #sorts the list from highest to lowest number of stations
  
    sortedlist = sorted(riverswithstationno, key=lambda i: i[-1], reverse = True)
    finallist = []

    counter = 0 
    #adds rivers to the list untill it has added N number of rivers
    while counter < N:

        finallist.append(sortedlist[counter])
        counter +=1

    #if the number of stations in the next river in the list is the same as the last, it
    #continues to add these rivers to the list untill the condition is no longer met
    while sortedlist[counter-1][1] == sortedlist[counter][1]:
        finallist.append(sortedlist[counter])
        counter += 1

    return finallist







