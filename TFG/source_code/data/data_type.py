from enum import Enum

class Data_Type(Enum):
    IP = "IP"
    DOMAIN = "Domain"
    HASH = "Hash"
    EMAIL = "Email"
    URL = "URL"
    KEY_STRING = "Key String"

    def get_data_type_list():
        data_type_list = []
        for data_type in Data_Type:
            data_type_list.append(data_type.value)
        return data_type_list

    #def create_data_object_by_type(self, data):
    #    match self:
    #        case Data_Type.IP:
    #            return IP(data)
    #        case Data_Type.DOMAIN:
    #            return Domain(data)
    #        case _:
    #            print("[Scan Tool Type] [", self.value, "] This data type is not configured to create a data object by type")
