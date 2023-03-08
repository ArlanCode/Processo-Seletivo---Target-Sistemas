import json

#Question 2
def fibonacci(num):
  num = int(num)

  if(num == 0):
    return f"O número '{num}' pertence a sequência de Fibonacci."
  
  elif(num >= 0):
    fibo_sequence = [0,1] #Armazena a sequência de Fibonacci
    
    while (fibo_sequence[-1] < num): #Cria a Fibonacci até chegar no número informado ou passa apenas um elemento da sequência
      fibo_sequence.append(fibo_sequence[-1] + fibo_sequence[-2])

    if (num == fibo_sequence[-1]): #Verifica se o número pertence a sequência de Fibonacci
      return f"O número '{num}' pertence a sequência de Fibonacci."
    else:
      return f"O número '{num}' Não pertence a sequência de Fibonacci."
    
  else:
    return "Informe um número inteiro e positivo!"

#print(fibonacci(13)) #Teste da Função



#Question 3
with open("dados.json", encoding='utf-8') as dados_json: 
    dados_mensal = json.load(dados_json)

def monthly_profit(dados):
  values = list(value['valor'] for value in dados if value['valor'] > 0) #Valores do faturamento diário da distribuidora
  values.sort()
  mean_values = sum(values) / len(values) #Faturamento médio
  better_days = sum((1 for value in values if value > mean_values)) #Quantidade de dias com faturamento acima da média

  return (f"Detalhamento Mensal:\n" +
          f"\nMenor faturamento ocorrido em um dia do mês: R${values[0]:.2f}" +
          f"\nMaior faturamento ocorrido em um dia do mês: R${values[-1]:.2f}" +
          f"\nNúmero de dias no mês em que o valor de faturamento diário foi superior à média mensal: {better_days} dias")

#print(monthly_profit(dados_mensal)) #Teste da Função



#Question 4
profit = [{"estado":"SP", "valor": 67836.43 },
          {"estado":"RJ", "valor": 36678.66 },
          {"estado":"MG", "valor": 29229.88 },
          {"estado":"ES", "valor": 27165.48 },
          {"estado":"Outros", "valor": 19849.53 }]

def percentage(dados):
  amount = sum((value['valor'] for value in dados)) #Valor total do faturamento da distribuidora
  profits = ""

  for item in dados:
    num_percent = item["valor"] * 100 / amount #Valor da porcetagem de cada estado
    profits += f"\n{item['estado']}: {num_percent:.2f}%"

  return "Percentual do Faturamento Mensal:\n" + profits
  
#print(percentage(profit)) #Teste da Função



#Question 5
def string_reverse(word):
  new_word = ""

  for letter in word:
    new_word = letter + new_word #Invertendo a String

  return(new_word)

#print(string_reverse("arlan")) #Teste da Função


#               - Code by @ArlanCode - 