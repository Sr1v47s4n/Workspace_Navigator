from Employees.models import AdminData


def usr_code():
    import random
    import math

    def code_creater():
        ls = [i for i in range(0, 10)]
        num_6 = ""
        for i in range(6):
            index = math.floor(random.random() * 10)
            num_6 += str(ls[index])
        return num_6

    def is_unique():
        code = code_creater()
        try:
            WebUsr = AdminData.objects.get(usrCode=code)
        except AdminData.DoesNotExist:
            return code

    return is_unique()
