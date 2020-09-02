#views generates the views for each of the pages connected to the website

from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic, Entry

from .forms import TopicForm, EntryForm
# Create your views here.

def index(request):
	"""Home page for Learning Log"""
	return render(request, 'learning_logs/index.html')

@login_required #need to update settings so that Django knows where to find the login
def topics(request):
	"""Show all topics."""
	#2 The request object Django recieved from the server. 
	topics = Topic.objects.filter(owner=request.user).order_by('date_added') #Shows users only the topics that belong to them
	context = {'topics': topics}
	return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
	"""Show a single topic and all its entries."""
	topic = Topic.objects.get(id=topic_id) #use get function to retrieve the id
	#Ensure that topic belongs to the current user.
	if topic.owner != request.user:
		raise Http404

	entries = topic.entry_set.order_by('-date_added') #Get entries associated with the topic and order them according to date_added, reverse order
	context = {'topic': topic, 'entries': entries}	#store these in a context dictionary and return to topic.html
	return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
	"""Add a new topic."""
	if request.method != 'POST':
		#No data submitted; create a blank form
		form = TopicForm()
	else:
		#POST data submitted: process data
		form = TopicForm(data=request.POST)
		if form.is_valid():
			new_topic = form.save(commit=False)
			new_topic.owner = request.user
			new_topic.save()
			return redirect('learning_logs:topics') #Redirects to the topics view

	#Display a blank or invalid form
	context = {'form': form}
	return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
	"""Add a new entry for a particular topic."""
	topic = Topic.objects.get(id=topic_id)
	if request.method != 'POST':
		# No data submitted; create a blank form. 
		form = EntryForm()
	else:
		# POST data submitted; process data
		form = EntryForm(data=request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.topic = topic
			new_entry.save()
			return redirect('learning_logs:topic', topic_id=topic_id)

	# Display a blank or invalid form.
	context = {'topic': topic, 'form': form}
	return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
	"""Edit an existing entry."""
	entry = Entry.objects.get(id=entry_id)
	topic = entry.topic
	if topic.owner != request.user:
		raise Http404

	if request.method != 'POST':
		form = EntryForm(instance=entry)
	else:
		#POST data submitted: process
		form = EntryForm(instance=entry, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('learning_logs:topic', topic_id=topic.id)

	context = {'entry': entry, 'topic': topic, 'form': form}
	return render(request, 'learning_logs/edit_entry.html', context)

