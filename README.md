SpelunkyWadUtility
==================

Unpacks and repacks the .wad&amp;.wix file pairs from the game Spelunky

Requires Python 3. Or maybe it doesn't really require it, you can try with 2.7 too I guess /shrug. It's all standard library stuff.

Usage
=====

* Copy the .py files to the directory with the **.wad**/**.wix** files you want to mess with. This could be "..\Spelunky\Data\Textures" for an example
* To unpack, either just run the **unpack.py** straight up and it'll unpack the first **.wad**/**.wix** pair it finds, or drag&drop a **.wad**/**.wix** file on it.
* Unpacked files will be in **unpacked** subdirectory
* To i.e. modify a texture. Find it in the **unpacked** subdirectory, edit to your liking, and move it to the **repack** subdirectory that should've been created for you.
  * Don't make any extra directories in the **repack** subdirectory, just dump your files there
* Run **repack.py**, which will rebuild the **.wad**/**.wix** files

* If you made a booboo, there should always be backups made on the first unpack named something like **.wad.orig**. You can run the included convenience script **restore_original.py** to copy them over the current **.wad**/**.wix**