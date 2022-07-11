from django.db import models

#Djangoが元から持つモジュール
from django.contrib.auth.models import User

class Acount(models.Model):

#ユーザー認証のインスタンス（１対１の関係）
    user = models.OneToOneField(User, on_delete=models.CASCADE)


#追加フィールド作成
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    acount_image = models.ImageField(upload_to="profile_pics",blank=True)

    def __str__(self):
        return self.user.username