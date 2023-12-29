#include "helpers.h"
#include <math.h>
#include <stdio.h>

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
    for(int i = 0; i < (width / 2); i++)
    {
        int firstRedPixel = image[0][i].rgbtRed;
        int lastRedPixel = image[0][width - i].rgbtRed;

        int *ptrFirstRedPixel = &firstRedPixel;
        int *ptrLastRedPixel = &lastRedPixel;

        int tempRed = 0;
        tempRed = *ptrFirstRedPixel;
        *ptrFirstRedPixel = *ptrLastRedPixel;
        *ptrLastRedPixel = tempRed;
    }

    for(int i = 0; i < (width / 2); i++)
    {
        int firstBluePixel = image[0][i].rgbtBlue;
        int lastBluePixel = image[0][width - i].rgbtBlue;

        int *ptrFirstBluePixel = &firstBluePixel;
        int *ptrLastBluePixel = &lastBluePixel;

        int tempBlue = 0;
        tempBlue = *ptrFirstBluePixel;
        *ptrFirstBluePixel = *ptrLastBluePixel;
        *ptrLastBluePixel = tempBlue;
    }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
