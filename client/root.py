import os

def get_root_dir(extra_path = "") -> str:
	return os.path.abspath("..") + extra_path