from json import dumps
from source_code.data.data_type import Data_Type
from zoomeyehk.sdk import ZoomEye as Zoomeye_tool
from source_code.settings.api_keys import ZOOMEYE_KEY
from source_code.tools.type_tools.pasive_info_tool import Pasive_Info_Tool

class ZoomEye(Pasive_Info_Tool):
    def __init__(self):
        super().__init__("ZoomEye", [Data_Type.IP, Data_Type.DOMAIN, Data_Type.KEY_STRING])


    def scan_and_load_fetched_info(self):

        api_key = ZOOMEYE_KEY

        if api_key == None:
            print("[ZoomEye] You need to configure your API key to use this tool.")
            return 0

        scan = Zoomeye_tool(api_key)

        match self.scan_data_manager.input_data.data_type:
            case Data_Type.IP:
                search = "ip:" + self.scan_data_manager.input_data.data
            case Data_Type.DOMAIN:
                search = "site:" + self.scan_data_manager.input_data.data
            case Data_Type.KEY_STRING:
                search = self.scan_data_manager.input_data.data
        
        output_data = type(self.scan_data_manager.input_data)(self.scan_data_manager.input_data.data)
        try:
            results = scan.dork_search(search)
        except Exception as exception:
            print("[ZoomEye] An unexpected error has been detected:\n" + str(exception))
            print("[ZoomEye] Please check your conexion with the ZoomEye API.")
            return 0
        
        info = dumps(results, indent=2)
        output_data.add_info(info, self.tool_name)
        self.scan_data_manager.add_output_data(output_data)