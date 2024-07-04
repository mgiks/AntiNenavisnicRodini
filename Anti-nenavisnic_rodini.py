def fix():
        hash = {"киргизия": ["Кыргызстан"],
                "киргизии":["Кыргызстана","Кыргызстану","Кыргызстане"],
                "киргизию":["Кыргызстан"],
                "киргизией":["Кыргызстаном"],
                "киргизиею":["Кыргызстаном"],
                "киргизский":["Кыргызский"]}
        #Range of cirillic characters 
        uni_val = range(1040, 1104)
        KR = input("Текст ебашь: ")
        output = KR

        dot_ind = 0
        l = 0
        r = 1

        if len(KR) == 0:
                return KR

        while r < len(KR):
                while r < len(KR) and ord(KR[r]) in uni_val:
                        if KR[r] == ".":
                                dot_ind = r
                        r += 1

                word = KR[l:r]
                loweredWord = word.lower()
                if loweredWord in hash.keys():
                        if word.lower() == "киргизии":
                                sentence = KR[dot_ind: r]
                                print(f"\nПроблема здесь:")
                                print(sentence)
                                print(f"\nТут спорно, отсюда варианты {hash['киргизии']}")
                                choice = int(input("Выбирай(1,2,3): "))
                                output = output.replace(word, hash[loweredWord][choice - 1])
                        else:
                                output = output.replace(word, hash[loweredWord][0])
                
                r += 1
                l = r

        return output

fix()