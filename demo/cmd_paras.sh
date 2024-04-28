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

function procParas3()
{
    # 单个字符选项：如果选项不需要参数，可以直接使用一个字符表示。
    # 带参数选项：如果选项需要一个参数，应在选项字符后接一个冒号“:”。选项参数可以
    #             紧跟在选项之后，也可以以空格隔开。选项参数的首地址会赋给optarg变量。
    # 可选参数选项：如果选项的参数是可选的，应在选项字符后接两个冒号“::”。当提供
    #              了参数时，它必须紧跟在选项之后，不能以空格隔开，否则getopt会
    #              认为该选项没有参数，并将optarg赋值为NULL。
    # 实测发现，如果带有冒号，即带参，两种写法都可以 -n10 -n 10)
    # 但是如果不带冒号，则不能跟参数
    while getopts "tn:a::" opt
    do
        # OPTIND 的主要用途是跟踪下一个要处理的参数的位置。当使用 getopts 解析参数时，
        # 它会按照顺序检查位置参数，并使用 OPTIND 来记住下一个要检查的参数的位置。
        echo "==> OPTIND:$OPTIND opt:${opt} para:${OPTARG}"
        case "${opt}" in
            n)
                name=${OPTARG}
                ;;
            a)
                age=${OPTARG}
                ;;
            t)
                echo "test"
                ;;
            *)
                echo "error"
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
# procParas3 $@

# check para
if [ -z "$name" ] || [ "$age" -eq 0 ]; then
    usage
    exit 1
fi

# print result
echo "name : $name"
echo " age : $age"
