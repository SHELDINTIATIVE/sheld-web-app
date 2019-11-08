from django.shortcuts import render
from django.views.generic import (
	ListView,
	DetailView,
	)

from . models import Event


class EventListView(ListView):
	model = Event
	context_page_name = 'events'
	paginate_by = 6
	template_name = 'events/event_list.html'


class EventDetailView(DetailView):
	model = Event
	context_page_name = 'event'
	template_name = 'events/event_detail.html'