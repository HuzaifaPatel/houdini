cmake_minimum_required(VERSION 3.5)

# Settings:
set(CTEST_DASHBOARD_ROOT                "/home/huzi/Documents/houdini/buildroot/build/host-cmake-3.28.3/Tests/CTestTest")
set(CTEST_SITE                          "huzi")
set(CTEST_BUILD_NAME                    "CTestTest-Linux-g++-VerboseOutput")

set(CTEST_SOURCE_DIRECTORY              "/home/huzi/Documents/houdini/buildroot/build/host-cmake-3.28.3/Tests/CTestTestVerboseOutput")
set(CTEST_BINARY_DIRECTORY              "/home/huzi/Documents/houdini/buildroot/build/host-cmake-3.28.3/Tests/CTestTestVerboseOutput")
set(CTEST_CMAKE_GENERATOR               "Unix Makefiles")
set(CTEST_CMAKE_GENERATOR_PLATFORM      "")
set(CTEST_CMAKE_GENERATOR_TOOLSET       "")
set(CTEST_BUILD_CONFIGURATION           "$ENV{CMAKE_CONFIG_TYPE}")
set(CTEST_COVERAGE_COMMAND              "/usr/bin/gcov")
set(CTEST_NOTES_FILES                   "${CTEST_SCRIPT_DIRECTORY}/${CTEST_SCRIPT_NAME}")

CTEST_START(Experimental)
CTEST_CONFIGURE(BUILD "${CTEST_BINARY_DIRECTORY}")
CTEST_BUILD(BUILD "${CTEST_BINARY_DIRECTORY}")
CTEST_TEST(BUILD "${CTEST_BINARY_DIRECTORY}")
