cmake_minimum_required(VERSION 3.22 FATAL_ERROR)
set(CMAKE_CXX_STANDARD 17) 
project(sensorium)

include(${CMAKE_BINARY_DIR}/dependencies/conan_toolchain.cmake)

find_package(protobuf REQUIRED)

set(SOURCES "${CMAKE_CURRENT_SOURCE_DIR}/src/main.cpp")

add_executable(sensorium ${SOURCES})
target_link_libraries(sensorium PRIVATE protobuf::protobuf)
target_compile_features(sensorium PRIVATE cxx_std_17)