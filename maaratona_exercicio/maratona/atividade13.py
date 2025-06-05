num=int(input("digite um numero de 1 a 3999: "))
if 1 <= num <=3999:
    valores=[(1000,"m"),(900,"cm"),(500,"d"),(400,"cd"),(100,"c"),(90,"xc"),(50,"L"),(40,"xl"),(10,"x"),(9,"ix"),(5,"v"),(4,"iv"),(1,"i")]
    romano=""
    i=0

    while i < len(valores):
        valor= valores[i][0]
        simbolo= valores[i][1]
        while num >= valor:
            romano=romano+simbolo 
            num=num -valor 
        i=i+1
    print("numero romano: ",romano)
else:
    print("numero fora do intervalo.")