from PIL import Image


with Image.open("panick.png") as im:
    width = round(im.size[0] / 32)
    height = round(im.size[1] / 32)
    new_width = 32 * width
    new_height = 32 * height
    im_resized = im.resize((new_width, new_height))

    for i in range(1, width + 1):
        for x in range(1, height + 1):
            image_cropped = im_resized.crop([32*(x-1), 32*(i-1), 32*x, 32*i]).save(f"panick-{i}-{x}.png", "PNG")
