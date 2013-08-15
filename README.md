SpelunkyWadUtility
==================

Unpacks and repacks the .wad&amp;.wix file pairs from the game Spelunky

Requires at least Python 3.1, probably even newer version, so just get the latest. Tested on 3.3.2.

Usage
=====

* Copy the **.py** files to the directory with the **.wad/.wix** files you want to mess with.
  * This could be "..\Spelunky\Data\Textures" for an example for textures.
* To unpack, run **unpack.py** or drag&drop a specific **.wad/.wix** file on it.
* To repack modified files, dump them in the **repack** subdirectory as is. **Don't** make any extra directories there.
* Run **repack.py**, which will rebuild the **.wad/.wix** files.

Notes
=====

* If you made a booboo, there are backups made on the first unpack named something like **.wad.orig**.
* You can run the included convenience script **restore_original.py** to copy them over the current **.wad/.wix**.
