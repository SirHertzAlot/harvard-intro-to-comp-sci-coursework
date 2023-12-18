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

    // TODO: Print number of years
}
