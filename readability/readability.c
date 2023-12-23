#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    string text = get_string("Please enter your string of text: \n");

    int letters = count_letters(text);
    int words =  count_words(text);
    int sentences = count_sentences(text);

    float L = (float) letters / (float) words * 100;
    float S = (float)sentences / (float)words * 100;

    int index = round(0.0588 * L - 0.296 * S - 15.8);

    if(index < 1)
    {
        printf("Before Grade 1 \n");
    }else if(index > 16)
    {
        printf("Grade 16+\n");
    } else
    {
        printf("Grade %i\n", index);
    }
}


int count_letters(char* text)
{
    int count = 0;

    for(int i = 0; i < strlen(text) + 1; i++)
    {
        char character = text[i];

        if((character >= 'a' && character <= 'z') || (character >= 'A' && character <= 'Z'))
        {
            count++;
        }
    }

    return count;
}

int count_words(char* text)
{
  int spaces = 0;
  int words = 0;

  for(int i = 0; i < strlen(text) + 1; i++)
  {
      char character = text[i];

      if(character == ' ' || character == '\0')
      {
          spaces++;
      }
  }
    words = spaces + 1;
    return words;
}

int count_sentences(char* text)
{
    int count = 0;

    for(int i = 0; i < strlen(text) + 1; i++)
    {
        char character = text[i];

        if(character == '!' || character == '?' || character == '.')
        {
            count++;
        }
    }

    return count;
}
