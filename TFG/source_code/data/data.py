class Data:
    def __new__(cls, data, data_type):
        if cls.check_format(cls, data) == False:
            print("[", data_type,"] Incorrect format for this data type")
            return None
        instance = super().__new__(cls)
        return instance

    def __init__(self, data, data_type):
        self.data = data
        self.data_type = data_type
        self.info = ""

    def check_format(self, data):
        print("[", self.__qualname__, "] Check format function not overwritten, cant check:", data)
        return False
    
    def add_info(self, info, tool_name):
        box_size = (len(tool_name)+2)
        top_bottom = "\n#" + (box_size*"#") + "#\n"
        padding = "#" + (box_size*" ") + "#"

        self.info += top_bottom + padding
        self.info += "\n# " + tool_name + " #\n"
        self.info += padding + top_bottom + "\n" + info + "\n"
