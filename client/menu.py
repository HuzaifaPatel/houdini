from houdini import make_buildroot, start_vm

menu_options = {
	'1':make_buildroot,
	'2':start_vm
}

def display_menu():
	print("Welcome to Houdini\n\nEnter your Choice")
	print("1. Make Buildroot")
	print("2. Start VM")

def get_user_choice():
	choice = input("Enter your Choice: ")
	return choice.strip()

def main():
	while True:
		display_menu()
		choice = get_user_choice()

		if choice in menu_options:
			menu_options[choice]()
		else:
			print("Invalid choice. Please try again.")

main()