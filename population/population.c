#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int startSize;
    do
    {
        startSize = get_startSize("What is our start size?");
        if(startSize < 9)
        {
            startSize = get_startSize("Please make sure your start size is bigger than 9.");
        }
    }
    while(startSize < 1);

    // TODO: Prompt for end size
    int endSize;
    do
    {
        endSize = get_startSize("What is our start size?");
        if(endSize < 9)
        {
            endSize = get_startSize("Please make sure your start size is bigger than 9.");
        }
    }
    while(endSize < 1);

    // TODO: Calculate number of years until we reach threshold
    int calculateYearsTillEndSize(void)
    {
        int born = startSize / 3;
        int died = startSize / 4;
        int lp = 0;

        int LlamasPerYear(void){
            return int lp = startSize + born + died;
            printf("Llamas Per Year =: %i", lp);
        }
        int years = 1;

        do
        {
            years(lp);
        }
        while()
    }

    // TODO: Print number of years
}
