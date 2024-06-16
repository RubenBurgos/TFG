from source_code.data.data import Data
from source_code.data.data_type import Data_Type


class Key_String(Data):
    def __init__(self, data):
        super().__init__(data, Data_Type.KEY_STRING)

    def check_format(self, data):
        if type(data) == str:
            return True
        else:
            return False
