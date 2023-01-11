from django.db import models
from django.contrib.auth.models import AbstractUser

class UserInfo(AbstractUser):
    SEX = [('男', '男'), ('女', '女'), ('その他', 'その他')]
    firstname2 = models.CharField(max_length = 20)
    lastname2 = models.CharField(max_length = 20)
    sex = models.CharField(max_length=10, choices=SEX)
    age = models.IntegerField(default = 20)
    point = models.IntegerField(default = 0)

class Address(models.Model):
    zip_code = models.CharField(verbose_name='郵便番号',max_length=8,blank=True)
    address1 = models.CharField(verbose_name='都道府県',max_length=40,blank=True)
    address2 = models.CharField(verbose_name='市区町村番地',max_length=40,blank=True)


class MonsterList(models.Model):
    name = models.CharField(max_length=10)
    images = models.ImageField(upload_to='images')


class Owner(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, blank=True)
    monster = models.ForeignKey(MonsterList, on_delete=models.CASCADE, blank=True)

    class Meta:
        ordering = ['monster']
        constraints = [
            models.UniqueConstraint(fields=['user', 'monster'], name='unique_user_monster'),
        ]

        

        

