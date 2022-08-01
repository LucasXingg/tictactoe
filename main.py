import pyglet
import matrixOperation as mO

win = pyglet.window.Window(width = 800, height = 800, caption = 'tic-tac-toe!' )

# load img
back = pyglet.image.load('./img/back.tiff')
ximg = pyglet.image.load('./img/x.tiff')
oimg = pyglet.image.load('./img/o.tiff')
selimg = pyglet.image.load('./img/select.tiff')
redimg = pyglet.image.load('./img/red.tiff')
blueimg = pyglet.image.load('./img/blue.tiff')

#col position
scale_factor = win.width/back.width
st_po = 124 * scale_factor
sq_wid = 200 * scale_factor

# init background
back_shape = pyglet.sprite.Sprite(back, x = 0, y = 0)
back_shape.update(scale_x = scale_factor, scale_y = scale_factor)
back_c = pyglet.shapes.Rectangle(0, 0, win.width, win.height, color = (255, 255, 255))
class game(object):
    def __init__(self):
        self.mat = mO.matrixCreate(9, 9, rand = False, randlist = [int(0), int(1), int(2)])
        self.term = 1
        self.valid_step = mO.matrixCreate(3, 3, int(1))
        self.resu_mat = mO.matrixCreate(3, 3)
        self.resu = 0

    def step(self, x, y):
        px = (x - st_po) // sq_wid
        py = (y - st_po) // sq_wid
        px = int(px)
        py = int(py)
        area_x = (px + 3) // 3 - 1
        area_y = (py + 3) // 3 - 1
        if self.mat[py][px] == 0:
            if self.valid_step[area_y][area_x] == 1:
                self.mat[py][px] = self.term
                self.term += 2
                self.newArea(px, py)
                self.gameProcess()
                self.resu = self.rule(self.resu_mat)
        if self.term == 3:
            self.term = -1

    def newArea(self, x, y):
        ax = x % 3
        ay = y % 3
        empty_count = 0
        for i in range(3):
            for j in range(3):
                if self.mat[i + 3 * ay][j + 3 * ax] == 0:
                    empty_count += 1
        if empty_count == 0:
            self.valid_step = mO.matrixCreate(3, 3, int(1))
        else:
            self.valid_step = mO.matrixCreate(3, 3, int(0))
            self.valid_step[ay][ax] = 1

    def gameProcess(self):
        for y in range(3):
            for x in range(3):
                if self.resu_mat[y][x] == 0:
                    par_mat = mO.partSelect(self.mat, y * 3, x * 3, (y + 1) * 3, (x + 1) * 3)
                    par_resu = self.rule(par_mat)
                    self.resu_mat[y][x] = par_resu

    def rule(self, mat):
        for i in range(3):
            x_val = 0
            y_val = 0
            for j in range(3):
                x_val += mat[i][j]
                y_val += mat[j][i]
            if x_val == 3 or y_val == 3:
                return 1
            elif x_val == -3 or y_val == -3:
                return -1
        m_dia = 0
        c_dia = 0
        for i in range(3):
            m_dia += mat[i][i]
            c_dia += mat[i][2 - i]
        if m_dia == 3 or c_dia == 3:
            return 1
        elif m_dia == -3 or c_dia == -3:
            return -1
        return 0

    def restart(self, x, y):
        if y <= win.height and y > win.height - st_po:
            self.__init__()

    def checkRange(self, x, y):
        range_l = st_po
        range_r = win.width - st_po
        if x >= range_l and x <= range_r and y >= range_l and y <= range_r:
            return True
        else:
            return False


my = game()

def space_draw():
    back_c.draw()
    for y in range(3):
        for x in range(3):
            if_c = 1
            if my.resu_mat[y][x] == 1:
                c_shape = pyglet.sprite.Sprite(blueimg, x = 0, y = 0)
            elif my.resu_mat[y][x] == -1:
                c_shape = pyglet.sprite.Sprite(redimg, x = 0, y = 0)
            else:
                if_c = 0
            if if_c == 1:
                c_shape.update(scale_x = scale_factor, scale_y = scale_factor, x = st_po + x * 3 * sq_wid, y = st_po + y * 3 * sq_wid)
                c_shape.draw()
    back_shape.draw()
    for y in range(3):
        for x in range(3):
            if my.valid_step[y][x] == 1:
                valid_shape = pyglet.sprite.Sprite(selimg, x = 0, y = 0)
                valid_shape.update(scale_x = scale_factor, scale_y = scale_factor, x = st_po + x * 3 * sq_wid, y = st_po + y * 3 * sq_wid)
                valid_shape.draw()
    for y in range(len(my.mat)):
        for x in range(len(my.mat[y])):
            if_draw = 1
            if my.mat[y][x] == 1:
                xshape = pyglet.sprite.Sprite(ximg, x = 0, y = 0)
            elif my.mat[y][x] == -1:
                xshape = pyglet.sprite.Sprite(oimg, x = 0, y = 0)
            else:
                if_draw = 0
            if if_draw == 1:
                xshape.update(scale_x = scale_factor * 2, scale_y = scale_factor * 2, x = st_po + sq_wid * x, y = st_po + sq_wid * y)
                xshape.draw()
    if my.resu == 1:
        label = pyglet.text.Label('Blue Win!', x = win.width / 2, y = win.height - st_po / 2, anchor_x = 'center', anchor_y = 'center', color = (53, 122, 161, 255))
        label.draw()
    elif  my.resu == -1:
        label = pyglet.text.Label('Red Win!', x = win.width / 2, y = win.height - st_po / 2, anchor_x = 'center', anchor_y = 'center', color = (205, 48, 114, 255))
        label.draw()

@win.event
def on_mouse_press(x, y, button, modifiers):
    if my.resu == 0 and my.checkRange(x, y):
        my.step(x, y)
    elif my.resu == 1 or my.resu == -1:
        my.restart(x, y)



@win.event
def on_draw():
    win.clear
    space_draw()


pyglet.app.run()

