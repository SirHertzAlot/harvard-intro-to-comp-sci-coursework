#include <stdio.h>
#include <stdlib.h>

typedef unsigned char BYTE;

int main(int argc, char *argv[])
{
    if(argc != 2)
    {
        printf("Useage: ./recover filename.raw ");
        return 1;
    }
    char *filename = argv[1];
    FILE *file = fopen(argv[1], "r");

    BYTE buffer[512];

    while (fread(buffer, 512, BLOCK_SIZE, file) == BLOCK_SIZE)
    {
        if((buffer[0] == 0xff) && (buffer[1] == 0xd8) && (buffer[2] == 0xff) && (buffer[3] & 0xf0) == 0xe0)
        {
            while(sprintf(filename, "%03i.jpg", 2) == -1);
            FILE *img = fopen()
        } else {

        }
    }
    fclose(file);
}
