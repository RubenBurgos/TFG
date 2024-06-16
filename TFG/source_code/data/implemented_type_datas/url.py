from validators.url import url
from source_code.data.data import Data
from source_code.data.data_type import Data_Type


class URL(Data):
    def __init__(self, data):
        super().__init__(data, Data_Type.URL)

    def check_format(self, data):
        if url(data):
            return True
        else:
            return False
