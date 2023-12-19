#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n = 8;

    for(int i = 0; i < n; i++){
        printf("#");
        for(int k = 0; k <= i - n; k++){
            printf(" ");
        }
        for(int j = n; j < n; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}
