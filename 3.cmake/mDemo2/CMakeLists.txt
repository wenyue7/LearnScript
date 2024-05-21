#指定运行此配置文件所需的 CMake 的最低版本
CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

#项目名称
PROJECT(mDemoPrj)

SET (Demo_VERSION_MAJOR 3)
SET (Demo_VERSION_MINOR 6)

# 让 CMake 支持 gdb 只需要指定 Debug 模式下开启 -g 选项:
SET(CMAKE_BUILD_TYPE "Debug")
SET(CMAKE_CXX_FLAGS_DEBUG "$ENV{CXXFLAGS} -O0 -Wall -g -ggdb")
SET(CMAKE_CXX_FLAGS_RELEASE "$ENV{CXXFLAGS} -O3 -Wall")
# 指定编译器
SET(CMAKE_C_COMPILER "/usr/bin/arm-linux-gnueabihf-gcc")
SET(CMAKE_CXX_COMPILER "/usr/.....")

# 指定生成链接链接库的存放路径,不指定的话默认是存放在跟当前 CMakeLists.txt 一样的路径
# 该设置也可以跟随 ADD_LIBRARY 指令，放在该指令之前，这样控制更精确
SET(LIBRARY_OUTPUT_PATH ${PROJECT_BINARY_DIR}/lib)

# 指定生成可执行文件后的存放路径
# 该设置也可以跟随 ADD_EXECUTABLE 指令，放在该指令之前，这样控制更精确
SET(EXECUTABLE_OUTPUT_PATH ${PROJECT_BINARY_DIR}/bin)

# 指定生成目标
# ADD_EXECUTABLE(Demo ${DIR_SRCS})
# TARGET_LINK_LIBRARIES (Demo  ${EXTRA_LIBS})

# 如果工程存在多个目录，需要确保每个要管理的目录存在一个CMakeLists.txt
# 无论CMakeLists.txt文件在根目录还是子目录中，也无论一个工程有一个还是多个CMakeList文件，文件里的路径起点均为文件当前位置
# 该指令可以指定中间二进制和目标二进制文件的存放位置，可以使用类似 ADD_SUBDIRECTORY(src bin) 的形式，这项当于在编译的时候把 src的名字改成bin。
ADD_SUBDIRECTORY(src)

# ======================================================================================================================== 使用外部库
# 原始方法
# 使用外部库最基础的写法是需要一下三个部分
#     1. INCLUDE_DIRECTORIES  对应 gcc/g++ 的 -I 参数，写在顶层主调 CMakeLists.txt 中就可以，可以传递到子文件夹中
#     2. LINK_DIRECTORIES 对应 gcc/g++ 的 -L 参数,指定库文件的路径
#     3. TARGET_LINK_LIBRARIES 对应 gcc/g++ 的 -l 参数，为了方便使用可以在第2步之后使用一个变量保存用到的库 (SET(......))

# 使用查找包的方式
# FIND_PACKAGE 用来调用预定义在 CMAKE_MODULE_PATH 下的 Find<name>.cmake模块
# FIND_PACKAGE 执行后会赋值的变量:
#     <name>_FOUND
#     <name>_INCLUDE_DIRS 或 <name>_INCLUDES
#     <name>_LIBRARIES 或 <name>_LIBS
#     <name>_DEFINITIONS
message(STATUS "    CMAKE_MODULE_PATH: " ${CMAKE_MODULE_PATH})
SET(CMAKE_MODULE_PATH "<指向.cmake文件目录>")
FIND_PACKAGE(OpenCV REQUIRED)
IF(NOT OpenCV_FOUND)
    MESSAGE(FATAL_ERROR "OpenCV Not Found!")
ENDIF(NOT OpenCV_FOUND)
message(STATUS "OpenCV library status:")
message(STATUS "    config: ${OpenCV_DIR}")
message(STATUS "    version: ${OpenCV_VERSION}")
message(STATUS "    libraries: ${OpenCV_LIBS}")
message(STATUS "    include path: ${OpenCV_INCLUDE_DIRS}")

# ======================================================================================================================== 使用外部库  end
