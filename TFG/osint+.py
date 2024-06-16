import os
from simple_term_menu import TerminalMenu
from source_code.data.data_type import Data_Type
from source_code.data.scan_data_manager import Scan_Data_Manager
from source_code.tools.scan_tool_type import Scan_Tool_Type

class Osint_Plus:
    def __init__(self):
        self.tool_list = [] # INICIAR TODAS LAS TOOLS

    def run(self):
        self.starting_menu()

    def starting_menu(self):
        os.system("clear")
        print("""PONER BANNER AQUI CON CREADOR COPYRIGT Y ADVERTENCIA DE USO COMO USAR ETC
              """)
        options = ["Start", "Exit"]
        starting_menu = TerminalMenu(options)
        menu_entry_index = starting_menu.show()
        selection = options[menu_entry_index]
        if selection == "Start":
            self.input_data_menu()
        elif selection == "Exit":
            os.system("clear")
            print("PONER MENSAJE DE SALIDA")
            exit(0)    

    def input_data_menu(self):
        scan_data_manager = Scan_Data_Manager()
        options = Data_Type.get_data_type_list()
        options.append("Exit")
        input_data_menu = TerminalMenu(options)
        while(scan_data_manager.input_data == None):
            os.system("clear")
            print("""Select the input data type to be scanned:
                """)
            menu_entry_index = input_data_menu.show()
            selection = options[menu_entry_index]
            if selection == "Exit":
                os.system("clear")
                print("PONER MENSAJE DE SALIDA")
                exit(0)
            for option in options:
                if option == selection:
                    if(scan_data_manager.set_input_data(option)):
                        print("Input data set up correctly")
                        self.pause_button("Continue")
                        self.scan_type_menu(scan_data_manager)
                    else:
                        self.pause_button("Retry")
                    break
    
    def pause_button(self, button_msg):
        options = [button_msg]
        continue_menu = TerminalMenu(options)
        continue_menu.show()

    def scan_type_menu(self, scan_data_manager):
        os.system("clear")
        print("""Select the scan type for the input data:
              """)
        options = Scan_Tool_Type.get_scan_tool_type_list()
        options.append("Exit")
        scan_type_menu = TerminalMenu(options)
        menu_entry_index = scan_type_menu.show()
        selection = options[menu_entry_index]
        if selection == "Exit":
            os.system("clear")
            print("PONER MENSAJE DE SALIDA")
            exit(0)
        for option in options:
            if option == selection:
                self.select_tools_menu(scan_data_manager, option)                
                break    
        
    def select_tools_menu(self, scan_data_manager, scan_tool_type):
        no_tools = False
        scan_tools = []
        available_tools = []
        for tool in self.tool_list:
            if tool.scan_tool_type.value == scan_tool_type and tool.entry_data_types.__contains__(scan_data_manager.input_data.data_type):
                available_tools.append(tool)

        if len(available_tools) != 0:
            options = ["Start Scan", "Deselect Tools", "Exit"]
        else:
            print("There are no configured tools for this kind of scan with this kind of input data")
            options = ["Exit"]
            no_tools = True
            
        select = True
        while(1):
            if no_tools == False:
                os.system("clear")
                if select:
                    print("""Select the tools that will scan the input data.""")
                    options = available_tools + options[-3:]
                else:
                    print("""Deselect the tools that will not scan the input data.""")
                    options = scan_tools + options[-3:]
                print("""\n Selected tools:""", scan_tools, "\n")
            # AÑADIR EL FOR CON LAS TOOLS CON INPUTDATA TYPE IGUAL AL INTRODUCIDO y SACANTYPE EL SELECIONADO (LOS NOMBRES)
            select_tools_menu = TerminalMenu(options)
            menu_entry_index = select_tools_menu.show()
            selection = options[menu_entry_index]
            if selection == "Start Scan": # AÑADIR MENSAJE DE SIGUIR CON OTRO SCAN, O ESPERAR A QUE ACABE Y LANZAR SCANEOS
                self.pause_button("Continue")
            elif selection == "Deselect Tools":
                select = False
                options.remove("Deselect Tools")
                options.insert(-1, "Select Tools")
            elif selection == "Select Tools":
                select = True
                options.remove("Select Tools")
                options.insert(-1, "Deselect Tools")
            elif selection == "Exit":
                os.system("clear")
                print("PONER MENSAJE DE SALIDA")
                exit(0)
            else:
                if select:
                    scan_tools.append(selection)
                    available_tools.remove(selection)
                else:
                    scan_tools.remove(selection)
                    available_tools.append(selection)

osint_plus_platform = Osint_Plus()
osint_plus_platform.run()