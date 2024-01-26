from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
import uuid


class MyUserManager(BaseUserManager):
    def create_user(self, email=None, user_id=None, password=None, **kwargs):

        user = self.model(
            user_id=user_id,
            email=email,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, user_id=None, **kwargs):
        user = self.create_user(
            email=email,
            user_id=user_id,
        )
        user.is_admin = True
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    uuid_field = models.UUIDField(default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=255, unique=True, null=True, blank=True)
    date_joined = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return str(self.id)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

class EmailVerifyOtp(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    otp = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)



# Create your models here.