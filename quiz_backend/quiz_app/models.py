from django.db                  import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='nom de category', unique=True)
    desc = models.TextField(verbose_name='description de category')
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Quiz(models.Model):
    LEVEL_CHOICE = ({'facile': 'FACILE', 'moy': 'MOYEN', 'diff': 'DIFFICILE'})
    creator      = models.ForeignKey(User, verbose_name='Createur de quiz', on_delete=models.CASCADE)
    category     = models.ForeignKey(Category, verbose_name="category", on_delete=models.CASCADE)
    question     = models.CharField(max_length=255, verbose_name='question', unique=True)
    proposition  = models.CharField(max_length=255, verbose_name='proposition')
    proposition1 = models.CharField(max_length=255, verbose_name='proposition1')
    proposition2 = models.CharField(max_length=255, verbose_name='proposition2')
    response     = models.CharField(max_length=255, verbose_name='response')
    level        = models.CharField(max_length=255, verbose_name='level', choices=LEVEL_CHOICE)
    valeur       = models.PositiveSmallIntegerField(default=1)
    created_at   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category.name}: {self.question}."
    
    def quiz_value(self):
        l = self.level
        self.valeur = 1 if l == 'facile' else 2 if l == 'moy' else 5
        return self.valeur

class Score(models.Model):
    LEVEL_CHOICE = ({'facile': 'FACILE', 'moy': 'MOYEN', 'diff': 'DIFFICILE'})
    Player   = models.ForeignKey(User, verbose_name='Joueur de quiz', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name="Score dans cette categorie", on_delete=models.CASCADE)
    level    = models.CharField(max_length=8, verbose_name='level', choices=LEVEL_CHOICE)
    score    = models.PositiveIntegerField(default=0)
    created  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.Player.username}: {self.score} points."
