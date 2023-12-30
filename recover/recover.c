#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    if(argc != 2)
    {
        printf("Useage: ./recover filename.raw ");
        return 1;
    }
    char *filename = argv[1];
    FILE *file = fopen(argv[1], "r");

    if(file == NULL)
    {
        printf("File not found.");
        return 1;
    }

    BYTE buffer[4];

    uint8_t signature[] = {0xff, 0xd8, 0xff}

    while (fread(buffer, 1, 4, file) == 4)
    {
        if((buffer[0] != signature[0]) && (buffer[1] != signature[1]) && (buffer[2] != signature[2]) && (buffer[3] & 0xf0) == 0xe0)
        {
            printf("Doesn't appear to be a jpeg.");
        }


    }
    fclose(file);
}
