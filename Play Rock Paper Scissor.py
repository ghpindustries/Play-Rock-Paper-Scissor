x = input().upper()
y = {'R','P','S'}.pop()
if (x=='R'and y=='S') or (x=='S' and y=='P')or(x=='P'and y=='R'):
   print(f"You Win!!!\n~~CONGRATS~~\n You:{x}\n Computer:{y}")
elif (y=='R'and x=='S') or (y=='S' and x=='P')or(y=='P'and x=='R'):
   print(f"You Lose!!!\n~~TRY AGAIN:-(~~\n You:{x}\n Computer:{y}")
elif x==y:print('===========\n====TIE====\n===========')
else:print('=====Error=====\nInput Format: R\n\tor\nInput Format: S\n\tor\nInput Format: P')
