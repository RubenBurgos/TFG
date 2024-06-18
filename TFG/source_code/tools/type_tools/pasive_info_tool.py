from tool import Tool
from scan_tool_type import Scan_Tool_Type

class Pasive_Info_Tool(Tool):
    def __init__(self, tool_name, entry_data_types, scan_data_manager):
        super().__init__(tool_name, Scan_Tool_Type.PASIVE, entry_data_types, scan_data_manager)