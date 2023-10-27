def calculate_parity_bit(binary_number):
    count_ones = binary_number.count('1')

    # If the count of ones is even, return '0' for even parity
    if count_ones % 2 == 0:
        return '0'
    else:
        return '1'

def check_answer(binary_number, answer):
    parity_bit = calculate_parity_bit(binary_number)
    
    if parity_bit == answer:
        return True
    else:
        return False

# Quiz Questions
questions = [
    {
        'question': "Determine the parity bit for the following 8-bit binary number: 10101010",
        'options': ["Odd parity bit", "Even parity bit", "No parity bit"],
        'answer': "Even parity bit"
    },
    {
        'question': "Identify whether the following 9-bit binary number has odd or even parity: 110111001",
        'options': ["Odd parity", "Even parity"],
        'answer': "Odd parity"
    },
    {
        'question': "Find the missing bit to make the following 7-bit binary number have even parity: 110010_",
        'options': ["1", "0"],
        'answer': "1"
    },
    {
        'question': "Determine if the following 6-bit binary number has odd or even parity: 101101",
        'options': ["Odd parity", "Even parity"],
        'answer': "Odd parity"
    },
    {
        'question': "Find the missing bit to ensure the following 8-bit binary number has odd parity: 110011__",
        'options': ["0", "1"],
        'answer': "1"
    }
]

# Quiz Execution
for i, question in enumerate(questions):
    print(f"Question {i+1}: {question['question']}")
    for j, option in enumerate(question['options']):
        print(f"{chr(ord('A')+j)}) {option}")
    
    # Take user's answer
    user_answer = input("Your answer (A, B, C ): ")
    
    # Check if the answer is correct
    if check_answer(question['answer'], user_answer):
        print("Correct!\n")
    else:
        print(f"Wrong Answer. The correct answer is {question['answer']}.\n")