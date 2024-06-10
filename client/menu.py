import importlib
from procedures import *
from style import colors
import config
import sys

menu_options = {
	'1':make_buildroot,
	'2':start_vm,
	'3':set_buildroot_pkg,
	'4':set_kernel_ver,
	'5':make_olddefconfig,
	'6':help_,
	'7':exit_program
}

def display_menu():
	print("1. Make Buildroot")
	print("2. Start VM")
	print("3. Set Buildroot Packages")
	print("4. Set Kernel Version")
	print("5. Make Olddefconfig")
	print("6. Help")
	print("7. Exit")

def get_user_choice():
    choice = input(colors.BOLD + colors.CYAN + "Enter your Choice: " + colors.RESET)
    return choice.strip()

def menu():
	try:
		print(colors.BOLD + colors.CYAN + "Welcome to Houdini\n" + colors.RESET)
		while True:
			display_menu()
			choice = get_user_choice()
			importlib.reload(config)
			if choice in menu_options:
				menu_options[choice]()
			else:
				print("Invalid choice. Please try again.")

	except KeyboardInterrupt:
		print("\b\b  \n")
		print(colors.BOLD + colors.GREEN + "Exiting" + colors.RESET)
		exit(0)

menu()