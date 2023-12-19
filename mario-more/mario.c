#include <cs50.h>
#include <stdio.h>

int main(void)
{
    for(int n = 0; n < 8; n++){
        printf("#");
        for(int j = n; j < 8; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}
