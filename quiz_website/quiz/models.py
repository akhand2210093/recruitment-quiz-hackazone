from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, student_number, email, name, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not student_number:
            raise ValueError('Users must have a student number')

        user = self.model(
            email=self.normalize_email(email),
            student_number=student_number,
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    student_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    
    objects = UserManager()

    USERNAME_FIELD = 'student_number'
    REQUIRED_FIELDS = ['email', 'name']

    def __str__(self):
        return self.name

class Question(models.Model):
    section = models.IntegerField()
    text = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255)  # Store only the correct answer

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class UserResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.name}: {self.score}'
