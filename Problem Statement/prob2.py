def analyze_paragraphs(p1, p2):
    # Split paragraphs into words (case-insensitive)
    words1 = set(word.lower() for word in p1.split())
    words2 = set(word.lower() for word in p2.split())

    # a) Unique words in each paragraph
    unique1 = words1 - words2
    unique2 = words2 - words1

    # b) Common words between both paragraphs
    common = words1 & words2

    print("Unique words in Paragraph 1:")
    print(unique1)
    print("Unique words in Paragraph 2:")
    print(unique2)
    print("Common words in both paragraphs:")
    print(common)
    print("All unique words found in both paragraphs:")
    print(words1 | words2)


if __name__ == "__main__":
    print("Enter Paragraph 1:")
    p1 = input()
    print("Enter Paragraph 2:")
    p2 = input()
    analyze_paragraphs(p1, p2)
