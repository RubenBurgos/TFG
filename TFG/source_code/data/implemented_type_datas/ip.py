from data import Data
from data_type import Data_Type

class IP(Data):
    def __init__(self, data):
        super().__init__(data, Data_Type.IP)

    def check_format(self, data):
        pass