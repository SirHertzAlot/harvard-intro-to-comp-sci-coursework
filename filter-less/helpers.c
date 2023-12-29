#include "helpers.h"
#include <math.h>

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
                    image[i][j].rgbtRed = sepiaRed ;
                } else {
                    image[i][j].rgbtGreen = sepiaRed;
                }

                if(round(sepiaGreen) > 255)
                {
                    sepiaGreen = 255;
                    image[i][j].rgbtBlue = sepiaGreen;
                } else {
                    image[i][j].rgbtGreen = sepiaGreen;
                }
                if(round(sepiaBlue) > 255)
                {
                    sepiaBlue = 255;
                    image[i][j].rgbtGreen = sepiaBlue;
                } else {
                    image[i][j].rgbtGreen = sepiaBlue;
                }
            }
        }
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}