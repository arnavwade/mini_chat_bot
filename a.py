print("Welcome to my chatbot...")
Name = input("Enter your name:-")
print(f"Hello ,{Name} Nice to meet you.")
print("what would you like to talk about?")
print("1. My day")
print("2. My hobbies")
print("3. About you")
print("4. Nothing")
while True:
    choice = input("enter your choice no.:\n")  
    if choice == "1":
        mood = input("How was your day?").lower()
        if mood == "good":
             print(f"oh nice to hear that my friend, {Name}!")
        elif mood == "bad":
            print(f"Dont worry ,{Name} tomorrow is a new day .")
            print("I hope you had a great day!")
    elif choice == "2":
        hobby = input("What is your hobby?")   
        print(f"oh wow,{hobby} ,it sounds great! {Name}.")
    elif choice == "3":
        print("I am just a simple chatbot.")
        print("I enjoy talking with you.")
        print("I am created using python.")
    elif choice == "4":
        print(f"OK!, No worries it was nice talking to you,{Name}.")
        print(f"Have a wonderful day ahead {Name},Goodbye!")
        break
    else:
        print(f"Invalid choice no. {Name}!")

