#include <stdio.h>

int main() {
    
    int a,b,c,d,e,f;
    int x,y;

    scanf("%d %d %d %d %d %d", &a, &b, &c, &d, &e, &f);
    
    for (x = -999; x < 1000; x++) {
        for (y = -999; y < 1000; y++) {
            if (((a*x) + (b*y) == c) && ((d*x) + (e*y) == f))
                printf("%d %d\n", x,y);
        }
    }

    return 0;
}

