import random
from math_quiz import math_quiz


def function_A(min, max):
    """
    Random integer.
    """
    return random.randint(min, max)


def function_B():
    return random.choice(['+', '-', '*'])


def function_C(num1, num2, o):
    ques = f"{num1} {o} {num2}" 
    if o == '+': 
      ans = num1 + num2 #changes the operaor
    elif o == '-':
      ans = num1 - num2 #changes the operaor
    else:
      ans = num1 * num2
    return ques, ans

def math_quiz():
    score = 0
    total_ques = 3 #changes number type.because we need intiger here

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_ques):
        num1 = function_A(1, 10);
        num2 = function_A(1, 5); #again made int as we have used randint
        operator = function_B()

        prob ,ans = function_C(num1, num2, operator)
        print(f"\nQuestion: {prob}")
        try:
          useranswer = int(input("Your answer: "))

        except ValueError:
          print('Not Valid Input : ')
          continue

        if useranswer == ans:
            print("Correct! You earned a point.")
            score += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ans}.")

    print(f"\nGame over! Your score is: {score}/{total_ques}")

if __name__ == "__main__":
    math_quiz()
