import requests  # Biblioteca para fazer requisições HTTP, como acessar APIs.

# Função para converter de dólar (ou outra moeda base) para real
def conversao_dolar_em_real(valor, taxa_cambio_base, moeda):
    # Calcula o valor convertido e arredonda para 2 casas decimais
    valor_dolar_em_real = round(valor * taxa_cambio_base, 2)
    # Exibe o valor convertido
    print(valor, f"{moeda} em real:", valor_dolar_em_real, "R$")

# Função para converter de real para dólar (ou outra moeda base)
def conversao_real_em_dolar(valor, taxa_cambio_base, moeda):
    # Calcula o valor convertido e arredonda para 2 casas decimais
    valor_real_em_dolar = round(valor / taxa_cambio_base, 2)
    # Exibe o valor convertido
    print(valor, f"R$ em {moeda}:", valor_real_em_dolar, f"{moeda}")

# Função para trocar a moeda base
def trocar_moeda_base(moeda):
    try:
        # Faz a requisição para a API com a moeda base especificada
        url = f"https://v6.exchangerate-api.com/v6/85c84e455130e641dbb62b51/latest/{moeda}"
        response = requests.get(url)  # Requisição GET para obter os dados
        data = response.json()  # Converte a resposta para JSON
        # Obtém a taxa de câmbio do real em relação à moeda base
        taxa_cambio_base = data["conversion_rates"]["BRL"]
        return taxa_cambio_base  # Retorna a taxa de câmbio
    except requests.exceptions.RequestException as e:
        # Captura erros de conexão ou requisição e exibe uma mensagem
        print(f"Erro ao acessar a API: {e}")
        return None

# Função para exibir o menu de troca de moeda base
def menu_trocar_moeda_base():
    # Exibe as opções de moedas disponíveis para troca
    print("\n" + "="*30)
    print("      TROCAR MOEDA BASE")
    print("="*30)
    print("[1] USD - Dólar Americano")
    print("[2] EUR - Euro")
    print("[3] BRL - Real Brasileiro")
    print("[4] GBP - Libra Esterlina")
    print("[5] JPY - Iene Japonês")
    print("[6] CAD - Dólar Canadense")
    print("[7] AUD - Dólar Australiano")
    print("[0] Cancelar e voltar")
    print("="*30)
    while True:
        try:
            # Dicionário que mapeia as opções para os códigos de moedas
            moedas_padroes = {
                1: "USD",
                2: "EUR",
                3: "BRL",
                4: "GBP",
                5: "JPY",
                6: "CAD",
                7: "AUD"
            }
            # Solicita ao usuário que escolha uma moeda
            moeda = int(input("Digite o valor correspondente à moeda desejada: "))
            if moeda in moedas_padroes:
                return moedas_padroes[moeda]  # Retorna a moeda selecionada
            elif moeda == 0:
                print("Voltando ao menu...")
                return None  # Retorna ao menu principal
            else:
                print("Digite um valor válido!")
        except ValueError:
            # Trata entradas inválidas que não podem ser convertidas em inteiro
            print("DIGITE VALORES VÁLIDOS!")

# Função principal para iniciar o programa
def comecar():
    try:
        # Configura a moeda padrão como USD (Dólar Americano)
        url = f"https://v6.exchangerate-api.com/v6/85c84e455130e641dbb62b51/latest/USD"
        response = requests.get(url)  # Faz a requisição para a API
        data = response.json()  # Converte a resposta para JSON
        taxa_cambio_base = data["conversion_rates"]["BRL"]  # Taxa padrão para BRL
        moeda = "USD"  # Define a moeda base padrão
    except requests.exceptions.RequestException as e:
        # Exibe mensagem de erro se não conseguir acessar a API
        print(f"Erro ao acessar a API: {e}")
        return None

    while True:
        # Exibe o menu principal do conversor
        print("\n" + "="*30)
        print("         CONVERSOR DE MOEDAS")
        print(f"A moeda Base atual é {moeda}")
        print("="*30)
        print(f"[1] Converter {moeda} para REAL")
        print(f"[2] Converter REAL para {moeda}")
        print("[3] Trocar moeda base")
        print("[0] Sair")
        print("="*30)

        try:
            # Solicita a escolha do usuário
            escolha_usuario = int(input("Digite a escolha: "))

            if escolha_usuario not in [0, 1, 2, 3]:
                print("Digite uma opção válida!")

            elif escolha_usuario in [1, 2]:
                # Verifica se há uma taxa de câmbio disponível
                if taxa_cambio_base is None:
                    print("Erro: Nenhuma taxa de câmbio disponível. Troque a moeda base.")
                    continue
                valor = float(input("Digite o valor que gostaria de converter: "))
                # Valida se o valor é positivo
                if valor <= 0:
                    print("Erro: O valor deve ser maior que zero.")
                    continue
                # Realiza a conversão com base na escolha do usuário
                if escolha_usuario == 1:
                    conversao_dolar_em_real(valor, taxa_cambio_base, moeda)
                else:
                    conversao_real_em_dolar(valor, taxa_cambio_base, moeda)

            elif escolha_usuario == 3:
                # Permite ao usuário trocar a moeda base
                nova_moeda = menu_trocar_moeda_base()
                if nova_moeda:
                    moeda = nova_moeda
                    taxa_cambio_base = trocar_moeda_base(moeda)

            elif escolha_usuario == 0:
                # Encerra o programa
                print("Obrigado por usar o Conversor de Moedas. Até logo!")
                break

        except ValueError:
            # Trata erros de entrada inválida
            print("O valor está inválido!")

# Inicia o programa
comecar()

