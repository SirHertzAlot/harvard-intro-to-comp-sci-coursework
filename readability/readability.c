#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    string text = get_string("Please enter your string of text: \n");

    int letters = count_letters(text);
    int words =  count_words(text);
    int sentences = count_sentences(text);

    int L = letters / words * 100.0;
    int S = sentences / words * 100.0;

    int index = 0.0588 * L - 0.296 * S - 15.8;

    printf("Grade %i\n", index);
}


int count_letters(char* text)
{
    int count = 0;

    for(int i = 0; i < strlen(text); i++)
    {
        char character = text[i];

        if(isalpha(character) > 1)
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

  for(int i = 0; i < strlen(text); i++)
  {
      char character = text[i];

      if(isspace(character) != 0)
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

    for(int i = 0; i < strlen(text); i++)
    {
        char character = text[i];

        if(ispunct(character) > 1)
        {
            count++;
        }
    }

    return count;
}
