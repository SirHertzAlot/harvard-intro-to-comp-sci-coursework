// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

int count;
FILE *file;

// TODO: Choose number of buckets in hash table
const unsigned int N = 10400;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    int value = hash(word);

    node *start = table[value];
    while(start->next != NULL)
    {
        if(strcasecmp(word, start->word) == 0)
        {
            return true;
        }
        start = start->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    int n = 0;
    int base = toupper(word[0]) - 'A';

    for(int i = 0; i < strlen(word); i++)
    {
        const char lower = tolower(word[i]);

        if(isalpha(lower))
        {
            int c = lower + (strlen(word) * i * lower) + (strlen(word) % lower);

            if(c > 2000)
            {
                n = c % 1000;
            }
            else
            {
                n = base + c;
            }
        }
    }
    // TODO: Improve this hash function
    return n;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    file = fopen(dictionary, "r");
    char *word = NULL;

    if(file == NULL)
    {
        return false;
    }

    while(fscanf(file, "%s", word) != EOF)
    {
        //Allocate memory for node.
        node *n = malloc(sizeof(node));

        if(n == NULL)
        {
            return false;
        }

        strcpy(n->word, word);
        //Set Next to null if there is no next.
        n->next = NULL;

        n->next = table[count];
        table[count] = n;

        count++;
    }

    return false;

    fclose(file);
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    if(file != NULL)
    {
        fclose(file);
        return true;
    }
    return false;
}
