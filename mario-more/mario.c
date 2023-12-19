#include <cs50.h>
#include <stdio.h>

int main(void)
{
    for(int n = 1; n < 8; n++){
        printf("#\n");
        for(int j = n; j < 8; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}
