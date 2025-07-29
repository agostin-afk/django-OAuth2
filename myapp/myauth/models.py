from django.db import models

class userAuth(models.Model):

    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'userAuth'
        verbose_name_plural = 'userAuths'
    name = models.CharField(max_length=45)
    email = models.EmailField(max_length=254)
    pwd = models.CharField()