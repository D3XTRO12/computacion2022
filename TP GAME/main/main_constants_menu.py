from character_factory.character import *
from controller_cration.character_controler import *

def character_constants(self):
    
    for i in range (0,2):
        print("Character Creation Tool\nRemember, the 3 constant characteristics \nof your character (strength, agility and health) cant be 0 \nand the sum of all has to be 15")
        name = input("Enter the name of your character")
        age = int(input("Enter the age of your character"))
        strength = int(input("Enter the strength of your character"))
        agility = int(input("Enter the agility of your character"))
        health = int(input("Enter the health points of your character"))
        choice = int(input("Choose your race\n1: Warrior\n2: Elf\n3: Archer"))
        while True:
            if choice == 1:
                class_type = 'Warrior'
                break
            elif choice == 2:
                class_type = 'Elf'
                break
            elif choice == 3:
                class_type = 'Archer'
                break
            else:
                print("Wrong option. Choose a valid option")
        Character(name, age, strength, agility, health, class_type)
        
        
        save_character_file()
        

def enemy_creation_menu(self):
    pass