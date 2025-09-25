print("Raspunde corect la cat mai multe intrebari.\n")
print("Mai jos ai o lista de intrebari, iar pentru a promova, este nevoie sa raspunzi corect la 8 intrebari din 10.\n")
print("Lista de intrebari:\n")


quiz_list = {
    "q1":{
        "question":"Cat face 2 + 3?\n a. 5\n b. 6\n c. 4\nRaspuns: ",
        "options":{"a":5,"b":6,"c":4}
    },
    "q2":{
        "question":"Cat face 3*5?\n a. 8\n b. 15\n c. 10\nRaspuns: ",
        "options":{"a":8,"b":15,"c":10}
    },
    "q3":{
        "question":"Cat face 11*11?\n a. 121\n b. 111\n c. 122\nRaspuns: ",
        "options":{"a":121,"b":111,"c":122}
    }
}

right_answer = {
    "r1" : 5,
    "r2" : 15,
    "r3" : 121
}


answers = []
tries = 9

for a in quiz_list:

    answer = input(quiz_list[a]["question"])

    
    while answer not in ("a","b","c") and tries > 0:
        print(f"Nu ai ales o varianta buna, mai ai {tries} incercari. Alege una dintre optiunile disponibile: a, b sau c!")
        answer = input(quiz_list[a]["question"])
        tries -= 1

    if tries == 0:
        print("Ai depasit numarul maxim de incercari!")
        break
    elif answer in ("a","b","c"):
        answers.append(quiz_list[a]["options"][answer])
    else:
        answers.append(None)


print("Raspunsurile tale au fost:", *answers, sep=", ")

final_answers = []
for ans, r in zip(answers,right_answer):
    if ans == right_answer[r]:
        #print(ans,right_answer[r])
        final_answers.append(ans)

print("Raspunsurile corecte sunt:",*final_answers, sep=", ")
print("Ai raspuns corect la",len(final_answers), "intrebari din 3")




