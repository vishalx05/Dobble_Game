import string
import random
symbols=[]
symbols=list(string.ascii_letters)
card1=[0]*5
card2=[0]*5
pos1=random.randint(0,4)
pos2=random.randint(0,4)
samesymbols=random.choice(symbols)
print(samesymbols)
if(pos1==pos2):
    card1[pos1]=samesymbols
else:
    card1[pos1]=samesymbols
    card2[pos2]=samesymbols
    card1[pos2]=random.choice(symbols)
    symbols.remove(card1[pos2])

    card2[pos1]=random.choice(symbols)
    symbols.remove(card2[pos1])

for i in range(0,5):
    if(i!=pos1 and i!=pos2):
        alphabet1=random.choice(symbols)

        symbols.remove(alphabet1)
        alphabet2=random.choice(symbols)
        symbols.remove(alphabet2)
        card1[i]=alphabet1
        card2[i]=alphabet2

print(card1)
print(card2)
ch=input("enter the guess")
if ch==samesymbols:
    print("right")
else:
    print("no")