from process import (print_program, get_menu_num, print_menu_anyone, print_menu_members,
                     process_members, process_anyone, current_member)




# 메인 프로그램
is_logged_in = False
while True:
    print_program()

    if is_logged_in == False:
        print_menu_anyone()
        num_menu = get_menu_num()
        is_exit, login_result = process_anyone(num_menu)
        if login_result:
            current_member = login_result
            is_logged_in = True
        if is_exit:
            break

    elif is_logged_in:
        print_menu_members()
        num_menu = get_menu_num()
        is_exit = process_members(num_menu, current_member)
        if is_exit:
            break

