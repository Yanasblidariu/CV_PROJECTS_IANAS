from django.db import models

class WorkoutPlan(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Exercises(models.Model):
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    muscle_group = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class NutritionPlan(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    meals = models.TextField()

    def __str__(self):
        return self.title

class Diet(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    calories = models.IntegerField()
    proteins = models.DecimalField(max_digits=5, decimal_places=2)
    carbs = models.DecimalField(max_digits=5, decimal_places=2)
    fats = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

class ExercisesDiet(models.Model):
    exercise = models.ForeignKey(Exercises, on_delete=models.CASCADE)
    diet = models.ForeignKey(Diet, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.exercise.name} - {self.diet.name}"

class Feedback(models.Model):
    message = models.TextField()
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback - {self.date_submitted}"
    