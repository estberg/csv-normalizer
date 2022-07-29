from .utf8 import UTF8
from datetime import datetime
import pytz

class Timestamp(UTF8):
    def normalize(self, input):
        input = super().normalize(input)
        date = datetime.strptime(input, "%m/%d/%y %I:%M:%S %p")
        pacific = pytz.timezone('US/Pacific')
        pacific_date = pacific.localize(date)
        return pacific_date.astimezone(pytz.timezone('US/Eastern')).isoformat()

