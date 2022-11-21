message = "888884444466666235419999911111333332354177777222225555523541235418...84...46...67...69...91...13...37...67...72...25...57...67...6"
# !!!КЛЮЧИ!!!
KEYH = {"М": 0, "У": 0, "Н1": 0, "И1": 0, "Ц": 0, "И2": 0, "П": 0, "А": 0, "Л": 0, "Ь": 0, "Н2": 0, "Ы": 0, "Й": 0}
KEYV = {"Ц": 0, "Е": 0, "Н": 0, "Т": 0, "Р": 0}
# !!!КЛЮЧИ ДЛЯ СОЗДАНИЯ МАТРИЦЫ!!!
VerticalKey = ["Ц", "Е", "Н", "Т", "Р"]
HorisontalKey = ["М", "У", "Н", "И", "Ц", "И", "П", "А", "Л", "Ь", "Н", "Ы", "Й"]
# Матричный блок, инструменты
DESORTV = {"Ц": 0, "Е": 0, "Н": 0, "Т": 0, "Р": 0}
DESORTH = {"М": 0, "У": 0, "Н1": 0, "И1": 0, "Ц": 0, "И2": 0, "П": 0, "А": 0, "Л": 0, "Ь": 0, "Н2": 0, "Ы": 0, "Й": 0}
oncount = False
outstr = ""
MatrixBlock = []
BlankMass = []
j = 0
ja = 0


for i in message:
    j += 1
    ja += 1
    BlankMass.append(i)

    # Перебор
    if (ja < len(message)) and (len(MatrixBlock) == len(HorisontalKey)):
        oncount = True
        print(MatrixBlock)

    # Соответствие
    if j == len(VerticalKey):
        j = 0
        MatrixBlock.append(BlankMass)
        BlankMass = []

    if (len(MatrixBlock) == len(HorisontalKey)) or oncount:
        oncount = False
    
        # Вертикальная десортировка
        k = 0
        elem = []
        for got in sorted(KEYH):
            DESORTH[got] = MatrixBlock[k]
            k += 1
        MatrixBlock = []

        # Горизонтальная десортировка
        elements = list(DESORTH.items())
        
        k = 0
        elem = []
        elemout = []
        for elm in range(len(DESORTV)):
            for el in elements:
                if k < 5:
                    elem.append(el[1][k])
                if len(elem) == len(DESORTH):
                    elemout.append(elem)
                    elem = []
                    k += 1

        k = 0
        for got in sorted(KEYV):
            DESORTV[got] = elemout[k]
            k += 1

        # Преобразование в строку
        elements = list(DESORTV.items())
        for el in elements:
            for elms in el[1]:
                outstr += elms
print(outstr)
