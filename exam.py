bagalar=[]
while True:
    x=input("Баға енгіз:")
    if x=="stop":
        break
    bagalar.append(int(x))
    if len(bagalar)>=4:
        arm=bagalar[0]
        m1=bagalar[1]
        m2=bagalar[2]
        exam=bagalar[3]
        r1=arm*0.6+m1*0.2+m2*0.2
        final_result=(r1+exam)/2
        print("R1:",r1)
        print("Қортынды баға:",final_result)
