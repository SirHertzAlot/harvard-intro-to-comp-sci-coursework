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
    int lp = (startSize + born) - died;
    int lpy = 0;

    int years = 0;
    int result = 0;

    do
    {
        years++;
        lpy += lp;
    }
    while(lpy < endSize);


    printf("Start size: %i, \n", startSize);
    printf("Llamas Per Year: %i, \n", lpy);
    printf("End size: %i, \n", endSize);
    printf("Years: %i, \n", years);

}
