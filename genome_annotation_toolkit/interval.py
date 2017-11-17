__author__ = 'Rens Holmer'


class Interval(object):
	"""
	"""
	def __init__(self, seqid, source, interval_type, start, end, score, strand, phase, attributes):
		self.seqid = seqid
		self.source = source
		self.interval_type = interval_type
		self.start = start
		self.end = end
		self.score = score
		self.strand = strand
		self.phase = phase
		self.attributes = attributes
		self.ID = attributes[ID]
		del attributes[ID]