#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int startSize = 0;
    do
    {
        startSize = get_int("Please make sure your start size is bigger than 9. \n");
    }
    while(startSize == 0);

    // TODO: Prompt for end size
    int endSize = 0;
    do
    {
        endSize = get_int("Please make sure your end size is bigger than your start size. \n");
    }
    while(endSize == 0);

    // TODO: Calculate number of years until we reach threshold
    int born = startSize / 3;
    int died = startSize / 4;
    int lp = 0;


    lp = startSize + born - died;
    printf("Llamas Per Year =: %i", lp);


    int years = 0;

    do
    {
        int result = years * lp;
        printf("%i \n", result);
        return years++;
    }
    while(startSize < endSize);

    // TODO: Print number of years
    printf("It took %i, years. \n", years);
}
