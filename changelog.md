# General

* Added the `sources` folder where you can easily keep videos you want to import

# build.lua

* Modified `writeScriptHeader`'s table of signals to match the new values of Factorio 1.1
* Modified `writeScriptHeader`'s table of signals such that `"raw-wood"` was changed to `"artillery-wagon"`
* Changed testing for `unix` such that it doesn't show an error on the command line when using Windows
* Added a `total_frames` count to easily display how many frames to set for the movie after the script has finished
* Added a graceful exit for the `LoadBitmap` such that it returns false when it cannot load the specified file
* Added a meaningful message that get's displayed when the previous function fails
* Changed some formatting to make it a little cleaner