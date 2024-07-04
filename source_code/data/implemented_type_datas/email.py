from validators.email import email
from source_code.data.data import Data
from source_code.data.data_type import Data_Type


class Email(Data):
    def __init__(self, data):
        super().__init__(data, Data_Type.EMAIL)

    def check_format(self, data):
        if email(data):
            return True
        else:
            return False
