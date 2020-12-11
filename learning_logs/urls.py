"""Defines URL patterns for learning_logs."""

# path function helps map URLs to views
from django.urls import path

from . import views
 
app_name = 'learning_logs' # distinguish this urls.py
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all topics.
    path('topics/', views.topics, name='topics'),
    # Detail page for a single topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding a new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page for editing an entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]

# path (1,2,3)
# 1 - string that routes current request properly, '' matches base URL
# 2 - specifies which function to call in views.py
# 3 - name index for URL pattern to refer in other code sections