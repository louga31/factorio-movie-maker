---@diagnostic disable: undefined-global
-- screenshot recorder

--[[
    Copy and paste the text below this comment prepended with "/c" into the 
    game console to record the movie.

    `i` is the current frame
    `frames_to_record` is the amount of frames to record. The map by default can
    only hold a max of 4800 frames before you run out of memory.
    `location_of_output` is the folder name that you would like the images to 
    be saved to
    `file_format` is the format of the images to generate.
    `resolution` and `zoom` are passed into the screenshot command.

    The offset of `7` is to wait for the machine to catch up with it's timer as
    it has a 7-tick delay.
]]

local i = 1;
local frames_to_record = 4800;
local location_of_output = "video-output";
local file_format = "png";
local resolution = {3200, 1920};
local zoom = 0.25;

script.on_event(defines.events.on_tick, function(event)
    if i > 6 and i <= frames_to_record + 7 then
        game.take_screenshot{
            position={0, 0},
            resolution=resolution,
            zoom=zoom,
            path=location_of_output .. "/" .. i - 6 .. ".png"
        };
        i = i + 1;
    end
end);
game.ticks_to_run = frames_to_record + 7;