print('Seja muito bem-vindo ao Quiz do Ney!')
pergunta01 = input('Você deseja continuar?(sim/não)')   

if pergunta01 != "sim":
  print('Vai si fude então') 
  quit()    

pontos = 0

print('Começando...')
print('Qual o nome completo do Neymar? \n (A) Neymar júnior da silva \n (B) Neymar júnior Souza \n (C) Neymar da Silva Júnior \n (D) Neymar Souza Júnior')
Resposta01 = input('Resposta:')

if Resposta01 == "C" or Resposta01 == "c": 
 print('Boa.Essa estava facil!')
 pontos = pontos + 10
else: 
 print('Errou!')

print('Em que dia o menino Ney nasceu? \n (A) 15 de Fevereiro \n (B) 5 de Fevereiro \n (C) 8 de Março \n (D) 10 de Fevereiro')
Resposta02 = input('Resposta:')

if Resposta02 == "B" or Resposta02 == "b": 
 print('Você é bom em!! Vamos ver se consegue essa.')
 pontos = pontos + 10
else: 
 print('Errou bobinho!')

print('Qual o time que revelou o Neymar? \n (A) Flamengo \n (B) Barcelona \n (C) Botafogo \n (D) Santos')
Resposta03 = input('Resposta:')

if Resposta03 == "D" or Resposta03 == "d": 
 print('Ta indo bem. Agora para finalizar quero ver se sabe essa...')
 pontos = pontos + 10
else: 
 print('Ai foi besta em!')

print('Em que ano o Neyzinho foi jogar no Barcelona? \n (A) 2011 \n (B) 2009 \n (C) 2012 \n (D) 2013')
Resposta04 = input('Resposta:')

if Resposta04 == "C" or Resposta04 == "c": 
 print('Muito bom meu caro! Voce finalizou o Quiz')
 pontos = pontos + 10
else: 
 print('Putzz! Errou em amigo.')

print('Parábens você completou o quiz é fez' , pontos ,'Pontos')

