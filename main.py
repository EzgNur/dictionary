meme_dict = {
    "LOL": "Komik bir şeye verilen cevap",
    "CRINGE": "Garip ya da utandırıcı bir şey",
    "ROFL": "Bir şakaya karşılık cevap",
    "SHEESH": "Onaylamamak",
    "CREEPY": "Korkunç",
    "AGGRO": "Agresifleşmek/sinirlenmek"
}

word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
    print(word, "kelimesinin anlamı: " ,meme_dict[word])
    
    #print({word} "kelimesinin anlamı:" {meme_dict[word]})
else:
    print("Sözlükte böyle bir kelime yok!")
