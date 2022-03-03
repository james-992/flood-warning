

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import *
from floodsystem.analysis import *
from floodsystem.flood import stations_highest_rel_level, stations_over_threshold
from floodsystem.plot import *
from floodsystem.datafetcher import *
import numpy
from floodsystem.stationdata import MonitoringStation



def risk_values(station):
    lower, upper = station.typical_range
    typicalrange = upper - lower
    #short range derivative
    p = 4
    dt = 1
    print(station)
    dates, levels = (fetch_measure_levels(station.measure_id,
                                        dt=datetime.timedelta(days=dt)))

    print(levels)

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
    h = MonitoringStation.relative_water_level(station)


    if derivative2now > 6:
        derivative2now = 6
        

    #returns the derivative scaled relative to the typical range from both 1 day and 1 week
    return h, derivative1now/typicalrange, derivative2now/typicalrange

"""N = 5
stations = build_station_list()
update_water_levels(stations)

for station in stations_highest_rel_level(stations, (N+1)):
    station_name = station[0]
    #specific_station = None
    if station[0] == "Letcombe Bassett":
        print("Letcombe Bassett is not shown, it's data is bad")
        pass 
    else: 
        for station_obj in stations:
            if station_obj.name == station_name:
                specific_station = station_obj
                h, derivative1, derivative2 = risk_values(specific_station)
                print(station_name, h, derivative1, derivative2)

            else:
                pass"""



def run():
    """Assessing flood risk based off the implementations done in both milestones. Rated from 'severe', 'high', 'moderate', and 'low.
        Should list the TOWNS where flood risk is greatest'"""
    
    stations = build_station_list()
    update_water_levels(stations)

    print(risk_values(stations[0]))

    #   WAYS OF MEASURING RISK
    #   - stations_with_highest_rel_level()
    #   - stations_over_threshold()

    #   Weighted sum?
    #   Find the change in river level over the previous couple days - is it increasing? USE TASK 2F POLYNOMIAL - CALC DY/DX

    C1 = 1
    C2 = 1

    low = 1.0
    moderate = 1.5
    high = 2.0
    severe = 2.5


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

    classification_list_init = []

    for station in stations_above_threshold:
        

        if station.name == "Letcombe Bassett":
            continue
        """if station.name == "Bissoe":
            continue
        else:"""

        try:
            h, grad1, grad2 = risk_values(station)

            risk_factor = h + C1*grad1 + C2*grad2

            if risk_factor >= low:
                classification_list_init.append((station.town, "low"))
            elif risk_factor >= moderate:
                classification_list_init.append((station.town, "moderate"))
            elif risk_factor >= high:
                classification_list_init.append((station.town, "high"))
            elif risk_factor >= severe:
                classification_list_init.append((station.town, "severe"))
        
        except KeyError or IndexError:
            print(station.name)
        
    print(classification_list_init)

    classification_list = []
    for station in classification_list_init:
        if station[0] not in classification_list:
            classification_list.append(station[0])
    








if __name__ == "__main__":
    print("Task 2G running...")
    run()