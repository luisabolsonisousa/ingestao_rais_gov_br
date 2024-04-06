# ingestao_rais_gov_br

site do governo utilizado para fazer as ingestões: https://bi.mte.gov.br/bgcaged/
-------------------------- 
Login:                   
    Usuário - basico
    SENHA - 12345678
--------------------------

Rais -> rais vinculo -> escolher a estrutura que voce deseja para seus dados (pegue apenas de um ano, o processo de ingestao vai trazer o range que voce deseja) -> APENAS APOS O SITE CONSEGUIR CARREGAR OS DADOS -> dentro das ferramentas de desenvolvedor no website -> dardoweb.cgi -> capturar o payload na versao source para colocar no seu dict para inserir na funcao

IMPORTANTE : no payload que voce capturou vem o ano que vc fez o pedido no site por exemplo 2022 - renomeie ele para ANOVARIAVEL


aqui um exemplo das entradas que voce pode utilizar:

-------------------------------------------------------------------------------------------------------------------------
start = 2006
final = 2022
queries = {
            #"idade":f"NT=86301101&EA=https%3A%2F%2Fbi.mte.gov.br%2Fbgcaged%2Fcaged_rais_vinculo_id%2F&EC=0%3B7C725A%3BBAB19E%3BD9D6CA%3BF0EEDB&AQ=caged_rais_vinculo_basico_tab.par&AC=1&XC=1&IN=1&UM=1&UU=0&US=basico&DF=https%3A%2F%2Fbi.mte.gov.br%2Fbgcaged%2Fcaged_rais_vinculo_id%2Fcaged_rais_vinculo_basico_tab.php&ND=&CJ=Base+de+Gest%E3o+do+MTE%3A%3ACAGED&LI=Capital&V1=Ano+inicial&V2=Ano+final&CO=Sexo+Trabalhador&V3=Ano+inicial&V4=Ano+final&UB=Faixa+Et%E1ria&V9=Ano+inicial&V0=Ano+final&QU=---------N%E3o---------&V5=Ano+inicial&V6=Ano+final&SL=Faixa+Remun+M%E9dia+%28SM%29&V7=Ano+inicial&V8=Ano+final&CN=-%3EFrequ%EAncia&CE1=Soma&TT=&IU=&OL=SemOrdem&OC=SemOrdem&OQ=SemOrdem&PL=&YZAno=0&YCAno=%22ANOVARIAVEL%22%3ANOME%3BANOVARIAVEL&YZV%EDnculo+Ativo+31%2F12=0&YCV%EDnculo+Ativo+31%2F12=%221%22%3ANOME%3BSim"
            }
-------------------------------------------------------------------------------------------------------------------------


Apos definir seus parametros chame rode o notebook e chame a funcao com seus parametros dessa forma:
ingestao_rais(start,final,queries)


-------------------------------------------------------------------------------------------------------------------------

Isso vai gerar arquivos com o range de ano que voce escolheu dentro da pasta que voce esta rodando o codigo

PS: tem algumas variaveis no rais que tem limite de data ou comecam em 2005 se voce selecionar elas e colocar um range fora o codigo vai dar erro


Install libs:
pip install BeautifulSoup4
pip install urllib3

Eu utilizei o kernel 3.11.4 python

---*---*----*-----*----*

Obrigada por utilizar, estou constantemente tentando achar um tempo para melhorar o codigo e trazer logs de erro para vós orientar melhorar ao usar o codigo, o tempo é limitado tenham paciencia com minha pessoa :P 

Caso queiram ajudar entrem em contato ;)

Muito obrigada! Se usarem o codigo por favor lembrem-se de dar os créditos pra mim, é muito importante!
