#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    FILE *file = fopen(argv[1], "r");

    typedef uint8_t BYTE;

    

    fclose(file);
}
