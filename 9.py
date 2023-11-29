dicionario = {

}

quantidade_dados = int(input("Digite quantos dados quer ter na agenda: "))
contador = 0
while contador < quantidade_dados:
    nome = input("\nDigite seu nome: ").strip()
    idade = input("Digite sua idade: ").strip()
    telefone = input("Digite seu telefone: ").strip()
    cpf = input("Digite seu cpf: ").strip()

    dicionario[nome] = []
    dicionario[nome].append({
        "nome":nome,
        "cpf":cpf,
        "idade":idade,
        "telefone":telefone
    })

    contador += 1

for nome, listaDados in dicionario.items():
    print(f"Dados da pessoa {nome}")
    for dadosPessoas in listaDados:
        for chave, valor in dadosPessoas.items():
            print(f"Chave: {chave}, Valor: {valor}")