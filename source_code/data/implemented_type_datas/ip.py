from source_code.data.data import Data
from validators.ip_address import ipv4, ipv6
from source_code.data.data_type import Data_Type


class IP(Data):
    def __init__(self, data):
        super().__init__(data, Data_Type.IP)

    def check_format(self, data):
        if ipv4(data) or ipv6(data):
            return True
        else:
            return False
