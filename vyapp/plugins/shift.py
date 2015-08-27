class Shift(object):
    def __init__(self, area, width=4, char=' '):
        self.width = width
        self.char  = char
        area.install(('NORMAL', '<Key-greater>', lambda event: event.widget.shift_sel_right(self.width, self.char)),
                     ('NORMAL', '<Key-less>', lambda event: event.widget.shift_sel_left(self.width)))


install = Shift


