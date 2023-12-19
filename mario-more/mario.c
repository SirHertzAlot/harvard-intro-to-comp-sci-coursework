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

    for(int n = 8; n > 0; n--){
        printf("#");
        for(int j = 0; j > 8; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}
