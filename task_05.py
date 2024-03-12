import datetime
from datetime import *


def date_in_future(integer=0):
    if isinstance(integer, int):
        return (datetime.now() + timedelta(days=integer)).strftime('%d-%m-%Y %H:%M:%S')
    else:
        return datetime.now().strftime('%d-%m-%Y %H:%M:%S')


print(date_in_future())
