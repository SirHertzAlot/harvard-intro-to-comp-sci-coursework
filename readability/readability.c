#include <cs50.h>
#include <ctype.h>
#include <stdio.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);



int main(void)
{
    int letters = count_letters(string text);
    int words =  count_words(string text);
    int sentences = count_sentences(string text);

    int l = letters / words * 100.0;
    int s = sentences / words * 100.0;

    int index = (0.0588 * L) - (0.296 * S) - 15.8;
}


int count_letters(string text)
{
    return 0;
}

int count_words(string text)
{
    return 0;
}

int count_sentences(string text)
{
    return 0;
}
