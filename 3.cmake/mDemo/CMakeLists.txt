# ============================================================================== base options
#指定运行此配置文件所需的 CMake 的最低版本
CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

#项目名称
PROJECT(mDemoPrj)

SET (Demo_VERSION_MAJOR 3)
SET (Demo_VERSION_MINOR 6)

STRING(TIMESTAMP current_year "%Y" UTC)
STRING(TIMESTAMP current_time "%Y-%m-%d %H:%M:%S")
MESSAGE(STATUS "current time: ${current_time}")

# 可选的<mode>关键字确定消息的类型，这会影响消息的处理方式：
# FATAL_ERROR:        CMake错误，停止处理和生成。
# SEND_ERROR:         CMake错误，继续处理，但跳过生成。
# WARNING:            CMake警告，继续处理。
# AUTHOR_WARNING:     CMake警告（dev），继续处理。
# DEPRECATION:        如果分别启用了变量CMAKE_ERROR_DEPRECATED 或 
#                     CMAKE_WARN_DEPRECATED，则CMake弃用错误或警告，否则没有消息。
# (none) or NOTICE:   打印到stderr的重要消息以吸引用户的注意。
# STATUS:             项目用户可能会感兴趣的主要有趣消息。理想情况下，这些消息
#                     应该简洁明了，不超过一行，但仍能提供信息。
# VERBOSE:            适用于项目用户的详细参考消息。这些消息应提供在大多数情况下
#                     不会引起关注的其他详细信息，但对于希望更深入地了解正在发生
#                     的事情的项目开发人员来说可能很有用。
# DEBUG:              详细的信息性消息旨在提供给在项目本身上进行开发的开发人员，
#                     而不是只想构建该项目的用户。这些消息通常对构建项目的其他
#                     用户不感兴趣，并且通常与内部实现细节密切相关。
# TRACE:              具有非常低级的实现细节的细粒度消息。使用此日志级别的消息
#                     通常仅是临时的，并且有望在发布项目，打包文件等之前被删除。

# CMake命令行工具在stdout上显示STATUS 到 TRACE 的消息，该消息前面带有两个连字符
# 和一个空格。所有其他消息类型都发送到stderr，并且不带连字符前缀。
MESSAGE(STATUS "-------- MAIN CMAKELISTS MSG --------")

# 存放cmake指令指向的 CMakeLists.txt 的路径变量:
#     PROJECT_SOURCE_DIR
#     <projectname>_SOURCE_DIR
# 用户执行cmake指令的路径:
#     PROJECT_BINARY_DIR
#     <projectname>_BINARY_DIR
# CMAKE_CURRENT_LIST_FILE: 输出调用这个变量的 CMakeLists.txt 的完整路径
# CMAKE_CURRENT_LIST_LINE：输出这个变量所在的行
# CMAKE_CURRENT_SOURCE_DIR：当前处理的 CMakeLists.txt 所在的路径
# CMAKE_CURRRENT_BINARY_DIR：如果是 in-source 编译，它跟 CMAKE_CURRENT_SOURCE_DIR 
#                            一致，如果是 out-of-source编译，他指的是 target 编译目录。
# CMAKE_CURRENT_BINARY_DIR 和 CMAKE_CURRENT_SOURCE_DIR 是面向 CMakeLists.txt
#     文件的源和目标根目录，而不像 PROJECT_SOURCE_DIR 和 PROJECTE_BINARY_DIR
#     是面向整个项目的源和目标的根目录
# CMAKE_MODULE_PATH：这个变量用来定义自己的 cmake 模块所在的路径。如果你的工程比较
#                    复杂，有可能会自己编写一些 cmake 模块，这些 cmake 模块是随你的
#                    工程发布的，为了让 cmake 在处理CMakeLists.txt 时找到这些模块。

# 需要通过 SET 指令，将自己的 cmake 模块路径设置一下。注意，CMAKE_MODULE_PATH 有
# 高优先级，当需要重写标准Find<package>.cmake文件时可能很有用。
MESSAGE(STATUS "    PROJECT_SOURCE_DIR: " ${PROJECT_SOURCE_DIR})
MESSAGE(STATUS "    mDemoPrj_SOURCE_DIR: " ${mDemoPrj_SOURCE_DIR})
MESSAGE(STATUS "    PROJECT_BINARY_DIR: " ${PROJECT_BINARY_DIR})
MESSAGE(STATUS "    mDemoPrj_BINARY_DIR: " ${mDemoPrj_BINARY_DIR})
MESSAGE(STATUS "    CMAKE_ROOTR: " ${CMAKE_ROOT})
MESSAGE(STATUS "    CMAKE_CURRENT_LIST_FILE: " ${CMAKE_CURRENT_LIST_FILE})
MESSAGE(STATUS "    CMAKE_CURRENT_LIST_LINE: " ${CMAKE_CURRENT_LIST_LINE})
MESSAGE(STATUS "    CMAKE_CURRENT_BINARY_DIR: " ${CMAKE_CURRENT_BINARY_DIR})
MESSAGE(STATUS "    CMAKE_CURRENT_SOURCE_DIR: " ${CMAKE_CURRENT_SOURCE_DIR})

MESSAGE(STATUS "-------- SET/GET ENV --------")
MESSAGE(STATUS "    HOME dir: $ENV{HOME}")
SET(ENV{HOME} "new home name")
MESSAGE(STATUS "    after set, HOME dir: $ENV{HOME}")
MESSAGE(STATUS "-------- SET/GET ENV END --------")

MESSAGE(STATUS "-------- EXEC SHELL CMD --------")

# 使用 ALL 关键字意味着这个自定义目标将作为默认构建目标的一部分被执行
# 如果只想在显式请求时才运行这个目标，可以省略 ALL
# 显式执行的方法为：执行cmake之后，显式执行：make my_custom_target
ADD_CUSTOM_TARGET(my_custom_target ALL
    # 当这个目标被构建时，会执行下面的 COMMAND
    COMMAND ${CMAKE_COMMAND} -E echo "My custom target is running!"
    # 这是一个可选的 COMMENT，它将在构建时显示在控制台中
    COMMENT "Running a custom target"
    # VERBATIM 选项告诉 CMake 不要对 COMMAND 进行任何解释或转义
    VERBATIM
)
# 如果想要让这个自定义目标成为默认构建目标（即，当只运行 'make' 或 'cmake --build .' 时），
# 可以添加一个 ALL 依赖。但注意，这通常不是推荐的做法，除非自定义目标是项目构建流程
# 的核心部分。这个方法不好用，可能是cmake不支持，需要的话建议直接在 add_custim_target
# 中添加 ALL
# add_dependencies(ALL my_custom_target)


# add_custom_command 在 CMake 中通常用于向特定的目标（如可执行文件、库或自定义目标）
# 添加自定义构建规则。
# 在 add_custom_command 的使用中，不能同时指定 TARGET 和 OUTPUT ，除非它们是在
# add_custom_command 的不同参数中使用的。在 add_custom_command 的上下文中，TARGET
# 参数通常用于将自定义命令与现有的目标（如可执行文件或库）关联起来，而 OUTPUT 参数
# 则用于指定自定义命令生成的输出文件。
# 如果这个自定义命令是某个目标的一部分，你需要将它添加到该目标的依赖中
# 例如，你可以使用 add_dependencies() 来添加一个依赖
ADD_CUSTOM_COMMAND(
    COMMAND ${CMAKE_COMMAND} -E echo "My custom command(TARGET) is running!"
    COMMENT "Running a custom command(TARGET)"
    VERBATIM
    # 将此自定义命令与 generate_header 目标关联起来
    TARGET my_custom_target
)

SET(M_CUSTOM_FILE ${CMAKE_CURRENT_BINARY_DIR}/custom_command.h)
# FILE(WRITE ${M_CUSTOM_FILE} "")
ADD_CUSTOM_COMMAND(
    OUTPUT ${M_CUSTOM_FILE}
    COMMAND ${CMAKE_COMMAND} -E echo "My custom command(OUTPUT) is running!" # > ${M_CUSTOM_FILE}
    COMMENT "Running a custom command(OUTPUT)"
    VERBATIM
)
# 创建一个自定义目标，该目标依赖于生成的文件
ADD_CUSTOM_TARGET(generate_file ALL DEPENDS ${M_CUSTOM_FILE})


MESSAGE(STATUS "-------- EXEC SHELL CMD END --------")


MESSAGE(STATUS "-------- FILE OPT --------")
# 创建一个目录
FILE(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/my_directory)
FILE(WRITE ${CMAKE_CURRENT_BINARY_DIR}/my_directory/file_opt.txt "write to file\n")
FILE(READ ${CMAKE_CURRENT_BINARY_DIR}/my_directory/file_opt.txt READ_MSG)
MESSAGE(STATUS "READ FROM FILE: ${READ_MSG}")
# FILE(APPEND filename "String to append")
# FILE(COPY source destination)
# FILE(RENAME source destination)
# FILE(REMOVE [file1 ...])
# FILE(REMOVE_RECURSE [dir1 ...])
# # 执行系统命令
# FILE(EXPR output variable operation)
# # 获取文件大小
# FILE(SIZE filename variable)
# # 获取文件权限
# FILE(GET_RUNTIME_DEPENDENCIES variable dependencies)
# # 遍历目录
# FILE(GLOB variable [RELATIVE path] [globbing expressions]...)
# FILE(GLOB_RECURSE variable [RELATIVE path] [globbing expressions]...)
# # 创建列表文件
# FILE(CONFIGURE OUTPUT output_file CONTENT content)

MESSAGE(STATUS "-------- FILE OPT END --------")

MESSAGE(STATUS "-------- DIRPROPERTY --------")
# GET_DIRECTORY_PROPERTY 获取的常见目录属性：
#   DEFINED_VARIABLES - 获取在当前目录的 CMakeLists.txt 文件中定义的所有变量的列表。
#   INCLUDE_DIRECTORIES - 获取为当前目录设置的包含目录列表。
#   LINK_DIRECTORIES - 获取为当前目录设置的链接目录列表。
#   COMPILE_DEFINITIONS - 获取为当前目录设置的编译定义列表。
#   COMPILE_OPTIONS - 获取为当前目录设置的编译选项列表。
#   DEFINITIONS - 获取为当前目录设置的宏定义列表（包括 -D 标志）。
#   CACHE_VARIABLES - 获取在 CMake 缓存中定义的所有变量的列表。
#   DIRECTORY - 获取当前处理的 CMakeLists.txt 文件的目录路径。
#   SOURCE_DIR - 获取源的目录路径。
#   BINARY_DIR - 获取二进制文件的目录路径。
#   CMAKE_HOME_DIRECTORY - 获取 CMake 主目录的路径，即运行 CMake 的顶层项目的路径。
#   CMAKE_CURRENT_SOURCE_DIR - 获取当前源代码目录的路径。
#   CMAKE_CURRENT_BINARY_DIR - 获取当前二进制目录的路径。
#   CMAKE_CURRENT_LIST_DIR - 获取包含当前处理的 CMakeLists.txt 文件的目录的路径。
#   CMAKE_CURRENT_LIST_FILE - 获取当前处理的 CMakeLists.txt 文件的完整路径。
#   CMAKE_CURRENT_LIST_LINE - 获取当前处理的 CMakeLists.txt 文件中的行号。
GET_DIRECTORY_PROPERTY(M_BINARY_DIR BINARY_DIR)
# 打印获取到的变量列表
MESSAGE(STATUS "M_BINARY_DIR: " ${M_BINARY_DIR})
MESSAGE(STATUS "-------- DIRPROPERTY END --------")

# ============================================================================== base options end

# ============================================================================== compile options
# 编译选项相关的CMake 变量如下：
# CMAKE_C_FLAGS =
# CMAKE_C_FLAGS_DEBUG = -g
# CMAKE_C_FLAGS_MINSIZEREL = -Os -DNDEBUG
# CMAKE_C_FLAGS_RELEASE = -O3 -DNDEBUG
# CMAKE_C_FLAGS_RELWITHDEBINFO = -O2 -g -DNDEBUG
# 
# CMAKE_CXX_FLAGS =
# CMAKE_CXX_FLAGS_DEBUG = -g
# CMAKE_CXX_FLAGS_MINSIZEREL = -Os -DNDEBUG
# CMAKE_CXX_FLAGS_RELEASE = -O3 -DNDEBUG
# CMAKE_CXX_FLAGS_RELWITHDEBINFO = -O2 -g -DNDEBUG
# 等号右边是通过在CMakeLists.txt中打印对应变量得到的默认值。
# 对于C语言设置CMAKE_C_FLAGS相关参数，C++语言设置CMAKE_CXX_FLAGS相关参数。
# 并且分为DEBUG，RELEASE，MINSIZEREL和RELWITHDEBINFO四种类型。
#
# 以C++语言编译选项为例：
# CMAKE_CXX_FLAGS_DEBUG：编译Debug版本的时候会采用的编译选项，默认只有一个-g选项，包含调试信息；
# CMAKE_CXX_FLAGS_RELEASE：编译Release版本的时候采用的编译选项，默认包-O3选项，该选项表示优化等级；
# CMAKE_CXX_FLAGS_MINSIZEREL：主要减小目标文件大小，选项-Os就是这个作用；
# CMAKE_CXX_FLAGS_RELWITHDEBINFO：包含调试信息的Release版本，-O2和-g，优化的同时也包含了调试信息；
# CMAKE_CXX_FLAGS：这个选项没有默认值；
# 公共的选项，不管是Release还是Debug都需要设置。这种情况还可以把公共的设置放在CMAKE_CXX_FLAGS变量里面

# 让 CMake 支持 gdb 只需要指定 Debug 模式下开启 -g 选项:
# 如果以变量作为 if 的判断条件，只要非空就是有效
# 可以通过-DCMAKE_BUILD_TYPE=Release 或者 -D CMAKE_BUILD_TYPE=Release 参数在编译时修改
if(NOT CMAKE_BUILD_TYPE)
    SET(CMAKE_BUILD_TYPE "Debug")
endif(NOT CMAKE_BUILD_TYPE)
MESSAGE(STATUS "    -- enter CMAKE_BUILD_TYPE " ${CMAKE_BUILD_TYPE})
# 以下参数同样可以在使用cmake 时通过 -D 参数修改
SET(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall -Wextra") # debug 和 release 都会使用的公用flag
SET(CMAKE_C_FLAGS_DEBUG "$ENV{CXXFLAGS} -O0 -g -ggdb")
SET(CMAKE_C_FLAGS_RELEASE "$ENV{CXXFLAGS} -O3")
SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra")
SET(CMAKE_CXX_FLAGS_DEBUG "$ENV{CXXFLAGS} -O0 -g -ggdb")
SET(CMAKE_CXX_FLAGS_RELEASE "$ENV{CXXFLAGS} -O3")
# add_compile_options 不区分编译器
# add_compile_options("-Wall")
# add_compile_options("-Wextra")

# 指定编译器
# SET(CMAKE_C_COMPILER "/usr/bin/arm-linux-gnueabihf-gcc")
# SET(CMAKE_CXX_COMPILER "/usr/.....")

# 变量 CMAKE_INCLUDE_CURRENT_DIR 的作用:
# 自动添加 CMAKE_CURRENT_BINARY_DIR 和 CMAKE_CURRENT_SOURCE_DIR 到当前处理的
# CMakeLists.txt。相当于在每个 CMakeLists.txt 加入:
#   INCLUDE_DIRECTORIES(${CMAKE_CURRENT_BINARY_DIR} ${CMAKE_CURRENT_SOURCE_DIR})
SET(CMAKE_INCLUDE_CURRENT_DIR ON)  # 不知道为什么失灵
INCLUDE_DIRECTORIES(${CMAKE_CURRENT_BINARY_DIR} ${CMAKE_CURRENT_SOURCE_DIR})

# 指定生成链接链接库的存放路径,不指定的话默认是存放在跟当前 CMakeLists.txt 一样的路径
# 该设置也可以跟随 ADD_LIBRARY 指令，放在该指令之前，这样控制更精确
MESSAGE(STATUS "    Before set LIBRARY_OUTPUT_PATH: " ${LIBRARY_OUTPUT_PATH})
SET(LIBRARY_OUTPUT_PATH ${PROJECT_BINARY_DIR}/lib)
MESSAGE(STATUS "    After set LIBRARY_OUTPUT_PATH: " ${LIBRARY_OUTPUT_PATH})

# 指定生成可执行文件后的存放路径
# 该设置也可以跟随 ADD_EXECUTABLE 指令，放在该指令之前，这样控制更精确
SET(EXECUTABLE_OUTPUT_PATH ${PROJECT_BINARY_DIR}/bin)
# ============================================================================== compile options end

# ============================================================================== 表达式
# 参考博客：https://zhuanlan.zhihu.com/p/437404485
# 生成器表达式的格式形如$<...>，可以嵌套，可以用在很多构建目标的属性设置和特定的CMake命令中。
# 值得强调的是，生成表达式被展开是在生成构建系统的时候，所以不能通过解析配置CMakeLists.txt阶段的message命令打印
# 具体细节可以到博客中查看
# ============================================================================== 表达式 end

# ============================================================================== custome compile options
# configure_file(<input> <output> [COPYONLY] [ESCAPE_QUOTES] [@ONLY] [NEWLINE_STYLE [UNIX|DOS|WIN32|LF|CRLF] ])
# configure_file 主要实现如下两个功能:
#     1. 将 <input> 文件里面的内容全部复制到 <output> 文件中；
#     2. 根据参数规则，替换 @VAR@ 或 ${VAR} 变量；
# 参数解析
#     COPYONLY        仅拷贝 <input> 文件里面的内容到 <output> 文件， 不进行变量的替换；
#     ESCAPE_QUOTES   使用反斜杠（C语言风格）来进行转义；
#     @ONLY           限制替换， 仅仅替换 @VAR@ 变量， 不替换 ${VAR} 变量
#     NEWLINE_STYLE   指定输入文件的新行格式， 例如：Unix 中使用的是 \n, windows 中使用的 \r\n
# **注意: ** COPYONLY 和 NEWLINE_STYLE 是冲突的，不能同时使用；
#         CONFIGURE_FILE可以调用一次，也可以调用多次，多次调用的时候，如果变量有修改，会使用
#         最后调用 CONFIGURE_FILE 时的变量，也可以理解为，只有最后一次调用 CONFIGURE_FILE 是
#         有效的。
#
# 加入一个配置头文件，用于处理 CMake 对源码的设置
# configure_file 命令用于加入一个配置头文件 config.h ，这个文件由 CMake 从 config.h.in 生成，
#                通过这样的机制，将可以通过预定义一些参数和变量来控制代码的生成。
# configure.h.in 中的 #cmakedefin USE_MYMATH 可以对应到 CMakeLists.txt 中的宏
CONFIGURE_FILE (
    "${PROJECT_SOURCE_DIR}/config.h.in"
    "${PROJECT_BINARY_DIR}/config.h"
    )

# option(<option_variable> "help string describing option" [initial value])
# 提供一个选项供用户选择为ON或OFF。 如果未提供初始值，则使用OFF。该选则可以在调用CMAKE时使用形如
#     cmake -D USE_MYMATH=OFF ..
#     或 cmake -DUSE_MYMATH=OFF ..
# 的方式来设定，通过cmake指令设定的优先级要高于 option 的默认值
# 是否使用自己的 MathFunctions 库
# option 命令添加了一个 USE_MYMATH 选项，并且默认值为 ON 。
OPTION(USE_MYMATH "Use provided math implementation" ON)
MESSAGE(STATUS "    USE_MYMATH is: " ${USE_MYMATH})

# 是否加入 MathFunctions 库
if (USE_MYMATH)
    MESSAGE(STATUS "    USE_MYMATH is valid")
    # 这里关闭是因为在 config.h.in 中有定义，正常添加宏定义是需要打开的
    # ADD_DEFINITIONS(-DUSE_MYMATH)  
    INCLUDE_DIRECTORIES ("${PROJECT_SOURCE_DIR}/src/math")
    ADD_SUBDIRECTORY (src/math)
    SET (EXTRA_LIBS ${EXTRA_LIBS} mathFunctions)
endif (USE_MYMATH)
# ============================================================================== custome compile options end

# ============================================================================== add git info 
#-- ver 1 直接由CMake写文件
FIND_PACKAGE(Git)
# 生成版本描述字符串类似 TAG-X-gHASH
EXECUTE_PROCESS(COMMAND ${GIT_EXECUTABLE} describe --abbrev=6 --dirty --always --tags
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
    OUTPUT_VARIABLE  GIT_REPO_VERSION
    OUTPUT_STRIP_TRAILING_WHITESPACE
)

# 获取最新提交作者
EXECUTE_PROCESS(COMMAND ${GIT_EXECUTABLE} log -1 --format=%an
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
    OUTPUT_VARIABLE  GIT_REPO_AUTHOR
    OUTPUT_STRIP_TRAILING_WHITESPACE
)
# 获取最新 commit 日期，YYYY-MM-DD
EXECUTE_PROCESS(COMMAND ${GIT_EXECUTABLE} log -1 --format=%cd --date=short
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
    OUTPUT_VARIABLE  GIT_REPO_DATE
    OUTPUT_STRIP_TRAILING_WHITESPACE
)
# 获取最新 commit Hash
EXECUTE_PROCESS(COMMAND ${GIT_EXECUTABLE} log -1 --format=%H
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
    OUTPUT_VARIABLE  GIT_REPO_HASH
    OUTPUT_STRIP_TRAILING_WHITESPACE
)
# 写入头文件宏定义的版本字符串，日期和 Hash
FILE(WRITE ${PROJECT_BINARY_DIR}/git_version.h
    "#define GIT_VER \"${GIT_REPO_VERSION}\"\n#define GIT_AUTHOR \"${GIT_REPO_AUTHOR}\"\n#define GIT_DATE \"${GIT_REPO_DATE}\"\n#define GIT_HASH \"${GIT_REPO_HASH}\"\n"
)
# 包含引用目录，源文件可以直接用 #include "git_version.h" 包含
INCLUDE_DIRECTORIES(${PROJECT_BINARY_DIR})


#-- ver 2 借助config

SET(GIT_LOG_FORMAT "%h author: %<|(30)%an %cd %s %d")

EXECUTE_PROCESS(COMMAND ${GIT_EXECUTABLE} log -1 --oneline --date=short --pretty=format:${GIT_LOG_FORMAT}
    WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}
    OUTPUT_VARIABLE EXEC_OUT
    ERROR_VARIABLE EXEC_ERROR
    RESULT_VARIABLE EXEC_RET
    OUTPUT_STRIP_TRAILING_WHITESPACE
    ERROR_STRIP_TRAILING_WHITESPACE)

if (NOT EXEC_RET)
    SET(VERSION_LOG ${EXEC_OUT})
    STRING(REPLACE "\"" "\\\"" VERSION_LOG ${VERSION_LOG})
    MESSAGE(STATUS "git version: " ${VERSION_LOG})
    SET(VERSION_HISTORY "\"${VERSION_LOG}\"")
endif()

# 从新生成 config.h 以包含版本信息
CONFIGURE_FILE (
    "${PROJECT_SOURCE_DIR}/config.h.in"
    "${PROJECT_BINARY_DIR}/config.h"
    )



#-- ver 3 借助config 生成多条log
SET(VERSION_CNT         0)
SET(VERSION_MAX_CNT     9)
SET(VERSION_INFO        "\"unknown mpp version for missing VCS info\"")
FOREACH(CNT RANGE ${VERSION_MAX_CNT})
    SET(VERSION_HISTORY_${CNT} "NULL")
ENDFOREACH(CNT)

IF(EXISTS "${PROJECT_SOURCE_DIR}/../../.git")
    find_package(Git)
    IF(GIT_FOUND)
        # get current version info
        SET(GIT_LOG_FORMAT "%h author: %<|(30)%an %cd %s")

        EXECUTE_PROCESS(COMMAND ${GIT_EXECUTABLE} log -1 --oneline --date=short --pretty=format:${GIT_LOG_FORMAT}
            WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}
            OUTPUT_VARIABLE EXEC_OUT
            ERROR_VARIABLE EXEC_ERROR
            RESULT_VARIABLE EXEC_RET
            OUTPUT_STRIP_TRAILING_WHITESPACE
            ERROR_STRIP_TRAILING_WHITESPACE)

        IF(NOT EXEC_RET)
            SET(VERSION_INFO ${EXEC_OUT})
            MESSAGE(STATUS "current version:")
            MESSAGE(STATUS "${VERSION_INFO}")
            STRING(REPLACE "\"" "\\\"" VERSION_INFO ${VERSION_INFO})
            SET(VERSION_INFO "\"${VERSION_INFO}\"")
        ELSE(NOT EXEC_RET)
            MESSAGE(STATUS "git ret ${EXEC_RET}")
            MESSAGE(STATUS "${EXEC_ERROR}")
        ENDIF(NOT EXEC_RET)

        SET(GIT_LOG_FORMAT "%h author: %<|(30)%an %cd %s %d")

        # get history version information
        # setup logs
        MESSAGE(STATUS "git version history:")
        foreach(CNT RANGE ${VERSION_MAX_CNT})
            EXECUTE_PROCESS(COMMAND ${GIT_EXECUTABLE} log HEAD~${CNT} -1 --oneline --date=short --pretty=format:${GIT_LOG_FORMAT}
                WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}
                OUTPUT_VARIABLE EXEC_OUT
                ERROR_VARIABLE EXEC_ERROR
                RESULT_VARIABLE EXEC_RET
                OUTPUT_STRIP_TRAILING_WHITESPACE
                ERROR_STRIP_TRAILING_WHITESPACE)

            IF(NOT EXEC_RET)
                SET(VERSION_LOG ${EXEC_OUT})
                STRING(REPLACE "\"" "\\\"" VERSION_LOG ${VERSION_LOG})
                MESSAGE(STATUS ${VERSION_LOG})
                SET(VERSION_HISTORY_${CNT} "\"${VERSION_LOG}\"")
                math(EXPR VERSION_CNT "${VERSION_CNT}+1")
            ENDIF(NOT EXEC_RET)
        ENDFOREACH(CNT)
        MESSAGE(STATUS "total ${VERSION_CNT} git version recorded")
    ENDIF(GIT_FOUND)
ENDIF(EXISTS "${PROJECT_SOURCE_DIR}/../../.git")

CONFIGURE_FILE(
    "${PROJECT_SOURCE_DIR}/config.h.in"
    "${PROJECT_BINARY_DIR}/config.h"
    @ONLY
)
# ============================================================================== add git info end

# ============================================================================== cmake 脚本

# include 指令用法：
# include(<file|module> [OPTIONAL] [RESULT_VARIABLE <VAR>] [NO_POLICY_SCOPE])
# 可知 include 指令用来载入并运行来自于文件或模块的 CMake 代码。

# (1)  cmake文件里面通常包含的信息:
#     - '.cmake文件'里包含了一些"公共(复用)"的'cmake命令'和一些'宏|函数'
#     - 当CMakeLists.txt'包含该.cmake文件'时,当'编译'运行时,该.cmake里的一些命令就会
#       在该'包含处'得到加载'执行',在'后续'能够'调用该.cmake里'的一些宏和函数
#     - .cmake文件是一个'模块(module)文件',可以被'include'到CMakeLists.txt中
# 注意：cmake'脚本'不要包含'工程之类'的信息 -->例如:add_subdirectory()、CMAKE_CURRENT_之类的
#       cmake'不要'调用CMakeLists.txt
#
# (2) .cmake模块文件被加载的时机是在CMakeLists.txt 中
#     - include(module_name|file)
#     - find_package(module_name)
# 注意：这两种加载方式是有区别的,或者说find_package中'.cmake全文件名'有一定的要求。
#       另外如果加载的是文件(file)，则需要在命令中添加 .cmake 后缀，如果是模块，则不需要
#       .cmake 后缀，例如：
#           include(OpenCV)
#           include(my_file.cmake)

# 普通文件(file)
# 1）相对路径: 是相对include指令所在的CMakeLists.txt的路径
# 2）绝对路径(建议): 一般我们会将'cmake'文件放到cmake目录下,所以前缀一般是：
#    CMAKE_CURRENT_SOURCE_DIR/cmake/file
# 注意：这里的'file'文件,必须以'.cmake'结尾
#
# 模块文件(module)
# 1）首先搜索'Cmake builtin module directory' -->'cmake 内置的module目录'-->'centos7 /usr/share/cmake/MOdules/'
# 2）找不到'再搜索'-->'CMAKE_MODULE_PATH'
# 3）再找不到,则'报错'-->'NOTFOUND'
# 注意：include 命令中非'.cmake'结尾的文件表示是'module'-->会自动查找'内建-->CMAKE_MODULE_PATH'路径下的"module_name.cmake"文件
#       另外这里的搜索路径是 include 的搜索路径，可能与 find_packet 会有区分
#
# include(src/CMakeLists.txt) -->cmake也可以这样做,但是相对'add_subdirectory(src)',我们'不推荐'前者
# 原因： include破坏了'Build Tree'的机制-->不能将'Source Tree'在'build'下'映射'成'Build Tree'

# 同样需要加在 ADD_SUBDIRECTORY 之前才能传递到子目录
INCLUDE("src/main.cmake")

# 自定义函数
my_custom_function(MY_VARIABLE "Hello, CMake! This my custom function")
message(STATUS "MY_VARIABLE: ${MY_VARIABLE}")

# ============================================================================== cmake 脚本 end

# ============================================================================== 其他

# 指定生成目标
# ADD_EXECUTABLE(Demo ${DIR_SRCS})
# TARGET_LINK_LIBRARIES (Demo  ${EXTRA_LIBS})

# SET(<VAR> -) 主调用CMakeLists.txt文件通过SET设置的变量可以传递到子目录的CMakeLists.txt中，
# 但反过来不行,无论在 ADD_SUBDIRECTORY 之前还是之后

# 主调CMakeLists.txt向子目录中的CMakeLists.txt中传递变量时需要将变量的设置放在
# ADD_SUBDIRECTORY 指令之前，否则传不下去
SET(MAINVAL "this is main CMakeLists VAL")

# 如果工程存在多个目录，需要确保每个要管理的目录存在一个CMakeLists.txt

# 无论CMakeLists.txt文件在根目录还是子目录中，也无论一个工程有一个还是多个CMakeList文件，
# 文件里的路径起点均为文件当前位置。

# 该指令可以指定中间二进制和目标二进制文件的存放位置，可以使用类似 ADD_SUBDIRECTORY(src bin) 的形式，
# 这项当于在编译的时候把 src 的名字改成bin。
ADD_SUBDIRECTORY(src)

# ============================================================================== 其他 end

# ============================================================================== cmake 常用架构方式
# 1. 类似当前demo，添加各个子文件夹，在子文件夹中各自编译
# 2. 子文件夹中只负责将相应文件收集到变量中，最终变量在顶层cmake中处理
# 3. 使用target_sources 命令，可以理解是子文件夹主动提交必要的目标文件，而不是顶层cmake向下查询
# ============================================================================== cmake 常用架构方式 end

# ============================================================================== install and test
# install用于指定在安装时运行的规则。它可以用来安装很多内容，可以包括目标二进制、
# 动态库、静态库以及文件、目录、脚本等：
#     install(TARGETS <target>... [...])          目标文件：通过ADD_EXECUTABLE或者ADD_LIBRARY定义的目标文件，
#                                                           即可执行二进制、动态库、静态库
#     install({FILES | PROGRAMS} <file>... [...]) 普通文件/脚本之类：用于安装一般文件
#     install(DIRECTORY <dir>... [...])           目录：安装目录
#     install(SCRIPT <file> [...])                cmake脚本
#     install(CODE <code> [...])
#     install(EXPORT <export-name> [...])

# 参数 DESTINATION 用于指定安装目录，该指定是以 CMAKE_INSTALL_PREFIX 变量指向的路径开始，
# 例如 DESTINATION bin 表示 ${CMAKE_INSTALL_PREFIX}/bin，但是如果 bin 以 / 开头就表示绝对路径，
# 变量 CMAKE_INSTALL_PREFIX 就不起作用了

# 变量 CMAKE_INSTALL_PREFIX 可以在编译的时候进行控制，例如: cmake -DCMAKE_INSTALL_PREFIX=. .. 
# 或 cmake -DCMAKE_INSTALL_PREFIX=$PWD ..
MESSAGE(STATUS "    CMAKE_INSTALL_PREFIX: " ${CMAKE_INSTALL_PREFIX})
# 指定 mathFunctions 库的安装路径
if (USE_MYMATH)
    INSTALL(TARGETS mathFunctions DESTINATION bin)
    INSTALL(FILES src/math/mathFunctions.h DESTINATION include)  # 安装文件时注意以当前 CMakeListas.txt 文件为路径的起点
endif (USE_MYMATH)
INSTALL(TARGETS demo DESTINATION bin)
INSTALL(FILES "${PROJECT_BINARY_DIR}/config.h" DESTINATION include)

# ============================================================================== install and test end


# ============================================================================== 使用外部库
# 原始方法
# 使用外部库最基础的写法是需要以下三个部分
#     1. INCLUDE_DIRECTORIES  对应 gcc/g++ 的 -I 参数，写在顶层主调 CMakeLists.txt 中就可以，
#        可以传递到子文件夹中
#     2. LINK_DIRECTORIES 对应 gcc/g++ 的 -L 参数,指定库文件的路径
#     3. TARGET_LINK_LIBRARIES 对应 gcc/g++ 的 -l 参数，为了方便使用可以在第2步之后
#        使用一个变量保存用到的库 (SET(......))

# 使用查找包的方式
# FIND_PACKAGE 用来调用预定义在 CMAKE_MODULE_PATH 下的 Find<name>.cmake模块
# FIND_PACKAGE 执行后会赋值的变量:
#     <name>_FOUND
#     <name>_INCLUDE_DIRS 或 <name>_INCLUDES
#     <name>_LIBRARIES 或 <name>_LIBS
#     <name>_DEFINITIONS


# find_packet()的用法:
# find_packet()有两种模式，Module模式和Config模式，其中Module模式是基础用法，Config模式较为复杂。
# Module模式下，如果按照用户指定的配置找不到包，主会自动进入Config模式
# 
# - Module模式:
# find_package(<PackageName> [version] [EXACT] [QUIET] [MODULE] [REQUIRED]
#              [[COMPONENTS] [components...]] [OPTIONAL_COMPONENTS components...]
#              [NO_POLICY_SCOPE])
# 其中：
#   version 如果指定就必须检查找到的包的版本是否与version兼容
#   EXACT 与version配合使用，如果指定version的同时又指定EXACT，必须检查找到的包的版本是否与version匹配
#   QUIET 如果查找失败，不会在屏幕上输出（如果指定了REQUIRED，则QUIET失效）
#   MODULE 只在Module模式下查找
#   REQUIRED 表示一定要找到包，如果失败则停止cmake
#   COMPONENTS components 表示一定要找到组件，如果失败则停止cmake
#   OPTIONAL_COMPONENTS components 表示找不到组件，也继续执行cmake
# 
# 查找顺序：Module 模式下查找名为 Find<PackageName>.cmake 的文件，
#     先在 CMAKE_MODULE_PATH 变量对应的路径下查找，如果路径为空或者查找失败，
#     则在 cmake 安装时的module目录下查找，如：/usr/lib/x86_64-linux-gnu/cmake
#
# - Config模式：
# find_package(<PackageName> [version] [EXACT] [QUIET] [REQUIRED] [[COMPONENTS] [components...]]
#              [CONFIG|NO_MODULE] [NO_POLICY_SCOPE] [NAMES name1 [name2 ...]]
#              [CONFIGS config1 [config2 ...]] [HINTS path1 [path2 ... ]] [PATHS path1 [path2 ... ]]
#              [PATH_SUFFIXES suffix1 [suffix2 ...]] [NO_DEFAULT_PATH] [NO_PACKAGE_ROOT_PATH]
#              [NO_CMAKE_PATH] [NO_CMAKE_ENVIRONMENT_PATH] [NO_SYSTEM_ENVIRONMENT_PATH]
#              [NO_CMAKE_PACKAGE_REGISTRY] [NO_CMAKE_BUILDS_PATH] # Deprecated; does nothing.
#              [NO_CMAKE_SYSTEM_PATH] [NO_CMAKE_SYSTEM_PACKAGE_REGISTRY]
#              [CMAKE_FIND_ROOT_PATH_BOTH | ONLY_CMAKE_FIND_ROOT_PATH | NO_CMAKE_FIND_ROOT_PATH])
# 查找顺序：Config模式下查找名为 <PackageName>.Config.cmake 或 <lower-case-package-name>-config.cmake 的文件
# 查找顺序如下：
#   1. <PackageName>_ROOT 的cmake变量或者环境变量
#      注意：如果指定了 <PackageName>_DIR cmake变量，那么 <PackageName>_ROOT 将不起作用
#   2. cmake特定的缓存变量
#      CMAKE_PREFIX_PATH
#      CMAKE_FRAMEWORK_PATH
#      CMAKE_APPBUNDLE_PATH
#      可以通过设定NO_CMAKE_PATH来关闭这一查找顺序
#   3. cmake待定的环境变量
#      <PackageName>_DIR
#      CMAKE_PREFIX_PATH
#      CMAKE_FRAMEWORK_PATH
#      CMAKE_APPBUNDLE_PATH
#      可以通过NO_CMAKE_ENVIRONMENT_PATH来跳过
#   4. HINT字段指定的路径
#   5. 系统环境变量PATH
#      其中如果是以/bin或者/sbin结尾的，会自动转化为其父目录
#      通过指定NO_SYSTEM_ENVIRONMENT_PATH来跳过
#   6. 存储在cmake的"User Package Registry"(用户包注册表)中的路径。
#      通过设定NO_CMAKE_PACKAGE_REGISTRY，或者：设定CMAKE_FIND_PACKAGE_NO_PACKAGE_REGISTRY为true来避开
#   7. 设定为当前系统定义的cmake变量：
#      CMAKE_SYSTEM_PREFIX_PATH
#      CMAKE_SYSTEM_FRAMEWORK_PATH
#      CMAKE_SYSTEM_APPBUNDLE_PATH
#      通过设定NO_CMAKE_SYSTEM_PATH来跳过
#   8. 在cmake的"System Package Registry"(系统包注册表）中查找。
#      通过设定NO_CMAKE_SYSTEM_PACKAGE_REGISTRY跳过。或者通过设定
#      CMAKE_FIND_PACKAGE_NO_SYSTEM_PACKAGE_REGISTRY为true
#   9. 从PATHS字段指定的路径中查找


message(STATUS "    CMAKE_MODULE_PATH: " ${CMAKE_MODULE_PATH})
FIND_PACKAGE(OpenCV REQUIRED)
IF(NOT OpenCV_FOUND)
    MESSAGE(FATAL_ERROR "OpenCV Not Found!")
ENDIF(NOT OpenCV_FOUND)
message(STATUS "OpenCV library status:")
message(STATUS "    config: ${OpenCV_DIR}")
message(STATUS "    version: ${OpenCV_VERSION}")
message(STATUS "    libraries: ${OpenCV_LIBS}")
message(STATUS "    include path: ${OpenCV_INCLUDE_DIRS}")

# ============================================================================== 使用外部库  end

# ============================================================================== add test
# CMake 提供了一个称为 CTest 的测试工具。我们要做的只是在项目根目录的 CMakeLists 文件中
# 调用一系列的 add_test 命令
# 启用测试
ENABLE_TESTING()

# 测试程序是否成功运行
ADD_TEST(test_run ${PROJECT_BINARY_DIR}/bin/demo 5 2)

# 测试帮助信息是否可以正常提示
add_test (test_usage ${PROJECT_BINARY_DIR}/bin/demo)
set_tests_properties (test_usage
    PROPERTIES PASS_REGULAR_EXPRESSION "Usage: .* base exponent")

# 测试 5 的平方
add_test (test_5_2 ${PROJECT_BINARY_DIR}/bin/demo 5 2)

set_tests_properties (test_5_2
    PROPERTIES PASS_REGULAR_EXPRESSION "is 25")

# 测试 10 的 5 次方
add_test (test_10_5 ${PROJECT_BINARY_DIR}/bin/demo 10 5)

set_tests_properties (test_10_5
    PROPERTIES PASS_REGULAR_EXPRESSION "is 100000")

# 测试 2 的 10 次方
add_test (test_2_10 ${PROJECT_BINARY_DIR}/bin/demo 2 10)

set_tests_properties (test_2_10
    PROPERTIES PASS_REGULAR_EXPRESSION "is 1024")

# 上面的代码包含了四个测试。第一个测试 test_run 用来测试程序是否成功运行并返回 0 值。
# 剩下的三个测试分别用来测试 5 的 平方、10 的 5 次方、2 的 10 次方是否都能得到正确的结果。
# 其中 PASS_REGULAR_EXPRESSION 用来测试输出是否包含后面跟着的字符串。

# 如果要测试更多的输入数据，像上面那样一个个写测试用例未免太繁琐。这时可以通过编写宏来实现：
# 定义一个宏，用来简化测试工作
# macro (do_test arg1 arg2 result)
#     add_test (test_${arg1}_${arg2} ${PROJECT_BINARY_DIR}/bin/demo ${arg1} ${arg2})
#     set_tests_properties (test_${arg1}_${arg2}
#         PROPERTIES PASS_REGULAR_EXPRESSION ${result})
# endmacro (do_test)
 
# 使用该宏进行一系列的数据测试
# do_test (5 2 "is 25")
# do_test (10 5 "is 100000")
# do_test (2 10 "is 1024")
# ============================================================================== add test end

# ============================================================================== CPack 包
# 构建一个 CPack 安装包
# include(<file|module> [OPTIONAL] [RESULT_VARIABLE <var>] [NO_POLICY_SCOPE])
# Loads and runs CMake code from the file given. Variable reads and writes access the scope of the 
# caller (dynamic scoping). If OPTIONAL is present, then no error is raised if the file does not exist. 
# If RESULT_VARIABLE is given the variable <var> will be set to the full filename which has been 
# included or NOTFOUND if it failed.

# If a module is specified instead of a file, the file with name <modulename>.cmake is searched first in 
# CMAKE_MODULE_PATH, then in the CMake module directory. There is one exception to this: if the file which 
# calls include() is located itself in the CMake builtin module directory, then first the CMake builtin 
# module directory is searched and CMAKE_MODULE_PATH afterwards. See also policy CMP0017.

# See the cmake_policy() command documentation for discussion of the NO_POLICY_SCOPE option.

include (InstallRequiredSystemLibraries)
set (CPACK_RESOURCE_FILE_LICENSE
  "${CMAKE_CURRENT_SOURCE_DIR}/License.txt")
set (CPACK_PACKAGE_VERSION_MAJOR "${Demo_VERSION_MAJOR}")
set (CPACK_PACKAGE_VERSION_MINOR "${Demo_VERSION_MINOR}")
include (CPack)

# 上面的代码做了以下几个工作：
#     1. 导入 InstallRequiredSystemLibraries 模块，以便之后导入 CPack 模块；
#     2. 设置一些 CPack 相关变量，包括版权信息和版本信息，其中版本信息用了上一节定义的版本号；
#     3. 导入 CPack 模块。
# 接下来的工作是像往常一样构建工程，并执行 cpack 命令。
# 生成二进制安装包：
#     cpack -C CPackConfig.cmake
# 生成源码安装包
#     cpack -C CPackSourceConfig.cmake

# ============================================================================== CPack 包 end

MESSAGE(STATUS "-------- MAIN CMAKELISTS MSG END --------")
