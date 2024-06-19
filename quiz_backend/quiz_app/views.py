from django.contrib.auth             import authenticate, login, logout
from django.http                     import HttpResponse, JsonResponse
from django.views.decorators.csrf    import csrf_exempt,csrf_protect
from rest_framework.parsers          import JSONParser
from rest_framework.response         import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models      import User
from .serializers                    import *
from .models                         import *

# Create your views here.
@csrf_protect
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            if created:
                return JsonResponse({'token': token.key})
        else:
            return JsonResponse({'message': 'Invalid email or password'}, status=401)
    return JsonResponse({'message': 'HTTP method not allowed'}, status=405)

@csrf_protect
def log_out(request):
    logout(request)
    return Response({'message': 'Déconnexion réussie'}, status=200)

@csrf_exempt
def userList(request):
    """
    List all objects of User, or create a new User.
    """
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            token, created = Token.objects.get_or_create(user=serializer.instance)
            data = {
                'user': serializer.data,
                'token': token.key
            }
            return JsonResponse(data, status=201)
            # return JsonResponse(serializer.data, {'token': token.key}, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def userDetail(request, pk):
    """
    Retrieve, update or delete a User
    """
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        archive = Archive(content_object=user, archived_by=request.user)
        archive.save()
        user.delete()
        return HttpResponse(status=204)

@csrf_exempt
def categoryList(request):
    """
    List all objects of Category, or create a new Category.
    """
    if request.method == 'GET':
        categories = Category.objects.order_by('creator').all()
        serializer = CategorySerializer(categories, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def categoryDetail(request, pk):
    """
    Retrieve, update or delete a Category
    """
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CategorySerializer(category, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        archive = Archive(content_object=category, archived_by=request.user)
        archive.save()
        category.delete()
        return HttpResponse(status=204)

@csrf_exempt
def QuizList(request):
    """
    List all objects of Quiz, or create a new Quiz.
    """
    if request.method == 'GET':
        quizzes = Quiz.objects.filter(creator=request.user).all()
        serializer = QuizSerializer(quizzes, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = QuizSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def QuizDetail(request, pk):
    """
    Retrieve, update or delete a Quiz
    """
    try:
        quiz = Quiz.objects.get(pk=pk)
    except Category.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = QuizSerializer(quiz)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = QuizSerializer(quiz, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        archive = Archive(content_object=quiz, archived_by=request.user)
        archive.save()
        quiz.delete()
        return HttpResponse(status=204)

@csrf_exempt
def ScoreList(request):
    """
    List all objects of Score, or create a new Score.
    """
    if request.method == 'GET':
        player = Player.objects.get(user=request.user)
        scores = Score.objects.filter(player=player).order_by('level').all()
        serializer = ScoreSerializer(scores, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ScoreSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def ScoreDetail(request, pk):
    """
    Retrieve, update or delete a Score
    """
    try:
        score = Score.objects.get(pk=pk)
    except Category.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ScoreSerializer(score)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ScoreSerializer(score, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        archive = Archive(content_object=score, archived_by=request.user)
        archive.save()
        score.delete()
        return HttpResponse(status=204)

@csrf_exempt
def PlayerList(request):
    """
    List all objects of Player, or create a new Player.
    """
    if request.method == 'GET':
        players = Player.objects.filter(user=request.user).all()
        serializer = ScoreSerializer(players, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ScoreSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def PlayerDetail(request, pk):
    """
    Retrieve, update or delete a Player
    """
    try:
        player = Player.objects.get(pk=pk)
    except Player.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PlayerSerialiser(player)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PlayerSerialiser(player, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        archive = Archive(content_object=player, archived_by=request.user)
        archive.save()
        player.delete()
        return HttpResponse(status=204)


@csrf_exempt
def ArchiveList(request):
    """
    List all objects of Archive, or create a new Archive.
    """
    if request.method == 'GET':
        archive = Archive.objects.all()
        serializer = ScoreSerializer(archive, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ScoreSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
