#include <cs50.h>
#include <stdio.h>

int get_cents(void);
int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);
int calculate_pennies(int cents);

int main(void)
{
    // Ask how many cents the customer is owed
    int cents = get_cents();

    // Calculate the number of quarters to give the customer
    int quarters = calculate_quarters(cents);
    cents = cents - quarters * 25;

    // Calculate the number of dimes to give the customer
    int dimes = calculate_dimes(cents);
    cents = cents - dimes * 10;

    // Calculate the number of nickels to give the customer
    int nickels = calculate_nickels(cents);
    cents = cents - nickels * 5;

    // Calculate the number of pennies to give the customer
    int pennies = calculate_pennies(cents);
    cents = cents - pennies * 1;

    // Sum coins
    int coins = quarters + dimes + nickels + pennies;

    // Print total number of coins to give the customer
    printf("%i\n", coins);
}

int get_cents(void)
{
    int n = get_int("Please enter cents amount: \n");

    do{
        if(n <= 0)
        {
            printf("Please use positive values");
        }
    }
    while(n < 0);

    return n;
}

int calculate_quarters(int cents)
{
    int quarterCount = 0;
    if(cents > 24)
    {
        while(cents > 0)
        {
            cents -= 25;
            quarterCount++;
        }
    } else {
        while(cents > 0)
        {
            cents -= 25;
            quarterCount++;
        }
    }
    return quarterCount;
}

int calculate_dimes(int cents)
{
    int dimeCount = 0;
    if(cents > 9 && cents < 25)
    {
        while(cents > 0)
        {
            cents -= 10;
            dimeCount++;
        }
    } else {
        while(cents > 0)
        {
            cents -= 10;
            dimeCount++;
        }
    }
    return dimeCount;
}

int calculate_nickels(int cents)
{
    int nickleCount = 0;
    if(cents > 4 && cents < 10)
    {
        while(cents > 0)
        {
            cents -= 5;
            nickleCount++;
        }
    } else {
        while(cents > 0)
        {
            cents -= 5;
            nickleCount++;
        }
    }
    return nickleCount;
}

int calculate_pennies(int cents)
{
    int pennyCount = 0;
    if(cents > 0 && cents < 5)
    {
        while(cents > 0)
        {
            cents -= 1;
            pennyCount++;
        }
    } else {
        while(cents > 0)
        {
            cents -= 1;
            pennyCount++;
        }
    }

    return pennyCount;
}
