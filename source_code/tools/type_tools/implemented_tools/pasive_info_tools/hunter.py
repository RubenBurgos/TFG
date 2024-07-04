import requests
from json import dumps, loads
from source_code.data.data_type import Data_Type
from source_code.settings.api_keys import HUNTER_KEY
from source_code.tools.type_tools.pasive_info_tool import Pasive_Info_Tool

class Hunter(Pasive_Info_Tool):
    def __init__(self):
        super().__init__("Hunter", [Data_Type.EMAIL])


    def scan_and_load_fetched_info(self):
        
        url = 'https://api.hunter.io/v2/email-verifier'

        querystring = {
            'email': self.scan_data_manager.input_data.data,
            'api_key': HUNTER_KEY
        }

        if querystring["api_key"] == None:
            print("[Hunter] You need to configure your API key to use this tool.")
            return 0

        try:
            response = requests.request(method='GET', url=url, params=querystring)
        except Exception as exception:
            print("[Hunter] An unexpected error has been detected:\n" + str(exception))
            print("[Hunter] Please check your conexion with the Hunter API.")
            return 0
        
        if response.status_code == 200:
            output_data = type(self.scan_data_manager.input_data)(self.scan_data_manager.input_data.data)

            decodedResponse = loads(response.text)
            info = dumps(decodedResponse, indent=2)

            output_data.add_info(info, self.tool_name)
            self.scan_data_manager.add_output_data(output_data)
        else:
            print("[Hunter] API Response status code not 200, it responded :" + str(response.status_code) + " - " + str(response.reason))