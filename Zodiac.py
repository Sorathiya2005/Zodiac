# find Zodiac sign and symbol from given user input

male_zodiac=None
female_zodiac=None

print("Enter male's  Birth date and Birth month")
D=int(input('Day= '))
M=int(input('Month= '))

if (M==3 and D>=21) or (M==4 and D<=19):
    print('Zodiac sign is--> ARIES')
    print('zodiac symbol is--> THE RAM')
    male_zodiac=1
elif (M==4 and D>=20) or (M==5 and D<=20):
    print('Zodiac sign is--> TAURUS')
    print('zodiac symbol is--> THE BULL')
    male_zodiac=2
elif (M==5 and D>=21) or (M==6 and D<=20):
    print('Zodiac sign is--> GEMINI')
    print('zodiac symbol is--> THE TWINS')
    male_zodiac=3
elif (M==6 and D>=21) or (M==7 and D<=22):
    print('Zodiac sign is--> CANjCER')
    print('zodiac symbol is--> THE CRAB')
    male_zodiac=4
elif (M==7 and D>=23) or (M==8 and D<=22):
    print('Zodiac sign is--> LEO')
    print('zodiac symbol is--> THE LION')
    male_zodiac=5
elif (M==8 and D>=23) or (M==9 and D<=22):
    print('Zodiac sign is--> VIGRO')
    print('zodiac symbol is--> THE VIRGIN')
    male_zodiac=6
elif (M==9 and D>=23) or (M==10 and D<=22):
    print('Zodiac sign is--> LIBRA')
    print('zodiac symbol is--> THE SCALES')
    male_zodiac=7
elif (M==10 and D>=23) or (M==11 and D<=21):
    print('Zodiac sign is--> SCORPIO')
    print('zodiac symbol is--> THE SCORPION')
    male_zodiac=8
elif (M==11 and D>=22) or (M==12 and D<=21):
    print('Zodiac sign is--> SAGITTARIUS')
    print('zodiac symbol is--> THE ARCHER')
    male_zodiac=9
elif (M==12 and D>=22) or (M==1 and D<=19):
    print('Zodiac sign is--> CAPRICON')
    print('zodiac symbol is--> THE GOAT')
    male_zodiac=10
elif (M==1 and D>=20) or (M==2 and D<=18):
    print('Zodiac sign is--> AQUARIUS')
    print('zodiac symbol is--> THE WATER BEARE')
    male_zodiac=11
elif (M==2 and D>=19) or (M==3 and D<=20):
    print('Zodiac sign is--> PISCES')
    print('zodiac symbol is--> THE FISHESH')
    male_zodiac=12
else:
    print('wrong input')

print("Enter female's  Birth date and Birth month")
D=int(input('Date= '))
M=int(input('Month= '))

if (M==3 and D>=21) or (M==4 and D<=19):
    print('Zodiac sign is--> ARIES')
    print('zodiac symbol is--> THE RAM')
    female_zodiac=1
elif (M==4 and D>=20) or (M==5 and D<=20):
    print('Zodiac sign is--> TAURUS')
    print('zodiac symbol is--> THE BULL')
    female_zodiac=2
elif (M==5 and D>=21) or (M==6 and D<=20):
    print('Zodiac sign is--> GEMINI')
    print('zodiac symbol is--> THE TWINS')
    female_zodiac=3
elif (M==6 and D>=21) or (M==7 and D<=22):
    print('Zodiac sign is--> CANjCER')
    print('zodiac symbol is--> THE CRAB')
    female_zodiac=4
elif (M==7 and D>=23) or (M==8 and D<=22):
    print('Zodiac sign is--> LEO')
    print('zodiac symbol is--> THE LION')
    female_zodiac=5
elif (M==8 and D>=23) or (M==9 and D<=22):
    print('Zodiac sign is--> VIGRO')
    print('zodiac symbol is--> THE VIRGIN')
    female_zodiac=6
elif (M==9 and D>=23) or (M==10 and D<=22):
    print('Zodiac sign is--> LIBRA')
    print('zodiac symbol is--> THE SCALES')
    female_zodiac=7
elif (M==10 and D>=23) or (M==11 and D<=21):
    print('Zodiac sign is--> SCORPIO')
    print('zodiac symbol is--> THE SCORPION')
    female_zodiac=8
elif (M==11 and D>=22) or (M==12 and D<=21):
    print('Zodiac sign is--> SAGITTARIUS')
    print('zodiac symbol is--> THE ARCHER')
    female_zodiac=9
elif (M==12 and D>=22) or (M==1 and D<=19):
    print('Zodiac sign is--> CAPRICON')
    print('zodiac symbol is--> THE GOAT')
    female_zodiac=10
elif (M==1 and D>=20) or (M==2 and D<=18):
    print('Zodiac sign is--> AQUARIUS')
    print('zodiac symbol is--> THE WATER BEARE')
    female_zodiac=11
elif (M==2 and D>=19) or (M==3 and D<=20):
    print('Zodiac sign is--> PISCES')
    print('zodiac symbol is--> THE FISHESH')
    female_zodiac=12
else:
    print('wrong input')

if male_zodiac==None or female_zodiac==None:
    print('invalid')
else:
    if male_zodiac==1 and (female_zodiac in (1,3,5,7,9,11)):
        print("favourable")
    elif male_zodiac==1 and (female_zodiac in (2,6,8,12)):
        print("less favourable")
    elif male_zodiac==1 and (female_zodiac in (4,10)):
        print('critical')
    elif male_zodiac==2 and (female_zodiac in (2,4,6,8,10,12)):
        print("favourable")
    elif male_zodiac==2 and (female_zodiac in (1,3,7,9)):
        print("less favourable")
    elif male_zodiac==2 and (female_zodiac in (5,11)):
        print('critical')
    elif male_zodiac==3 and (female_zodiac in (1,3,5,7,9,11)):
        print('favourable')
    elif male_zodiac==3 and (female_zodiac in (2,4,8,10)):
        print('less favourable')
    elif male_zodiac==3 and (female_zodiac in (6,12)):
        print('critical')
    elif male_zodiac==4 and (female_zodiac in (2,4,6,8,10,12)):
        print('favouruble')
    elif male_zodiac==4 and (female_zodiac in (3,5,9,11)):
        print('less favourable')
    elif male_zodiac==4 and (female_zodiac in (1,7)):
        print('critical')
    elif male_zodiac==5 and (female_zodiac in (1,3,5,7,9,11)):
        print('favouruble')
    elif male_zodiac==5 and (female_zodiac in (4,6,10)):
        print('less favourable')
    elif male_zodiac==5 and (female_zodiac in (2,8,12)):
        print('critical')
    elif male_zodiac==6 and (female_zodiac in (2,4,6,8,10,12)):
        print('favouruble')
    elif male_zodiac==6 and (female_zodiac in (1,5,7,11)):
        print('less favourable')
    elif male_zodiac==6 and (female_zodiac in (3,9)):
        print('critical')
    elif male_zodiac==7 and (female_zodiac in (1,3,5,7,9,11)):
        print('favouruble')
    elif male_zodiac==7 and (female_zodiac in (2,6,8,12)):
        print('less favourable')
    elif male_zodiac==7 and (female_zodiac in (4,10)):
        print('critical')
    elif male_zodiac==8 and (female_zodiac in (2,4,6,8,10,12)):
        print('favouruble')
    elif male_zodiac==8 and (female_zodiac in (1,3,7,9)):
        print('less favourable')
    elif male_zodiac==8 and (female_zodiac in (5,11)):
        print('critical')
    elif male_zodiac==9 and (female_zodiac in (1,3,5,7,9,11)):
        print('favouruble')
    elif male_zodiac==9 and (female_zodiac in (2,4,8,10)):
        print('less favourable')
    elif male_zodiac==9 and (female_zodiac in (6,12)):
        print('critical')
    elif male_zodiac==10 and (female_zodiac in (2,4,6,8,10,12)):
        print('favouruble')
    elif male_zodiac==10 and (female_zodiac in (1,3,5,7,9,11)):
        print('critical')
    elif male_zodiac==11 and (female_zodiac in (1,3,5,7,9,11)):
        print('favouruble')
    elif male_zodiac==11 and (female_zodiac in (4,6,10,12)):
        print('less favourable')
    elif male_zodiac==11 and (female_zodiac in (2,8)):
        print('critical')
    elif male_zodiac==12 and (female_zodiac in (2,4,6,8,10,12)):
        print('favouruble')
    elif male_zodiac==12 and (female_zodiac in (1,5,7,11)):
        print('less favourable')
    elif male_zodiac==12 and (female_zodiac in (3,9)):
        print('critical')
    else:
        print('bye.....')
print('have a great day.... ')