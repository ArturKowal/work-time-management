from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import MaxValueValidator, MinValueValidator

class MyAccountManager(BaseUserManager):
	def create_user(self, email, name,last_name, password=None):
		if not email:
			raise ValueError('Users must have an email address')
		if not name:
			raise ValueError('Users must have a name')
		if not last_name:
			raise ValueError('Users must have a last name')

		user = self.model(
			email=self.normalize_email(email),
			name=name,
			last_name=last_name,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, name,last_name, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			name=name,
			last_name=last_name,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


class Account(AbstractBaseUser):
	email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
	ident					= models.PositiveIntegerField(default=1234, validators=[MinValueValidator(1000), MaxValueValidator(9999)],unique=True)
	name 					= models.CharField(max_length=30, unique=False)
	last_name 				= models.CharField(max_length=30, unique=False)
	date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin				= models.BooleanField(default=False)
	is_active				= models.BooleanField(default=True)
	is_staff				= models.BooleanField(default=False)
	is_superuser			= models.BooleanField(default=False)


	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['name','last_name']

	objects = MyAccountManager()

	def __str__(self):
		return self.name#, str(self.last_name), str(self.email)

	# For checking permissions. to keep it simple all admin have ALL permissons
	def has_perm(self, perm, obj=None):
		return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
	def has_module_perms(self, app_label):
		return True