# 2) Fibonacci

fbseq = [0, 1] # lista iniciada com os valores 0 e 1

num = int(input("Insira um número: ")) # para informar entrada de um número
while fbseq[-1] < num:
    fbprox = fbseq[-1] + fbseq[-2] # soma dos dois termos anteriores
    fbseq.append(fbprox) #adiciona o próximo número na lista

if num in fbseq:
    print(f'O número {num} inserido pertence a sequência de Fibonacci.')
else:
    print(f'O número {num} inserido não pertence a sequência de Fibonacci.')