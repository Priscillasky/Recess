"""x = 0;
while x < 10:
    print(x)
    x+= 1
"""

    #Break statement ~ Terminates the loop
"""for number in range(1,10):
    if number == 5:
        break
    print(number)
"""

    #continue statement
"""for number in range(1,10):
    if number == 5:
        continue
    print(number)
"""

"""phones = ["iPhone","Samsung","Tecno"]
for phone in phones:
    if phone == "iPhone":
        break
        print(phones)
"""

#Exception handling (try,except,finally)
"""
    try block:
    except:
    finally:
"""

#try:
   # x = 10/0
#except ZeroDivisionError:
   # print("Error:Division by zero") #cannot divide by zero
#finally:
    #print("This is always executed") # complete execution

"""
DICTIONARY
Example 5
    dictionary {}
"""
"""emotion = {
    'happy':"Happiness is good for you",
    'sad': "There is a light at the end of the tunnel",
    'angry': "Take a deep breathe",
    'fearful': 'Fearful',
    'disappointed': 'Disappointed',
}
#Prompt the user to enter their emotions
user_emotion = input("How are you feeling today")

if user_emotion in emotion:
    print(emotions[user_emotion])
else:
    print("Im sorry ,i dont understand this emotion")

    ##Exercise 1
    #Program to ask students about their mental health
    #Prompt on a scale of 1 to 10 to rate their mental health
"""
print("welcome to therapy")
name = input("Please enter your name:")
mentalHealth = {
    'one': "That's great,please keep it up!",
    'two':"Oh sorry dear,everything will me okay",
    'three':"Oh sorry dear,everything will me okay",
    'four':"Oh sorry dear,everything will me okay",
    'five':"Oh sorry dear,everything will me okay",
    'six':"Halfway there,please dont give up",
    'seven':"Sorrow is a valid emotion",
    'eight':"Well tried,u can get there ",
    'nine':"You are happy!",
    'ten':"Thats great,keep it up!",

}
Health = input("On a scale of 1 to 10,rate your mental health")
Health = Health.lower()

if Health in mentalHealth:
    print(mentalHealth[Health])
else:
    print("Im sorry,i dont understand")
