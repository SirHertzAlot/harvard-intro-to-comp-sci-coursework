#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n;

    do
    {
        n = get_int("Height: ?");

    }while( n <= 1 || n > 9);

    for(int i = 0; i < n; i++){
        //Print Spaces
        for(int k = 0; k <= n - i; k++)
        {
            printf(" ");
        }
        for(int j = -i; j <= 0; j++)
        {
            printf("#");
        }
        printf("  ");

        for(int j = -i; j <= 0; j++)
        {
            printf("#");
        }
        for(int k = 0; k <= n - i; k++)
        {
            printf(" ");
        }
        printf("\n");
    }
}
