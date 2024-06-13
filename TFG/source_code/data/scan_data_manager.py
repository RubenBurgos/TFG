from data_type import Data_Type

class Scan_Data_Manager:

    def set_input_data(self, input_data, data_type_name):
        for data_type in Data_Type:
            if data_type.value == data_type_name:
                data = data_type.get_data_object_by_type(data)
                if data.check_format():
                    self.input_data = data
                    return self.input_data.data
                else:
                    return None
            
    def add_output_data(self):
        pass
