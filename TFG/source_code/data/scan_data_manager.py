from data_type import Data_Type

class Scan_Data_Manager:
    def __init__(self):
        self.input_data = None
        self.output_data = []

    def set_input_data(self, input_data, data_type_name):
        for data_type in Data_Type:
            if data_type.value == data_type_name:
                data = data_type.get_data_object_by_type(input_data)
                self.input_data = data
                return self.input_data
            
    def add_output_data(self, data):
        for output_data_object in self.output_data:
            if output_data_object.data == data.data:
                output_data_object.add_info(data.info)
        self.output_data.append(data)

