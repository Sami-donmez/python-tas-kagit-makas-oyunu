import random
kontrol=True
while(kontrol):
    seca=input("1-taş\n2-kagıt\n3-makas\n0-çıkış\n")
    secb=random.randint(1,3)
    
    if(len(seca)!=0):
        if(int(seca)==0):
            print("Oyunu oynadıgınız için teşekkür ederiz.İyi günler.")
            break
        elif(0<int(seca)<4):
            if(int(seca)==1):
                if(int(secb)==1):
                    print("1.Oyuncu: Taş \n Makine: Taş \n OYUN BERABERE")
                elif(int(secb)==2):
                    print("1.Oyuncu: Taş \n Makine: Kagıt \n MAKİNE KAZANDI")
                else:
                    print("1.Oyuncu: Taş \n Makine: Makas \n OYUNCU 1 KAZANDI ")
            elif(int(seca)==2):
                if(int(secb)==1):
                    print("1.Oyuncu: Kagıt \n Makine: Taş \n OYUNCU 1 KAZANDI ")
                elif(int(secb)==2):
                    print("1.Oyuncu: Kagıt \n Makine: Kagıt \n OYUN BERABERE")
                else:
                    print("1.Oyuncu: Kagıt \n Makine: Makas \n MAKİNE KAZANDI ")
            else:
                if(int(secb)==1):
                    print("1.Oyuncu: Makas \n Makine: Taş \n MAKİNE KAZANDI ")
                elif(int(secb)==2):
                    print("1.Oyuncu: Makas \n Makine: Kagıt \n OYUNCU 1 KAZANDI")
                else:
                    print("1.Oyuncu: Makas \n Makine: Makas \n OYUN BERABERE")
            
        else:
            print("hatalı secim")
        
    else:
        print("boş eleman girdiniz")
        kontrol=True
#exit()

