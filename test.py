d = {
    'Армия': ['майор', "танк"],
    'Про студентов': ['студент', 'универ', 'декан'],
    'Медицинские': ['шприц']
}

text = 'Лёд по ногами майора'
for cat in d:
    keywords = d[cat]
#    print(cat,keywords)
    for keyword in keywords:
        if keyword in text:
            print(cat)
 #           return(cat)
