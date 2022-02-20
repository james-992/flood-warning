"""for task 2B"""

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


def stations_highest_rel_level(stations, N):
    """returns list of N stations where the relative water level is highest"""

    #   Set empty list
    stations_with_high_level = []


    for station in stations:
        #   collect relative water level        
        relative_water_level = MonitoringStation.relative_water_level(station)

        #   ignore inconsistent data
        if relative_water_level is None:
            pass
        else:
            #   append station name and rel. water level to list
            stations_with_high_level.append((station.name, relative_water_level))
    
    #   sort the stations in descending order 
    sorted_stations = sorted(stations_with_high_level, key=lambda tuple: tuple[1], reverse=True)

    #   slice the array for N stations
    return sorted_stations[:N]
