year = int(input())
happy_year_codition = False

while not happy_year_codition:
    year += 1
    set_year = set()

    for i in range(len(str(year))):
        set_year.add(str(year)[i])

    happy_year_codition = len(set_year) == len(str(year))

print(year)