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

int hash_count = 0;
int count = 0;
FILE *file;

// TODO: Choose number of buckets in hash table
const unsigned int N = 10400;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    int value = hash(word);
    char lower[LENGTH + 1];

    node *start = table[value];

    for(int i = 0; i < strlen(word); i++)
    {
        lcword[i] = tolower(word[i]);
    }

    while(start != NULL)
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

    for(int i = 0; i != strlen(word); i++)
    {
        const char lower = tolower(word[i]);

        if(isalpha(lower))
        {
            int c = lower + (strlen(word) * i * lower) + (strlen(word) % lower);

            if(c > 2000)
            {
                n = c % 1000;
            }
            n += c;
        }
        if(hash_count > 3)
        {
            return n = n % 100;
        }
        hash_count++;
    }
    // TODO: Improve this hash function
    return n;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    file = fopen(dictionary, "r");

    if(dictionary == NULL)
    {
        return false;
    } else {
        char w[LENGTH + 1];

        while(fscanf(file, "%s", w) != EOF)
        {
            //Allocate memory for node.
            node *n = malloc(sizeof(node));

            if(n == NULL)
            {
                return false;
            }

            strcpy(n->word, w);
            int value = hash(w);

            n->next = table[value];
            table[value] = n;
            count++;
        }
    }

    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    //Iterate over table with N being the stopping point.
    for(int i = 0; i < N; i++)
    {
        //Starting point of traversal
        node *n = table[i];

        while(n != NULL)
        {
            //Temporary node to make sure we don't orphan any nodes.
            node *n_t = n;

            //Next node
            n = n->next;

            //Free last node.
            free(n_t);
        }

        //Check and see if we are at the end of our node and freed all nodes.
        if(n == NULL && i == N - 1)
        {
            return true;
        }
    }

    return false;
}
