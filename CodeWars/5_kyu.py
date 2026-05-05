## regex password validattion
def validate_p_word():
    regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{6,}$'

    return regex