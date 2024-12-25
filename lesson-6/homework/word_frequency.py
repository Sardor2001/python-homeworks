import string
from collections import Counter


# Function to read the file and count word frequency
def count_word_frequency():
    # Check if "sample.txt" exists
    try:
        with open("sample.txt", "r") as file:
            text = file.read()
    except FileNotFoundError:
        print("File 'sample.txt' not found.")
        # If the file does not exist, prompt the user to create one
        text = input("File not found. Please type a paragraph to create the file: ")
        with open("sample.txt", "w") as file:
            file.write(text)

    # Remove punctuation and convert text to lowercase
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Split the text into individual words
    words = text.split()

    # Count word frequencies using Counter
    word_count = Counter(words)

    # Total words in the file
    total_words = len(words)

    # Top 5 most common words
    top_5_words = word_count.most_common(5)

    # Display the output
    print(f"Total words: {total_words}")
    print("Top 5 most common words:")
    for word, count in top_5_words:
        print(f"{word} - {count} times")

    # Save the report to "word_count_report.txt"
    with open("word_count_report.txt", "w") as report_file:
        report_file.write("Word Count Report\n")
        report_file.write(f"Total Words: {total_words}\n")
        report_file.write("Top 5 Words:\n")
        for word, count in top_5_words:
            report_file.write(f"{word} - {count}\n")


# Main program
if __name__ == "__main__":
    count_word_frequency()
