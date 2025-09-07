from src.utils.config import Errors
class NoBrokerConnection(Exception):
    def __init__(self):
        super().__init__(Errors.NO_BROKER_CONNECTION)