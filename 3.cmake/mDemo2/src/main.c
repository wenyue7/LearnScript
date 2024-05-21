/*************************************************************************
  > File Name: ../src/main.c
  > Author: LiHongjin
  > Mail: 872648180@qq.com 
  > Created Time: Sun 20 Sep 2020 04:45:44 PM CST
 ************************************************************************/

#include<stdio.h>
#include<stdlib.h>
#include"config.h"

#ifndef USE_MYMATH
  #include<math.h>
#else
  #include "mathFunctions.h"
#endif

int main(int argc, char* argv[])
{
    if (argc < 3){
        // print version info
        printf("%s Version %d.%d\n", argv[0], Demo_VERSION_MAJOR, Demo_VERSION_MINOR);
        printf("Usage: %s base exponent \n", argv[0]);
        return 1;
    }
    double base = atof(argv[1]);
    int exponent = atoi(argv[2]);

#ifndef USE_MYMATH
    printf("Now we use the standard library. \n");
    double result = power(base, exponent);
#else
    printf("Now we use our own Math library. \n");
    double result = power(base, exponent);
#endif

    printf("%g ^ %d is %g\n", base, exponent, result);
    return 0;
}
