def text_analysis(text):
    # a) Count total number of words
    words = text.split()
    total_words = len(words)

    # b) Count total number of spaces
    total_spaces = text.count(' ')

    # c) Count frequency of each word (case-insensitive)
    from collections import Counter
    word_freq = Counter(word.lower() for word in words)

    # d) Top 3 most frequent words
    top3 = word_freq.most_common(3)

    # e) Count number of vowels in entire text
    vowels = 'aeiouAEIOU'
    vowel_count = sum(1 for char in text if char in vowels)

    # f) Sort the string with conversion to reverse ascending order
    sorted_str = ''.join(sorted(text, reverse=True))

    print(f"Total number of words: {total_words}")
    print(f"Total number of spaces: {total_spaces}")
    print("Frequency of each word:")
    for word, freq in word_freq.items():
        print(f"  {word}: {freq}")
    print("Top 3 most frequent words:")
    for word, freq in top3:
        print(f"  {word}: {freq}")
    print(f"Number of vowels: {vowel_count}")
    print(f"Sorted string in reverse ascending order: {sorted_str}")


if __name__ == "__main__":
    text = input("Enter the text to analyze: ")
    text_analysis(text)
