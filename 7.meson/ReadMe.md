# Meson 简介

Meson 是一种轻量级的开源构建系统，旨在提高软件的编译速度并简化构建配置过程。
它特别适用于大型 C、C++ 项目，但也支持其他编程语言，如 Python、Rust 和 Fortran。
Meson 的设计目标是提供一个高效、现代化、跨平台的构建工具，能够在各种操作系统（如
Linux、Windows、macOS）上顺利运行。

## Meson 的特点：

1. **高速构建**：
   - Meson 的构建速度非常快。它通过最大限度减少文件依赖的计算和构建步骤中的不必要
     操作，来加速编译过程。
   - 它通常与 Ninja 一起使用，Ninja 是一个高效的构建工具，可以非常快速地执行编译任务。

2. **简单的语法**：
   - Meson 使用一个基于 Python 的自定义脚本语言，其配置文件称为 `meson.build`。
     相较于传统的 Makefile 或 CMake，Meson 的语法更加简洁易读，降低了配置和维护
     项目的复杂性。

3. **自动依赖管理**：
   - Meson 可以自动检测系统中安装的库和依赖项，简化了依赖配置过程。它支持多种包
     管理系统，如 pkg-config、CMake、和 `vcpkg`。

4. **跨平台支持**：
   - Meson 具备强大的跨平台能力，支持 Linux、Windows、macOS 等不同操作系统。无论
     是编译原生代码还是跨平台开发，Meson 都能胜任。

5. **多语言支持**：
   - 虽然 Meson 最初主要用于 C 和 C++ 项目，但它也支持多种编程语言，如 Python、
     Rust、Java、Fortran 等。这使得 Meson 适合构建多语言项目。

6. **良好的测试支持**：
   - Meson 内置了强大的测试框架，允许开发者轻松定义和运行单元测试。同时，它还支持
     代码覆盖率分析和内存泄漏检查等功能。

7. **模块化架构**：
   - Meson 提供了大量可扩展模块，支持不同的构建需求。例如，它包含支持 Qt、GTK、
     GStreamer、SDL 等框架的模块，方便开发者集成各种项目依赖。

## Meson 的工作流程：
1. **初始化项目**：通过 `meson setup` 命令，Meson 读取 `meson.build` 文件，设置
   构建目录并生成 Ninja 或其他构建工具的文件。
2. **编译代码**：执行 `meson compile`，使用 Ninja 或其他后端工具完成编译任务。
3. **运行测试**：通过 `meson test` 运行项目的单元测试。
4. **安装项目**：执行 `meson install` 将编译后的项目文件安装到指定路径。

## 示例 `meson.build` 文件：

```meson
project('my_project', 'c')

executable('my_app', 'main.c')
```

这个简单的示例定义了一个 C 项目，并指定了编译一个名为 `my_app` 的可执行文件。


Ninja 是一个专为**速度和效率**设计的现代构建系统，旨在处理大规模项目的增量构建。
它的设计目标是比传统构建工具（如 `Make`）更快，尤其是在项目非常庞大的情况下。
Ninja 本身并不负责生成构建脚本，而是作为低层次的构建执行工具，通常与其他构建系统
（如 Meson、CMake）结合使用，以加快编译速度。

# Ninja简介

## Ninja 的特点

1. **极快的构建速度**：
   - Ninja 的设计理念就是速度。它通过**最小化文件 IO**、**优化依赖关系处理**，
     以及**并行执行任务**，来最大限度地减少不必要的编译步骤。
   - Ninja 特别擅长**增量构建**，即只编译那些自上次构建后被修改的文件，从而显著
     减少重复编译的时间。

2. **简单的设计**：
   - Ninja 的构建文件非常简洁、紧凑。它的构建脚本（`.ninja` 文件）是高度结构化的、
     易于解析的文本文件，但通常不会手动编写，而是由诸如 CMake 或 Meson 这样的上层
     工具生成。
   - Ninja 只处理构建规则和依赖关系，不提供复杂的宏或控制流功能，简化了构建过程。

3. **并行构建**：
   - Ninja 能够高效地管理并行任务，充分利用多核处理器，从而极大提高编译速度。它
     自动计算任务的依赖关系，确保最大程度的并发。

4. **精确的依赖管理**：
   - Ninja 可以非常准确地追踪文件依赖关系，确保每次构建只重新编译确实需要重新编译
     的部分。这种精确性有助于避免不必要的编译工作，从而提高效率。

5. **小体积和低内存占用**：
   - Ninja 是一个非常轻量的工具，二进制文件的大小很小，并且在处理大规模项目时对
     系统资源的需求也相对较低。这使得它适合在资源受限的环境下使用。

6. **构建日志**：
   - Ninja 可以生成构建日志，帮助开发者追踪构建过程中发生的错误或警告。此外，它
     也可以输出构建时间统计信息，便于分析构建过程中的瓶颈。

## Ninja 的工作流程

1. **生成 Ninja 构建文件**：通常由上层构建系统（如 Meson、CMake）生成一个 `.ninja`
   构建脚本，定义了构建目标、编译规则和依赖关系。
2. **执行构建**：通过运行 `ninja` 命令，它会根据生成的 `.ninja` 文件，自动执行
   编译和链接等步骤。
3. **增量构建**：Ninja 会在构建过程中记录所有生成文件的时间戳和状态信息，确保下一次
   构建只更新修改过的文件。

## Ninja 构建文件示例

以下是一个简单的 `.ninja` 文件示例：

```ninja
rule cc
  command = gcc -c $in -o $out
  description = Compiling $in

rule link
  command = gcc $in -o $out
  description = Linking $out

build hello.o: cc hello.c
build hello: link hello.o
```

这个文件定义了两条规则：
1. **cc**：用于编译 C 文件，生成 `.o` 对象文件。
2. **link**：用于链接对象文件，生成最终的可执行文件。

## Ninja 与 Make 的对比

- **速度**：Ninja 比 `Make` 更快，尤其是在处理增量构建时。Ninja 通过更高效的依赖
  追踪和并行构建实现显著的速度提升。
- **构建文件**：`Makefile` 通常是手动编写并具有复杂的语法，易出错。而 Ninja 构建
  文件通常由其他工具自动生成，简洁、无冗余。
- **复杂性**：`Make` 具有宏、条件判断等高级特性，灵活但复杂；而 Ninja 则简化了构建
  描述，只关注构建步骤本身，依赖外部工具生成配置文件。

## 使用场景

- **大型项目**：Ninja 特别适合管理数百到数千个文件的大型项目，通过其高效的并行执行
  和依赖管理加速构建。
- **增量构建**：在项目频繁修改的情况下，Ninja 能够快速响应变更，只重编译必要的部分，
  从而节省时间。



# Meson 的基础使用方法

Meson 项目的配置文件为 `meson.build`，它定义了项目的名称、编译的源文件、依赖库等
内容。Meson 通常与 Ninja 一起使用，Ninja 是 Meson 默认的后端工具，负责执行具体的
编译任务。

## Meson 的基本使用步骤：

1. **安装 Meson**：
   Meson 可以通过 Python 包管理器 `pip` 进行安装：
   ```bash
   pip install meson
   ```

2. **初始化项目**：
   在项目根目录创建一个名为 `meson.build` 的文件，定义项目的配置信息。

3. **设置构建目录**：
   执行 `meson setup` 命令，在专门的构建目录中生成构建配置文件。

4. **编译项目**：
   使用 `meson compile`（或 `ninja`）进行编译。

5. **运行测试**：
   执行 `meson test` 运行项目的单元测试。

6. **安装项目**（可选）：
   通过 `meson install` 安装项目的可执行文件或库文件。

## 可运行的 Demo 示例

以下是一个简单的 C 项目示例，该项目包含一个 `hello.c` 文件，并通过 Meson 构建系统
编译和运行。

### 文件结构：

```bash
my_project/
├── hello.c
└── meson.build
```

### `hello.c` 文件内容：

这是一个非常简单的 C 代码，它打印 "Hello, Meson!":

```c
#include <stdio.h>

int main() {
    printf("Hello, Meson!\n");
    return 0;
}
```

### `meson.build` 文件内容：

这是 Meson 的配置文件，定义了项目名称、语言和要编译的源文件。

```meson
project('my_project', 'c')

executable('hello', 'hello.c')
```

- `project('my_project', 'c')`：定义项目的名称为 `my_project`，使用的语言是 C。
- `executable('hello', 'hello.c')`：指定要编译的源文件 `hello.c`，生成的可执行
  文件名称为 `hello`。

### 编译和运行项目：

以下是如何使用 Meson 编译和运行该项目的步骤：

1. **创建构建目录并生成构建文件**：
   在项目目录中执行以下命令：
   ```bash
   meson setup builddir
   ```

   这将创建一个名为 `builddir` 的构建目录，并在其中生成 Ninja 构建文件。

2. **编译项目**：
   进入构建目录并编译项目：
   ```bash
   meson compile [-C builddir]
   ```

   这会调用 Ninja 来编译源文件并生成可执行文件 `hello`。如果在builddir目录之外，
   可以使用-C参数指定构建目录，如果在builddir之内，就可以直接执行`meson compile`

3. **运行可执行文件**：
   编译完成后，可以运行生成的可执行文件：
   ```bash
   ./builddir/hello
   ```

   输出结果应该是：
   ```
   Hello, Meson!
   ```

### 增加测试（可选）：

Meson 支持自动化测试。可以将测试添加到 `meson.build` 文件中，如下：
```meson
project('my_project', 'c')

executable('hello', 'hello.c')

test('basic', exe)
```

这里的 `test('basic', exe)` 定义了一个名为 `basic` 的测试，它运行 `hello` 可执行文件。

可以通过以下命令运行测试：
```bash
meson test -C builddir
```
