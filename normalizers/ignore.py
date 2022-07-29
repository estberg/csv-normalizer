from .base import Base

class Ignore(Base):
    def normalize(self, input):
        return None

