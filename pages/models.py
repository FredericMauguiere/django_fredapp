from django.db import models

class CatalogItem(models.Model):
    """
    model to store catalog items
    """
    name = models.TextField()
    price = models.FloatField(default=0.0)
    picture = models.ImageField(upload_to='pictures', blank=True, null=True)

    def __str__(self):
        """
        string representation of the model.
        """ 
        return self.name[:50]