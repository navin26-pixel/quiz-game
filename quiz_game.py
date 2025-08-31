"""
Cosmic Quiz Adventure
---------------------
An interactive space-themed quiz game with multiple difficulty levels,
power-ups, and a scoring system that rewards speed and accuracy.
"""

import time
import random

# Question database with multiple difficulty levels
questions = {
    "easy": [
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["A) Earth", "B Jupiter", "C) Saturn", "D) Mars"],
            "answer": "B",
            "type": "multiple_choice"
        },
        {
            "question": "A light-year measures ___",
            "options": ["A) Time", "B) Distance", "C) Brightness", "D) Energy"],
            "answer": "B",
            "type": "multiple_choice"
        }
    ],
    "medium": [
        {
            "question": "What is the approximate speed of light in vacuum?",
            "options": ["A) 299,792 km/s", "B) 150,000 km/s", "C) 450,000 km/s", "D) 100,000 km/s"],
            "answer": "A",
            "type": "multiple_choice"
        }
    ],
    "hard": [
        {
            "question": "Which scientist first proposed the uncertainty principle?",
            "options": ["A) Einstein", "B) Bohr", "C) Heisenberg", "D) Schrödinger"],
            "answer": "C",
            "type": "multiple_choice"
        }
    ]
}

# Power-ups that players can earn
power_ups = {
    "time_freezer": "Adds 15 seconds to your timer",
    "double_points": "Next correct answer worth 2x points",
    "skip": "Skip a challenging question"
}

def display_welcome():
    """Display a stylish welcome message"""
    print("✨" * 40)
    print("           COSMIC QUIZ ADVENTURE")
    print("✨" * 40)
    print("\nEmbark on an interstellar journey of knowledge!")
    print("Answer questions correctly to earn stardust points")
    print("Discover power-ups and climb the leaderboard\n")
    print("Power-ups available:")
    for up, desc in power_ups.items():
        print(f"   {up.replace('_', ' ').title()}: {desc}")

def select_difficulty():
    """Let player select difficulty level"""
    print("\nSelect difficulty:")
    print("1. Easy (Beginner Cosmonaut)")
    print("2. Medium (Space Explorer)")
    print("3. Hard (Astrophysics Expert)")
    
    while True:
        choice = input("Enter choice (1-3): ")
        if choice == "1":
            return "easy"
        elif choice == "2":
            return "medium"
        elif choice == "3":
            return "hard"
        else:
            print("Please enter a valid option (1-3)")

def ask_question(question_data):
    """Display question and get user answer"""
    print(f"\n{question_data['question']}")
    
    if question_data['type'] == "multiple_choice":
        for option in question_data['options']:
            print(f"   {option}")
    
    start_time = time.time()
    answer = input("\nYour answer (or type 'quit', 'hint', or 'power-up'): ")
    answer_time = time.time() - start_time
    
    return answer, answer_time

def check_answer(question_data, user_answer, score, answer_time):
    """Check if answer is correct and calculate score"""
    correct_answer = question_data['answer']
    
    if user_answer.upper() == correct_answer:
        # Base points + time bonus (faster answers worth more)
        time_bonus = max(0, 10 - int(answer_time))
        points_earned = 10 + time_bonus
        new_score = score + points_earned
        
        print(f"✓ Correct! Time bonus: +{time_bonus} points")
        print(f"✓ Total earned: {points_earned} stardust")
        return new_score, True
    else:
        print(f"✗ Incorrect. The correct answer was {correct_answer}")
        return score, False

def offer_hint(question_data):
    """Provide a hint for the current question"""
    if question_data['type'] == "multiple_choice":
        correct_option = question_data['answer']
        print(f"Hint: The correct answer starts with '{correct_option}'")
    else:
        print("Sorry, no hints available for this question type")

def main():
    """Main game function"""
    display_welcome()
    
    # Game loop
    while True:
        difficulty = select_difficulty()
        score = 0
        questions_asked = 0
        active_power_ups = []
        
        # Get questions for selected difficulty
        level_questions = questions[difficulty]
        random.shuffle(level_questions)  # Randomize question order
        
        for question in level_questions:
            questions_asked += 1
            
            # Ask question and get response
            user_answer, answer_time = ask_question(question)
            
            # Process special commands
            if user_answer.lower() == 'quit':
                print("Thanks for playing!")
                return
            elif user_answer.lower() == 'hint':
                offer_hint(question)
                user_answer, answer_time = ask_question(question)
            elif user_answer.lower() == 'power-up':
                if active_power_ups:
                    print(f"Active power-ups: {', '.join(active_power_ups)}")
                else:
                    print("You don't have any power-ups yet!")
                continue
            
            # Check answer and update score
            score, was_correct = check_answer(question, user_answer, score, answer_time)
            
            # Random power-up chance (20%) after correct answers
            if was_correct and random.random() < 0.2:
                power_up = random.choice(list(power_ups.keys()))
                active_power_ups.append(power_up)
                print(f"🎉 You earned a {power_up.replace('_', ' ')} power-up!")
        
        # End of round
        print(f"\n⭐ Round complete! Your final score: {score} stardust")
        print(f"📊 Questions answered: {questions_asked}")
        
        # Ask to play again
        play_again = input("\nWould you like to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            print("Thanks for playing Cosmic Quiz Adventure! 🚀")
            break

if __name__ == "__main__":
    main()