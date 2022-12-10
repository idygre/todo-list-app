import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


todos = functions.get_todos()

st.title("My Todo List")
st.subheader("Add new todo items")
st.write("Increase your productivity with this app")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a todo", placeholder="Add a new todo...",
              on_change=add_todo, key='new_todo')