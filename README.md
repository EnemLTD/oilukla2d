# oilukla2d
 Oilukla - it's easy python 2d game engine repository for your beginner's project's!

# How to install
Run your CMD as Administrator and write
```
pip install oilukla==0.1a0
```
And done!

# How to use
## Creating window
```
from oilukla import oilukla

wind = oilukla.window(640, 480, 'example name', (255, 255, 255), 60, None)

while oilukla.running:
 wind.w_close()
 wind.w_update()
```

## Set image on window
```
from oilukla import oilukla

image = 'JUST_EXAMPLE_NAME_AND_WAY.png'

wind = oilukla.window(640, 480, 'example name', True, None)

my_object = oiluklaentity(image)
my_object.scale_up(image, 80, 80)

while oilukla.running:
 wind.w_close()
 wind.w_update()
```

## Change position of image
```
from oilukla import oilukla

image = 'JUST_EXAMPLE_NAME_AND_WAY.png'

wind = oilukla.window(640, 480, 'example name', True, None)

my_object = oilukla.entity(image)
my_object.scale_up(image, 80, 80)

while oilukla.running:
 wind.w_close()
 my_object.transform(320, 240)
 wind.w_update()
```

# Engine syntaxis 
## oilukla.window
oilukla.window(res_x, res_y, title, bg_color, fps, icon) - Initializing window
 - res_x = Window Width
 - res_y = Window Height
 - title = Window Title
 - bg_color = Color of Background, as example (255,255,255)
 - fps = Frame Rate of Window
 - icon = Window Icon (As example way: 'res/favicon.png')


oilukla.window.w_name(nname) - Renaming window
 - nname = New Window Title

oilukla.window.w_update() - Update window, as example uses when you wanna to move sprite

oilukla.window.w_clear() - Filling background with color and clears sprites on scene

oilukla.window.w_close() - Closing event

## oilukla.entity
oilukla.entity(sprite, res_x, res_y) - Getting data
 - sprite = Sprite
 
oilukla.entity.transform(x, y) - Transform position of sprite
 - x = X Position of sprite
 - y = Y Position of sprite


oilukla.entity.scale_up(res_x, res_y) - Scalling sprite
 - res_x = Width of sprite
 - res_y = Height of sprite

## Final
Thank's for using my engine in your's feature projects!
Using GPL-3.0 License
