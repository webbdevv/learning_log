from django import forms

from .models import Topic, Entry #Use existing information about forms to create this form

class TopicForm(forms.ModelForm):
	class Meta:
		model = Topic
		fields = ['text']	#only a text field
		labels = {'text': ''}	#No label for the text field
		
class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ['text']
		labels = {'text': 'Entry'}
		widgets = {'text': forms.Textarea(attrs={'cols': 80})}