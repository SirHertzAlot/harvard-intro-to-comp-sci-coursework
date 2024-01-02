#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
  BYTE buffer[512];
  int n = 0;
  char filename[327];
  FILE *img;
  BYTE found = 0;

  if(argc != 2)
  {
    printf("Usage: ./recover filename \n");
    return 1;
  }

  FILE *file = fopen(argv[1], "r");
  if(file)
  {
    while (fread(buffer, 1, 512, file) == 512)
      {
        if(buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
          if(found == 1)
          {
            fclose(img);
          }
          else
          {
            found = 1;
          }
           sprintf(filename,"%03i.jpg",n);
          img = fopen(filename, "wb");
          n++;
        }
        if(found == 1)
        {
          fwrite(&buffer, 512, 1, img);
          printf("recovery successful. recovered %i items.\n", n);
        }
    }
    fclose(img);
    fclose(file);
  }
  else
  {
    printf("Error: file not found.\n");
    return 1;
  }
}
