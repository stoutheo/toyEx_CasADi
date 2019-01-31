cmake_minimum_required (VERSION 2.6)
project (ex1_casADi)

# instructions https://groups.google.com/forum/#!topic/casadi-users/J97bu3SxzlA

find_path(CASADI_INCLUDE_DIR
  casadi/casadi.hpp
  HINTS $ENV{CASADI_PREFIX}/include
)

if(CASADI_INCLUDE_DIR)
  set(CASADI_INCLUDE_DIR ${CASADI_INCLUDE_DIR} ${CASADI_INCLUDE_DIR}/casadi)
  set(CASADI_FOUND_INCLUDE TRUE)
  message(STATUS "Found CasADi include dir: ${CASADI_INCLUDE_DIR}")
else()
  message(STATUS "Could not find CasADi include dir")
endif()

find_library(CASADI_LIBRARY
    NAMES casadi
    HINTS ${CASADI_INCLUDE_DIR}/../lib $ENV{CASADI_PREFIX}/lib)
if(CASADI_LIBRARY)
    set(CASADI_LIBRARIES ${CASADI_LIBRARIES} ${CASADI_LIBRARY})
endif()

if(CASADI_LIBRARIES)
  message(STATUS "Found CasADi libs: ${CASADI_LIBRARIES}")
else()
  message(STATUS "Could not find CasADi libs")
endif()

if(CASADI_FOUND_INCLUDE AND CASADI_LIBRARIES)
  set(CASADI_FOUND TRUE)
endif()

set(EIGEN_INCLUDE_DIR $ENV{EIGEN_INCLUDE_DIR})
message(STATUS "Found EIGEN include dir: ${EIGEN_INCLUDE_DIR}")

include_directories(${CASADI_INCLUDE_DIR})
include_directories(${EIGEN_INCLUDE_DIR})

# add the executable
add_executable (ex1 ex1.cpp)
target_link_libraries (ex1  ${CASADI_LIBRARIES})

# add the executable
add_executable (ex_c_codegen_usage ex_c_codegen_usage.cpp)
target_link_libraries (ex_c_codegen_usage  ${CASADI_LIBRARIES})

add_executable (ex_c_codegen_usage2 ex_c_codegen_usage2.cpp)
target_link_libraries (ex_c_codegen_usage2  ${CASADI_LIBRARIES})
