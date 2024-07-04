from validators.domain import domain
from source_code.data.data import Data
from source_code.data.data_type import Data_Type


class Domain(Data):
    def __init__(self, data):
        super().__init__(data, Data_Type.DOMAIN)

    def check_format(self, data):
        if domain(data):
            return True
        else:
            return False
