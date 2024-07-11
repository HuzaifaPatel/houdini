from buildroot_manager import BuildrootManager
import importlib
import sys
import os
import houdini_config
import argparse
from style import Style
from run_trick import run_trick
from get_versions import get_versions
from server_status import server_status

def _initialize():
    euid = os.geteuid()

    if euid == 0:
        Style.print_color("Houdini should not be run as root", 'red')
        sys.exit(1)

def parser():
	_initialize()

	brm = BuildrootManager()
	# Create the parser
	parser = argparse.ArgumentParser(description="Houdini - A Container Escape Artist", formatter_class=argparse.ArgumentDefaultsHelpFormatter, allow_abbrev=False)

	# Add arguments
	parser.add_argument('--mkfs', action='store_true', help='Make filesystem')
	parser.add_argument('--mkkern', action='store_true', help='Make kernel')
	parser.add_argument('--run_trick', type=str, help='Run a trick')
	parser.add_argument('--start_vm', action='store_true', help='Start Virtual Machine')
	parser.add_argument('--get_versions', action='store_true', help='View Version Information of Software installed on VM')
	parser.add_argument('--server_status', action='store_true', help='Get Status of Houdini Server')

	# Parse the arguments
	args = parser.parse_args()

    # Check if no arguments are provided and print help
	if len(sys.argv) == 1:
		parser.print_help()
		sys.exit(1)

	if args.mkfs:
	    brm.make_filesystem()
	if args.mkkern:
	    brm.make_kernel()
	if args.run_trick:
	    run_trick(args.run_trick)
	if args.start_vm:
		brm.start_vm()
	if args.get_versions:
		get_versions()
	if args.server_status:
		server_status()