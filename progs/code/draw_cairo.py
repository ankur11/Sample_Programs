import cairo
from contextlib import contextmanager

@contextmanager
def saved(cr):
    cr.save()
    try:
        yield cr
    finally:
        cr.restore()

def Tree(angle):
    cr.move_to(0, 0)
    cr.translate(0, -65)
    cr.line_to(0, 0)
    cr.stroke()
    cr.scale(0.72, 0.72)
    if angle > 0.12:
        for a in [-angle, angle]:
            with saved(cr):
                cr.rotate(a)
                Tree(angle * 0.75)

surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, 280, 204)
cr = cairo.Context(surf)
cr.translate(140, 203)
cr.set_line_width(5)
Tree(0.75)
surf.write_to_png('fractal-tree.png')
