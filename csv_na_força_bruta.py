#arquivo no meu disco --> 'C:/Users/arthu/OneDrive/Área de Trabalho/spyder_trab/data/dados.csv'

with open('dados.csv', 'r') as f:
    results = []
    count = 1
    for line in f:
            words = line.split(',')
            results.append((words[0], words[1]))
 
climadict= {}

for dado in results:
    ano=int(dado[0])
    tmed=float(dado[1])
    climadict[ano] = tmed

#PARA menor, maior, medglob
menor = min(climadict.values())
value = menor
chave = list(climadict.keys())[list(climadict.values()).index(24.20)]
maior = max(climadict.values())
value1 = maior
chave1 = list(climadict.keys())[list(climadict.values()).index(25.97)]
medglob = sum(climadict.values())/len(climadict.values())


while True:
    x= input()
    dado = [(int(ano), float(tmed)) for ano, tmed in results]
        
    if x.find("menor") != -1:
        print(f'{chave} {format(value, ".2f")}')
        break
        
    if x.find("maior") != -1:
        print(f'{chave1} {format(value1, ".2f")}')
        break
        
    if x.find("medglob") != -1:
        print(f'{format(medglob, ".2f")}' )
        break
    
    if x.find("media") != -1:
       start_year = int(input())
       end_year = int(input())
       # Filter the data to include only the selected range of years
       filtered_dado = [(ano, tmed) for ano, tmed in dado if start_year <= ano <= end_year]
       # Calculate the mean temperature for the selected range of years
       total_temperature = sum(tmed for _, tmed in filtered_dado)
       num_years = len(filtered_dado)
       media = total_temperature / num_years if num_years > 0 else 0
       print(f'{media:.2f}')
       break
    
    if x.find("meddec") != -1:
        year_start = int(input())
        years_per_group = 10
        # Calculate the mean temperature for each ten-year period
        for i in range(year_start, year_start + 10, years_per_group):
            end_year = min(i + years_per_group - 1, 2021)  # Ensure the end year does not exceed 2021
            filtered_dado = [(ano, tmed) for ano, tmed in dado if i <= ano <= end_year]
            total_temperature = sum(tmed for _, tmed in filtered_dado)
            num_years = len(filtered_dado)
            meddec = total_temperature / num_years if num_years > 0 else 0
        print(f"{meddec:.2f}")
        break
    
    if x.find("varini") != -1:
        for i in climadict.values():
            print(format(i-24.91, ".2f"))
        break

  
