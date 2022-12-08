print("\n"," BMI kalkulačka", "\n", 16 * "=")

def bmi_kalkulacka(jmeno = input("Jak na tebe volají? ") , 
                   vaha  = int(input("Zadej svou váhu: ")), 
                   vyska = float(input("Zadej svou výšku v centimetrech: "))):
    vyska = vyska / 100
    bmi = vaha / vyska ** 2
    
    if bmi < 18.5:
        print(f"\n{jmeno} tvé BMI je {round(bmi,2)}, což spadá do kategorie 'PODVÍŽIVA'.\n{57 * '-'}")
    elif 18.5 <= bmi <= 25:
        print(f"\n{jmeno} tvé BMI je {round(bmi,2)}, což spadá do kategorie 'ZDRAVÁ VÁHA'.")
    elif 25 <= bmi <=30:
        print(f"\n{jmeno} tvé BMI je {round(bmi,2)}, což spadá do kategorie 'MÍRNÁ NADVÁHA'.")
    elif 30 <= bmi <= 40:
        print(f"\n{jmeno} tvé BMI je {round(bmi,2)}, což spadá do kategorie 'OBEZITA'.")
    else:
        print(f"\n{jmeno} tvé BMI je {round(bmi,2)}, což spadá do kategorie 'TĚŽKÁ OBEZITA'.")
                    
bmi_kalkulacka()