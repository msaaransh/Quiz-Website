from django.contrib import admin

# Register your models here.
from .models import LogMessage
from .models import Category
from .models import Participant
from .models import Quiz
from .models import QuizAttempt
from .models import QuizQuestion
from .models import QuizQuestionsAttempt

admin.site.register(LogMessage)
admin.site.register(Category)
admin.site.register(Participant)
admin.site.register(Quiz)
admin.site.register(QuizAttempt)
admin.site.register(QuizQuestion)
admin.site.register(QuizQuestionsAttempt)