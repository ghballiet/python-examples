from django.db import models

BIB_TYPES = [
	('Article','Article'),
	('Book','Book'),
	('Website','Website'),
	]

class Piece(models.Model):
	title = models.CharField(max_length=1000)
	date_written = models.CharField(blank=True,max_length=100)
	composer = models.ForeignKey('Composer')
	instrumentation = models.ForeignKey('Instrumentation',blank=True)
	score_image = models.FileField(upload_to='scores',max_length=1000)
	sound_clip = models.URLField(max_length=500)
	program_notes = models.TextField(max_length=2000,default="None available.")
	
	class Meta:
		ordering = ['composer','date_written','title']
	
	def __str__(self):
		return self.title + " (" + self. date_written + ") - " + str(self.composer)
	
	def __unicode__(self):
		return self.title + " (" + self. date_written + ") - " + str(self.composer)
	

class Composer(models.Model):
	name = models.CharField(max_length=500)
	birth_date = models.CharField(blank=True,max_length=4)
	death_date = models.CharField(blank=True,max_length=4)
	
	class Meta:
		ordering = ['name','birth_date']
	
	def __str__(self):
		return self.name + " (" + str(self.birth_date) + " - " + str(self.death_date) + ")"
	
	def __unicode__(self):
		return self.name + " (" + str(self.birth_date) + " - " + str(self.death_date) + ")"
	

class Instrumentation(models.Model):
	title = models.CharField(max_length=500)
	
	class Meta:
		ordering = ['title']
	
	def __str__(self):
		return self.title
	
	def __unicode__(self):
		return self.title
	

class Category(models.Model):
	title = models.CharField(max_length=500,unique=True)
	
	class Meta:
		ordering = ['title']
	
	def __str__(self):
		return self.title
	
	def __unicode__(self):
		return self.title
	

class Bibliography(models.Model):
	item_type = models.CharField(max_length=100,choices=BIB_TYPES)
	category = models.ForeignKey('Category')
	author = models.CharField(max_length=200)
	editor = models.CharField(max_length=200,blank=True)
	translator = models.CharField(max_length=200,blank=True)
	title = models.CharField(max_length=500)
	city = models.CharField(max_length=200,blank=True)
	publisher = models.CharField(max_length=500,blank=True)
	year = models.CharField(max_length=4,blank=True)
	journal_name = models.CharField(max_length=200,blank=True)
	journal_volume_no = models.CharField(max_length=200,blank=True)
	pages = models.CharField(max_length=100,blank=True)
	website_name = models.CharField(max_length=500,blank=True)
	website_address = models.URLField(max_length=500,blank=True)
	date_accessed = models.DateField(null=True,blank=True)
	annotation = models.TextField(max_length=5000,blank=True)
	
	class Meta:
		ordering = ['item_type','category','author','title']
	
	def __str__(self):
		return self.item_type + ": " + self.author + " - " + self.title
	
	def __unicode__(self):
		return self.item_type + ": " + self.author + " - " + self.title
	
