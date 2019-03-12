from datetime import datetime
from datetime import timedelta
import math


def add_gigasecond(moment):
    return moment + timedelta(seconds=pow(10, 9))