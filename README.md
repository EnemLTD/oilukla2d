# oilukla2d
 Oilukla - it's easy python 2d game engine repository for your beginner's project's!

# How to install
Run your CMD as Administrator and write
```
pip install oilukla2d
```
And done!

# How to use
## Creating window
```
from oilukla import *

win = oilwin(640, 480, 'example name', True, None)

win.draw_obj()
win.ena_window()
```

## Set image on window
```
from oilukla import *

image = 'JUST_EXAMPLE_NAME_AND_WAY.png'

win = oilukla.oilwin(640, 480, 'example name', True, None)

my_object = oilukla.oilentity(image, 16, 16)
my_object.add_object()

win.draw_obj()
win.ena_window()
```

## Change position of image
```
from oilukla import *

image = 'JUST_EXAMPLE_NAME_AND_WAY.png'

win = oilukla.oilwin(640, 480, 'example name', True, None)

my_object = oilukla.oilentity(image, 16, 16)
my_object.add_object()

my_object.x = 480
my_object.y = 128
my_object.transform()

win.draw_obj()
win.ena_window()
```
