from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserRole(models.TextChoices):
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'


class MySuperuser(BaseUserManager):
    def create_superuser(self, username, email=None,
                         password=None, **extra_fields):
        extra_fields.setdefault('role', UserRole.ADMIN)
        user = self.create_user(username, password, email, **extra_fields)
        user.is_admin = True
        user.save(using=self._db)
        return user


class City(models.Model):
    city = models.TextField(max_length=300, unique=True)


class User(AbstractUser):

    email = models.EmailField(
        max_length=254,
        unique=True,
        verbose_name='Электронная почта',
        help_text='Укажите электронную почту')

    username = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='Ник пользователя',
        help_text='Укажите ник пользователя')

    bio = models.TextField('Биография', blank=True,)
    role = models.CharField('Роль', max_length=20,
                            choices=UserRole.choices,
                            default=UserRole.USER,)
    city = models.ForeignKey(City, blank=True,
                             null=True,
                             related_name="user",
                             on_delete=models.PROTECT)
    confirmation_code = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='Код подтверждения',
    )

    @property
    def is_admin(self):
        return (self.role == UserRole.ADMIN
                or self.is_superuser
                or self.is_staff)

    @property
    def is_moderator(self):
        return self.role == UserRole.MODERATOR

    def __str__(self):
        return self.username


class Name(models.Model):
    """Author model"""

    first_name = models.TextField(max_length=100,
                                  verbose_name="Имя автора")
    last_name = models.TextField(max_length=100,
                                 verbose_name="Фамилия автора")
    name = models.ForeignKey(User,
                             null=True,
                             unique=True,
                             on_delete=models.CASCADE,
                             related_name='name'
                             )
