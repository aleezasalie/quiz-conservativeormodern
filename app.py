# Quiz Questions and options
questions = [
    ("Which word best describes you?", "A) Reserved", "B) Bold"),
    ("You have a day off, how do you spend it?", "A) At home with your family", "B) Going out to the movies (cinema)"),
    ("You're offered a job, it's a HUGE upgrade and pays way more. What do you do?", 
        "A) Stay at home, I'd rather remain within my comfort zone", 
        "B) Take the job, it's a good way to develop my skills"),
    ("In general, do you care what people think and are you committed to upholding societal expectations even at the expense of your own ambitions?", 
        "A) Yes", 
        "B) No"),
    ("You're offered two books. Which do you pick?", 
        "A) The classic novel, appreciating its timelessness", 
        "B) The new bestseller, curious about current ideas"),
    ("You’ve recently come into a small sum of money. What do you decide?", 
        "A) Save the money for the future", 
        "B) Spend it on something enjoyable now"),
    ("You have the opportunity to refurnish your house. Which do you choose?", 
        "A) The classic furniture, valuing its quality", 
        "B) The latest trends, excited for a fresh look"),
    ("You've been invited to two different events. Which do you choose?", 
        "A) The small gathering at a friend's house", 
        "B) The lively evening at a new venue")
]

# Variables to track user choices
a_count = 0
b_count = 0

# Function to run the quiz
def run_quiz():
    global a_count, b_count

    for i, question in enumerate(questions):
        print(f"Question {i + 1}: {question[0]}")
        print(question[1])
        print(question[2])

        # Continuously prompt the user until a valid response is given
        while True:
            answer = input("Your choice (A/B): ").upper()

            if answer == 'A':
                a_count += 1
                break
            elif answer == 'B':
                b_count += 1
                break
            else:
                print("Invalid choice, please choose A or B.")  # Prompt the user again

        print()  # Add a space after each question

    # Determine and display result
    if a_count > b_count:
        print("You are more conservative and traditional in your views.")
        print(
            "As someone who leans towards conservative views, you likely value stability, tradition, and the preservation of established norms. "
            "You appreciate the timelessness of classic approaches and prefer to maintain a sense of continuity with the past. Your decisions are often guided by a strong sense of duty and respect for societal expectations. "
            "You find comfort in familiar routines and are cautious about embracing rapid changes. Your approach to life reflects a commitment to preserving the integrity of long-standing values and practices, often favoring a thoughtful and measured approach over bold innovation."
        )
    elif b_count > a_count:
        print("You are more modern and progressive in your views.")
        print(
            "As someone with modern views, you are open to change and embrace new ideas and perspectives. "
            "You are curious about contemporary trends and enjoy exploring innovative approaches in various aspects of life. Your decisions reflect a desire to break away from traditional constraints and adopt a more flexible and progressive outlook. "
            "You are likely to be excited by new experiences and eager to stay updated with the latest developments, valuing the dynamism and possibilities that come with a modern approach."
        )
    else:
        print("You have a balanced mix of traditional and modern views.")
        print(
            "You embody a harmonious blend of both traditional and modern perspectives. "
            "You appreciate the value of historical norms and practices while remaining open to contemporary ideas and innovations. This balanced approach allows you to navigate various situations with a nuanced perspective, integrating the best of both worlds. "
            "You respect time-honored values but are also adaptable, recognizing the importance of staying current and flexible. Your approach to life reflects a thoughtful consideration of both past and present, enabling you to appreciate and integrate diverse viewpoints."
        )

# Run the quiz
run_quiz()
