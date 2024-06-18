class Tool:
    def __init__(self, tool_name, scan_tool_type, entry_data_types, scan_data_manager):
        self.tool_name = tool_name
        self.scan_tool_type = scan_tool_type
        self.entry_data_types = entry_data_types
        self.scan_data_manager = scan_data_manager

    def scan_and_load_fetched_info(self):
        print("[", self.app_name, "] Scan and load fetched information function not overwritten")