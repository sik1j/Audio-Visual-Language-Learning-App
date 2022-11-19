# Your header
# Jonathan Chan 301553184
# Sikij Karki 301

# your mother is a very nice woman

import cmpt120image
import random

# Jon
def recolorImage(img,color):
  # Add your code here

# Sikij
def minify(img):
  # Add your code here
  
def mirror(img):
  # Add your code here
  
def drawItem(canvas,item,row,col):
  # Add your code here
  
def distributeItems(canvas,item,n): 
  #loop to draw n items
  for i in range(n):
    row = random.randint(0, 300)
    col = random.randint(0, 400)
    drawItem(canvas, item, row, col)
  
