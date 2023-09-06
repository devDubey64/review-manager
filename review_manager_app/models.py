from django.db import models,IntegrityError

# Create your models here.
class Tag(models.Model):
	name = models.CharField(max_length=255, db_index=True, unique=True)
	created_at = models.DateTimeField(auto_now_add= True)
	updated_at = models.DateTimeField(auto_now= True)

	def save(self, *args, **kwargs):
		self.name = self.name.lower()
		try:
			super(Tag, self).save(*args, **kwargs)
		except IntegrityError:
			raise IntegrityError(f'Tag name: {self.name} not unique. Please try using a different name.')

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['id']

class Review(models.Model):
	review_id = models.AutoField(primary_key=True, db_index=True)
	text = models.TextField()
	author = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add= True)
	updated_at = models.DateTimeField(auto_now= True)
	tags = models.ManyToManyField('Tag', blank=True)

	def __str__(self):
		return f'Review #{self.review_id} by {self.author} with tags : {self.tags}'


	class Meta:
		ordering = ['-updated_at']