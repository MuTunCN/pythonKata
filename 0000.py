'''put number in the upper right'''
from PIL import Image, ImageFont, ImageDraw
def putUR(im):
    draw = ImageDraw.Draw(im)
    x, y = im.size
    iFont = ImageFont.truetype("C:/Windows/Fonts/Consolas/consolai.ttf", size=40)
    icolor = '#FF0000'
    draw.text((x -50, 0), '99', font=iFont, fill=icolor)
    im.show()

def main():
    im = Image.open('C:/Users/wtnTUN/Desktop/ac.jpeg')
    putUR(im)

if __name__ == '__main__':
    main()
    