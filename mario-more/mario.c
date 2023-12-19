#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n = 8;

    for(int i = 1; i < 8; i++){
        //Print Spaces
        for(int k = 0; k <= 8 - i; k++)
        {
            printf(" ");
        }
        for(int j = -i; j <= 0; j++)
        {
            printf("#");
        }
        printf("\n");
    }

    for(int i = 1; i < 8; i++){
        //Print Spaces
        for(int j = -i; j <= 8 + 8 + i; j++)
        {
            printf("#");
        }
        for(int k = 0; k <= 8 - i; k++)
        {
            printf(" ");
        }
        printf("\n");
    }
}
