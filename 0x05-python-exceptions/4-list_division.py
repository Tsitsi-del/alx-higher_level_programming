#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div_res = []
    temp = 0
    for count in range(0, list_length):
        try:
            temp = my_list_1[count] / my_list_2[count]
        except TypeError:
            temp = 0
            print("wrong type")
        except ZeroDivisionError:
            temp = 0
            print("division by 0")
        except IndexError:
            temp = 0
            print("out of range")
        finally:
            pass
        div_res.append(temp)
    return div_res
