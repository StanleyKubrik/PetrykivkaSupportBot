import win32com.client
import win32api


# def error_handler(func):
#     def print_message(*args, **kwargs):
#         try:
#             func(*args, **kwargs)
#         except Exception as ex:
#             tuple_error = ex.args
#             first_error = tuple_error[0]
#             second_error = tuple_error[2][5]
#             first = win32api.FormatMessage(first_error)
#             second = win32api.FormatMessage(second_error)
#             print(first + ' ' + second)
#     return print_message

def exchangeRun(base):
    # server = ''
    # task_name1 = ''
    # task_name2 = ''
    if base == 'Petrykivka':
        # Connect to the server
        server = "ss-bhstdp.dpst.kola"
        task_name1 = "Автообмен 1C в SQL"
        task_name2 = "ExchangeSQL-Petrykivka"
    elif base == 'Peremoga':
        server = "1c-pobeda7.dpst.kola"
        task_name1 = "1C Победа SQL"
        task_name2 = "ExchangeSQL-Peremoga"
    else:
        return f'Base {base} doesn\'t existing!'

    # Start Task1 on server
    # try:
    #     pythoncom.CoInitializeEx(0)
    #     scheduler = win32com.client.Dispatch('Schedule.Service')
    #     scheduler.Connect(server)
    #     root_folder = scheduler.GetFolder('\\')
    #     task1 = root_folder.GetTask(task_name1)
    #     task1_run = task1.Run("")
    #     task1_state = task1.State
    # except Exception as ex:
    #     tuple_error = ex.args
    #     first_error = tuple_error[0]
    #     second_error = tuple_error[2][5]
    #     first = win32api.FormatMessage(first_error)
    #     second = win32api.FormatMessage(second_error)
    #     return [1, f"Error on task '{task_name1}', base '{base}':"
    #                f"\n{first} {second}"
    #                f"\nExchange didn't complete!"]

    # Wait for Task1 to complete
    result1 = runTask(task_name=task_name1, server=server, base=base)
    if result1[0] == 1:
        # return result1[1]
        print(result1[1])

    # Start Task2 on current server
    result2 = runTask(task_name=task_name2, server=None, base=base)
    if result2[0] == 1:
        # return result2[1]
        print(result2[1])
    else:
        print(f'Exchange 1C7-{base} complete!')
        # return f'Exchange 1C7-{base} complete!'
    # try:
    #     scheduler = win32com.client.Dispatch('Schedule.Service')
    #     scheduler.Connect()
    #     root_folder = scheduler.GetFolder('\\')
    #     task2 = root_folder.GetTask(task_name2)
    #     task2_run = task2.Run("")
    #     task2_state = task2.State
    #     while task2_state != 4:
    #         import time
    #         time.sleep(5)
    #         task2_state = task2.State
    #     return [0]
    # except Exception as ex:
    #     tuple_error = ex.args
    #     first_error = tuple_error[0]
    #     second_error = tuple_error[2][5]
    #     first = win32api.FormatMessage(first_error)
    #     second = win32api.FormatMessage(second_error)
    #     return [1, f"Error on task '{task_name2}', base '{base}':"
    #                f"\n{first} {second}"
    #                f"\nExchange didn't complete!"]


def runTask(task_name, server, base):
    try:
        scheduler = win32com.client.Dispatch('Schedule.Service')
        scheduler.Connect(server)
        root_folder = scheduler.GetFolder('\\')
        task = root_folder.GetTask(task_name)
        task_run = task.Run("")
        task_state = task.State
        while task_state != 4:
            import time
            time.sleep(5)
            task_state = task.State
        return [0]
    except Exception as ex:
        tuple_error = ex.args
        first_error = tuple_error[0]
        second_error = tuple_error[2][5]
        first = win32api.FormatMessage(first_error)
        second = win32api.FormatMessage(second_error)
        return [1, f"Error on task '{task_name}', base '{base}':"
                   f"\n{first.strip()} {second.strip()}"
                   f"\nExchange didn't complete!"]
