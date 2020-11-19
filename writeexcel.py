import csv 
import json
import os

with open("item.json", "rb") as read:
	with open("Converted.txt", "wb") as copy:

		copy.write(read.read())