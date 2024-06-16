from source_code.data.data_type import Data_Type
from source_code.data.implemented_type_datas.ip import IP
from source_code.data.implemented_type_datas.domain import Domain
from source_code.data.implemented_type_datas.email import Email
from source_code.data.implemented_type_datas.hash import Hash
from source_code.data.implemented_type_datas.url import URL
from source_code.data.implemented_type_datas.key_string import Key_String

class Scan_Data_Manager:
    def __init__(self):
        self.input_data = None
        self.output_data = []

    def set_input_data(self, data_type_name):
        data = input("Enter de input data to be scanned: ")
        print("Data: " + data)
        data_object = None

        match data_type_name:
            case Data_Type.IP.value:
                data_object = IP(data)
            case Data_Type.DOMAIN.value:
                data_object = Domain(data)
            case Data_Type.EMAIL.value:
                data_object = Email(data)
            case Data_Type.HASH.value:
                data_object = Hash(data)
            case Data_Type.URL.value:
                data_object = URL(data)
            case Data_Type.KEY_STRING.value:
                data_object = Key_String(data)
            case _:
                print("[Scan Data Manager] [", data_type_name, "] This data type is not configured to be set as input data")

        if data_object != None:
            self.input_data = data_object
            return True
        else:
            return False
           
    def add_output_data(self, data):
        for output_data_object in self.output_data:
            if output_data_object.data == data.data:
                output_data_object.add_info(data.info)
        self.output_data.append(data)
