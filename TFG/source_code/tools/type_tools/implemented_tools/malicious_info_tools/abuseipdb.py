import requests
from json import dumps, loads
from source_code.tools.type_tools.malicious_info_tool import Malicious_Info_Tool
from source_code.data.data_type import Data_Type

class AbuseIPDB(Malicious_Info_Tool):
    def __init__(self):
        super().__init__("AbuseIPDB", [Data_Type.IP])


    def scan_and_load_fetched_info(self):
        
        url = 'https://api.abuseipdb.com/api/v2/check'

        querystring = {
            'ipAddress': self.scan_data_manager.input_data.data,
            'maxAgeInDays': '90',
            'verbose': True
        }

        headers = {
            'Accept': 'application/json',
            'Key': 'b1b453f03f6060d8c817d82aa5b11ae745ff09b0d9f5959dd608f07243b5e432799604a772f7c48f'
        }

        response = requests.request(method='GET', url=url, headers=headers, params=querystring)
        if response.status_code == 200:
            output_data = type(self.scan_data_manager.input_data)(self.scan_data_manager.input_data.data)

            decodedResponse = loads(response.text)
            info = dumps(decodedResponse, indent=2)

            output_data.add_info(info, self.tool_name)
            self.scan_data_manager.add_output_data(output_data)
        else:
            print("[AbuseIPDB] API Response status code not 200, it responded :" + str(response.status_code) + " - " + str(response.reason))