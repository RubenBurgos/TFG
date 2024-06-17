from nmap import PortScanner # type: ignore
from source_code.tools.type_tools.active_info_tool import Active_Info_Tool
from source_code.data.data_type import Data_Type

class Nmap(Active_Info_Tool):
    def __init__(self, scan_data_manager):
        super().__init__("Nmap", [Data_Type.IP], scan_data_manager)

    def scan(self):
        nmap = PortScanner()
        nmap.scan(self.scan_data_manager.input_data.data, arguments="--version-intensity 9 -A -p- -vvv")

    def load_fetched_info(self):
        pass

# Nmap --version-intensity 9 -A -p- -vvv <ip X.x.x.z> scanme.nmap.org