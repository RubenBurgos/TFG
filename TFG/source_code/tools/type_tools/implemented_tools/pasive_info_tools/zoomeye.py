from json import dumps
from zoomeyehk.sdk import ZoomEye as Zoomeye_tool
from source_code.tools.type_tools.pasive_info_tool import Pasive_Info_Tool
from source_code.data.data_type import Data_Type

class ZoomEye(Pasive_Info_Tool):
    def __init__(self):
        super().__init__("ZoomEye", [Data_Type.IP, Data_Type.DOMAIN, Data_Type.KEY_STRING])


    def scan_and_load_fetched_info(self):
        scan = Zoomeye_tool("98CA1d0D-746C-970F0-E7B1-47D635171a2")

        match self.scan_data_manager.input_data.data_type:
            case Data_Type.IP:
                search = "ip:" + self.scan_data_manager.input_data.data
            case Data_Type.DOMAIN:
                search = "site:" + self.scan_data_manager.input_data.data
            case Data_Type.KEY_STRING:
                search = self.scan_data_manager.input_data.data
        
        output_data = type(self.scan_data_manager.input_data)(self.scan_data_manager.input_data.data)
        
        results = scan.dork_search(search)
        info = dumps(results, indent=2)
        output_data.add_info(info, self.tool_name)
        self.scan_data_manager.add_output_data(output_data)
