#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n = 8;

    for(int i = 0; i < 8; i++){
        //Print blocks
        for(int l = -i;l <= -8; l--)
        {
            printf("#");
        }

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

        for(int m = 0; m < 8; m++)
        {
            for(int k = 0; k <= -8; k++)
            {
                printf(" ");
            }
            for(int l = -m; l <= 0; l++)
            {
                printf("#");
            }
            for(int k = 0; k <= 8 - m; k++)
            {
                printf(" ");
            }
            printf("\n");
        }
}
