from enum import Enum
from source_code.data.implemented_type_datas.ip import IP

class Data_Type(Enum):
    IP = "IP"

    def create_data_object_by_type(self, data):
        match self:
            case Data_Type.IP:
                return IP(data)
            case _:
                print("[Scan Tool Type] [", self.value, "] This data type is not configured to create a data object by type")
