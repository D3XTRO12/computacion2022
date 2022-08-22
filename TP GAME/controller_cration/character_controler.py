from xml.dom.minidom import CharacterData
from character_factory.character import *
character_data = Character
character_list = [character_data.get_name, character_data.get_age, character_data.get_strength, character_data.get_agility, character_data.get_health, character_data.get_type]
def save_character_file(self):
    choice_file = int(input("Which character do these stats belong to?\n1: Player 1\n2: Player 2\n3: Player 3\nChoose an option: "))
    while True:
        
        if choice_file == 1:
        
            chosen_file = 'character_1.txt'
            with open(chosen_file, "w") as archive:
                archive.writelines(character_list)
            break

        elif choice_file == 2:
        
            chosen_file = 'character_2.txt'
            with open(chosen_file, "w") as archive:
                archive.writelines(character_list)
            break
        
        elif choice_file == 3:
        
            chosen_file = 'character_3.txt'
            with open(chosen_file, "w") as archive:
                archive.writelines(character_list)
            break
        
        else:
        
            print("Wrong option. Choose a valid option")
