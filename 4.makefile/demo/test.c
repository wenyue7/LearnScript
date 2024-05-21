/*************************************************************************
    > File Name: test.c
    > Author: LiHongjin
    > Mail: 872648180@qq.com 
    > Created Time: Fri May  5 18:20:53 2023
 ************************************************************************/

#include <stdio.h>
#include "mfunc.h"

int main()
{
    printf("hello world!\n");

    printf("==> demo: %s\n", __FILE__);
    mfunc();
    mfunc2();

#ifdef MCRO_TEST
    printf("have define %s\n", "MCRO_TEST");
#endif
    printf("MCRO_TEST2 val:%s\n", MCRO_TEST2);

    return 0;
}
