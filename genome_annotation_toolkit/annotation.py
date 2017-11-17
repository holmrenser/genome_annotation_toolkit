__author__ = 'Rens Holmer'

from genome import Genome
from parse_gff import parse_gff

class Annotation(object):
	"""
	"""
	def __init__(self, fasta_file = None, gff_file = None):
		self.genome = Genome(fasta_file)
		self.features = {interval.ID:interval for interval in parse_gff(gff_file)}
