import sys
from client.root import get_root_dir
sys.path.append(get_root_dir('/client'))
sys.path.append(get_root_dir('/config'))
sys.path.append(get_root_dir('/api'))

#test. remove after
sys.path.append(get_root_dir('/overlay-fs/houdini'))