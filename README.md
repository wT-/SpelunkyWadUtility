SpelunkyWadUtility
==================

Unpacks and repacks the .wad&amp;.wix file pairs from the game Spelunky

Requires Python 3. Or maybe it doesn't really require it, you can try with 2.7 too I guess /shrug. It's all standard library stuff.

Usage
=====

* Copy the **.py** files to the directory with the **.wad**/**.wix** files you want to mess with.
  * This could be "..\Spelunky\Data\Textures" for an example for textures.
* To unpack, run **unpack.py** or drag&drop a specific **.wad**/**.wix** file on it.
* To repack modified files, dump them in the **repack** subdirectory as is. **Don't** make any extra directories there.
* Run **repack.py**, which will rebuild the **.wad**/**.wix** files
---
* If you made a booboo, there are backups made on the first unpack named something like **.wad.orig**.
* You can run the included convenience script **restore_original.py** to copy them over the current **.wad**/**.wix**.