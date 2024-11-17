# src/ui/user_interface.py

def get_execution_mode() -> str:
    """
    実行モードをユーザーから入力として受け取る。
    """
    print("Select execution mode:")
    print("1. Persistent mode (runs every 5 minutes)")
    print("2. Single execution mode")
    choice = input("Enter 1 or 2: ")

    if choice == '1':
        return 'persistent'
    elif choice == '2':
        return 'once'
    else:
        print("Invalid input. Defaulting to single execution mode.")
        return 'once'
