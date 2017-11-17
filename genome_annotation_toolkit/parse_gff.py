__author__ = 'Rens Holmer'

import sys
import urllib
from interval import Interval

def format_attributes(attribute_string):
	attributes = {}
	parts = attribute_string.split(';')
	for part in parts:
		part = part.strip()
		if not part:
			continue
		key,value = part.split('=')
		key = key.strip()
		value = value.strip()
		value = urllib.unquote(value)
		values = [v.strip() for v in value.split(',')]
		attributes[key] = values
	return {}

def format_score(score):
	try:
		return float(score)
	except:
		return score

def format_phase(phase):
	try:
		return int(phase)
	except:
		return phase


def parse_gff(gff_file):
	with open(gff_file, 'r') as file_handle:
		for line in file_handle:
			line = line.strip()
			if line[0] == '#' or not line:
				continue
			parts = line.split('\t')
			seqid = parts[0]
			source = parts[1]
			interval_type = parts[2]
			start = int(parts[3])
			end = int(parts[4])
			score = format_score(parts[5])
			strand = parts[6]
			phase = format_phase(parts[7])
			attributes = format_attributes(parts[8])
			interval = Interval(seqid = seqid, source = source, interval_type = interval_type,
				start = start, end = end, score = score, strand = strand, phase = phase,
				attributes = attributes)
			yield interval