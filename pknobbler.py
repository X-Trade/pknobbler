from PIL import Image, ImageDraw, ImageColor
from argparse import ArgumentParser


width = 55
height = 55
frames = 16
border = 2
size = (width, height*frames)

background = (0,0,0,0)
foreground = (255,0,0,255)

startangle = (0 - 90) - 150
endangle = (0 - 90) + 150
anglerange = endangle - startangle
anglestep = anglerange / frames

filmstrip = Image.new('RGBA', size, color=background)
canvas = ImageDraw.Draw(filmstrip)

for framenum in range(frames):
    frametop = (framenum) * height
    framebot = ((framenum+1) * height - 1)
    bounds = [(border, frametop+border), (width-border, framebot-border)]
    endangle2 = startangle + (anglestep * framenum)
    canvas.arc(bounds, startangle, endangle2, fill=foreground, width=10)

filmstrip.save('test.png', 'PNG')
