def get_one_line(day_number):
    "pass the number of day, return the lyric for that day, input should be between 1 to 12"

    base_first_line = "On the {} day of Christmas my true love gave to me: "
    days = "zero first second third fourth fifth sixth seventh eighth ninth tenth eleventh twelfth".split()
    lyrics = "twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."

    n = day_number
    if n < 1 or n > 12:
        raise ValueError('the number of day should be between 1 to 12')

    if n == 1:
        line = base_first_line.format(days[n]) + lyrics.split(', ')[-n:][0][4:]
        return line
    else:
        line = base_first_line.format(
            days[n]) + ', '.join(lyrics.split(', ')[-n:])
        return line


def recite(start_verse, end_verse):

    # exception check --- just for practice
    if start_verse > end_verse:
        raise ValueError('start_verse should less or equal to end_verse')
    if start_verse < 1 or end_verse < 1 or start_verse > 12 or end_verse > 12:
        raise ValueError('range should be between 1 to 12')
    if type(start_verse) != type(1) or type(end_verse) != type(1):
        raise TypeError('input should be an integer')


    lines = []
    for day_number in range(start_verse, end_verse+1):
        line = get_one_line(day_number)
        lines.append(line)
    return lines
