# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.28

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /home/huzi/Documents/houdini/buildroot/host/bin/cmake

# The command to remove a file.
RM = /home/huzi/Documents/houdini/buildroot/host/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/huzi/Documents/houdini/buildroot/build/host-ccache-4.8.2

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/huzi/Documents/houdini/buildroot/build/host-ccache-4.8.2

# Utility rule file for check_format.

# Include any custom commands dependencies for this target.
include CMakeFiles/check_format.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/check_format.dir/progress.make

CMakeFiles/check_format:
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --progress-dir=/home/huzi/Documents/houdini/buildroot/build/host-ccache-4.8.2/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Checking code formatting"
	misc/format-files --all --check

check_format: CMakeFiles/check_format
check_format: CMakeFiles/check_format.dir/build.make
.PHONY : check_format

# Rule to build all files generated by this target.
CMakeFiles/check_format.dir/build: check_format
.PHONY : CMakeFiles/check_format.dir/build

CMakeFiles/check_format.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/check_format.dir/cmake_clean.cmake
.PHONY : CMakeFiles/check_format.dir/clean

CMakeFiles/check_format.dir/depend:
	cd /home/huzi/Documents/houdini/buildroot/build/host-ccache-4.8.2 && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/huzi/Documents/houdini/buildroot/build/host-ccache-4.8.2 /home/huzi/Documents/houdini/buildroot/build/host-ccache-4.8.2 /home/huzi/Documents/houdini/buildroot/build/host-ccache-4.8.2 /home/huzi/Documents/houdini/buildroot/build/host-ccache-4.8.2 /home/huzi/Documents/houdini/buildroot/build/host-ccache-4.8.2/CMakeFiles/check_format.dir/DependInfo.cmake
.PHONY : CMakeFiles/check_format.dir/depend

