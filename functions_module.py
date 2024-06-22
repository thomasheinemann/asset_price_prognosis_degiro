# This module provides functions for date and time issues

# some basic packages / modules
import pandas as pd

# library for estimator base class
from datetime import datetime, timedelta
import pandas as pd

# time conversion function from minutes to hh:mm
def convert_minutes_to_time(minutes):
    hours = minutes // 60
    minutes_remaining = minutes % 60
    return f"{hours:02d}:{minutes_remaining:02d}"

# Convert convert minutes to time (hh:mm) from reference time (hh:mm)
def convert_minutes_to_time_from_reference_time(minutes, reference_time):
    
    return str(timedelta(minutes=minutes+convert_time_to_minutes(reference_time)))

# time conversion function from hh:mm to minutes
def convert_time_to_minutes(time):
    hours, minutes = map(int, time.split(':'))
    return hours * 60 + minutes

# Get the current date
def current_date():
    return datetime.now().strftime("%Y-%m-%d")

# Get the upcoming working day from a given day
def next_working_day(date):
    
    # Define the input date
    input_date = datetime.strptime(date, '%Y-%m-%d')

    # Calculate the next working day
    next_working_day = input_date + timedelta(days=1)
    while next_working_day.weekday() not in range(5):
        next_working_day += timedelta(days=1)
    return next_working_day.strftime('%Y-%m-%d')