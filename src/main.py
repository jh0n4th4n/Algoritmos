from fatorial import calcular_fatorial
from fibonacci import gerar_fibonacci
from primos import eh_primo
from ordenacao import ordenar_lista
from palindromo import eh_palindromo
from mdc_mmc import calcular_mdc_mmc
from busca_linear import busca_linear
from quicksort import quicksort
from contagem_vogais import contar_vogais
from inverter_string import inverter_string
from potencia import potencia
from numero_perfeito import numero_perfeito
from busca_binaria import busca_binaria
from fatorial_recursivo import calcular_fatorial_recursivo
from decimal_binario import decimal_para_binario
from mergesort import mergesort
from hanoi import resolver_hanoi
from pilha import Pilha


def menu():
    print("=== Resolvendo Algoritmos com GitHub Copilot ===")
    print("1  - Calcular fatorial (iterativo)")
    print("2  - Gerar sequência de Fibonacci")
    print("3  - Verificar se um número é primo")
    print("4  - Ordenar lista (Bubble Sort)")
    print("5  - Verificar se é palíndromo")
    print("6  - Calcular MDC e MMC")
    print("7  - Busca linear")
    print("8  - Ordenar lista (QuickSort)")
    print("9  - Contar vogais de um texto")
    print("10 - Inverter string")
    print("11 - Calcular potência")
    print("12 - Verificar número perfeito")
    print("13 - Busca binária")
    print("14 - Calcular fatorial (recursivo)")
    print("15 - Converter decimal para binário")
    print("16 - Ordenar lista (MergeSort)")
    print("17 - Torre de Hanói")
    print("18 - Demonstração de Pilha (Stack)")
    print("0  - Sair")


def ler_inteiro(mensagem: str) -> int:
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")


def ler_lista_inteiros(mensagem: str) -> list[int]:
    while True:
        entrada = input(mensagem).strip()
        try:
            return [int(x) for x in entrada.split()]
        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros separados por espaço.")


def main():
    while True:
        print()
        menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            n = ler_inteiro("Digite um número inteiro não negativo: ")
            try:
                print(f"Fatorial de {n} é {calcular_fatorial(n)}")
            except ValueError as e:
                print(f"Erro: {e}")

        elif opcao == "2":
            n = ler_inteiro("Quantos termos da sequência de Fibonacci você deseja? ")
            try:
                print(f"Sequência de Fibonacci: {gerar_fibonacci(n)}")
            except ValueError as e:
                print(f"Erro: {e}")

        elif opcao == "3":
            n = ler_inteiro("Digite um número inteiro: ")
            print(f"{n} é primo." if eh_primo(n) else f"{n} não é primo.")

        elif opcao == "4":
            lista = ler_lista_inteiros("Digite números inteiros separados por espaço: ")
            print(f"Lista ordenada (Bubble Sort): {ordenar_lista(lista)}")

        elif opcao == "5":
            texto = input("Digite uma palavra ou frase: ")
            print("É palíndromo!" if eh_palindromo(texto) else "Não é palíndromo.")

        elif opcao == "6":
            a = ler_inteiro("Digite o 1º número: ")
            b = ler_inteiro("Digite o 2º número: ")
            resultado = calcular_mdc_mmc(a, b)
            print(f"MDC({a},{b})={resultado['MDC']} | MMC({a},{b})={resultado['MMC']}")

        elif opcao == "7":
            lista = ler_lista_inteiros("Digite os números: ")
            valor = ler_inteiro("Digite o valor a buscar: ")
            print("Encontrado!" if busca_linear(lista, valor) else "Não encontrado.")

        elif opcao == "8":
            lista = ler_lista_inteiros("Digite os números: ")
            print(f"Ordenado (QuickSort): {quicksort(lista)}")

        elif opcao == "9":
            texto = input("Digite um texto: ")
            print(f"Quantidade de vogais: {contar_vogais(texto)}")

        elif opcao == "10":
            texto = input("Digite uma string: ")
            print(f"Invertida: {inverter_string(texto)}")

        elif opcao == "11":
            base = ler_inteiro("Base: ")
            exp = ler_inteiro("Expoente: ")
            print(f"{base}^{exp} = {potencia(base, exp)}")

        elif opcao == "12":
            n = ler_inteiro("Digite um número: ")
            print("Número perfeito!" if numero_perfeito(n) else "Não é número perfeito.")

        elif opcao == "13":
            lista = ler_lista_inteiros("Digite os números: ")
            valor = ler_inteiro("Valor a buscar: ")
            print("Encontrado!" if busca_binaria(lista, valor) else "Não encontrado.")

        elif opcao == "14":
            n = ler_inteiro("Digite um número: ")
            print(f"[Recursivo] Fatorial: {calcular_fatorial_recursivo(n)}")

        elif opcao == "15":
            n = ler_inteiro("Digite um número: ")
            print(f"{n} em binário: {decimal_para_binario(n)}")

        elif opcao == "16":
            lista = ler_lista_inteiros("Digite os números: ")
            print(f"Ordenado (MergeSort): {mergesort(lista)}")

        elif opcao == "17":
            n = ler_inteiro("Quantidade de discos: ")
            if n > 0:
                movimentos = resolver_hanoi(n, "A", "B", "C")
                print(f"Movimentos ({len(movimentos)}):")
                for mov in movimentos:
                    print(mov)
            else:
                print("Número de discos deve ser maior que zero.")

        elif opcao == "18":
            print("=== Demonstração de Pilha ===")
            pilha = Pilha()
            print("Digite valores (Enter para finalizar):")
            while True:
                item = input("Valor: ")
                if item.strip() == "":
                    break
                try:
                    pilha.empilhar(int(item))
                except ValueError:
                    print("Digite somente números!")
            print(f"Pilha criada: {pilha}")
            print("Desempilhando...")
            while not pilha.esta_vazia():
                print("->", pilha.desempilhar())
            print("Pilha vazia!")

        elif opcao == "0":
            print("Saindo... Obrigado por utilizar o programa!")
            break

        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
