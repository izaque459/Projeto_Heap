import heapq
from palavras import palavras


def heapsort(input_list):
    tam = len(input_list)
    
    h = []
    output_list = []
    for i in range(0,tam):
        heapq.heappush(h,input_list[i])
    
    for i in range(0,tam):
        output_list.append(heapq.heappop(h))

    return output_list



teste = sorted(palavras)

print("\n Palavras em ordem qualquer \n")
print(palavras)

palavras_ordenadas = heapsort(palavras)
print("\n Palavras ordenadas pelo algoritmo HeapSort \n")
print(palavras_ordenadas)

if palavras_ordenadas == teste:
    print(" \nPalavras ordenadas corretamente\n")
else:
    print(" \n Palavras ordenadas incorretamente \n")