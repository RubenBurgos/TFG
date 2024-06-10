import os
from simple_term_menu import TerminalMenu

class osint_plus:
    def __init__(self) -> None:
        pass

    def run(self):
        while(1):
            os.system("clear")
            self.starting_menu()

    def starting_menu(self):
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
        print("""Select the scan type for the input data:
              """)
        options = ["Pasivo", "Malicioso", "Activo"] # Importar el enum y llamar a funcion de creacion de lista de tipos
        scan_type_menu = TerminalMenu(options)
        menu_entry_index = scan_type_menu.show()
        selection = options[menu_entry_index]
        for option in options:
            if option == selection: # meter en una funcion el siguiente menu pasandole el tipo de scan a realizar y el input type viene del scan data manager (pasar por arg) para filtrar tools
               
                if(True): # Si esta bien el tipo se continua
                    self.pause_button("Continue")
                    # self.scan_type_menu() menu seleccion de tools

                break    
        

osint_plus_platform = osint_plus()
osint_plus_platform.run()