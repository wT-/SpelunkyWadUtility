#!/usr/bin/env python
"""
Created on Aug 12, 2013

@author: wT
@version: 1.2
"""

from __future__ import print_function

import sys
sys.dont_write_bytecode = True # It's just clutter for this small scripts
import shutil
import traceback

from unpack import get_wad_path, get_wix_path


if __name__ == '__main__':
	try:
		input = raw_input # Python 2 <-> 3 fix
	except NameError:
		pass
	try:
		yesno = input(r"Overwrite both (potentially modified) .wad and .wix files with originals? [y/n]: ").lower()
		if yesno == "y" or yesno == "yes":
			try:
				shutil.move(get_wad_path() + ".orig", get_wad_path())
				shutil.move(get_wix_path() + ".orig", get_wix_path())
			except:
				print("No .orig files to restore")
			else:
				print("Done")
		else:
			print("Not restoring")
	except SystemExit as e:
		print(e)
	except:
		traceback.print_exc()
