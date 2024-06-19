from rest_framework.authentication      import SessionAuthentication, BasicAuthentication
from django.contrib.contenttypes.fields import GenericForeignKey
from rest_framework.permissions         import IsAuthenticated
from django.contrib.contenttypes.models import ContentType
from rest_framework.response            import Response
from rest_framework.views               import APIView
from django.db                          import models
from django.contrib.auth.models         import User

# Create your models here.
class AuthToken(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes     = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user), # `django.contrib.auth.User` instance.
            'auth': str(request.auth), # None
        }
        return Response(content)

class Category(models.Model):
    name    = models.CharField(max_length=255, verbose_name='nom de category', unique=True)
    desc    = models.TextField(verbose_name='description de category')
    time    = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, verbose_name='Createur de quiz', on_delete=models.CASCADE)

    def __str__(self):
        return self.namew

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
    valeur       = models.PositiveSmallIntegerField(default=0)
    validated    = models.BooleanField(default=False)
    created_at   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category.name}: {self.question}."

    def quiz_value(self):
        l = self.level
        if self.validated:
            self.valeur = 1 if l == 'facile' else 2 if l == 'moy' else 5
        else: self.valeur = 0
        return self.valeur

class Player(models.Model):
    user       = models.ForeignKey(User, verbose_name='Joueur de quiz', on_delete=models.CASCADE)
    quizzes    = models.ManyToManyField(Quiz, verbose_name="quizzes")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.score} points."

class Score(models.Model):
    LEVEL_CHOICE = ({'facile': 'FACILE', 'moy': 'MOYEN', 'diff': 'DIFFICILE'})
    player   = models.ForeignKey(Player, verbose_name='Joueur de quiz', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name="Score dans cette categorie", on_delete=models.CASCADE)
    level    = models.CharField(max_length=8, verbose_name='level', choices=LEVEL_CHOICE)
    score    = models.PositiveIntegerField(default=0)
    created  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.Player.username}: {self.score} points."

    def finalScore(self):
        self.score
        for x in self.player.quizzes:
            self.score += x.quiz_value()
        return self.score


class Archive(models.Model):
    content_type   = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id      = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    archived_at    = models.DateTimeField(auto_now_add=True)
    archived_by    = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        # Archive(content_object=Object)
        return f"Archived {self.content_type.name} at {self.archived_at} by {self.archived_by}."
