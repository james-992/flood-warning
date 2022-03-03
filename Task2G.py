

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
    h = MonitoringStation.relative_water_level(station)

    #   setting a limit for the derivative over the shorter time period as it is susceptible to being very high
    d2lim = 6
    if derivative2now > d2lim or derivative2now < (-d2lim):
        derivative2now = d2lim

    #returns the derivative scaled relative to the typical range from both 1 day and 1 week
    return h, derivative1now/typicalrange, derivative2now/typicalrange



def run():
    """Assessing flood risk based off the implementations done in both milestones. Rated from 'severe', 'high', 'moderate', and 'low.
        Should list the TOWNS where flood risk is greatest'"""
    
    #   build and update station list
    stations = build_station_list()
    update_water_levels(stations)

    #   define risk factor coefficients
    C0 = 3
    C1 = 1
    C2 = 0.5

    #   define risk level limits
    moderate = 1.5
    high = 3.0
    severe = 8.0

    #   threshold tolerance for rel water level
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
        
        if station.name == "Letcombe Bassett" or station.town == None:
            continue


        #   Spot errors in data and do not use them
        try:
            h, grad1, grad2 = risk_values(station)
        except IndexError:
            print("Inconsistent data, the problematic station is: ", station.name)
            continue
        

        #   Defining our 'risk_factor'
        risk_factor = (C0*(h-tol)) + (C1*grad1) + (C2*grad2)

        #   apply different risk levels dependent on risk factor
        if risk_factor < 0:
            continue
        elif risk_factor <= moderate:
            classification_list_init.append((station.town, risk_factor, "low"))
        elif risk_factor <= high:
            classification_list_init.append((station.town, risk_factor,"moderate"))
        elif risk_factor <= severe:
            classification_list_init.append((station.town, risk_factor,"high"))
        else:
            classification_list_init.append((station.town, risk_factor,"severe"))
    
        

    #   empty list for non-duplicate towns
    classification_list = []

    for station in classification_list_init:
        #   iterating over full list of risky towns

        if station[0] not in classification_list:
            classification_list.append(station) 
    
    #   sorting into separate lists:
    low_risk_stations = []
    moderate_risk_stations = []
    high_risk_stations = []
    severe_risk_stations = []

    for station in classification_list:
        if station[2] == 'low':
            low_risk_stations.append(station[0])
        elif station[2] == 'moderate':
            moderate_risk_stations.append(station[0])
        elif station[2] == 'high':
            high_risk_stations.append(station[0])
        elif station[2] == 'severe':
            severe_risk_stations.append(station[0])



    print("There are", len(low_risk_stations), "low risk towns:")
    for station in low_risk_stations:
        print(station)

    print("There are", len(moderate_risk_stations), "moderate risk towns:")
    for station in moderate_risk_stations:
        print(station)
    
    print("There are", len(high_risk_stations), "high risk towns:")
    for station in high_risk_stations:
        print(station)

    print("There are", len(severe_risk_stations), "severe risk towns:")
    for station in severe_risk_stations:
        print(station)
    





if __name__ == "__main__":
    print("Task 2G running...")
    run()