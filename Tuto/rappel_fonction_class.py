"""
Définition de fonctions
"""
def my_first_function() :
    print("Hello World")
    return(0)

def my_second_function(my_string) :
    len_my_string = len(my_string)
    if len_my_string > 10 :
        return(False)
    return(True)

def my_third_function(my_string, max_len) :
    """
    rtype : boolean, int
    """
    len_my_string = len(my_string)
    if len_my_string > max_len :
        return(False, len_my_string)
    return(True, len_my_string)

"""
Utilisation de fonctions avec ou sans paramètres"""
ret_first_function = my_first_function()
print(ret_first_function)

ret_second_function = my_second_function("Hello World")
if ret_second_function is True :
    my_first_function()
# print(ret_second_function)
print()
ret_second_test_function = my_second_function("Guardia 1 Paris")

if ret_second_test_function is True :
    my_first_function()
# print(ret_second_test_function)
print()
ret_third_test_function = my_second_function("Hello")
if ret_third_test_function is True :
    my_first_function()
print(ret_third_test_function)

is_true_third, len_str = my_third_function("Hello World", 10)
is_true_third_2, len_str_2 = my_third_function("Hello World", 50)
print(is_true_third, len_str)
print(is_true_third_2, len_str_2)

"""
Défitition d'une classe"""
class myFirstClass() :
    def __init__(self, my_string, max_len) :
        self.my_string = my_string
        self.max_len = max_len
        self.len_my_string = len(my_string)
        self.array_test = []
    
    def my_public_function(self) :
        if self.len_my_string > self.max_len :
            return(False)
        return(True)
    
    def append_array(self, value) :
        self.array_test.append(value)

"""
Instanciation d'une classe
"""
class_test = myFirstClass("Hello", 10)
print(class_test.my_public_function())

"""
Utilisation d'une méthode de classe
"""
class_test.append_array("append1")
print(class_test.array_test)
class_test.append_array("append2")
print(class_test.array_test)
