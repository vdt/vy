"""
Mode: 1
Event: <Control-Key-1> 
Description: Add selection from the cursor positon to the beginning of the file.


Mode: 1
Event: <Control-Key-2> 
Description: Add selection from the cursor position to the end of the file.


Mode: 1
Event: <Control-a> 
Description: Add selection from the beginning to the end of the file.
"""


def install(area):
    area.install(('NORMAL', '<Control-Key-1>', lambda event: event.widget.sel_text_start()),
                 ('NORMAL', '<Control-Key-2>', lambda event: event.widget.sel_text_end()),
                 ('NORMAL', '<Control-a>', lambda event: event.widget.select_all()))

