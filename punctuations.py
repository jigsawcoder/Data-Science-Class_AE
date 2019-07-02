def punc(str):
    punctuations = ''' !"#$%&'()*+,-./:;?@[\]^_`{|}~ '''
    for x in str.lower():
        if x in punctuations:
            str = str.replace(x, "")

    print(str)

str = " Welcome???@@##$ to#$% Geeks%$^for$%^&Geeks "
punc(str)
