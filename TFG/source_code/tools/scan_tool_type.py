from enum import Enum

class Scan_Tool_Type(Enum):
    PASIVE = "Pasive"
    MALICIOUS = "Malicious"
    ACTIVE = "Active"

    def get_scan_tool_type_list():
        data_type_list = []
        for data_type in Scan_Tool_Type:
            data_type_list.append(data_type.value)
        return data_type_list