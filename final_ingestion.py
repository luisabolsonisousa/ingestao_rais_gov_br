import requests
import os
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# URL do endpoint
url = "https://bi.mte.gov.br/scripts10/dardoweb.cgi"
path_current_folder  = os.getcwd()

def ingestao_rais(start, end, queries):    
    with requests.Session() as session:
        session.verify = False  # Desabilitar a verificação SSL
        for chave, valor in queries.items():
            folder_name = chave
            print(folder_name)
            for i in range(start, end):
                ano_variavel = i
                print(i)
                query_string = valor
                # Substitui {ano_variavel} pelo valor de ano_variavel
                query_string = query_string.replace("ANOVARIAVEL", str(ano_variavel))
                print(query_string)
                # Envia a solicitação POST
                response = session.post(url, data=query_string)

                # Resposta do servidor
                html = response.text

                soup = BeautifulSoup(html, 'html.parser')

                link_original = soup.find('frame', {'name': 'tabela'}).get('src')

                link_csv = link_original[:-5] + ".csv"

                # Link do arquivo CSV
                url_csv = link_csv

                # Faz o download do arquivo
                response_csv = session.get(url_csv)

                # Caminho do diretório local onde você deseja salvar o arquivo
                diretorio_local = f"{path_current_folder}/{folder_name}"

                # Se o diretório não existir, cria-o
                if not os.path.exists(diretorio_local):
                    os.makedirs(diretorio_local)

                # Caminho completo do arquivo local
                caminho_local = os.path.join(diretorio_local, f"{folder_name}_{ano_variavel}.csv")
                print(f"Valor de ano_variavel: {ano_variavel}")

                # Verifica se o download foi bem-sucedido (código de status 200)
                if response_csv.status_code == 200:
                    # Salva o conteúdo no arquivo local com o nome desejado
                    with open(caminho_local, 'wb') as file:
                        file.write(response_csv.content)
                    print(f"Download concluído. Arquivo salvo em {caminho_local}")
                else:
                    print(f"Erro ao baixar o arquivo. Código de status: {response_csv.status_code}")


