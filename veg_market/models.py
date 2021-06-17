from django.db import models

class FoodTypes(models.Model):
	types = models.CharField(max_length=10)
	slug = models.SlugField()

	def __str__(self):
		return self.types


class Food(models.Model):
	name = models.CharField(max_length=10, unique = True)
	slug = models.SlugField()
	quantity = models.IntegerField()
	note = models.TextField()
	foodtypes = models.ForeignKey(FoodTypes, on_delete = models.CASCADE) 
	#on_delete表示當對應的FoodTypes被刪除時，Food也一起刪除(CASCADE)

	def __str__(self):
		return "<{}>{}({}):{}".format(self.foodtypes, self.name, self.quantity, self.note)

		
