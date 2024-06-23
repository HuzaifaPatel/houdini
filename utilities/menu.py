from buildroot_manager import BuildrootManager
from style import Style
import importlib
import sys
import os
import houdini_config

class Menu:
	def __init__(self, title):
		self.title = title
		self.brm = BuildrootManager()
		self.options = {
		    '1': ("Make Buildroot", self.brm.make_buildroot),
		    '2': ("Start VM", self.brm.start_vm),
		    # '3': ("Run Trick", BuildrootManager.run_trick),
		    '4': ("Help", self.help),
		    '5': ("Exit", self.exit_program)
		}

	def display_menu(self):
		Style.print_color(f"=== {self.title} ===", 'cyan')
		for key, (description, _) in self.options.items():
			print(f"{key}. {description}")

	def get_user_choice(self):
		choice = input(Style.BOLD + Style.CYAN + "Enter your Choice: " + Style.RESET)
		return choice.strip()

	@classmethod
	def help():
		return 1

	@classmethod
	def exit_program():
		Style.print_color("\nExiting", 'green')
		exit(0)

	def reload_config(self):
		importlib.reload(houdini_config)
		KERNEL_VERSION = houdini_config.KERNEL_VERSION

	def run(self):
		try:
			Style.print_color("Welcome to Houdini\n", 'cyan')
			while True:
				self.display_menu()
				choice = self.get_user_choice()
				self.reload_config()
				if choice in self.options:
					self.options[choice][1]()
				else:
					print("Invalid choice. Please try again.")
		except KeyboardInterrupt:
			print("\b\b  \n")
			Style.print_color("Exiting", 'green')
			sys.exit(0)