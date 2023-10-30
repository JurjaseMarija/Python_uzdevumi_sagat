"""
Papildināt programmu ar ciklu, kurā sarakstā esošiem uzvārdiem tiktu 
pievienots klāt doktora nosaukums - Dr.
"""
""""
# 1.variants
saraksts1=["Kalniņš", "Opmanis", "Vēzis", "Almane"]
sarakts2=[]

for uzvards in saraksts1:
    doktors="Dr. "+uzvards
    sarakts2.append(doktors)

    print(sarakts2)



""""

 # 2.variants
saraksts1=["Kalniņš", "Opmanis", "Vēzis", "Almane"]

def pievienot_dokt(uzvards):
    return "Dr. "+uzvards

saraksts2=list(map(pievienot_dokt, saraksts1))
print(saraksts2)
