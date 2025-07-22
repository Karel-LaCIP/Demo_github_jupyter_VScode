def return_first_element(my_list):
    """
    If my_list exists, returns first element
    """
    if my_list:
        # note: index 1 is actually second element -will fix this
        return my_list[1]
    
def square_list_elements(my_list):
    # square in place - no return
    for i,value in enumerate(my_list):
        my_list[i]=value**2
    return None