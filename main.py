import pyglet
import matrixOperation as mO

display = pyglet.canvas.get_display()
screens = display.get_screens()
win = pyglet.window.Window(width = 1000, height = 1000, screen = screens[0])

# load img
back = pyglet.image.load('./img/back.tiff')
ximg = pyglet.image.load('./img/x.tiff')
oimg = pyglet.image.load('./img/o.tiff')

#col position
scale_factor = win.width/back.width
st_po = 124 * scale_factor
sq_wid = 200 * scale_factor

# init background
back_shape = pyglet.sprite.Sprite(back, x = 0, y = 0)
back_shape.update(scale_x = scale_factor, scale_y = scale_factor)
class val(object):
    def __init__(self):
        self.mat = mO.matrixCreate(9, 9, rand = False, randlist = [int(0), int(1), int(2)])
        self.term = "m"

my = val()

def space_draw():
    for y in range(len(my.mat)):
        for x in range(len(my.mat[y])):
            if_draw = 1
            if my.mat[y][x] == 1:
                xshape = pyglet.sprite.Sprite(ximg, x = 0, y = 0)
            elif my.mat[y][x] == 2:
                xshape = pyglet.sprite.Sprite(oimg, x = 0, y = 0)
            else:
                if_draw = 0
            if if_draw == 1:
                xshape.update(scale_x = scale_factor * 2, scale_y = scale_factor * 2, x = st_po + sq_wid * x, y = st_po + sq_wid * y)
                xshape.draw()

@win.event
def on_mouse_press(x, y, button, modifiers):
    px = (x - st_po) // sq_wid
    py = (y - st_po) // sq_wid
    px = int(px)
    py = int(py)
    my.mat[py][px] += 1
    if my.mat[py][px] == 3:
        my.mat[py][px] = 0


@win.event
def on_draw():
    win.clear
    back_shape.draw()
    space_draw()


pyglet.app.run()

