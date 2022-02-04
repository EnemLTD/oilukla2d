# oilukla2d
 Oilukla - it's easy python 2d game engine repository for your beginner's project's!

# How to install
Run your CMD as Administrator and write
```
pip install oilukla
```
And done!

# How to use
## Creating window
```
from oilukla.oilukla import oilwin

win = oilwin(640, 480, 'example name', True, None)

win.draw_obj()
win.ena_window()
```

## Set image on window
```
from oilukla.oilukla import oilentity, oilwin

image = 'JUST_EXAMPLE_NAME_AND_WAY.png'

win = oilwin(640, 480, 'example name', True, None)

my_object = oilentity(image, 16, 16)
my_object.add_object()

win.draw_obj()
win.ena_window()
```

## Change position of image
```
from oilukla.oilukla import oilentity, oilwin

image = 'JUST_EXAMPLE_NAME_AND_WAY.png'

win = oilwin(640, 480, 'example name', True, None)

my_object = oilentity(image, 16, 16)
my_object.add_object()

my_object.x = 480
my_object.y = 128
my_object.transform()

win.draw_obj()
win.ena_window()
```

# Engine syntaxis 
## OILWIN
oilwin(res_x, res_y, title, resiz, icon) - Initializing window
 - res_x = Window Width
 - res_y = Window Height
 - title = Window Title
 - resiz = Resizable mode (True - Block, False - Unblock)
 - icon = Window Icon (As example way: 'res/favicon.png')


oilwin.resize_win(nres_x, nres_y) - Resizing window
 - nres_x = New Window Width
 - nres_y = New Window Height


oilwin.rename_win(ntitle) - Renaming window
 - ntitle = New Window Title


oilwin.ena_window() - Enabling window


oilwin.draw_obj() - Drawing objects and window

## OILENTITY
oilentity(sprite, res_x, res_y) - Getting data
 - sprite = Sprite
 - res_x = Width of sprite
 - res_y = Height of sprite
 
oilentity.add_object() - Setting object on screen

oilentity.transform() - Setting position of object

## Final
Thank's for using my engine in your's feature projects!
Using GPL-3.0 License
