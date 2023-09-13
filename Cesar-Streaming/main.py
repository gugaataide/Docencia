from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

def logar(navegador):
    navegador.get('http://testezap.clubetv.xyz/login.php')  # Substitua 'URL_DA_PÁGINA_DE_LOGIN' pela URL real
    user = navegador.find_element('xpath', '//*[@id="usuario"]')
    senha = navegador.find_element('xpath', '//*[@id="senha"]')

    user.send_keys('admin')
    senha.send_keys('Cc150602117700@')

    botao_login = navegador.find_element('xpath', '//*[@id="FormLogin"]/div[3]/div[2]/button')
    botao_login.click()
    sleep(5)
    
    senha2 = navegador.find_element('xpath', '//*[@id="usuario"]')
    senha2.send_keys('tomatesverdesfritos')
    botao_login.click()
    
    
logar(navegador)

# Depois de fazer login, você pode continuar com outras ações no site
# ...

# Feche o navegador após o uso








'''

#Automação do download das planilhas

lista_contatos = pd.read_csv('/Users/guga/Downloads/Planilha sem título - Página1-2.csv')

navegador.get("https://web.whatsapp.com")

while len(navegador.find_elements('id', 'side')) < 1:
    sleep(1)
    
#entrou no wpp

mensagem = input('Digite a mensagem a ser enviada: ')

for i, m in enumerate(lista_contatos["pessoa"]):
    pessoa = lista_contatos.loc[i, "pessoa"]
    numero = lista_contatos.loc[i,"numero"]
    texto = urllib.parse.quote(f'Olá,{pessoa}! {mensagem}')
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    navegador.get(link)
    while len(navegador.find_elements('id', 'side')) < 1:
        sleep(1)
        
    navegador.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div').send_keys(Keys.ENTER)
    sleep(5)
'''