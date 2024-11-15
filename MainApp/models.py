
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

class LogMessage(models.Model):
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"

class Category(models.Model):
    name = models.CharField(max_length=100)
    correct_marks = models.IntegerField()
    incorrect_marks = models.IntegerField()
    difficulty_level = models.IntegerField(blank=True)

    def __str__(self):
        return self.name
    class Meta :
        verbose_name_plural = "Categories"
    
class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=40)
    image = models.ImageField(blank=True)
    attempted_quiz = models.IntegerField(null=True,blank=True)
    created_quiz = models.IntegerField(null=True,blank=True)
    last_login_date = models.DateField(blank=True,null=True)
    rank = models.IntegerField(blank=True,null=True)
    age = models.IntegerField(blank=True,null=True)
    gender = models.CharField(max_length=1,blank=True,null=True)

    def __str__(self):
        return self.name
    
class Quiz(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by_admin = models.BooleanField(blank=True,null=True)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE,blank=True,null=True)
    max_marks = models.IntegerField()
    max_time = models.IntegerField()
    num_questions = models.IntegerField()

    def __str__(self):
        return self.title
    class Meta :
        verbose_name_plural = "Quizzes"
    
class QuizQuestion(models.Model):
    
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    title = models.CharField(max_length=100)
    question_text = models.CharField(max_length=500)
    option1_text = models.CharField(max_length=500)
    option2_text = models.CharField(max_length=500)
    option3_text = models.CharField(max_length=500)
    option4_text = models.CharField(max_length=500)
    correct_option = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)])

    def __str__(self):
        return self.title
    
class QuizAttempt(models.Model):
    
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='attempts')
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField()
    attempted_questions = models.IntegerField()
    final_score = models.IntegerField()
    quiz_rank = models.IntegerField()

    def __str__(self):
        return f"Quiz {self.quiz} attempted by {self.participant} at {self.started_at} "
    
class QuizQuestionsAttempt(models.Model):
    
    quiz_attempt = models.ForeignKey(QuizAttempt, on_delete=models.CASCADE, related_name='answers')
    quiz_question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE, related_name='questions')
    option_selected = models.IntegerField()
    is_correct = models.BooleanField()
    marks = models.IntegerField()

    def __str__(self):
        return f"Question {self.quiz_question} attempted by {self.quiz_attempt.participant} "