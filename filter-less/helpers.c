#include "helpers.h"
#include <math.h>
#include <stdio.h>
#include <string.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for(int i = 0; i < height; i++)
    {
        for(int j= 0; j < width; j++)
        {
            if(image)
            {
                int avg = image[i][j].rgbtRed + image[i][j].rgbtBlue + image[i][j].rgbtGreen / 3;
                image[i][j].rgbtRed = round(avg);
                image[i][j].rgbtBlue = round(avg);
                image[i][j].rgbtGreen = round(avg);
            }
        }
    }
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for(int i = 0; i < height; i++)
    {
        for(int j= 0; j < width; j++)
        {
            if(image)
            {
                int sepiaRed = round(.393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue);
                int sepiaGreen = round(.349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue);
                int sepiaBlue = round(.272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue);

                if(round(sepiaRed) > 255)
                {
                    sepiaRed = 255;
                    image[i][j].rgbtRed = sepiaRed;
                } else {
                    image[i][j].rgbtRed = sepiaRed;
                }

                if(round(sepiaGreen) > 255)
                {
                    sepiaGreen = 255;
                    image[i][j].rgbtGreen = sepiaGreen;
                } else {
                    image[i][j].rgbtGreen = sepiaGreen;
                }
                if(round(sepiaBlue) > 255)
                {
                    sepiaBlue = 255;
                    image[i][j].rgbtBlue = sepiaBlue;
                } else {
                    image[i][j].rgbtBlue = sepiaBlue;
                }
            }
        }
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for(int i = 0; i < height; i++)
    {
        for(int j = 0; j < width / 2; j++)
        {
            RGBTRIPLE tempData;

            tempData = image[i][j];
            image[i][j] = image[i][width - j - 1];
            image[i][width - j - 1] = tempData;
        }
    }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE img_cpy[height][width];

    memcpy(img_cpy, image, sizeof(image[height][width]));

    for(int i = 0; i < height; i++)
    {
        int full_count = 9;
        int sumRed = 0;
        int sumBlue = 0;
        int sumGreen = 0;

        for(int j = 0; j < width; j++)
        {
            if(i == 0)
            {
                while(i < height)
                {
                    sumRed += round(img_cpy[i][j].rgbtRed + img_cpy[i][j + 1].rgbtRed + img_cpy[i + 1][j].rgbtRed + img_cpy[i + 1][j + 1].rgbtRed)  / 4;
                    sumBlue += round(img_cpy[i][j].rgbtBlue + img_cpy[i][j + 1].rgbtBlue + img_cpy[i + 1][j].rgbtBlue + img_cpy[i + 1][j + 1].rgbtBlue) / 4;
                    sumGreen += round(img_cpy[i][j].rgbtGreen + img_cpy[i][j + 1].rgbtGreen + img_cpy[i + 1][j + 1].rgbtGreen + img_cpy[i + 1][j + 1].rgbtGreen) / 4;
                    i++;
                }

            }
            // else if((i == height) && (j == width - 1))
            // {
            //          sumRed += round(img_cpy[i][j].rgbtRed + img_cpy[i][j - 1].rgbtRed + img_cpy[i - 1][j].rgbtRed + img_cpy[i - 1][j - 1].rgbtRed)  / 4;
            //          sumBlue += round(img_cpy[i][j].rgbtBlue + img_cpy[i][j - 1].rgbtBlue + img_cpy[i - 1][j].rgbtBlue + img_cpy[i - 1][j - 1].rgbtBlue) / 4;
            //          sumGreen += round(img_cpy[i][j].rgbtGreen + img_cpy[i][j - 1].rgbtGreen + img_cpy[i - 1][j - 1].rgbtGreen + img_cpy[i - 1][j - 1].rgbtGreen) / 4;
            // }
            // else if((i > 0 && i < height) && (j > 0 && j < width))
            // {
            //         sumRed += round(img_cpy[i][j].rgbtRed + img_cpy[i + 1][j + 1].rgbtRed + img_cpy[i - height - 1][j - width - 1].rgbtRed) / 3;
            //         sumBlue += round(img_cpy[i][j].rgbtBlue + img_cpy[i + 1][j + 1].rgbtBlue + img_cpy[i - height - 1][j - width - 1].rgbtBlue) / 3;
            //         sumGreen += round(img_cpy[i][j].rgbtGreen + img_cpy[i + 1][j + 1].rgbtGreen + img_cpy[i - height - 1][j - width - 1].rgbtGreen) / 3;
            // }

            image[i][j].rgbtRed = sumRed;
            image[i][j].rgbtBlue = sumBlue;
            image[i][j].rgbtGreen = sumGreen;
        }
    }

}
