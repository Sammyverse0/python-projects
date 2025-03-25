import itertools

QandA = [["Who is Blackpink's leader?", "NONE"], 
         ["When did Blackpink debut?", "2016"],
         ["When is Blackpink's anniversary?", "8 august"]]
options = [["Jisoo","Lisa", "Jennie", "None"],
           ["2018","2020","2016","2019"],
           ["3 august","27 march","11 january","8 august"]]
money = 0

for (i,j) in zip(QandA,options):
    print(i[0])
    print("Options: ")
    print(f"a){j[0]}        b){j[1]}\nc){j[2]}       d){j[3]}")
    ans = input("write your answer: ")

    if ans.upper() == i[1].upper():
        print("Correct answer!")
        money = money + 1000
    else: 
        print("Incorrect answer!")
        break

print("Money won: ",money)