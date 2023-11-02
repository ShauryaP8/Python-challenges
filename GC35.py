class User:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.questions = {}

    def add_question(self, question, answer):
        self.questions[question] = answer

    def quiz_user(self, other_user):
        print(f"\n{self.name}, it's your turn to ask questions to {other_user.name}.")
        print(f"{other_user.name}, please answer each question with a single word.\n")
        for question, answer in self.questions.items():
            user_answer = input(question + " ")
            if user_answer.lower() == answer.lower():
                print("Correct!")
                self.score += 1
            else:
                print("Incorrect!")

    def get_score(self):
        return self.score


def main():
    num_users = int(input("Enter the number of users: "))
    users = []

    for i in range(num_users):
        name = input(f"Enter the name of user {i+1}: ")
        user = User(name)
        users.append(user)

    print("\n--- Question Creation ---")
    for user in users:
        print(f"\n{user.name}, it's your turn to create a question about yourself.")
        question = input("Enter the question: ")
        answer = input("Enter the answer: ")
        user.add_question(question, answer)

    print("\n--- Quiz Time ---")

    for i in range(num_users - 1):
        quizzer = users[i]
        quizzer.quiz_user(users[i+1])

    print("\n--- Final Scores ---")
    for user in users:
        print(f"{user.name}: {user.get_score()} points")


if __name__ == '__main__':
    main()