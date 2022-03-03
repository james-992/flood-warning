

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import *
from floodsystem.analysis import *
from floodsystem.flood import stations_highest_rel_level, stations_over_threshold
from floodsystem.plot import *
from floodsystem.datafetcher import *
import numpy


def find_rate_of_change(station):
    lower, upper = station.typical_range
    typicalrange = upper - lower
    #short range derivative
    p = 4
    dt = 1
    dates, levels = (fetch_measure_levels(station.measure_id,
                                        dt=datetime.timedelta(days=dt)))
    poly, d0 = polyfit(dates, levels, p)
    derivative1 = numpy.polyder(poly, m=1)   
    derivative1now = derivative1(0)
    #long range derivative
    dt = 7
    p = 4
    dates, levels = (fetch_measure_levels(station.measure_id,
                     dt=datetime.timedelta(days=dt)))  

    poly, d0 = polyfit(dates, levels, p)
    derivative2 = numpy.polyder(poly, m=1)   
    derivative2now = derivative2(0)
    return derivative1now/typicalrange, derivative2now/typicalrange

"""N = 5
stations = build_station_list()
update_water_levels(stations)

for station in stations_highest_rel_level(stations, (N+1)):
    station_name = station[0]
    #specific_station = None
    if station[0] == "Letcombe Bassett":
        print("Letcombe Bassett is not shown, it's data is codswallop")
        pass 
    else: 
        for station_obj in stations:
            if station_obj.name == station_name:
                specific_station = station_obj
                derivative1, derivative2 = find_rate_of_change(specific_station)
                print(station_name, derivative1, derivative2)

            else:
                pass"""
            
            
                


                        




def run():
    """Assessing flood risk based off the implementations done in both milestones. Rated from 'severe', 'high', 'moderate', and 'low.
        Should list the TOWNS where flood risk is greatest'"""
    
    stations = build_station_list()
    update_water_levels(stations)

    #   WAYS OF MEASURING RISK
    #   - stations_with_highest_rel_level()
    #   - stations_over_threshold()

    #   Weighted sum?
    #   Find the change in river level over the previous couple days - is it increasing? USE TASK 2F POLYNOMIAL - CALC DY/DX
    #   


    tol = 1

    #   find stations above arbitrary tolerance
    stations_above_threshold_init = stations_over_threshold(stations, tol)

    #   create empty list for the station obj to be appended to
    stations_above_threshold = []

    for station in stations_above_threshold_init:
        
        for station_obj in stations:
            #   finding the station objects

            if station[0] == station_obj.name:
                stations_above_threshold.append(station_obj)

    classification_list = []

    for station in stations_above_threshold:
        h, grad1, grad2 = find_rate_of_change()

        risk_factor = 







if __name__ == "__main__":
    print("Task 2G running...")
    run()