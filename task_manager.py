import easygui

task_dictionary = {
    "T1" : {
        "Title" : "Design Homepage",
        "Description" : "Create a mockup of the homepage",
        "Assignee" : "JSM",
        "Priority" : 3,
        "Status" : "In progress"
    },
    "T2" : {
        "Title" : "Implement Login page",
        "Description" : "Create the Login page for the website",
        "Assignee" : "JSM",
        "Priority" : 3,
        "Status" : "Blocked"
    },
    "T3" : {
        "Title" : "Fix navigation menu",
        "Description" : "Fix the navigation menu to be more user-friendly",
        "Assignee" : "None",
        "Priority" : 1,
        "Status" : "Not Started"
    },
    "T4" : {
        "Title" : "Add payment processing",
        "Description" : "Implement payment processing for the website",
        "Assignee" : "JLO",
        "Priority" : 2,
        "Status" : "In Progress"
    },
    "T5" : {
        "Title" : "Create an About Us page",
        "Description" : "Create a page with information about the company",
        "Assignee" : "BDI",
        "Priority" : 1,
        "Status" : "Blocked"
    }
}

team_member_dictionary = {
    "JSM" : {
        "Name" : "John Smith",
        "Email" : "John@techvision.com",
        "Tasks Assigned" : ["T1", "T2"]
    },
    "JLO" : {
        "Name" : "Jane Love",
        "Email" : "Jane@techvision.com",
        "Tasks Assigned" : ["T4"]
    },
    "BDI" : {
        "Name" : "Bob Dillon",
        "Email" : "Bob@techvision.com",
        "Tasks Assigned" : ["T5"]
    }
}

def menu():
    """A function which contains the menu for the program. The user can 
    choose to add a new task, update an exsiting task, search for a team
    member or task, generate a summary report, or ouput the task 
    collection."""
    options = {
        "Add Task" : add_task,
        "Update Task" : update_task,
        #"Search" : search,
        #"Generate Report" : generate_report,
        "Output Tasks" : output_tasks,
        "Quit" : quit
    }

    menu_choices = []

    for key in options:
        menu_choices.append(key)

    title = "Task Managment System - Menu"
    user_choice = easygui.buttonbox("What would you like to do?", title, \
    choices = menu_choices)

    function = options[user_choice]()

def add_task():
    """This is a function that allows the user to add a task to the task
    dictionary. It asks the user for the tasks title, description, 
    assignee, priority, status, and adds an automatic sequential task
    ID to the task."""
    task_count = 1
    for key in task_dictionary:
        task_count += 1
    
    task_id = (f"T{task_count}")

    title = "Task Managment System - Add Task"

    status_list = ["In Progress", "Blocked", "Not Started"]

    assignee_list = ["JSM", "JLO", "BDI", "None"]

    task_title = easygui.enterbox(f"Please enter the title of the task", title)
    task_description = easygui.enterbox(f"Please enter the description for \
{task_title}", title)
    task_assignee = easygui.buttonbox(f"Please enter the assignee for \
{task_title}", title, choices = assignee_list)
    task_priority = easygui.integerbox(f"Please enter the priority for \
{task_title} from 1-3", title, lowerbound=1, upperbound=3)
    task_status = easygui.buttonbox(f"Please enter the status for \
{task_title}", title, choices = status_list)
    
    task_dictionary[task_id] = {
        "Title" : task_title,
        "Description" : task_description,
        "Assignee" : task_assignee,
        "Priority" : task_priority,
        "Status" : task_status
    }

    team_member_dictionary[task_assignee]["Tasks Assigned"].append(task_id)
    
    menu()

def output_tasks():
    """This is a function which prints all of the tasks in a readable
    format in an easygui message box."""
    for task_id, content in task_dictionary.items():
        msg = f"Title: {content['Title']}\n"
        msg += f"Description: {content['Description']}\n"
        msg += f"Assignee: {content['Assignee']}\n"
        msg += f"Priority: {content['Priority']}\n"
        msg += f"Status: {content['Status']}\n"

        easygui.msgbox(msg, title = f"Task ID: {task_id}")

    menu()

def update_task():
    """This function will allow the user to update a task. They will
    be able to update the tasks status, assign a team member to a task,
    and when a tasks status is complete, it should automatically be
    removed from the team members task list."""

    task_titles = []

    for task_id, titles in task_dictionary.items():
        task_titles.append(titles["Title"])

    task_choice = easygui.buttonbox("What task would you like to update \
a detail of?", "Update Task", task_titles)

    task_id_num = 1

    check = True

    while check == True:
        for i in task_titles:
            if i != task_choice:
                task_id_num += 1               
            else:
                check = False
                break

    task_id = f"T{task_id_num}"

    task_info = []

    for task_information in task_dictionary[task_id]:
        task_info.append(task_information)

    edit_choice = easygui.buttonbox(f"What detail of {task_choice} \
would you like to edit?", "Edit Choice", task_info)

    assignee_list = ["JSM", "JLO", "BDI", "None"]

    status_list = ["Completed", "In Progress", "Blocked", "Not Started"]

    if edit_choice == "Assignee":
        task_dictionary[task_id][edit_choice] = easygui.buttonbox(f"Please \
select the new assignee for {task_choice}", "Update Assignee", \
choices = assignee_list)
    elif edit_choice == "Priority":
        task_dictionary[task_id][edit_choice] = easygui.integerbox(f"Please \
enter the updated priority for {task_choice} from 1 - 3", title = "Update Priority", \
lowerbound = 1, upperbound = 3)
    elif edit_choice == "Status":
        task_dictionary[task_id][edit_choice] = easygui.buttonbox(f"Please \
select the updated status for {task_choice}", title = "Update Status", \
choices = status_list)
    elif edit_choice == "Title":
        task_dictionary[task_id][edit_choice] = easygui.enterbox(f"Please \
enter the new title for {task_choice}", title = "Update Title")
    else:
        task_dictionary[task_id][edit_choice] = easygui.enterbox(f"Please \
enter the new description for {task_choice}", title = "Update Description")

    if task_dictionary[task_id][edit_choice] == "Completed":
        task_assignee = task_dictionary[task_id]["Assignee"]
        task_dictionary[task_id]["Assignee"] = "None"
        team_member_dictionary[task_assignee]["Tasks Assigned"].pop(task_id)

    menu()

def quit():
    """This function will allow the user to quit the program."""
    quit

menu()