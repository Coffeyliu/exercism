# This is the modified code according to comments.Try to make it better.

base_first_line = "On the {} day of Christmas my true love gave to me: "
days = "zero first second third fourth fifth sixth seventh eighth ninth tenth eleventh twelfth".split()
lyrics = "twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.".split(', ')


def get_one_line(day_number: int) -> str:
    "pass the number of day, return the lyric for that day, input should be between 1 to 12"

    n = day_number
    if n == 1:
        line = base_first_line.format(days[n]) + lyrics[-n:][0][4:]
        return line
    else:
        line = base_first_line.format(days[n]) + ", ".join(lyrics[-n:])
        return line


def recite(start_verse: int, end_verse: int) -> list:
    """return lines of lyrics according to inputs. 

    Note: inputs should be between 1 to 12 and should be an integer
    """

    return [get_one_line(day_number) for day_number in range(start_verse, end_verse+1)]
