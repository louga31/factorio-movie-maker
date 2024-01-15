# Factorio Movie Maker

This project encodes a 178x100 3-bit color movie in a [Factorio](http://www.factorio.com) map, now updated for Factorio version 1.1.58.

## Contents:

* `images` are where individual frames of the source video are stored.
* `script` is where console commands are recorded, to be pasted into Factorio.
* `sources` are where you can put your video files.
* `movie.zip` is the original unchanged save file, compatible with Factorio 0.15.
* `movie-updated.zip` is the updated save file, compatible with Factorio version 1.1, with no changes made to it other than the necessary migrations.
* `movie-corrected.zip` is the update save file, but with signal `"raw-wood"` replaced with signal `"artillery-wagon"`, using `corrector.py`.
* `build.lua` is the original image conversion script, with minor compatibility changes. See `changelog.md` for details on what is different.
* `build.py` is a Python translation of build, which is slightly less verbose. ~~Can be used if you already have/prefer Python.~~ Currently WIP.
* `corrector.py` produces a blueprint that can be placed over the player to change the aforementioned `"raw-wood"` signals. Used to create `movie-corrected.zip`.
* `screenshot_recorder.lua` is a script that you can use to record the movie player while in game.
* `screenshot_combiner.py` is a script that you can use to combine the output images of `screenshot_recorder.lua` to a video file of your choosing.
* `example_output.mp4` is an example recording of the movie player in action, of [Darude's Feel the Beat](https://www.youtube.com/watch?v=aLZQ-0dHbiU) music video.

## Usage

1. Install dependencies. You can either:
    1. Install [FFmpeg](http://www.ffmpeg.org/download.html) and [Lua](http://lua-users.org/wiki/LuaBinaries) if you don't already have them.  
       Or
    2. Install [Python 3](https://www.python.org/downloads/) and `pip install -r requirements.txt` if you want to used `extractor.py` instead of standalone FFMPEG.

2. Obtain a source picture or video.  It must have a 16:9 aspect ratio or it will be stretched.  In this example it is called `source.mp4` and placed in the `sources/` folder.

3. Extract each frame from the source and encode it with the palette of the screen to `images`. This can be done either of 2 ways:  
    * Lua and FFMPEG:  

        ```
        cd factorio-movie-maker
        ffmpeg -i sources/source.mp4 -i palette.bmp -filter_complex "fps=20,scale=178:100:flags=lanczos,paletteuse" -pix_fmt bgr24 images/%04d.bmp
        ```

    * Python 3  

        ```
        cd factorio-movie-maker
        python extractor.py sources/source.mp4
        ```

4. Next, create the script files by running `lua build.lua` or ~~`python build.py`~~, depending on which method you prefer. This will populate your `script` folder with numbered text files titled `topXX.txt` and `bottomXX.txt`. This will also output the total number of frames that the movie uses, which is needed later.

5. Start Factorio and load `movie-corrected.zip` by installing it in your `saves` folder.

6. Open each file in the `script` directory, select all, and copy/paste it into the Factorio console. Keep in mind the map file as provided can only store 4800 frames of video, unless you expand it. Attempting to run any script greater than `script/top08.txt` or `script/bottom08.txt` will result in missing-combinator errors.

7. Open the constant combinator at position {-183,-1}.  Change the red signal to the frame count of your movie, as learned earlier.

## Create a recording of the in-game movie player:

Once the movie is loaded and playing, you can use the following steps to create a video file to prove that you did it:

1. Reset the frame count combinator back to a value of 1.

2. Go into editor mode using `/editor` in the console, navigate to the time options and pause the game.  
   In addition, you can also change the time of day and freeze it to a particular value. Back when the video player was first made, the color contrast on lamps was different, so to get a more visible effect you can change the time of day to night and freeze it there.

3. Change the frame count back to the number of frames of your movie.

3. Open `screenshot_recorder.lua`. Change any parameters in the heading bit and then copy the code itself. Paste the code into the console **prepended with `/c`** to run the code as a command. Make sure you have the settings set to what you want before you run the command, because if you want to start over you must repeat the previous steps.

4. Wait until the script finishes. It will take a screenshot centered around the screen every tick for however many frames you specified. Each screenshot will be written to your Local Factorio `script-output` folder.

5. From here, you can either stitch the files together into a video using FFMPEG, or use the provided `screenshot_combiner.py` to do the same.

