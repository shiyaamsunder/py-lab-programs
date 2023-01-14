questions = [
             "A single packet on data link is known as?", 
             "Web pages are written using?",
             "What is the full form of IP?",
             "Who is known as father of computer?",
             "Pascaline is known as:",
             ]
options =[
        ["A. Path",                  "B. Frame", 
         "C. Block",                 "D. Group"],
        ["A. FTP",                   "B. HTTP", 
         "C. HTML",                  "D. URL"],
        ["A. Interface program",     "B. Interface protocol", 
         "C. Internet Program",      "D. Internet Protocol"],
        ["A. James Gosling",         "B. Dennis Ritchie",
         "C. Charles Babbage",       "D. John Carmack"],
        ["A. Adding Machine",        "B. Difference Machine", 
         "C. Multiplication Machine","D. Division Machine"],
        ]

answers = ["b", "c", "d", "c", "a"]

keys = zip(questions, options, answers)

score = 0
for ques, opts, ans in keys:
    print("")
    print(ques)
    for opt in opts:
        print("\t" + opt)
    print("")

    choice = input("Enter choice: ")

    if(choice.lower() == ans):
        score+=1


print("Score: ", score)
