from procedures import *
from style import colors
import sys
import os

menu_options = {
    '1': ("Make Buildroot", make_buildroot),
    '2': ("Start VM", start_vm),
    '3': ("Run Trick", run_trick),
    '4': ("Help", help_),
    '5': ("Exit", exit_program)
}

class Menu:
	def __init__(self, title, options):
		self.title = title
		self.options = options

	def display_menu(self):
		print(colors.BOLD + colors.CYAN + f"=== {self.title} ===" + colors.RESET)
		for key, (description, _) in self.options.items():
			print(f"{key}. {description}")

	def get_user_choice(self):
		choice = input(colors.BOLD + colors.CYAN + "Enter your Choice: " + colors.RESET)
		return choice.strip()

	def run(self):
		try:
			print(colors.BOLD + colors.CYAN + "Welcome to Houdini\n" + colors.RESET)
			while True:
				self.display_menu()
				choice = self.get_user_choice()
				reload_config()
				if choice in self.options:
					self.options[choice][1]()
				else:
					print("Invalid choice. Please try again.")
		except KeyboardInterrupt:
			print("\b\b  \n")
			print(colors.BOLD + colors.GREEN + "Exiting" + colors.RESET)
			sys.exit(0)