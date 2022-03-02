

from floodsystem.stationdata import build_station_list, update_water_levels


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




if __name__ == "__main__":
    print("Task 2G running...")
    run()