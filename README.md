Simulador de Mutação Neural

Um script em Python que usa Biopython para simular uma mutação pontual em uma sequência de DNA e verificar seu impacto na proteína traduzida, no contexto de doenças neurofisiológicas.

Contexto

Criado no âmbito da pesquisa sobre bases neurofisiológicas de doenças neurais (como a Doença de Huntington), para simular como uma única troca de base no DNA pode ou não alterar a proteína resultante — um dos mecanismos centrais por trás de mutações associadas a doenças genéticas.

Como funciona

O script recebe uma sequência de DNA e usa a biblioteca Biopython para:

Traduzir a sequência original em proteína
Simular uma mutação pontual (troca de uma base em uma posição específica)
Traduzir a sequência mutada em proteína
Comparar as duas proteínas para classificar o tipo de mutação:
Silenciosa: a proteína não muda (a mutação não teve efeito funcional)
Missense/Nonsense: a proteína muda, indicando potencial impacto na função neural
Como rodar

Instale a dependência (caso ainda não tenha):

bash
pip install biopython

Execute o script:

bash
python simular_mutacao_neural.py
Exemplo de uso

Entrada (sequência de início de um canal iônico):

ATGGCCATTGTAATGGGCCGCTGA

Saída:

--- RESULTADOS DA SIMULAÇÃO ---
DNA Original:  ATGGCCATTGTAATGGGCCGCTGA
DNA Mutado:    ATGGCCATTGGAATGGGCCGCTGA (Mutação na pos 10: T->G)
------------------------------
Proteína Original: MAIVMGR
Proteína Mutada:   MAIVMGR

Resultado: Mutação Silenciosa (Não altera a função neurofisiológica).
Funcionalidades
Tradução de DNA em proteína usando Biopython
Simulação de mutação pontual em posição definida
Classificação automática do impacto da mutação (silenciosa vs. missense/nonsense)
Possíveis melhorias futuras
Permitir escolher a posição e a nova base via input do usuário
Simular múltiplas mutações em uma única execução
Adicionar suporte para identificar mutações nonsense (códon de parada prematuro) separadamente das missense
Tecnologias

Python, Biopython
