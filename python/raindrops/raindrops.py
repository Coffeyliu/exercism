def convert(number):
    result = ""
    if number % 3 == 0:
        result = result + 'Pling'
    if number % 5 == 0:
        result = result + 'Plang'
    if number % 7 == 0 :
        result = result + 'Plong'
    
    return result if len(result) != 0 else str(number)
