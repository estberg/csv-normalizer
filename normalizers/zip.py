from .utf8 import UTF8

class Zip(UTF8):
    def normalize(self, input):
        input = super().normalize(input)
        if not input.isnumeric():
            raise ValueError
        #TODO: does this work if it is not a str but a bytearray?
        return input.zfill(5)