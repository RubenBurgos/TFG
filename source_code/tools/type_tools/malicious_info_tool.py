from source_code.tools.tool import Tool
from source_code.tools.scan_tool_type import Scan_Tool_Type

class Malicious_Info_Tool(Tool):
    def __init__(self, tool_name, entry_data_types):
        super().__init__(tool_name, Scan_Tool_Type.MALICIOUS, entry_data_types)