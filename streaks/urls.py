from django.urls import path
from . import views

urlpatterns = [
    path('invalidate/', views.invoke_streak_cron),
    path('health/', views.streak_health)
]
