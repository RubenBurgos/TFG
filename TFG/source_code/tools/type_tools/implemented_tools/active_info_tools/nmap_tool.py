from json import dumps
from nmap import PortScanner, PortScannerError
from source_code.tools.type_tools.active_info_tool import Active_Info_Tool
from source_code.data.data_type import Data_Type

class Nmap(Active_Info_Tool):
    def __init__(self):
        super().__init__("Nmap", [Data_Type.IP, Data_Type.DOMAIN])


    def scan_and_load_fetched_info(self):
        try:
            nmap = PortScanner()
        except PortScannerError:
            print('[Nmap] Nmap tool not found, check if Nmap is installed')
            return 0
        
        results = nmap.scan(self.scan_data_manager.input_data.data, arguments="--version-intensity 9 -A -p- -vvv")
        
        if "error" in nmap.scaninfo():
            print("[Nmap] Scan errors:", nmap.scaninfo()['error'])
        else:
            output_data = type(self.scan_data_manager.input_data)(self.scan_data_manager.input_data.data)
            info = dumps(results, indent=2)
            output_data.add_info(info, self.tool_name)
            self.scan_data_manager.add_output_data(output_data)
