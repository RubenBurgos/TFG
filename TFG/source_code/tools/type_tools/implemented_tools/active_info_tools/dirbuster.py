import os
from json import dumps
from pydirbuster import Pybuster
from source_code.data.data_type import Data_Type
from source_code.tools.type_tools.active_info_tool import Active_Info_Tool

class DirBuster(Active_Info_Tool):
    def __init__(self):
        super().__init__("DirBuster", [Data_Type.URL])


    def scan_and_load_fetched_info(self):
        absolute_path = os.path.dirname(__file__)
        wordlist = os.path.join(absolute_path, "dirbuster_wordlist/wordlist.txt")

        try:
            scan = Pybuster(url=self.scan_data_manager.input_data.data, 
                            wordfile=wordlist, exts=["html", "htm","php", "conf", "pdf", "doc", "xml", "txt", "jpg", "png"], 
                            threads=1)
            results = scan.Run()
        except Exception as exception:
            print("[DirBuster] An unexpected error has been detected:\n" + str(exception))
            return 0

        output_data = type(self.scan_data_manager.input_data)(self.scan_data_manager.input_data.data)
        info = dumps(results, indent=2)
        output_data.add_info(info, self.tool_name)
        self.scan_data_manager.add_output_data(output_data)