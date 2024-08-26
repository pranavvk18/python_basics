questions = [
    [
        "What is the capital of India?", "1) New Delhi", "2) Lucknow", "3) Bengaluru", "4) Mumbai", 1
    ],
    [
        "Which river is considered the holiest in Hinduism and is often referred to as the Ganga?",
        "1) Yamuna", "2) Godavari", "3) Brahmaputra", "4) Ganges", 4
    ],
    [
        "Who is known as the Father of the Nation in India for his role in the country's independence movement?",
        "1) Jawaharlal Nehru", "2) Sardar Patel", "3) Subhas Chandra Bose", "4) Mahatma Gandhi", 4
    ],
    [
        "What is the national currency of India?", "1) Indian Rupee (INR)", "2) Dollar", "3) Euro", "4) Yen", 1
    ],
    [
        "Which famous Indian monument is considered one of the Seven Wonders of the World and was built as a symbol of love?",
        "1) Qutub Minar", "2) Red Fort", "3) Hawa Mahal", "4) Taj Mahal", 4
    ]
]

count = 0

for question in questions:
    print(question[0])
    print("a." + question[1], "b." + question[2])
    print("c." + question[3], "d." + question[4])

    ans = input("Choose the option : ").lower()  
    if ans == str(question[5]):
        print("Correct !!")
        count += 1
    else:
        print("Incorrect!!")

print("The total correctly answered questions are:", count)