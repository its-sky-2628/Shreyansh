import streamlit as su
import matplotlib.pyplot as plt
su.set_page_config(page_title="Student Performance Analyzer",layout="centered")
Sub = {
    # this is no of choice that i give to user
    "M": ["Algebra", "Geometry", "Calculation", "Word Problems"],
    "S": ["Concept Weakness", "Lack of Practice", "Numerical Problems", "Theory Gaps"],
    "E": ["Grammar", "Vocabulary", "Comprehension", "Spelling"],
    "O": ["Concept Weakness", "Not Prepared", "Unable to Understand", "High-Level Questions"]
}
#
overall=[]
particular=[] #This is for storing the user input for graph generate
specific=[]
su.title("Student Performance Analyser") #heading appeear on UI
su.subheader("Analyze your mistake")

select=su.selectbox("Do you want to analyse for",["Particular Subject","Specific Subject"]) #choice that user have
su.write(f"You choose {select}")
if select=="Particular Subject":
    for a in Sub["O"]:    #for traversing in dictionary 
            value=su.number_input(f"Number of mistakes in {a}", min_value=0, step=1)
            particular.append(value)
    
else :
    choice=su.radio("Pick your subject",["Mathematics","Science","English"])   
    su.write(f"You choose {choice}")

    if choice== "Mathematics": 
        for u in Sub["M"]:
             Math=su.number_input(f"Number of mistakes in {u}", min_value=0, step=1) #for partcular subject 
             specific.append(Math)
    elif choice== "Science": 
        for u in Sub["S"]:
            Science=su.number_input(f"Number of mistakes in {u}", min_value=0, step=1)
            specific.append(Science)
    elif choice=="English":
        for u in Sub["E"]:
            English=su.number_input(f"Number of mistakes in {u}", min_value=0, step=1)
            specific.append(English)
if su.button("Show Chart"): #chart generate
    if select == "Particular Subject":
        labels = Sub["O"] #for one axis to be from subject list
        values = particular
    else:
        if choice == "Mathematics":
            labels = Sub["M"]
        elif choice == "Science":
            labels = Sub["S"]
        else:
            labels = Sub["E"]
        values = specific

    fig, ax = plt.subplots()

    ax.bar(labels, values)
    ax.set_xlabel("Mistake Type")
    ax.set_ylabel("Number of Mistakes")
    ax.set_title(f"Mistake Analysis - {select}")
    plt.xticks(rotation=20)
    su.pyplot(fig)
    mistake=values.index(max(values)) #this will gives index of maximum value in value
    least=values.index(min(values))
    su.subheader(f"Your Weakness is in {labels[mistake]}")
    su.write("You should focus on this and work hard 😟")
    su.subheader(f"Your Strong Point is in {labels[least]}") #it provides labels whose value is least
    su.write("You are going good in this ,keep it up 😊")

 ye rha code maine jitna bnya tha tumko jo bhi AI ya parent wala add krni ho improve krna ho add kr dena
