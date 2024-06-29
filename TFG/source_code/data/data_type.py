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