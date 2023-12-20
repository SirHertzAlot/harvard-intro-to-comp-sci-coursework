#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <cs50.h>

int main(void)
{
  long cc;
  cc = get_long("Please enter card number");

  //Convert number into string, so we can then grab each individual character's ASCII value.
  char ccn[20];

  //Convert each character in string to ASCII value of each digit, then insert into CCN character array.
  sprintf(ccn, "%li", cc);

  int result;

  int length = strlen(ccn);

  //Loop through the digits of the credit card number, printing each digit.
  for(int i = strlen(ccn) - 1; i >= 0; i--)
    {
      //The sum of all the even indexes.
      int evenSum = 0;
      //The sum of all the odd indexes.
      int oddSum = 0;
      //The sum of all the even products.
      int evenProduct = 0;
      //Convert from ASCII value to actual number value.
      int num = ccn[i] - '0';

      //Check which indexes are even.
      if(i % 2 == 0){
        int count = 0;
        char productDigits[10];
        int evenProductToCheck = 0;
        int copyOfProductToCheck = 0;

        evenProductToCheck += (num * 2);
        copyOfProductToCheck = evenProductToCheck;

        //Check digits place while preserving value.
        do {
          evenProduct += evenProductToCheck;
          evenProductToCheck /= 10;
          ++count;
        } while (evenProductToCheck != 0);

        if(count > 1)
        {
          evenProduct -= copyOfProductToCheck;
          sprintf(productDigits, "%02d", evenProduct);
          for(int j = 0; j < strlen(productDigits); j++){
            int num2 = productDigits[j] - '0';
            evenProduct += num2;
          }
        }
      } else {
        int oddNum = ccn[i] - '0';
        oddSum += oddNum;
      }

        //Then take digits of each product and add them together.
        evenSum += evenProduct;

        if(result == 0)
        {
          result = oddSum + evenSum;
        } else {
          result += oddSum;
          result += evenSum;
        }
      }

  //Check if the card number is valid.
      if(result == 20 && strlen(ccn) - length == 5)
      {
        if(ccn[0] == '3' && ccn[1] == '4')
        {
          printf("AMEX\n");
        } else if( ccn[0] == '3' && ccn[1] == '7') {
          printf("AMEX\n");
        }
      }
      else if(result == 20 && strlen(ccn) - length == 4)
      {
        if(ccn[0] == '5' && ccn[1] == '1')
        {
          printf("MASTERCARD\n");
        } else if(ccn[0] == '5' &&  ccn[1] == '2')
        {
            printf("MASTERCARD\n");
        } else if(ccn[0] == '5' &&  ccn[1] == '3')
        {
            printf("MASTERCARD\n");
        } else if(ccn[0] == '5' &&  ccn[1] == '4')
        {
            printf("MASTERCARD\n");
        } else if(ccn[0] == '5' &&  ccn[1] == '5')
        {
            printf("MASTERCARD\n");
        }
      }
      else if((result == 20 && strlen(ccn) - length == 7) || (strlen(ccn) - length == 4  && ccn[0] == '4'))
      {
        printf("VISA\n");
      }
      else
      {
        printf("INVALID\n");
      }
    }
