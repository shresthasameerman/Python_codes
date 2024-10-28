todo_task=[]
task_status=[]

def addTask():
    task = input("please enter task:  ")
    if task.strip() == "":
        print("please enter task")
    else:
        todo_task.append(task)
        task_status.append("incomplete")

def viewTask():
    if len(todo_task) == 0:
        print("to do task to display")
    else:
        for i, (task,status) in enumerate(zip(todo_task,task_status),1):
            print(f"{i}-(task):{status}")


def updateTask():
    task_num = int(input("please enter task number: "))
    task_status[task_num - 1]="complete"

def visualize():
    categories = ["complete","incomplete"]
    counts = [task_status.count("complete"),task_status.count("incomplete")]
    plt.bar(categories.counts)
    plt.title("task bar")
    plt.xlabel("task status")
    plt.ylabel("counts")
    plt.show()


addTask()
