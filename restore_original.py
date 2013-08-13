#!python3
"""
Created on Aug 12, 2013

@author: wT
"""

import sys
sys.dont_write_bytecode = True # It's just clutter for this small scripts
import shutil

from unpack import get_wad_path, get_wix_path


if __name__ == '__main__':
	yesno = input(r"Overwrite both (potentially modified) .wad and .wix files with originals? [y/n]: ").lower()
	if yesno == "y" or yesno == "yes":
		shutil.copy2(get_wad_path() + ".orig", get_wad_path())
		shutil.copy2(get_wix_path() + ".orig", get_wix_path())
		print("Done")
	else:
		print("Not restoring")
