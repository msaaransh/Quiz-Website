from django.contrib import admin
from django.contrib.admin import AdminSite

class CustomAdminSite(AdminSite):
    def get_app_list(self, request):
        app_list = super().get_app_list(request)

        # Reorder models within the specified app (e.g., 'quiz')
        for app in app_list:
            if app['app_label'] == 'MainApp':  # Replace 'quiz' with your app label
                # Custom ordering of models within the 'quiz' app
                app['models'].sort(key=lambda x: ['Category','Participant','Quiz','QuizQuestion','QuizAttempt', 'QuizQuestionsAttempt'].index(x['object_name']))

        return app_list

# Instantiate the custom admin site
custom_admin_site = CustomAdminSite(name='custom_admin')

from MainApp.models import Quiz, Category, Participant,QuizQuestion,QuizAttempt,QuizQuestionsAttempt  # Import models
from .custom_admin import custom_admin_site

custom_admin_site.register(Category)
custom_admin_site.register(Participant)
custom_admin_site.register(Quiz)
custom_admin_site.register(QuizQuestion)
custom_admin_site.register(QuizAttempt)
custom_admin_site.register(QuizQuestionsAttempt)