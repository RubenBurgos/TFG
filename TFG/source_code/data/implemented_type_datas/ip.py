import ipaddress
from source_code.data.data import Data
from source_code.data.data_type import Data_Type


class IP(Data):
    def __init__(self, data):
        super().__init__(data, Data_Type.IP)

    def check_format(self, data):
        try:
            ipaddress.ip_address(data)
            return True
        except:
            return False

a = IP("127.0.0.1")
print(a.data_type)
