import json
import time
import random

FILE_NAME = "qn.json"

# class question:
#     def __init__(self, text, option, correct_ans):
#         pass
    
#     def check_answer(self, answer):
#         pass
s = time.strftime("%a, %d %b %Y %H:%M:%S", 
             time.gmtime(1627987508.6496193))
print(f"you start at {s}")

class quiz:
    def __init__(self):
        print("start a new journey!")
    
    def load_questions(self, filename):
        global questions 
        questions = []
        global options 
        options = []
        global answer
        answer = []
        global category 
        category = []
        global hardCat
        hardCat = []
        global MediumCat
        MediumCat = []
        global EasyCat
        EasyCat = []
            
         
        with open(filename, 'r') as f:
            data = json.load(f)
            for i in data:
                questions.append(i["question"])
                answer.append(i["answer"])
                category.append(i["category"])
                options.append(i["options"])
            
            for i in data:
                if(i["category"] == "General Knowledge"):
                    EasyCat.append(i)
                elif(i["category"] == "Computer Science"):
                    MediumCat.append(i)
                elif(i["category"] == "Mathematics"):
                    hardCat.append(i)
                
    
    def take_quiz(self, name):
        print(f"Here some qn {name}")
        global correctAnsList
        correctAnsList = []
        n = 10
        li = random.sample(range(0, 29), n)
        i = 0
        cate = int(input("What category you chose: 1.Hard/2.Medium/3.Easy Or 4/Normal: "))
        
        if cate == 4:
            while (len(li)):
                # if len(li) < 0:
                #     break
                print(len(li))
                flag = li.pop()
                i+=1
                print(f"{i}. {questions[flag]}")
                for index, qn in enumerate(options[flag]):
                    print(f"{index+1}: {qn}")
                
                userAns = int(input("plz write just option number: "))
                if options[flag][userAns-1] == answer[flag]:
                    correctAnsList.append(1)
                    print("ans is correct")
                else:
                    print(f"ans is not correct. the correct ans is {answer[flag]}")
        else:
            
            
            strQ = 0
            endQ = 0
            if cate == 1:
                strQ = 10
                endQ = 18
            elif cate == 2:
                strQ = 19
                endQ = 29
            elif cate == 3:
                strQ = 0
                endQ = 9
            
            m = 5
            listN = random.sample(range(0, 10), m)
            
            while(len(listN)):
                pass
                
                
                
                      
        
    def save_result(self, user_info, time_taken):
        print(f"{user_info} you take and end at {time_taken} min")
    
    def show_score(self):
        score = len(correctAnsList)*3
        print(f"your total score is: ", end="")
        if score >= 25:
            print(f"{score}. You done Excellent!")
        elif score >= 20:
            print(f"{score}. You done very good!")
        elif score >= 15:
            print(f"{score}. You done good!")
        elif score >= 10:
            print(f"{score}. You done bad")
        else:
            print(f"{score}. You done so bad")
            
    

c1 = quiz()
c1.load_questions(FILE_NAME)
c1.take_quiz("abdullah")
# e = time.strftime("%a, %d %b %Y %H:%M:%S", 
#              time.gmtime(1627987508.6496193))
# c1.save_result("abdullah", e)
# c1.show_score()