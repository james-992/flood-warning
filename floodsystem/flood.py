"""for task 2B"""

from turtle import update

from sympy import monic
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import update_water_levels

def stations_over_threshold(stations, tol):
    """returns all stations with a water level over a threshold ratio"""

    #Update list of station objects
    update_water_levels(stations)

    stations_over_tol = []

    #iterate over stations
    for station in stations:

        #   define the relative water level ratio using the method relative_water_level
        relative_water_level = MonitoringStation.relative_water_level(station)

        #   Ignore inconsistent data 
        if relative_water_level is None:
            pass

        elif relative_water_level > tol:
            #create new list with stations over tolerance
            stations_over_tol.append((station.name, relative_water_level))
            
    
    return sorted(stations_over_tol, key=lambda tuple: tuple[1], reverse=True)