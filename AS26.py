def calculate_average_word_length(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            words = text.split()  # Split the text into words based on spaces

            # Remove punctuation from words (optional)
            words = [word.strip(".,!?\"'-()[]{}<>:;") for word in words]

            total_word_length = sum(len(word) for word in words)
            num_words = len(words)

            if num_words == 0:
                print("The file is empty or contains no words.")
            else:
                average_length = total_word_length / num_words
                return average_length

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return None

# Example usage:
file_path = 'sample_text.txt'  # Replace with the path to your text file
average_length = calculate_average_word_length(file_path)

if average_length is not None:
    print(f"The average word length in the text is: {average_length:.2f} characters")
