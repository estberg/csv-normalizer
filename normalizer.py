#!/usr/bin/env python

import sys
import csv
import traceback
from normalizers.ignore import Ignore
from normalizers.duration import Duration
from normalizers.uppercase import Uppercase
from normalizers.utf8 import UTF8
from normalizers.timestamp import Timestamp
from normalizers.zip import Zip

DELIMITER = ','
COLUMNS = ['Timestamp', 'Address', 'ZIP', 'FullName', 'FooDuration', 'BarDuration', 'TotalDuration', 'Notes']
NORMALIZERS = [Timestamp(), UTF8(), Zip(), Uppercase(), Duration(), Duration(), Ignore(), UTF8()]

def normalizer():
    try:
        columns = input()
        print(columns)
        #TODO: handle column header normalization?
        #TODO: handle case where the columns are in a different order?
    except EOFError:
        print("Missing 1st row with column headers", file=sys.stderr)
        return 1
    writer = csv.writer(sys.stdout)
    while True:
        try:
            next = input()
            line = next.splitlines()
            reader = csv.reader(line, delimiter=DELIMITER)
            row = list(reader)[0]
            if len(row) != len(COLUMNS):
                print("Invalid data, row has {} columns but should have {} columns".format(len(row), len(columns)), file=sys.stderr)
            else:
                result = [NORMALIZERS[i].normalize(contents) for i, contents in enumerate(row)]
                result[-2] = result[-4] + result[-3] # calculate total duration
                writer.writerow(result)
        except EOFError:
            break
        except Exception as e:
            print("Row has invalid data {}".format(next), file=sys.stderr)
            traceback.print_exception(type(e), e, e.__traceback__, file=sys.stderr)
    return 0


if __name__ == '__main__':
    sys.exit(normalizer())
    