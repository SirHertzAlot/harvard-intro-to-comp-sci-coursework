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

    int L = (float) letters / (float) words * 100.0;
    int S = (float) sentences / (float) words * 100.0;

    int index = (0.0588 * L) - (0.296 * S) - 15.8;

    printf("Grade %i\n", index);
}


int count_letters(string text)
{
    int count = 0;

    for(int i = 0; i < strlen(text); i++)
    {
        char character = text[i];

        if(isalpha(character))
        {
            count++;
        }
    }

    return count;
}

int count_words(string text)
{
    int alphas = 0;
    int spaces = 0;
    int words = 0;

    for(int i = 0; i < strlen(text); i++)
    {
        char character = text[i];

        if(isalpha(character))
        {
            alphas++;
        }

        if(isspace(character))
        {
            spaces++;
        }

        if(alphas >= 1 && spaces == 1)
        {
            words++;
        }
    }

    return words;
}

int count_sentences(string text)
{
    int count = 0;

    for(int i = 0; i < strlen(text); i++)
    {
        char character = text[i];

        if(ispunct(character))
        {
            count++;
        }
    }

    return count;
}
