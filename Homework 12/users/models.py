from django.db import models

class UserCreate(models.Model):
    name = models.CharField(max_length= 80, unique= True, verbose_name= 'username')
    email = models.EmailField(blank= True, default='')
    isAdmin = models.BooleanField(default= False)
    password = models.CharField(verbose_name= 'password', max_length= 20, unique= True, null= False)
    birth_date = models.DateField(null= True, blank= True)

    class Meta:
        ordering = ["name", "birth_date"]

    @property
    def Info_get(self):
        return f"{self.name} {self.birth_date}"

    def __str__(self):
        return self.name