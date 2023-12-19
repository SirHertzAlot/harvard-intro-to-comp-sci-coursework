#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n = 8;

    for(int i = 0; i < 8; i++){
        for(int k = 0; k <= 8 - i; k++)
        {
            printf(" ");
        }
        for(int j = -i; j < 8; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}
