#include <cs50.h>
#include <stdio.h>

int main(void)
{
  long cc;
  int count = 0;
  int sum = 0;
  long int cardId = cc / pow(10, count - 2);

  do
  {
    cc = get_long("Please enter card number: \n");
  }
  while(cc >= 13 && cc <= 16);

  //Performing Luhn checksum
  while(cc >= 100)
    {
      int digit = cc % 10;

      //Grab the first 2 digits and store them for later review.
      if(count < 2)
      {
        cardId[count] += digit;
      }

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
    if((cardId[0] == 3 && cardId[1] == 4) || ((cardId[0] == 3 && cardId[1] == 7) && count == 15))
    {
      printf("AMEX\n");
    }
    else if ((cardId[0] == 5 && cardId[1] == 1) ||
      (cardId[0] == 5 && cardId[1] == 2) ||
      (cardId[0] == 5 && cardId[1] == 3) ||
      (cardId[0] == 5 && cardId[1] == 4) ||
      ((cardId[0] == 5 && cardId[1] == 5) && count == 16))
    {
      printf("MASTERCARD\n");
    }
    else if ((cardId[0] == 4) && (count == 13 || count == 16))
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
