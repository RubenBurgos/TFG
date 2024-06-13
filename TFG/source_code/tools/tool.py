class Tool:
    def __init__(self, app_name, scan_tool_type, entry_data_types, scan_data_manager):
        self.app_name = app_name
        self.scan_tool_type = scan_tool_type
        self.entry_data_types = entry_data_types
        self.scan_data_manager = scan_data_manager

    def error_message(self):
        print("[", self.app_name, "] Error message function not overwritten")

    def scan(self):
        print("[", self.app_name, "] Scan function not overwritten")

    def load_fetched_info(self):
        print("[", self.app_name, "] Load fetched information function not overwritten")