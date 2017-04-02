from PIL import Image
import text_on_center as TOC

myimg = Image.open("myimage.jpg")
centered_text = TOC.TextOnCenter(image=myimg, text="I LOVE PYTHON")
centered_text.draw_text()
centered_text.show_image()
centered_text.get_image().save("with_text.jpg")
