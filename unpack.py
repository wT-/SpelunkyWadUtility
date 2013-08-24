#!/usr/bin/env python
"""
Created on Aug 10, 2013

@author: wT
@version: 1.2
"""

from __future__ import print_function, unicode_literals

import sys
sys.dont_write_bytecode = True # It's just clutter for this small scripts

import os
import io
import platform
import traceback

class PathStorage():
	wad = None
	wix = None

def get_wad_path():
	if not PathStorage.wad:
		get_wix_path()
	return PathStorage.wad

def get_wix_path():
	if not PathStorage.wix:
		if len(sys.argv) > 1:
			if not is_valid_input(sys.argv[1]): # Let's assume argv[0] is the script name
				error_out_bad_input()
		else:
			for item in os.listdir("."): # "." should be the default. Why does Eclipse error out but command line works without it?
				if is_valid_input(item):
					break
			else: # Hahaa! Got to use for..else
				error_out_bad_input()
	return PathStorage.wix

def is_valid_input(input_file):
	if input_file.endswith(".wad") and os.path.exists(input_file + ".wix"):
		PathStorage.wad = input_file
		PathStorage.wix = input_file + ".wix"
	elif input_file.endswith(".wix"):
		wad, _ = os.path.splitext(input_file)
		PathStorage.wad = wad
		PathStorage.wix = input_file
	else:
		return False
	return True

def unpack_file(file_name, group, data):
	dest_path = os.path.join("unpacked", group)
	if not os.path.exists(dest_path):
		os.makedirs(dest_path)

	with io.open(os.path.join(dest_path, file_name), mode="wb") as output:
		output.write(data)
		print("Unpacked", file_name)

def prepare_directory():
	# First make backups
	import shutil
	index_file = get_wix_path()
	wad_file = get_wad_path()
	if not os.path.exists(index_file + ".orig"):
		shutil.copy2(index_file, index_file + ".orig")
	if not os.path.exists(wad_file + ".orig"):
		shutil.copy2(wad_file, wad_file + ".orig")
	# Secondly create repack dir if it's not there yet
	if not os.path.exists('repack'):
		os.mkdir("repack")

def error_out_bad_input():
	sys.exit("I need a .wad or .wix file, ya dingus")

if platform.system() == "Windows":
	import atexit
	@atexit.register
	def pause_on_exit():
		# input("Press enter to close")
		os.system("pause") # os.system'ing anything is supposedly awful. Let's keep it for now
	del atexit

if __name__ == '__main__':
	try:
		prepare_directory()

		with io.open(get_wad_path(), mode='rb') as wad_file:
			with io.open(get_wix_path(), mode="r") as index_file:
				for line in index_file:
					if line.startswith("!group"):
						_, group = line.split()
					else:
						file_name, offset, size = line.split()
						wad_file.seek(int(offset))
						data = wad_file.read(int(size))
						if len(data) == 0:
							print("Error while unpacking. Hit end-of-file before we should've. Is {} corrupted?".format(get_wad_path()))
							break
						unpack_file(file_name, group, data)
	except SystemExit as e:
		print(e)
	except:
		traceback.print_exc()
