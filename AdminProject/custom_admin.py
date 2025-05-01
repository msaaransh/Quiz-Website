from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.admin import SimpleListFilter

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

class RankFilter(SimpleListFilter):
    title = 'Overall Rank'  # Displayed title in the filter
    parameter_name = 'rank'  # URL parameter name

    def lookups(self, request, model_admin):
        return [
            ('high', 'Below 50'),
            ('medium', '50-100'),
            ('low', 'Above 100'),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'high':
            return queryset.filter(rank__lt=50)
        if self.value() == 'medium':
            return queryset.filter(rank__gte=50, rank__lte=100)
        if self.value() == 'low':
            return queryset.filter(rank__gt=100)


class CategoryAdmin(admin.ModelAdmin):
    # Display relevant columns in the admin list view
    list_display = ('name', 'correct_marks', 'incorrect_marks', 'difficulty_level')

class ParticipantAdmin(admin.ModelAdmin):
    # Display relevant columns in the admin list view
    list_display = ('name', 'email', 'attempted_quiz', 'created_quiz', 'last_login_date', 'rank', 'age','gender','image')
    list_filter = (RankFilter,'gender',)

class QuizAdmin(admin.ModelAdmin):
    # Display relevant columns in the admin list view
    list_display = ('title', 'category', 'created_on', 'max_marks')
    
    # Add filters to the admin panel
    list_filter = ('category','created_by_admin',)  # This adds a filter sidebar for 'category'

class QuizQuestionAdmin(admin.ModelAdmin):
    # Display relevant columns in the admin list view
    list_display = ('title', 'quiz')
    
    # Add filters to the admin panel
    list_filter = ('quiz',)  

class QuizAttemptAdmin(admin.ModelAdmin):
    # Display relevant columns in the admin list view
    list_display = ('participant', 'quiz', 'started_at','finished_at','attempted_questions','final_score','quiz_rank')
    
    # Add filters to the admin panel
    list_filter = ('quiz','participant',)  # This adds a filter sidebar for 'Quiz'

class QuizQuestionAttemptAdmin(admin.ModelAdmin):
    # Display relevant columns in the admin list view
    list_display = ('quiz_attempt', 'quiz_question', 'option_selected','is_correct','marks')
    
    # Add filters to the admin panel
    list_filter = ('quiz_attempt', 'quiz_question',)  

custom_admin_site.register(Category,CategoryAdmin)
custom_admin_site.register(Participant,ParticipantAdmin)
custom_admin_site.register(Quiz,QuizAdmin)
custom_admin_site.register(QuizQuestion,QuizQuestionAdmin)
custom_admin_site.register(QuizAttempt,QuizAttemptAdmin)
custom_admin_site.register(QuizQuestionsAttempt,QuizQuestionAttemptAdmin)