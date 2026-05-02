from Bio.Seq import Seq # Importa a classe 'Seq', que entende que o texto é um dado biológico, não apenas letras.
from Bio.Data import CodonTable

def simular_mutacao_neural(sequencia_dna): #define função
    # 1. Sequência Original
    dna_original = Seq(sequencia_dna) #Transforma a string (texto) que você digitou em um objeto de sequência oficial do Biopython.
    proteina_original = dna_original.translate(to_stop=True)
    
    # 2. Simular uma mutação pontual (Ex: Trocar a base na posição 10 de A para G)
    # Isso pode simular um polimorfismo associado a uma doença neural
    lista_dna = list(dna_original)
    posicao = 9  # Lembre-se que Python começa a contar do 0
    base_antiga = lista_dna[posicao]
    lista_dna[posicao] = "G" 
    dna_mutado = Seq("".join(lista_dna))
    
    # 3. Traduzir a nova sequência
    proteina_mutada = dna_mutado.translate(to_stop=True)
    
    print("--- RESULTADOS DA SIMULAÇÃO ---")
    print(f"DNA Original:  {dna_original}")
    print(f"DNA Mutado:    {dna_mutado} (Mutação na pos {posicao+1}: {base_antiga}->G)")
    print("-" * 30)
    print(f"Proteína Original: {proteina_original}")
    print(f"Proteína Mutada:   {proteina_mutada}")
    
    if proteina_original == proteina_mutada:
        print("\nResultado: Mutação Silenciosa (Não altera a função neurofisiológica).")
    else:
        print("\nResultado: Mutação Missense/Nonsense (Potencial impacto na função neural!)")

# Exemplo: Uma sequência de início de um canal iônico
seq_exemplo = "ATGGCCATTGTAATGGGCCGCTGA"
simular_mutacao_neural(seq_exemplo)