from source_code.tools.tool import Tool
from source_code.tools.scan_tool_type import Scan_Tool_Type

class Active_Info_Tool(Tool):
    def __init__(self, app_name, entry_data_types, scan_data_manager):
        super().__init__(app_name, Scan_Tool_Type.ACTIVE, entry_data_types, scan_data_manager)
