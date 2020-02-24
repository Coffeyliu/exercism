def get_one_line(day_number):
    "pass the number of day, return the lyric for that day, input should be between 1 to 12"

    # shirouto: this is nice. The way you created these structures and used them in the latter code, 
    # factoring out the logic and the data of your code separately. This is very good practice.
    # The problem is that this helper function is to be called multiple times, and each time it goes through
    # the trouble of creating these objects again and again. A waste. These values are constants, after all: your
    # code never modifies them. So why not pull them our of your function all together. You could even factor them out
    # all together into some comfigration file (no need to go that far for this exercise: just place them in the top level
    # of your module should be enough).
    base_first_line = "On the {} day of Christmas my true love gave to me: "
    days = "zero first second third fourth fifth sixth seventh eighth ninth tenth eleventh twelfth".split()
    # shirouto: the only way you use this fellow is by first splitting it: 
    #
    # >>> lyrics.split(", ")
    #
    # So why not do it only once, here? Or even better, only once upon module loading by placing this in the top level (see above)?
    lyrics = "twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."

    n = day_number

    if n < 1 or n > 12:
        raise ValueError("the number of day should be between 1 to 12")

    if n == 1:
        line = base_first_line.format(days[n]) + lyrics.split(", ")[-n:][0][4:]

        return line
    else:
        line = base_first_line.format(days[n]) + ", ".join(lyrics.split(", ")[-n:])

        return line


def recite(start_verse, end_verse):

    # exception check --- just for practice

    if start_verse > end_verse:
        raise ValueError("start_verse should less or equal to end_verse")

    if start_verse < 1 or end_verse < 1 or start_verse > 12 or end_verse > 12:
        raise ValueError("range should be between 1 to 12")
    # shirouto: Well, if you find this confusing, please ask me for more details.
    # python is a dynamical language. Type annotations (the things you saw me use)
    # are not used during runtime: the interpretor is simply ignoring them. That means
    # that despite the fact that the language has provisioned syntax for type annotation
    # it will *always* remain fundamentally a dynamical language. Your type check here is
    # code that runs at run time. It will always run. And it will always cost you a little bit.
    # The problem is that doing that at runtime does not give you anything. It simply croaks, which
    # it does anyway: even if you do not have this check, since you use start_verse and end_verse later
    # on to index in a list, if you do not have something that can pass as an integer, it will blow.
    # So this is entirely for the programmer benefit, right? Well, if that is the case.
    # the accepted, reasonable way of handling this in python is to do it in a way that brings no
    # penalty at run time: comments, docstrings, and/or type annotation. There is no point to
    # crippling production performance over programmer convenience. CPython is a horribly slow implementation anyway.
    # TLDR; don't do this.
    # 
    # That being said, first, type(1) == int. So why not write directly int? Wasting another function call? They are not
    # for free (they take CPU time) especially in python.
    # Second, python is an object oriented language. If you really, no matter what, you must do a type check at runtime
    # (read above before considering --- or please do not), you most likely want to check that the object type is int *or* 
    # any subclass of int. So you should use isinstance(start_verse, int) instead.

    if type(start_verse) != type(1) or type(end_verse) != type(1):
        raise TypeError("input should be an integer")

    lines = []

    # shirouto: well, this is not too shabby,... but. There are better ways:
    # * there are more ``pythonic'' ways of accomplishing this (might be a good time to read the Zen of Python, if you haven't done it).
    #   For example, use a list comprehension directly:
    # >>> [get_one_line(verse_count) for verse_count in range(start_verse, end_verse+1)]
    #
    # * you could improve the return time of the function, by precomputing the entire list of verses (outside this function, as a constant 
    # evaluated on module load, or even reading the list from a configuration file/data base you populated ahead of time using your
    # get_one_line function), and simply using start_verse/end_verse here only to slice into the list and return the result.
    # >>> all_verses[start_verse:end_verse+1]
    for day_number in range(start_verse, end_verse + 1):
        line = get_one_line(day_number)
        lines.append(line)

    return lines
