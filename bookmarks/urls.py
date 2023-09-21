from django.urls import path
from bookmarks import views

urlpatterns = [
    path('likes/', views.BookmarkList.as_view()),
]
