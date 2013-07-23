from django.db import models
from django.forms import ModelForm
from flutemusic.models import *

class PieceForm(ModelForm):
	class Meta:
		model = Piece
	

class ComposerForm(ModelForm):
	class Meta:
		model = Composer
	

class InstrumentationForm(ModelForm):
	class Meta:
		model = Instrumentation
	

class CategoryForm(ModelForm):
	class Meta:
		model = Category
	

class BiblioForm(ModelForm):
	class Meta:
		model = Bibliography