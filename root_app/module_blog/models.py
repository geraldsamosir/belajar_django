from django.db import models


#class Author
class Author(models.Model):
	name = models.CharField('nama penulis',max_length=50)
	email = models.EmailField('email penulis',unique=True)
	bio  = models.TextField('tentang penulis')

	#nama  menu penulis yang muncul pada view
	class Meta:
		verbose_name_plural ='Semua penulis'

	def  __str__(self):
		return self.name


#classs for category
class Category(models.Model):
	cat_name = models.CharField('nama kategori',max_length=50)
	cat_description = models.CharField('deskripsi',max_length=255)
	
	#nama  menu kategori yang muncul pada view
	class Meta:
		verbose_name_plural ='Semua kategori'

	def  __str__(self):
		return self.cat_name

#class for tag
class Tag(models.Model):
	tag_name = models.CharField('nama tag',max_length=50)
	tag_description =models.CharField('deskripsi',max_length=255)

	#nama  menu tag yang pada view
	class Meta:
		verbose_name_plural ='Semua tag'
	def  __str__(self):
		return self.tag_name

# Class post
class Post(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	create_date = models.DateTimeField(auto_now_add=True,auto_now=False)
	update_date =  models.DateTimeField(auto_now_add=False,auto_now=True)
	author = models.ForeignKey(Author)
	categories = models.ManyToManyField(Category)
	tags = models.ManyToManyField(Tag)

	#nama  menu post yang muncul pada view
	class Meta:
		verbose_name_plural ='Semua post'

	def  __str__(self):
		return self.title
