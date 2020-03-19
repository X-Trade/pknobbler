from PIL import Image, ImageDraw, ImageColor
from argparse import ArgumentParser

def swap(a, b):
    return b, a

width = 55
height = 55
frames = 99
border = 2
size = (width, (height*frames*frames))

background = (0,0,0,0)
foreground = (255,0,0,178)

startangle = (0 - 90) - 150
endangle = (0 - 90) + 150
anglerange = endangle - startangle
anglestep = anglerange / (frames-1)

filmstrip = Image.new('RGBA', size, color=background)
canvas = ImageDraw.Draw(filmstrip)

for framenum2 in range(frames):
    startangle2 = startangle + (anglestep * framenum2)
    for framenum in range(frames):
        frametop = (framenum+(framenum2*frames)) * height
        framebot = frametop + height - 1
        bounds = [(border, frametop+border), (width-border, framebot-border)]
        endangle2 = startangle + (anglestep * framenum)
        if startangle2 > endangle2:
            startangle3 = endangle2
            endangle3 = startangle2
        else:
            startangle3 = startangle2
            endangle3 = endangle2
        print([framenum2, framenum, bounds, startangle2, endangle2])
        canvas.arc(bounds, startangle3, endangle3, fill=foreground, width=10)

filmstrip.save('output/test2.png', 'PNG')
