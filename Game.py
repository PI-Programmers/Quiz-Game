def give_options(x, y, z):
    print("a):", x)
    print("b):", y)
    print("c):", z)


print("Hello! Welcome To My Quiz Game" "\n" "All Questions Carries 10 Marks Each")
print()
ans = input("Are You Ready To Play ? ( Yes / No ) : ")
print()
a = "Note: Write Answers, Do Not Write Options"
score = 0
total_questions = 4

correct_ans = ["python", "steve jobs", "siri", "bitcoin"]
if ans.lower() == "yes":
    print(a)
    print("Question- What is the best Programming Language? ")
    give_options("Python", "C", "Java" )
    ans=input("Your Answer : ")
    if ans.lower() == correct_ans[0]:
        score=score+1
        print("Correct")
    else:
        print("Incorrect")
    
    print()

    print("Question- Who is the Founder of Apple Inc? ")
    give_options("Mark Zuckerberg", "Warren Buffet", "Steve jobs")
    ans = input("Your Answer : ")
    if ans.lower() == correct_ans[1]:
        score=score+1
        print("Correct")
    else:
        print("Incorrect")
    print()
    print("Question- What is the Name of Apple's Virtual Assistant? ")
    give_options("Google", "Siri", "Alexa")
    ans = input("Your Answer : ")
    if ans.lower() == correct_ans[2]:
        score=score+1
        print("Correct")
    else:
        print("Incorrect")
    print()
    print("Question- What is the best Investment? ")
    give_options("Share Capital", "Mutual Funds", "Bitcoin")
    ans = input("Your Answer : ")
    if ans.lower() == correct_ans[3]:
        score=score+1
        print("Correct")
    else:
        print("Incorrect")

    print("Thank You For Playing This Quiz Game")
print()

i = score * 10

if i <= 20:
    print("Oops, You Scored",i,"/ 40 | YOU ARE A NOOB")
elif i == 30:
    print("WoW, You Scored ",i,"/ 40 | YOU ARE QUITE SMART")
else:
    print("Congratulations, You Scored ",i,"/ 40 | YOU ARE A GENIUS")


