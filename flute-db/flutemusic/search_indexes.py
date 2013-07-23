from haystack import indexes
from haystack import site
from flutemusic.models import *

class PieceIndex(indexes.SearchIndex):
	text = indexes.CharField(document = True)
	title = indexes.CharField(model_attr='title')
	composer = indexes.CharField(model_attr='composer')
	program_notes = indexes.CharField(model_attr='program_notes')
	
	def get_queryset(self):
		return Piece.objects.all()

site.register(Composer, Instrumentation, Category, Bibliography, PieceIndex, Piece)