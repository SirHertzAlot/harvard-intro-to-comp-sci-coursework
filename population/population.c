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
    while(endSize <= startSize);

    // TODO: Calculate number of years until we reach threshold
    int born = startSize / 3;
    int died = startSize / 4;
    int llamasPerYear = startSize + born - died;
    int totalLlamas = 0;

    int start = startSize;
    int years = 0;

    for(int originalSize = startSize; result < endSize; years++)
    {
        result += startSize / 3 + startSize / 4;
        originalSize = result;
    }

    printf("Start size: %i \n", startSize);
    printf("End size: %i \n", endSize);
    printf("Years: %i \n", years);

}
