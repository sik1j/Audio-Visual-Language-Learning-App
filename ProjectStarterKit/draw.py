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
  #grabs size of the canvas
  row_length = canvas.getHeight()
  column_length = canvas.getWidth()
  
  #loop to draw n items
  for i in range(n):
    row = random.randint(0, row_length)
    col = random.randint(0, column_length)
    drawItem(canvas, item, row, col)
  
