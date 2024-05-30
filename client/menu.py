from houdini import make_buildroot, start_vm, update_packages, make_olddefconfig

menu_options = {
	'1':make_buildroot,
	'2':start_vm,
	'3':update_packages,
	'4':make_olddefconfig
}

def display_menu():
	print("Welcome to Houdini\n\nEnter your Choice")
	print("1. Make Buildroot")
	print("2. Start VM")
	print("3. Update Packages")
	print("4. Make Olddefconfig")

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