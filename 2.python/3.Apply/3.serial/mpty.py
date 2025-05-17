# 终端(terminal)、伪终端(seudo-Terminal)、tty、pty、、控制台(console)、shell的关系
# 参考博客：https://www.cnblogs.com/sparkdev/p/11460821.html

# TTY 是 Teletype 或 Teletypewriter 的缩写，原来是指电传打字机，后来这种设备逐渐键盘和显示器取代。不管是电传打字机还是键盘显示器，都是作为计算机的终端设备存在的，所以 TTY 也泛指计算机的终端(terminal)设备。
# 为了支持这些 TTY 设备，Linux 实现了一个叫做 TTY 的子系统。所以 TTY 既指终端，也指 Linux 的 TTY 子系统，当然 TTY 还有更丰富(混乱)的含义。
#
# -------- 早期的控制台和终端 --------
# 早期的终端(terminal) 是一台独立于计算机的机器(teletype 即, TTY)，它通过线缆与计算机相连 
# 早期的控制台就是一个直接控制设备的面板，上面有很多控制按钮。 在计算机里，把那套直接连接在电脑上的键盘和显示器就叫做控制台。
# 终端是通过串口连接到电脑上的，不是计算机自身的设备，而控制台是计算机本身就有的设备，一个计算机只有一个控制台。计算机启动的时候，所有的信息都会显示到控制台上，而不会显示到终端上。
# 这同样说明，控制台是计算机的基本设备，而终端是附加设备。计算机操作系统中，与终端不相关的信息，比如内核消息，后台服务消息，都可以显示到控制台上，但不会显示到终端上。
#
# 现在终端和控制台都由硬件概念，逐渐演化成了软件的概念。简单的说，能直接显示系统消息的那个终端称为控制台，其他的则称为终端(控制台也是一个终端)。或者我们在平时的使用中压根就不区分 Linux 中的终端与控制台。
# 
# ------ 从软件仿真终端到伪终端 ------
# 后来的终端慢慢演变成了键盘 + 显示器。如果我们要把内容输出到显示器，只要把这些内容写入到显示器对应的 TTY 设备就可以了，然后由 TTY 层负责匹配合适的驱动完成输出，这也是 Linux 控制台的工作原理。
# 现在的终端不再有 UART 或物理终端。相反，软件仿真出视频终端，并最终被渲染到 VGA 显示器。注意，这里出现了软件仿真终端，它们是运行在内核态的。显示器和 vSphere Client "Virtual Machine Console" 中的 tty1-tty6 都是软件仿真终端：
# /dev/tty1-/dev/tty6 是这些仿真终端在文件系统中的表示，程序通过对这些文件的读写实现对仿真终端的读写。
# 
# 为了便于将终端仿真移入用户空间，同时仍保持 TTY 子系统(TTY 子系统指 TTY 驱动和行规范)的完整，伪终端被发明了出来(pseudo terminal 或 pty)。伪终端在内核中分为两部分，分别是 master side 和 在 TTY 驱动中实现的 slave side。
# 当创建一个伪终端时，会在 /dev/pts 目录下创建一个设备文件，每打开一个终端，这个目录下都会多一个文件，关掉一个终端会少一个文件。
#
# ======== 总结 ========
# 终端(terminal)=tty     控制台的概念与终端含义非常相近，其实现在我们经常用它们表示相同的东西
# 伪终端(terminal)=pty   伪终端在内核中分为两部分，分别是 master side 和 在 TTY 驱动中实现的 slave side。
# shell                  tty是与计算机的输入输出相关的, Shell是与内核相关的
#
# 我们打开的终端桌面程序，比如 GNOME Terminal，其实是一种终端模拟软件。当终端模拟软件运行时，它通过打开 /dev/ptmx 文件创建了一个伪终端的 master 和 slave 对，并让 shell 运行在 slave 端。
# 当用户在终端模拟软件中按下键盘按键时，它产生字节流并写入 master 中，shell 进程便可从 slave 中读取输入；相反，shell 和它的子程序，将输出内容写入 slave 中，由终端模拟软件负责将字符打印到窗口中。
# 在系统层面讲，从高到低的关系： 伪终端的master --> 伪终端的slave --> shell --> kernel
# 参考博客：https://www.cnblogs.com/sparkdev/p/11605804.html
# 
# ======== 终端与伪终端的区别 =======
# 至此我们可以得出这样的结论：现在所说的终端已经不是硬件终端了，而是软件仿真终端(终端模拟软件)。
# 关于终端和伪终端，可以简单的理解如下：
#     真正的硬件终端基本上已经看不到了，现在所说的终端、伪终端都是软件仿真终端(即终端模拟软件)
#     一些连接了键盘和显示器的系统中，我们可以接触到运行在内核态的软件仿真终端(tty1-tty6)
#     通过 SSH 等方式建立的连接中使用的都是伪终端
#     伪终端是运行在用户态的软件仿真终端



#!/bin/python3
#coding:utf-8

# 程序说明：使用 pty 模拟两个伪端口，可以用于串口调试


# select.select(rlist, wlist, xlist[, timeout])
# 这是一个明白直观的 Unix select() 系统调用接口。 前三个参数是由‘可等待对象’组成的序列：可以是代表文件描述符的整数，或是带有名为 fileno() 的返回这样的整数的无形参方法的对象:
#     rlist：等待，直到可以开始读取
#     wlist：等待，直到可以开始写入
#     xlist：等待“异常情况”（请参阅当前系统的手册，以获取哪些情况称为异常情况）
# 
# 允许空的可迭代对象，但是否接受三个空的可迭代对象则取决于具体平台。（已知在 Unix 上可行但在 Windows 上不可行。） 可选的 timeout 参数以一个浮点数表示超时秒数。 
# 当省略 timeout 参数时该函数将阻塞直到至少有一个文件描述符准备就绪。 超时值为零表示执行轮询且永不阻塞。
# 
# 返回值是三个列表，包含已就绪对象，返回的三个列表是前三个参数的子集。当超时时间已到且没有文件描述符就绪时，返回三个空列表。
 
import pty
import os
import select
import threading
import time

slaveName1 = '--slave1 name null'
slaveName2 = '--slave2 name null'
 
def mkpty():
    global slaveName1,slaveName2

    #make pair of pseudo tty
    master1, slave1 = pty.openpty()
    master2, slave2 = pty.openpty()
    print('pyt1 masterName: ', os.ttyname(master1)," slaveName:", os.ttyname(slave1))
    print('pyt2 masterName: ', os.ttyname(master2)," slaveName:", os.ttyname(slave2))
    slaveName1 = os.ttyname(slave1)
    slaveName2 = os.ttyname(slave2)
    return master1, master2

def createInteraction():
    master1, master2 = mkpty()
    while True:
        rl, wl, el = select.select([master1, master2], [], [], 1)
        for master in rl:
            data = os.read(master, 128)
            # print("read %d data." %len(data))
            if master == master1:
                os.write(master2, data)
            else:
                os.write(master1, data)

def createInteractionWithThread():
    print("\n========= create pty thread =========\n")
    mThread = threading.Thread(target = createInteraction)
    print("\n========= start pty thread =========\n")
    mThread.start()


def test():
    print("\n========= create pty thread =========\n")
    mThread = threading.Thread(target = createInteraction)
    print("\n========= start pty thread =========\n")
    mThread.start()

    # time.sleep(1)
    print()
    print("slaveName1: " + slaveName1)
    print("slaveName2: " + slaveName2)

    print("\n========= main thread running =========\n")

if __name__ == "__main__":
    test()
