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
    while(startSize < 10);

    // TODO: Prompt for end size
    int endSize = 0;

    do
    {
        endSize = get_int("Please make sure your end size is bigger than your start size. \n");
    }
    while(endSize < startSize);

    // TODO: Calculate number of years until we reach threshold
    int born = startSize / 3;
    int died = startSize / 4;

    int years = 0;
    int result = startSize;

    for(int originalSize = startSize; result < endSize; years++)
    {
        result += born - died;
        originalSize = result;
        printf("Loop has completed: %i\n", result);
    }

    printf("Start size: %i \n", startSize);
    printf("End size: %i \n", endSize);
    printf("Years: %i \n", years);

}
