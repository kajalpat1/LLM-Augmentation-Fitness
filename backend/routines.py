def generate_routine(goal, fitness_level):
    base_plan = {
        "beginner":    ["Jumping Jacks", "Bodyweight Squats", "Wall Sit", "Plank"],
        "intermediate": ["Push-ups", "Lunges", "Mountain Climbers", "Bicycle Crunches"],
        "advanced":    ["Burpees", "Pull-ups", "Deadlifts", "Barbell Squats"]
    }
    goal_map = {
        "weight loss": ["HIT", "Cardio", "Bodyweight Circuits"],
        "muscle gain": ["Strength Training", "Progressive Overload", "Split Routines"],
        "endurance":   ["Steady-state Cardio", "Tempo Runs", "Core Circuits"]
    }

    return {
        "goal": goal,
        "level": fitness_level,
        "recommendations": goal_map.get(goal.lower(), []) +
                           base_plan.get(fitness_level.lower(), [])
    }
