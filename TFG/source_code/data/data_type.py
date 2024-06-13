from enum import Enum

class Data_Type(Enum):
    IP = "IP"

    def create_data_object_by_type(self, data):
        match self:
            case Data_Type.IP:
                return None # AÑADIR CREACION DE LOS DATA OBJECTS
            case _:
                print("[Scan Tool Type] [", self.value, "] This data type is not configured to create a data object by type")
