from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, render_to_response, redirect
from django.views import generic
from trivia.models import Question, MyUser
from django import forms
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.contrib.auth.models import User

# Create your views here.

#You have to pass all variables in your view to the template using
#the dictionary in the render call. 

class AnswerForm(forms.Form):
	answer = forms.CharField(label = 'answer ', max_length = 150)

def dailyview(request):
	if not request.user.is_authenticated():
		return redirect('/trivia/')

	date = timezone.now().date()
	q = get_object_or_404(Question, pk=date)
	q_text = q.question_text
	if request.method == 'POST':
		form = AnswerForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('results.html')
		else:
			form = AnswerForm()
	else:
		form = AnswerForm()
	return render(request, 'dailyquestion.html', {'date': date, 'question_text': q_text, 'form': form})

def resultsview(request, answer, question):
	flag = False
	if answer == question.answer_text:
		flag = True

	#if flag == True:
		#request.user.
	return render(request, 'results.html', {'flag': flag})

class leaderview(generic.ListView):

	model = MyUser
	template_name = "leaderboard.html"
	context_object_name = 'user_list'

	def get_queryset(self):
		if not self.request.user.is_authenticated():
			return redirect('/trivia/')
		"""Return the last five published questions."""
		return MyUser.objects.order_by('-num_total')

def profileview(request, userid):
	model = MyUser
	template_name = "profile.html"
	context_object_name = 'user'
	user = get_object_or_404(MyUser, pk=userid)
	return render(request, 'profile.html', {'user': user})

def user_login(request):
	context = RequestContext(request)

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/trivia/daily/')
			else:
				return HttpResponse("Your account does not exist. Please sign up")
		else:
			print "Invalid login details: {0}, {1}".format(username, password)
			return HttpResponse("Invalid login details supplied")
	else:
		return render_to_response('login.html', {}, context)

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password')

def register(request):
	context = RequestContext(request)

	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)

		if user_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			registered = True
		else:
			print user_form.errors
	else:
		user_form = UserForm()

	return render_to_response('signup.html', {'user_form': user_form, 'registered': registered}, context)
