from django.db import models

# Create your models here.


class Movies(models.Model):
    Movie_Title = models.CharField(max_length=700)
    movie_id = models.IntegerField(primary_key=True)

    class Meta:
        db_table = 'Movies'