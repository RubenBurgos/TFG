from pyhibp import pwnedpasswords, set_user_agent
from source_code.tools.type_tools.malicious_info_tool import Malicious_Info_Tool
from source_code.data.data_type import Data_Type

class HIBP(Malicious_Info_Tool):
    def __init__(self):
        super().__init__("HIBP (Have I Been Pwned)", [Data_Type.HASH, Data_Type.KEY_STRING])


    def scan_and_load_fetched_info(self):
        
        set_user_agent(ua="Osint+")
        try:
            if self.scan_data_manager.input_data.data_type == Data_Type.HASH:
                result = pwnedpasswords.is_password_breached(sha1_hash=self.scan_data_manager.input_data.data)
            else:
                result = pwnedpasswords.is_password_breached(password=self.scan_data_manager.input_data.data)
        except AttributeError as exception:
            print("[HBIP] " + str(exception))
            return None
        
        output_data = type(self.scan_data_manager.input_data)(self.scan_data_manager.input_data.data)
        
        if result == 0:
            info = "This password or (sha1) hash has not been breached."
        else:
            info = "This password or (sha1) hash has been breached, it has been used " + str(result) + " times."

        output_data.add_info(info, self.tool_name)
        self.scan_data_manager.add_output_data(output_data)