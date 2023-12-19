#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int startSize = 9;

    do
    {
        startSize = get_int("Please make sure your start size is bigger than 9. \n");
    }
    while(startSize <= 8);

    // TODO: Prompt for end size
    int endSize = 0;

    do
    {
        endSize = get_int("Please make sure your end size is bigger than your start size. \n");
    }
    while(endSize < startSize);

    // TODO: Calculate number of years until we reach threshold
    int population = startSize;
    int years = 0;

    for(int originalSize = startSize; population < endSize; years++)
    {
        population += originalSize / 3 - originalSize / 4;
        originalSize = population;
        printf("Loop has completed: %i\n", population);
    }

    printf("Start size: %i \n", startSize);
    printf("End size: %i \n", endSize);
    printf("Years: %i \n", years);

}
