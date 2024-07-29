# CMakeLists.txt
cmake_minimum_required(VERSION 3.10.2)

# 设置NDK路径（可选，如果已经在环境变量中设置了）
# set(CMAKE_TOOLCHAIN_FILE $ENV{NDK_ROOT}/build/cmake/android.toolchain.cmake)

# 设置Android平台和ABI
set(ANDROID_ABI "armeabi-v7a") # 或者其他ABI，如arm64-v8a, x86, x86_64等
set(ANDROID_PLATFORM 21) # 最小API级别，例如21对应Android 5.0 Lollipop

# 设置CMake Android属性
set(CMAKE_ANDROID_ARCH_ABI ${ANDROID_ABI})
set(CMAKE_ANDROID_NDK_TOOLCHAIN_VERSION clang)
set(CMAKE_SYSROOT $ENV{NDK_ROOT}/platforms/android-${ANDROID_PLATFORM}/arch-${ANDROID_ABI})
set(CMAKE_ANDROID_STL_TYPE c++_static) # 使用静态STL库

# 设置项目名称和源文件
project(NDKDemo)
add_executable(ndk-demo main.cpp)

# 查找并链接必要的库（如果有的话）
# find_library(...)
# target_link_libraries(ndk-demo ...)

# 设置输出路径（可选）
# set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/libs/${ANDROID_ABI})
# set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/bin/${ANDROID_ABI})
