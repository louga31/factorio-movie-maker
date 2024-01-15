# extractor.py

"""
Instead of using FFMPEG to extract the data, you can use this instead. It 
operates in the exact same way, except might be a little more user friendly if
you've already got Python installed.
"""

import imageio
from PIL import Image

import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="The source image or file to read")
    args = parser.parse_args()

    reader = imageio.get_reader(args.file)
    fps = reader.get_meta_data()["fps"]
    nframes = reader.get_meta_data()["nframes"]

    # Convoluted method to treat an image file as a palette
    # Geddit, convolution
    palette_data = Image.open("palette.bmp").getdata()
    palette_data = list(sum(palette_data, ())) # Flatten internal tuples to 1d
    palette_image = Image.new("P", (16, 16))
    palette_image.putpalette(palette_data)

    for i, frame in enumerate(reader):
        print(i)
        # Convert to image object
        img = Image.fromarray(frame).resize((178, 100), Image.Resampling.LANCZOS)
        # Dither the pixels to the palette's spec
        img = img.quantize(palette = palette_image)
        # Convert back to a truecolor file
        img = img.convert("RGB")
        # Save
        img.save("images/{:04d}.bmp".format(i+1))

if __name__ == "__main__":
    main()