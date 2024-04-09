#!/opt/local/bin/bash
#########################################################################
# File Name: cmd_paras.sh
# Author: LiHongjin
# mail: 872648180@qq.com
# Created Time: Tue Apr  9 09:43:18 2024
#########################################################################

# init para
name=""
age=0

function procParas()
{
    # 双中括号提供了针对字符串比较的高级特性，使用双中括号 [[ ]] 进行字符串比较时，
    # 可以把右边的项看做一个模式，故而可以在 [[ ]] 中使用正则表达式：
    # if [[ hello == hell* ]]; then
    #
    # 位置参数可以用shift命令左移。比如shift 3表示原来的$4现在变成$1，原来的$5现在变成
    # $2等等，原来的$1、$2、$3丢弃，$0不移动。不带参数的shift命令相当于shift 1。


    # proc cmd paras
    while [[ $# -gt 0 ]]; do
        key="$1"
        case ${key} in
            -n|--name)
                name="$2"
                shift # move to next para
                ;;
            -a|--age)
                age="$2"
                shift # move to next para
                ;;
            *)
                # unknow para
                echo "unknow para: ${key}"
                exit 1
                ;;
        esac
        shift # move to next para
    done
}

function procParas2()
{
    for para in $@
    do
        case ${para} in
            name)
                name="mySetName"
                ;;
            age)
                age="1024"
                ;;
            *)
                # unknow para
                echo "unknow para: ${para}"
                exit 1
                ;;
        esac
    done
}

function usage()
{
    echo "usage: $0 [-n|--name <name>] [-a|--age <age>]"
}



procParas $@
# procParas2 $@

# check para
if [ -z "$name" ] || [ "$age" -eq 0 ]; then
    usage
    exit 1
fi

# print result
echo "name : $name"
echo " age : $age"
