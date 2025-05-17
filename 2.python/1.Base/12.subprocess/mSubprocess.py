#!/usr/bin/env python
#########################################################################
# File Name: mSubprocess.py
# Author: LiHongjin
# mail: 872648180@qq.com
# Created Time: Sat 26 Oct 10:12:17 2024
#########################################################################

import subprocess

def run_command(command):
    """执行给定的 shell 命令并返回输出、错误和执行状态"""
    try:
        # 使用 subprocess.run() 执行命令
        result = subprocess.run(command, shell=True, check=True,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # 返回标准输出、标准错误和执行状态
        return result.stdout.strip(), result.stderr.strip(), result.returncode
    except subprocess.CalledProcessError as e:
        # 捕获并处理错误
        return e.stdout.strip(), e.stderr.strip(), e.returncode

def main():
    command = input("请输入要执行的 shell 命令: ")
    stdout, stderr, status = run_command(command)

    # 输出命令的结果和状态
    print("命令输出:\n", stdout)
    print("错误输出:\n", stderr)
    print("执行状态:", "成功" if status == 0 else f"失败 (状态码: {status})")

if __name__ == '__main__':
    main()
