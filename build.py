# movie_player.py

"""
README: currently unfinished, will work on later. For now, use `build.lua`

Python script translation of `build.lua`. Assumes the images have already been
extracted with FFMPEG or other. A little simpler, as this is more Python's forte
than Lua's.
"""

import imageio

import os

def main():
    # Load palette
    palette = {}
    pixels = imageio.imread("palette.bmp")
    for i in range(7):
        palette[tuple(pixels[0][i])] = i

    print(palette)

    # Load images list
    files = []
    for f in os.listdir("images"):
        file_path = os.path.join("images", f)
        if os.path.isfile(file_path):
            files.append(file_path)

    # Process images
    total_frames = 0
    for index, file in enumerate(files):
        print("processing {}".format(file))

        pixels = imageio.imread(file)
        print(pixels)

        count = 0
        for x in range(178):
            for y in range(100):
                color = palette[tuple(pixels[x][y])] or 0
                position = y_wire[y] + ((x-1)%3)*5
                if (y <= 50):
                    top_signals[position] = top_signals[position] + color * y_shift[y]
                else:
                    bottom_signals[position] = bottom_signals[position] + color * y_shift[y]

    # for index, file in pairs(files) do
    #     print("processing "..file)
    #     pixels = LoadBitmap(file)

    #     local count = 0
    #     for x = 1,178 do 
    #         for y = 1,100 do
    #             local color = palette[pixels[x][y]] or 0
    #             local position = y_wire[y] + ((x-1)%3)*5
    #             if (y <= 50) then
    #                 top_signals[position] = top_signals[position] + color * y_shift[y]
    #             else
    #                 bottom_signals[position] = bottom_signals[position] + color * y_shift[y]
    #             end
    #         end
    #         count = count + 1
    #         if (count == 3) then
    #             writeCombinator()
    #             count = 0
    #         end
    #     end
    #     writeCombinator()
    #     total_frames = total_frames + 1
    # end

    print("Total number of movie frames:", total_frames)

if __name__ == "__main__":
    main()