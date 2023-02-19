import win32com.client
import win32api
import pythoncom


def exchangeRun(base):
    if base == 'Petrykivka':
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
    result1 = runTask(task_name=task_name1, server=server, base=base)
    if result1[0] == 1:
        return result1[1]

    # Start Task2 on current server
    result2 = runTask(task_name=task_name2, server='service.dpst.kola', base=base)
    if result2[0] == 1:
        return result2[1]
    else:
        return f'Exchange 1C7-{base} complete!'


def runTask(task_name, server, base):
    try:
        pythoncom.CoInitializeEx(0)
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
