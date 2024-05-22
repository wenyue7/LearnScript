/*************************************************************************
    > File Name: prn.c
    > Author: LiHongjin
    > Mail: 872648180@qq.com
    > Created Time: Tue 21 May 2024 05:57:59 PM CST
 ************************************************************************/

#include <stdio.h>

int mprintf(int num)
{
    printf("======> func:%s line:%d num:%d\n", __func__, __LINE__, num);

    return 0;
}
