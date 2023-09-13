from selenium import webdriver

caminho_arquivo = "arquivo.txt"

# Inicializar o navegador
driver = webdriver.Chrome()  # Certifique-se de ter o ChromeDriver instalado e configurado

# Abrir uma página da web
url = 'https://pt.wikipedia.org/wiki/Brasil'  # Substitua pela URL da página que contém a tabela
driver.get(url)

# Localizar a tabela por um seletor CSS ou XPath adequado
table_element = driver.find_element('xpath','//*[@id="mw-content-text"]/div[1]/table[1]')  # Substitua pelo seletor correto

# Obter o conteúdo HTML da tabela
table_html = table_element.get_attribute('outerHTML')

# Imprimir o conteúdo HTML da tabela
print(table_html.count('<tr>'))


# Fechar o navegador
driver.quit()

with open(caminho_arquivo, 'w') as arquivo:
    arquivo.write(table_html)
