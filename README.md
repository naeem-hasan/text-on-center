# text-on-center
Place vertically and horizontally centered text on your photos! It can return PIL/Pillow Image objects.

## Features:
* You can use your PIL/Pillow Image objects.
* Or you can specify your image's background color and size.
* You can also set your custom font.
* Font size, color are also customizable.
* Multiline text is supported!

## How to use:
First, download the script and put it in the same directory you're working on so that you can import it.

Then make a `TextOnCenter` object and pass your PIL/Pillow Image object in `image` parameter, text in `text`. Look for example usage at the end.

## Initialization parameters:
* `image` - Pass your Image object here. If you don't, a blank Image object will be created, you can specify its background color.
* `image_size` - If you don't specify your image's size, size of the `image` object will be used. If you don't pass on your `image` object, default size `500x500` is to be used.
* `font_path` - Put your custom font path here. The default is `/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf`. If you don't have the font installed, PIL/Pillow will automatically choose the default font.
* `font_size` - Default font size is 50.
* `text_color` - Specify your desired color with a three numbers tuple with RGB values. Default is `(255, 255, 255)`.
* `bg_color` - Specify your background color, only effective if the `image` object is not passed along. Use a three numbers tuple with RGB values. Default is `(0, 0, 0)`.
* `text` - Pass on your text here. Note that, if your text is very long, you might want to break it down by putting newlines in between. You can use the default `textwrap` module of Python.

## Sample usage:
```python
from PIL import Image
import text_on_center as TOC

myimg = Image.open("myimage.jpg")
centered_text = TOC.TextOnCenter(image=myimg, font_size=80, text="I LOVE PYTHON")
centered_text.draw_text()
centered_text.show_image()
centered_text.get_image().save("with_text.jpg")
```

## Made with this script:
* ![I LOVE PYTHON](https://raw.githubusercontent.com/naeem-hasan/text-on-center/master/examples/with_text.jpg)

I'd love if you contribute!
