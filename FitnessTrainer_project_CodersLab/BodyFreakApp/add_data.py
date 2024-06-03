from BodyFreakApp.models import WorkoutPlan, NutritionPlan, Feedback,Diet,Exercises

beginner_workout_plan = WorkoutPlan.objects.create(
    title='Beginner Workout Plan',
    description='This workout plan is designed for beginners who are just starting their fitness journey. It focuses on basic exercises to build strength and endurance.'
)

intermediate_workout_plan = WorkoutPlan.objects.create(
    title='Intermediate Workout Plan',
    description='The intermediate workout plan is suitable for those who have some experience with exercise and want to challenge themselves further. It includes a combination of strength training and cardio exercises.'
)

advanced_workout_plan = WorkoutPlan.objects.create(
    title='Advanced Workout Plan',
    description='The advanced workout plan is for experienced individuals looking to push their limits and achieve peak fitness. It incorporates high-intensity interval training (HIIT), advanced strength exercises, and endurance challenges.'
)

weight_loss_nutrition_plan = NutritionPlan.objects.create(
    title='Weight Loss Nutrition Plan',
    description='This nutrition plan is designed to help individuals lose weight by providing balanced meals with controlled calorie intake. It includes a variety of healthy foods to support weight loss goals.',
    meals='Breakfast: Whole grain cereal with skim milk\nLunch: Grilled chicken salad\nDinner: Baked salmon with steamed vegetables',
)

muscle_gain_nutrition_plan = NutritionPlan.objects.create(
    title='Muscle Gain Nutrition Plan',
    description='The muscle gain nutrition plan is tailored for individuals looking to build lean muscle mass and strength. It includes high-protein meals to support muscle recovery and growth.',
    meals='Breakfast: Protein pancakes with Greek yogurt\nLunch: Grilled steak with quinoa and roasted vegetables\nDinner: Chicken breast with sweet potato and broccoli',
)


feedback1 = Feedback.objects.create(
    message='Great workout plan for beginners! I saw results after just a few weeks of following this routine.',
)

feedback2 = Feedback.objects.create(
    message='The weight loss nutrition plan helped me achieve my goals faster than I expected. The meals were delicious and easy to prepare.',
)

feedback3 = Feedback.objects.create(
    message='Ive been following the advanced workout plan for a few months now, and I can definitely feel myself getting stronger and more fit. Highly recommend it for anyone looking to challenge themselves.',
)

beginner_exercise = Exercises.objects.create(
    name='Push-up',
    description='Push-ups are a classic bodyweight exercise that targets the chest, shoulders, and triceps.',
    muscle_group='Chest, Shoulders, Triceps'
)

intermediate_exercise = Exercises.objects.create(
    name='Squats',
    description='Squats are a compound exercise that targets the quadriceps, hamstrings, glutes, and lower back.',
    muscle_group='Quadriceps, Hamstrings, Glutes, Lower Back'
)

advanced_exercise = Exercises.objects.create(
    name='Deadlift',
    description='The deadlift is a complex lift that targets multiple muscle groups, including the hamstrings, glutes, lower back, and traps.',
    muscle_group='Hamstrings, Glutes, Lower Back, Traps'
)

weight_loss_diet = Diet.objects.create(
    name='Low-Calorie Diet',
    description='The low-calorie diet is designed to create a calorie deficit for weight loss. It focuses on reducing calorie intake while still providing essential nutrients.',
    calories=1500,
    proteins=100,
    carbs=200,
    fats=50
)

muscle_gain_diet = Diet.objects.create(
    name='High-Protein Diet',
    description='The high-protein diet is ideal for muscle gain and recovery. It provides ample protein to support muscle growth while controlling carbohydrate and fat intake.',
    calories=2500,
    proteins=150,
    carbs=300,
    fats=80
)
