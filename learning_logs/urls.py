"""Defines URL patterns for learning_logs."""
from django.urls import path

from . import views

#Helps distinguish urls.py from the other urls.py that exist within the project
app_name = 'learning_logs'


urlpatterns =[
	#Home page
	path('', views.index, name='index'), #calls the index function from views file, third argument replaces url name with index
	path('topics/', views.topics, name='topics'),
	# Detail page for a single topic.
	path('topics/<int:topic_id>/', views.topic, name='topic'),
	# Page for adding a new topic
	path('new_topic/', views.new_topic, name='new_topic'),
	path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
	#Page for editing an entry
	path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]