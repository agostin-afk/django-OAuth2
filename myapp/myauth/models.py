from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class userAuth(models.Model):
    username = models.CharField(max_length=45, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=128, default='')

    def __str__(self):
        return self.username

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'