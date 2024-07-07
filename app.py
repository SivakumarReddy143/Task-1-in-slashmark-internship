import pandas as pd
import streamlit as st
import random

# Initialize an empty task list
tasks = pd.DataFrame(columns=['description', 'priority'])

# Load pre-existing tasks from a CSV file (if any)
try:
    tasks = pd.read_csv('tasks.csv')
except FileNotFoundError:
    pass

# Function to save tasks to a CSV file
def save_tasks():
    tasks.to_csv('tasks.csv', index=False)


# Function to add a task to the list
def add_task(description, priority):
    global tasks  # Declare tasks as a global variable
    new_task = pd.DataFrame({'description': [description], 'priority': [priority]})
    tasks = pd.concat([tasks, new_task], ignore_index=True)
    save_tasks()

# Function to remove a task by description
def remove_task(description):
    global tasks
    tasks = tasks[tasks['description'] != description]
    save_tasks()

# Function to list all tasks
def list_tasks():
    if tasks.empty:
        st.write("No tasks available.")
    else:
        st.write(tasks)

# Function to recommend a task based on machine learning
def recommend_task():
    if not tasks.empty:
        # Get high-priority tasks
        high_priority_tasks = tasks[tasks['priority'] == 'High']
        
        if not high_priority_tasks.empty:
            # Choose a random high-priority task
            random_task = random.choice(high_priority_tasks['description'])
            st.write(f"Recommended task: {random_task} - Priority: High")
        else:
            st.write("No high-priority tasks available for recommendation.")
    else:
        st.write("No tasks available for recommendations.")

# Streamlit App
st.title("Task Management App")

menu = ["Add Task", "Remove Task", "List Tasks", "Recommend Task"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add Task":
    st.subheader("Add Task")
    description = st.text_input("Enter task description")
    priority = st.selectbox("Enter task priority", ["Low", "Medium", "High"])
    if st.button("Add Task"):
        add_task(description, priority)
        st.success("Task added successfully.")

elif choice == "Remove Task":
    st.subheader("Remove Task")
    description = st.text_input("Enter task description to remove")
    if st.button("Remove Task"):
        remove_task(description)
        st.success("Task removed successfully.")

elif choice == "List Tasks":
    st.subheader("List Tasks")
    list_tasks()

elif choice == "Recommend Task":
    st.subheader("Recommend Task")
    if st.button("Recommend Task"):
        recommend_task()
