message = "сообщение11свсообщение11свсообщение11свсообщение11св"
# !!!KEYS!!!
KM = ["Ц", "Е", "Н", "Т", "Р"]
KN = ["М", "У", "Н", "И", "Ц", "И", "П", "А", "Л", "Ь", "Н", "Ы", "Й"]
# matrix
matrix = []
KMN = []
    
    
# tools
score = 0
all_score = 0
blank_mass = []
message += "."

# cycle
for i in message:
    if len(KMN) == len(KM):
        score += 1
        all_score += 1
        blank_mass.append(i)
        matrix.append(KMN)
        KMN = []
    elif all_score == len(message)-1:
        if len(KMN) == len(KM):
            matrix.append(KMN)
        else:
            string_left = len(KM) - len(KMN)
            if string_left == 0:
                all_score += 1
                matrix.append(KMN)
            else:
                for k in range(string_left):
                    if len(blank_mass) == 0:
                        object_left = len(KN) - len(blank_mass)
                    elif len(blank_mass) > 0:
                        object_left = len(KN) - len(blank_mass)-1
                    if object_left == 0:
                        score += 1
                        all_score += 1
                        KMN.append(blank_mass)
                    else:
                        score += 1
                        all_score += 1
                        for j in range(object_left):
                            blank_mass.append(".")
                        KMN.append(blank_mass)
                matrix.append(KMN)
    else:  
        score += 1
        all_score += 1
        blank_mass.append(i)
        if score == len(KN):
            score = 0
            KMN.append(blank_mass)
            blank_mass = []







output = []
codedicthorizontal = {"Ц":0, "Е":0, "Н":0, "Т":0, "Р":0}

for i in matrix:
    codedicthorizontal["Ц"] = i[0]
    codedicthorizontal["Е"] = i[1]
    codedicthorizontal["Н"] = i[2]
    codedicthorizontal["Т"] = i[3]
    codedicthorizontal["Р"] = i[4]
    sorted_codedicthorizontal = dict(sorted(codedicthorizontal.items()))
    print(sorted_codedicthorizontal)



codedictvertical = {"М":0, "У":0, "Н":0, "И":0, "Ц":0, "И":0, "П":0, "А":0, "Л":0, "Ь":0, "Н":0, "Ы":0, "Й":0}

for i in sorted_codedicthorizontal:
    codedictvertical["М"] = i[0][0] + i[1][0] + i[2][0] + i[3][0] + i[4][0]
    codedictvertical["У"] = i[0][1] + i[1][1] + i[2][1] + i[3][1] + i[4][1]
    codedictvertical["Н"] = i[0][2] + i[1][2] + i[2][2] + i[3][2] + i[4][2]
    codedictvertical["И"] = i[0][3] + i[1][3] + i[2][3] + i[3][3] + i[4][3]
    codedictvertical["Ц"] = i[0][4] + i[1][4] + i[2][4] + i[3][4] + i[4][4]
    codedictvertical["И"] = i[0][5] + i[1][5] + i[2][5] + i[3][5] + i[4][5]
    codedictvertical["П"] = i[0][6] + i[1][6] + i[2][6] + i[3][6] + i[4][6]
    codedictvertical["А"] = i[0][7] + i[1][7] + i[2][7] + i[3][7] + i[4][7]
    codedictvertical["Л"] = i[0][8] + i[1][8] + i[2][8] + i[3][8] + i[4][8]
    codedictvertical["Ь"] = i[0][9] + i[1][9] + i[2][9] + i[3][9] + i[4][9]
    codedictvertical["Н"] = i[0][10] + i[1][10] + i[2][10] + i[3][10] + i[4][10]
    codedictvertical["Ы"] = i[0][11] + i[1][11] + i[2][11] + i[3][11] + i[4][11]
    codedictvertical["Й"] = i[0][12] + i[1][12] + i[2][12] + i[3][12] + i[4][12]

sorted_codedictvertical = dict(sorted(codedictvertical.items()))
print(sorted_codedictvertical)
