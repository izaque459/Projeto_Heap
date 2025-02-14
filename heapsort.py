


def heapsort(input_list):
    tam = len(input_list)
    
    h = []
    output_list = []
    for i in range(0,tam):
        heapq.heappush(h,input_list[i])
    
    for i in range(0,tam):
        output = heappop(h)

    return output_list

lista_ordenada_python = sorted(lista_para_ordenar)
if lista_ordenada == lista_ordenada_python:
    print("\nOrdenação correta!")
else:
    print("\nOrdenação INCORRETA!")