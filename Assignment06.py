# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1/1/2022,Created starter script
# BorisU,8/17/2022,Modified code to complete assignment 06
# ---------------------------------------------------------------------------- #
# import os  for troubleshooting the current directory

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
file_name_str = "ToDoFile.txt"  # The name of the data file
#file_obj = None  # An object that represents a file  #used local variables instead
#row_dic = {}  # A row of data separated into elements of a dictionary {Task,Priority} #used local variables instead
table_lst = []  # A list that acts as a 'table' of rows
choice_str = ""  # Captures the user option selection

# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        file = open(file_name, "r")
        for line in file:
            task, priority = line.split(",")
            row = {"Task": task.strip(), "Priority": priority.strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows

    @staticmethod
    def add_data_to_list(task_to_add, priority, list_of_rows):
        """ Adds data to a list of dictionary rows

        :param task_to_add: (string) with name of task:
        :param priority: (string) with name of priority:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        row = {"Task": str(task_to_add).strip(), "Priority": str(priority).strip()}
        list_of_rows.append(row)
        return list_of_rows

    @staticmethod
    def remove_data_from_list(task_to_remove, list_of_rows):
        """ Removes data from a list of dictionary rows

        :param task_to_remove: (string) with name of task:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows, (bool) status of removal
        """
        status = False
        for row in list_of_rows:
            task, priority = dict(row).values()
            if task == task_to_remove:
                list_of_rows.remove(row)
                status = True

        return list_of_rows, status

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """ Writes data from a list of dictionary rows to a File

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        objFile = open(file_name, "w")
        for row in list_of_rows:
            objFile.write(row["Task"] + "," + row["Priority"] + "\n")
        objFile.close()

        return list_of_rows

    @staticmethod
    def validate_task_to_add_not_existing(task_to_add, list_of_rows):
        """ Validates that the task to be added doesn't already exist in the list
                :param task_to_add: (string) with name of file:
                :param list_of_rows: (list) you want filled with file data:
                :return: boolean existing -does task already exist?
        """
        existing = False
        for row in list_of_rows:
            task, priority = dict(row).values()
            if task == task_to_add:
                existing = True

        return existing

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def output_current_tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print()  # Add an extra line for looks
        print("************\u001b[1m Current ToDo List\u001b[0m ************")
        print("Task " + "|" + " Priority")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def output_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Please select from \u001b[1mMenu of Options\u001b[0m
        0) \x1B[4mRefresh\x1B[0m Data from File
        1) \x1B[4mAdd\x1B[0m a new Task
        2) \x1B[4mRemove\x1B[0m an existing Task
        3) \x1B[4mSave\x1B[0m Data to File        
        4) \x1B[4mExit\x1B[0m Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def output_successful_task_add():
        """ Display output of successful data add

         :return: nothing
         """
        print("****Task " + task + " and Priority " + priority + " was succesfully added****")

    @staticmethod
    def output_failed_task_add():
        """ Display output of failed data add  (duplicate)

         :return: nothing
         """
        print("*****Task " + task + " already exists. Please enter a unique task.*****")# check if task already on the list

    @staticmethod
    def output_successful_task_removal():
        """ Display output of successful data removal

            :return: nothing
            """
        print("****Task " + task + " was succesfully removed****")

    @staticmethod
    def output_failed_task_removal():
        """ Display output of failed data removal

            :return: nothing
            """
        print("****Task " + task + " not found. Please enter a valid task to remove.****")

    @staticmethod
    def output_successful_data_save():
        """ Display output of successful data save

            :return: nothing
            """
        print("****Data Saved to File***")
        #print("Table " + str(table_lst) + " was succesfully saved")  #if want to present more detail

    @staticmethod
    def output_rejected_data_save():
        """ Display output of rejected data save

            :return: nothing
            """
        input("****Data NOT saved, but previous data still exists. Press the [Enter] key to return to menu. ****")

    def output_successful_program_exit():
        """ Display output of requested user exit

            :return: nothing
            """
        print("****Exiting... Goodbye...***")

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def input_save_confirmation_choice():
        """ Gets the save confirmation choice from a user

        :return: string
        """
        choice = str(input("Save this data to file? (y/n) - ")).strip().lower()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def input_new_task_and_priority():
        """  Gets task and priority values to be added to the list

        :return: (string, string) with task and priority
        """
        task = str(input("What is the task? - ")).strip()
        priority = str(input("What is the priority? [high|medium|low] - ")).strip()
        return task, priority

    @staticmethod
    def input_task_to_remove():
        """  Gets the task name to be removed from the list

        :return: (string) with task
        """
        TaskToRemove = input("Which TASK would you like removed? - ")
        return TaskToRemove

# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
    #dirs = os.listdir()  troubleshooting current directory error
    #for file in dirs:
    #   print(file)

# load in data from file initially
Processor.read_data_from_file(file_name=file_name_str, list_of_rows=table_lst)

# Step 2 - Display a menu of choices to the user
while (True):

    # Step 3 Show current data
    IO.output_current_tasks_in_list(list_of_rows=table_lst)  # Show current data in the list/table
    IO.output_menu_tasks()  # Shows menu
    choice_str = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice

    # Refresh Data From File
    if choice_str.strip() == '0' or choice_str.strip().lower() == 'refresh' or choice_str.strip().lower() == 'ref':
        Processor.read_data_from_file(file_name=file_name_str, list_of_rows=table_lst)  # read file data
        continue

    # Add a new Task
    elif choice_str.strip() == '1' or choice_str.strip().lower() == 'add' or choice_str.strip().lower() == 'a':
        task, priority = IO.input_new_task_and_priority()
        if (Processor.validate_task_to_add_not_existing(task_to_add=task, list_of_rows=table_lst) ):
            IO.output_failed_task_add()
            continue
        else:
            table_lst = Processor.add_data_to_list(task_to_add=task, priority=priority, list_of_rows=table_lst)
            IO.output_successful_task_add()
            continue  # to show the menu

    # Remove an existing Task
    elif choice_str.strip() == '2' or choice_str.strip().lower() == 'remove' or choice_str.strip().lower() == 'rem':
        task = IO.input_task_to_remove()
        table_lst, status = Processor.remove_data_from_list(task_to_remove=task, list_of_rows=table_lst)
        if(status == True):
            IO.output_successful_task_removal()
        else:
            IO.output_failed_task_removal()
        continue  # to show the menu

    # Save Data to File
    elif choice_str.strip() == '3' or choice_str.strip().lower() == 'save' or choice_str.strip().lower() == 's':
        if(IO.input_save_confirmation_choice() == "y" ):
            table_lst = Processor.write_data_to_file(file_name=file_name_str, list_of_rows=table_lst)
            IO.output_successful_data_save()
        else:
            IO.output_rejected_data_save()
        continue  # to show the menu

    # Exit Program
    elif choice_str.strip() == '4' or choice_str.strip().lower() == 'exit' or choice_str.strip().lower() == 'x':
        IO.output_successful_program_exit()
        break  # by exiting loop



