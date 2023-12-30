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
                int avg = (image[i][j].rgbtRed + image[i][j].rgbtBlue + image[i][j].rgbtGreen) / 3;
                image[i][j].rgbtRed = avg;
                image[i][j].rgbtBlue = avg;
                image[i][j].rgbtGreen = avg;
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
                int sepiaRed = .393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue;
                int sepiaGreen = .349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue;
                int sepiaBlue = .272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue;

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

    memcpy (img_cpy, image, sizeof(img_cpy));

    for(int i = 0; i < height; i++)
    {
        int avg = 0;

        int count = 0;

        int sumRed = 0;
        int sumBlue = 0;
        int sumGreen = 0;

        for(int j = 0; j < width; j++)
        {
            if(i == 0 && j == 0)
            {
                    sumRed += img_cpy[i][j].rgbtRed + img_cpy[i + 1][j + 1].rgbtRed;
                    sumBlue += img_cpy[i][j].rgbtBlue + img_cpy[i + 1][j + 1].rgbtBlue;
                    sumGreen += img_cpy[i][j].rgbtGreen + img_cpy[i + 1][j + 1].rgbtGreen;
                    count++;
            }
            else if(i == height && j == width - 1)
            {
                    sumRed += img_cpy[i][j].rgbtRed + img_cpy[i - 1][j - 1].rgbtRed;
                    sumBlue += img_cpy[i][j].rgbtBlue + img_cpy[i - 1][j - 1].rgbtBlue;
                    sumGreen += img_cpy[i][j].rgbtGreen + img_cpy[i - 1][j - 1].rgbtGreen;
                    count++;
            }
            else
            {
                    sumRed += img_cpy[i][j].rgbtRed + img_cpy[i + 1][j + 1].rgbtRed + img_cpy[i - height - 1][j - width - 1].rgbtRed;
                    sumBlue += img_cpy[i][j].rgbtBlue + img_cpy[i + 1][j + 1].rgbtBlue + img_cpy[i - height - 1][j - width - 1].rgbtBlue;
                    sumGreen += img_cpy[i][j].rgbtGreen + img_cpy[i + 1][j + 1].rgbtGreen + img_cpy[i - height - 1][j - width - 1].rgbtGreen;
                    count++;
            }
            avg += (sumRed / count) + (sumBlue / count) + (sumGreen / count);
        }
    }


}
