#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int startSize = 0;
    do
    {
        if(startSize < 9)
        {
            startSize = get_int("Please make sure your start size is bigger than 9.");
        }
    }
    while(startSize < 1);

    // TODO: Prompt for end size
    int endSize;
    do
    {
        if(endSize < startSize)
        {
            endSize = get_int("Please make sure your start size is bigger than 9.");
        }
    }
    while(endSize < 1);

    // TODO: Calculate number of years until we reach threshold
    int born = startSize / 3;
    int died = startSize / 4;
    int lp = 0;


    lp = startSize + born + died;
    printf("Llamas Per Year =: %i", lp);


    int years = 1;

    do
    {
        int result = years * lp;
        printf("%i", result);
    }
    while(startSize < endSize);

    // TODO: Print number of years
}
