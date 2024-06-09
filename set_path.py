import sys
from client.root import get_root_dir
PY_CONFIG_FILE = get_root_dir('/client/config.py')
BUILDROOT_CONFIG_FILE = get_root_dir('/buildroot/.config')
sys.path.append(get_root_dir('/client'))
sys.path.append(get_root_dir('/config'))
sys.path.append(get_root_dir('/api'))
sys.path.append(get_root_dir('/buildroot'))
