#include <stdio.h>
#include <stdlib.h>

typedef unsigned char BYTE;

int main(int argc, char *argv[])
{
    FILE *file = fopen(argv[1], "r");

    BYTE buffer[512];

    while (fread(buffer, 512, BLOCK_SIZE, file) == BLOCK_SIZE)
    {
        if(buffer[0] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {

        } else {

        }
    }
    fclose(file);
}
