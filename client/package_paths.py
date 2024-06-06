from root import get_root_dir

config_path 			=	get_root_dir('/config/config.conf')
runc_mk_path 			=	get_root_dir('/buildroot/package/runc/runc.mk')
docker_cli_mk_path 		= 	get_root_dir('/buildroot/package/docker-cli/docker-cli.mk')
docker_engine_mk_path 	= 	get_root_dir('/buildroot/package/docker-engine/docker-engine.mk')
buildroot_path 			=	get_root_dir('/buildroot')