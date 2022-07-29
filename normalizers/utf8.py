from .base import Base

class UTF8(Base):
    def normalize(self, input):
        input = super().normalize(input)
        return input.encode('utf-8').decode('utf-8', 'replace')