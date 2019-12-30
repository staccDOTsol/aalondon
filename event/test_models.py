from django.test import TestCase

# Create your tests here.
from .models import get_recurrant_dates
import datetime


def test_get_recurrant_dates_every_month_on_first_monday():
    start_date = datetime.date(2020, 1, 6) 
    end_date = datetime.date(2020, 4, 7)
    day_index,day,month_index,start_date = 0,0,0,start_date
    returned_dates = get_recurrant_dates(day_index,day,month_index,start_date,end_date)
    expected_dates = [datetime.date(2020, 1, 6),datetime.date(2020, 2, 3),datetime.date(2020, 3, 2),datetime.date(2020, 4, 6)] 
    assert returned_dates == expected_dates

def test_get_recurrant_dates_every_month_on_second_monday():
    start_date = datetime.date(2020, 1, 13) 
    end_date = datetime.date(2020, 4, 13)
    day_index,day,month_index,start_date = 1,0,0,start_date
    returned_dates = get_recurrant_dates(day_index,day,month_index,start_date,end_date)
    expected_dates = [datetime.date(2020, 1, 13),datetime.date(2020, 2, 10),datetime.date(2020, 3, 9),datetime.date(2020, 4, 13)] 
    assert returned_dates == expected_dates

def test_get_recurrant_dates_every_month_on_third_wednesday():
    start_date = datetime.date(2020, 1, 15) 
    end_date = datetime.date(2020, 4, 15)
    day_index,day,month_index,start_date = 2,0,0,start_date
    returned_dates = get_recurrant_dates(day_index,day,month_index,start_date,end_date)
    expected_dates = [datetime.date(2020, 1, 15),datetime.date(2020, 2, 19),datetime.date(2020, 3, 18),datetime.date(2020, 4, 15)] 
    assert returned_dates == expected_dates


def test_get_recurrant_dates_every_month_on_fourth_thursday():
    start_date = datetime.date(2020, 1, 23) 
    end_date = datetime.date(2020, 4, 23)
    day_index,day,month_index,start_date = 3,0,0,start_date
    returned_dates = get_recurrant_dates(day_index,day,month_index,start_date,end_date)
    expected_dates = [datetime.date(2020, 1, 23),datetime.date(2020, 2, 27),datetime.date(2020, 3, 26),datetime.date(2020, 4, 23)] 
    assert returned_dates == expected_dates

def test_get_recurrant_dates_every_month_on_last_friday():
    start_date = datetime.date(2020, 1, 31) 
    end_date = datetime.date(2020, 4, 24)
    day_index,day,month_index,start_date = -1,0,0,start_date
    returned_dates = get_recurrant_dates(day_index,day,month_index,start_date,end_date)
    expected_dates = [datetime.date(2020, 1, 31),datetime.date(2020, 2, 28),datetime.date(2020, 3, 27),datetime.date(2020, 4, 24)] 
    assert returned_dates == expected_dates

### EVERY SECOND MONTH TESTS ###
def test_get_recurrant_dates_every_second_month_on_first_monday():
    start_date = datetime.date(2020, 1, 6) 
    end_date = datetime.date(2020, 5, 4)
    day_index,day,month_index,start_date = 0,0,1,start_date
    returned_dates = get_recurrant_dates(day_index,day,month_index,start_date,end_date)
    expected_dates = [datetime.date(2020, 1, 6),datetime.date(2020, 3, 2),datetime.date(2020, 5, 4)] 
    assert returned_dates == expected_dates

def test_get_recurrant_dates_every_second_month_on_second_monday():
    start_date = datetime.date(2020, 1, 13) 
    end_date = datetime.date(2020, 3, 9)
    day_index,day,month_index,start_date = 1,0,1,start_date
    returned_dates = get_recurrant_dates(day_index,day,month_index,start_date,end_date)
    expected_dates = [datetime.date(2020, 1, 13),datetime.date(2020, 3, 9)] 
    assert returned_dates == expected_dates

def test_get_recurrant_dates_every_second_month_on_third_wednesday():
    start_date = datetime.date(2020, 1, 15) 
    end_date = datetime.date(2020, 4, 15)
    day_index,day,month_index,start_date = 2,0,1,start_date
    returned_dates = get_recurrant_dates(day_index,day,month_index,start_date,end_date)
    expected_dates = [datetime.date(2020, 1, 15),datetime.date(2020, 3, 18)] 
    assert returned_dates == expected_dates


def test_get_recurrant_dates_every_second_month_on_fourth_thursday():
    start_date = datetime.date(2020, 1, 23) 
    end_date = datetime.date(2020, 4, 23)
    day_index,day,month_index,start_date = 3,0,1,start_date
    returned_dates = get_recurrant_dates(day_index,day,month_index,start_date,end_date)
    expected_dates = [datetime.date(2020, 1, 23),datetime.date(2020, 3, 26)] 
    assert returned_dates == expected_dates

def test_get_recurrant_dates_every_second_month_on_last_friday():
    start_date = datetime.date(2020, 1, 31) 
    end_date = datetime.date(2020, 4, 24)
    day_index,day,month_index,start_date = -1,0,1,start_date
    returned_dates = get_recurrant_dates(day_index,day,month_index,start_date,end_date)
    expected_dates = [datetime.date(2020, 1, 31),datetime.date(2020, 3, 27)] 
    assert returned_dates == expected_dates



### Every Third Month ###


def test_get_recurrant_dates_every_third_month_on_first_monday():
    start_date = datetime.date(2020, 1, 6) 
    end_date = datetime.date(2020, 7, 6)
    day_index,day,month_index,start_date = 0,0,2,start_date
    returned_dates = get_recurrant_dates(day_index,day,month_index,start_date,end_date)
    expected_dates = [datetime.date(2020, 1, 6),datetime.date(2020, 4, 6),datetime.date(2020, 7, 6)] 
    assert returned_dates == expected_dates



def test_get_recurrant_dates_every_third_month_on_second_monday():
    start_date = datetime.date(2020, 1, 13) 
    end_date = datetime.date(2020, 4, 13)
    day_index,day,month_index,start_date = 1,0,2,start_date
    returned_dates = get_recurrant_dates(day_index,day,month_index,start_date,end_date)
    expected_dates = [datetime.date(2020, 1, 13),datetime.date(2020, 4, 13)] 
    assert returned_dates == expected_dates

def test_get_recurrant_dates_every_third_month_on_third_wednesday():
    start_date = datetime.date(2020, 1, 15) 
    end_date = datetime.date(2020, 4, 15)
    day_index,day,month_index,start_date = 2,0,2,start_date
    returned_dates = get_recurrant_dates(day_index,day,month_index,start_date,end_date)
    expected_dates = [datetime.date(2020, 1, 15),datetime.date(2020, 4, 15)] 
    assert returned_dates == expected_dates


def test_get_recurrant_dates_every_third_month_on_fourth_thursday():
    start_date = datetime.date(2020, 1, 23) 
    end_date = datetime.date(2020, 4, 23)
    day_index,day,month_index,start_date = 3,0,2,start_date
    returned_dates = get_recurrant_dates(day_index,day,month_index,start_date,end_date)
    expected_dates = [datetime.date(2020, 1, 23),datetime.date(2020, 4, 23)] 
    assert returned_dates == expected_dates

def test_get_recurrant_dates_every_third_month_on_last_friday():
    start_date = datetime.date(2020, 1, 31) 
    end_date = datetime.date(2020, 4, 24)
    day_index,day,month_index,start_date = -1,0,2,start_date
    returned_dates = get_recurrant_dates(day_index,day,month_index,start_date,end_date)
    expected_dates = [datetime.date(2020, 1, 31),datetime.date(2020, 4, 24)] 
    assert returned_dates == expected_dates
