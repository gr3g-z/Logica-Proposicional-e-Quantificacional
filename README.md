# Lógica Proposicional e Quantificacional
## introdução
Esse repositório contém uma implementação simples de lógica proposicional e quantificacional. Nesse código, é possível criar bases de crenças e neles adicionar suas crenças, seguindo alguns formatos de frases que foram pré-determinados: 
    
<img align="Center" src="img/Formulas.png" width="75%" >

Você pode adicionar frases que seguem esses dez casos que estão na coluna 'frase' para preencher a sua base de crenças da forma que você quiser. Apesar de não estar representado na tabela você pode usar também substantivos femininos, e portanto pode usar também 'Alguma', 'Todas', 'Toda' e 'Nenhuma' nas suas frases. Para isso tudo funcionar, nos criamos um tradutor que transforma o texto da linguagem humana para a linguagem que a biblioteca nltk utiliza, podemos ver isso representado nas outras duas colunas da tabela. 

## Regras da base de crenças

O popósito da base de crenças e basicamente garantir que uma série de crenças não seja conflitantes entre eles, de uma forma que, uma crença só pode ser adicionada a base se não tiver nenhum tipo de conflito com as crenças que já se encontram na base, segue abaixo os quatro casos de crenças que não são adicionadas: 


1.  **Se a crença for uma tautologia:**

       Nesses Casos entrega um erro falando: 'Sua crença não será adicionada na base por ser uma Tautologia'

       *Exemplo:* Todo mortal é mortal


2.  **Se a crença for uma contradição:**

       Nesses Casos entrega um erro falando: 'Sua crença não será adicionada na base por ser uma Contradição'

       *Exemplo:* Algum mortal não é mortal


3.  **Se a nova crença que você quer adicionar é uma conclusão das crenças que já existem na base, ou seja, redundante:**
   
      Nesses Casos entrega um erro falando: 'Sua crença não será adicionada na base por ser redundante e não trazer valor informacional'

      *Exemplo:*
 
    - Todo homem é mortal (já na base)
    - Socrates é homem (já na base)
    - Socrates é mortal (crença a ser adicionada)

    Nesse caso a crença 'Socrates é mortal' não é adicionada, pois já é possível deduzir com as crenças que estão na base.

4.  **Se a nova crença que você quer adicionar é uma contradição comparado com as crenças que já existem na base:**

       Nesses Casos o código de diz com quais crenças a sua nova esta conflitando e te dar a chance de substituir

       *Exemplo:*
 
    - Todo homem é mortal (já na base)
    - Socrates é homem (já na base)
    - Socrates não é mortal (crença a ser adicionada)
  
      Ao colocar sua crença conflitante o seguinte aparece:

      <img align="Center" src="img/procedimento1.png" width="75%" >

      E junto a isso a opção de selecionar qual dos dois você quer trocar pela nova (1 ou 2):

      <img align="Center" src="img/procedimento2.png" width="75%" >

      Após selecionar algum dos números (Nesse caso o '1'), o seguinte acontece:

      <img align="Center" src="img/procedimento3.png" width="75%" >

      E agora sua base foi modificada
  
    

