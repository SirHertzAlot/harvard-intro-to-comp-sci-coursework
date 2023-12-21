#include <cs50.h>
#include <stdio.h>

int main(void)
{
  long cc = 0;
  int count = 0;
  int sum = 0;
  //Duplicate CC# to use to determine first 2 digits in #.
  long dupe_cc = cc;
  //Store first 2 digits for later review.
  int cardId = 0;

  do
    {
      cc = get_long("Please enter card number: \n");
    }
    while(cc >= 13 && cc <= 16);

  //Grab the first 2 digits of a long number.
  while(dupe_cc >= 100)
    {
       cardId = dupe_cc /= 10;
    }

  //Performing Luhn checksum
  while(cc > 0)
    {
      int digit = cc % 10;
      cc /= 10;
      count++;

      //Take every even digit and multiply it by 2. Then if it's greater than nine, subtract nine to get its digit sum. If it's odd, just add it to the running sum already presented.
      if(count % 2 == 0)
      {
        digit *= 2;
        if(digit > 9)
        {
          digit -= 9;
        }
      }
      sum += digit;
    }

  //If sum returns a number divisible by 10, then the card is valid. Afterwards we check the card Id for a match. No match, the card is invalid.
  if(sum % 10 == 0)
  {
    if(cardId == 34 || cardId == 37)
    {
      printf("AMEX\n");
    }
    else if (cardId == 51 ||
      cardId == 52 ||
      cardId == 53 ||
      cardId == 54 ||
      cardId == 55)
    {
      printf("MASTERCARD\n");
    }
    else if (cardId == 4)
      {
      printf("VISA\n");
      }
    else
    {
      printf("INVALID\n");
    }
  }
  else
  {
    printf("INVALID\n");
  }

  //All done!
  return 0;
}
