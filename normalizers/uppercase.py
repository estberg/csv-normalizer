from .utf8 import UTF8

class Uppercase(UTF8):
    def normalize(self, input):
        input = super().normalize(input)
        return input.encode('utf-8').decode('utf-8').upper()

