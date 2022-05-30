from django.shortcuts import render
from .models import Question
# Create your views here.
arr = []
ansArr = []
answers = Question.objects.all()

def home(request):
	return render(request,'home.html')

def exam(request):
	obj = Question.objects.all()
	return render(request,'exam.html',{'obj':obj})

def result(request,pk):
	score = 0
	for j in range(len(arr)):
		if arr[j] == ansArr[j]:
			score += 1
	return render(request, 'result.html',{"score":score})

	user = get_object_or_404(Choice, pk=pk)
	users = Choice.objects.all()
	scrArr = []
	for i in users:
		scores = i.correct
		scrArr.append(scores)
	avgScr = round(sum(scrArr)/len(users))
	return render(request, "result.html", {"user":user, 'avgScr':avgScr})