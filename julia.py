from __future__ import division
from PIL import Image, ImageDraw
from random import random, randint
import sys, math

def generateFractal():

  # Create the image
  im = Image.new("RGB", (width, height))
  draw = ImageDraw.Draw(im)

  # Set control
  newR = 0.0
  newI = 0.0
  oldR = 0.0
  oldI = 0.0
  maxIterations = 255
  smoothDiv = maxIterations / 255

  # Draw
  for y in range(0, height):
    for x in range(0, width):

      newR = (width / height) * (x - width / 2.0) / (0.5 * zoom * width) + xOffset
      newI = (y - height / 2.0) / (0.5 * zoom * height) + yOffset
      smooth = math.exp(-math.sqrt(newR*newR + newI*newI))

      # Start iterating
      for i in range(0, maxIterations):

        # Get the values of the previous iteration
        oldR = newR
        oldI = newI
        
        # Calculate the new real and imaginary parts
        newR = (oldR * oldR) - (oldI * oldI) + cr
        newI = 2.0 * (oldR * oldI) + ci

        smooth += math.exp(-math.sqrt(newR*newR + newI*newI))

        # Exit condition
        if newR*newR + newI*newI > 4.0:

          r = int(smooth / smoothDiv * rColor * rBright)
          g = int(smooth / smoothDiv * gColor * gBright)
          b = int(smooth / smoothDiv * bColor * bBright)

          if invertColors:
            r = 255-r
            g = 255-g
            b = 255-b

          draw.point([(x, y)], fill=(r, g, b))
          break

        elif i == maxIterations - 1: # Last iteration, draw with the brightiest value of each channel

          r = int(255 * rColor * rBright)
          g = int(255 * gColor * gBright)
          b = int(255 * bColor * bBright)
          
          if invertColors:
            r = 255-r
            g = 255-g
            b = 255-b

          draw.point([(x, y)], fill=(r, g, b))

    # Print progress
    if y % 10 == 0:
      print str((y / height) * 100) + "%"

  # Save
  im.save("julia.png")

# Parameters
width = 1280
height = 720

zoom = 1.0
xOffset = 0.0
yOffset = 0.0

cr = 0.285
ci = 0.01

invertColors = False

rColor = random()
gColor = random()
bColor = random()
rBright = randint(3, 10) # Min 1
gBright = randint(3, 10) # Min 1
bBright = randint(3, 10) # Min 1

generateFractal()
