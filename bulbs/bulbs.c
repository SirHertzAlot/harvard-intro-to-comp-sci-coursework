#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

int convertToBinary(char *str);
void print_bulb(int bit);

int main(void)
{
    string input = get_string("Enter a word or phrase.");
    int result = convertToBinary(input);
    return 0;
}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}

int convertToBinary(char *str)
{
  int length = strlen(str);
  int result[8];


    for(int i = 0; i < length; i++)
    {
        int k = 0;
        int ltr = str[i];

        while(k <= 7)
        {
            int r = ltr % 2;
            ltr /= 2;
            result[k] = r;
            k++;
        }

        for(int j = 7; j >= 0; j--)
        {
            print_bulb(result[j]);
        }
        printf("\n");
    }
  return result[7];
}
