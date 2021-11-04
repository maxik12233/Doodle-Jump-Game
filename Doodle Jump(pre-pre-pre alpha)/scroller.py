import colors
from MODULES import *

from rectangle_object import RectObject
from button_sprite import ButtonSprite


def create_scroller(self, x, y, w, h):
    scroller = Scroller(x, y, w, h)
    self.mouse_handlers.append(scroller.slider.handle_mouse_event)
    self.objects.append(scroller)


class Scroller:
    def __init__(self, x, y, w=200, h=100, rect_color=colors.GRAY40):

        self.rect_back = Rectangle(x, y, w, h, rect_color)
        w_l, h_l = w/1.2, h/10
        x_l, y_l = x + (w - w_l)/2, y + (h - h_l)/2
        self.rect_line = Rectangle(x_l, y_l, w_l, h_l, colors.BLACK)
        x_s, y_s = x_l+20, y_l - h_l/2 - 3  # Change x here. Also -3 just fixing texture(dont know why it not good)
        self.slider = Slider(x_s, y_s)

    def draw(self, surface):
        self.rect_back.draw(surface)
        self.rect_line.draw(surface)
        self.slider.draw(surface)

    def update(self):
        if self.slider.state == "pressed":
            dist = self.slider.cursor_pos[0] - self.slider.centerx
            if dist < 0:
                dx = -min(abs(dist), abs(self.rect_line.left-self.slider.centerx))
            elif dist > 0:
                dx = min(dist, self.rect_line.right-self.slider.centerx)
            else:
                dx = 0
            self.slider.move(dx, 0)


class Slider(ButtonSprite):
    def __init__(self, x, y):
        ButtonSprite.__init__(self, x, y, "", "textures/polzunok.png")

        self.cursor_pos = 0

    def handle_mouse_move(self, pos):
        self.cursor_pos = pos
        if self.state == "pressed":
            return
        if self.rect.collidepoint(pos):
            self.state = "hover"
        else:
            self.state = "normal"

    def handle_mouse_down(self, pos):
        if self.rect.collidepoint(pos):
            self.state = 'pressed'

    def handle_mouse_up(self, pos):
        if self.state == 'pressed' and self.rect.collidepoint(pos):
            self.state = 'hover'
        else:
            self.state = "normal"

    @property
    def back_color(self):
        return dict(normal=c.slider_normal_back_color,
                    hover=c.slider_hover_back_color,
                    pressed=c.slider_pressed_back_color)[self.state]


class Rectangle(RectObject):
    def __init__(self, x, y, w, h, color):
        RectObject.__init__(self, x, y, w, h)
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color,  self.rect)

    def __del__(self):
        print("ID ", self.ID, " deleted Rectangle")