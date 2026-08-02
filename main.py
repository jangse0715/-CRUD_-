from test01 import print_program, print_menu, working_process, get_menu_num

while True:
    print_program()
    print_menu()
    num_menu = get_menu_num()
    is_exit = working_process(num_menu)
    if is_exit == True: break


