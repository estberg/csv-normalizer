from .utf8 import UTF8
from datetime import timedelta
import sys

class Duration(UTF8):
    def normalize(self, input):
        try:
            input = super().normalize(input)
            hours, minutes, seconds_and_milliseconds = input.split(":")
            seconds, milliseconds = seconds_and_milliseconds.split(".")
            hours, minutes, seconds, milliseconds = [int(i) for i in [hours, minutes, seconds, milliseconds]]
            duration = timedelta(hours=hours, minutes=minutes, seconds=seconds, milliseconds=milliseconds)
            return duration.total_seconds()
        except:
            print(input, file=sys.stderr)
            raise ValueError