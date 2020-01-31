def convert(number):
    result = ""
    if number % 3 == 0:
        result = result + 'Pling'
    if number % 5 == 0:
        result = result + 'Plang'
    if number % 7 == 0 :
        result = result + 'Plong'
    
    # NOTE: again, there is a way to avoid that len() call
    # since result is either "" of some combination of "Pli*"
    # return result or str(number)
    return result if len(result) != 0 else str(number)
