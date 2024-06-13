import os
from simple_term_menu import TerminalMenu

class Osint_Plus:
    def __init__(self):
        tool_list=[] # INICIAR TODAS LAS TOOLS

    def run(self):
        while(1):
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
        os.system("clear")
        print("""Select the input data type to be scanned:
              """)
        options = ["IP", "Email"] # Importar el enum y llamar a funcion de creacion de lista de tipos
        input_data_menu = TerminalMenu(options)
        menu_entry_index = input_data_menu.show()
        selection = options[menu_entry_index]
        for option in options:
            if option == selection: # meter en una funcion lo de abajao para añadir input de datamanger y hacer solo el if(chekeo) deentro de esete if
                data = input("Enter de input data to be scanned: ") # Coger y chekear data
                print("Data: " + data)
                if(True): # Si esta bien el tipo se continua
                    self.pause_button("Continue")
                    self.scan_type_menu()
                else: # si esta mal crear menu de error
                    pass
                break
    
    def pause_button(self, button_msg):
        options = [button_msg]
        continue_menu = TerminalMenu(options)
        continue_menu.show()

    def scan_type_menu(self):
        os.system("clear")
        print("""Select the scan type for the input data:
              """)
        options = ["Pasivo", "Malicioso", "Activo"] # Importar el enum y llamar a funcion de creacion de lista de tipos
        scan_type_menu = TerminalMenu(options)
        menu_entry_index = scan_type_menu.show()
        selection = options[menu_entry_index]
        for option in options:
            if option == selection: # meter en una funcion el siguiente menu pasandole el tipo de scan a realizar y el input type viene del scan data manager (pasar por arg) para filtrar tools
                if(True): # Si hay apps para escanear se continua 
                    self.pause_button("Continue")
                    self.select_tools_menu()
                else: # si no hay mensaje de error y hacer otro o salir
                    pass
                break    
        
    def select_tools_menu(self):
        scan_tools = []
        available_tools = ["a", "b", "c"]
        options = ["Start Scan", "Deselect Tools","Exit"]
        select = True
        while(1):
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