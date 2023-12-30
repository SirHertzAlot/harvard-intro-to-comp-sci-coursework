#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    FILE *file = fopen(argv[1], "r");

    typedef uint8_t BYTE;

    BYTE buffer[512];

    while (fread(buffer, 512, BLOCK_SIZE, file) == BLOCK_SIZE)
    {

    }


    fclose(file);
}
