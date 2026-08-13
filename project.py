import string
import secrets

def gerar_senha(tamanho = 12):
 caracteres = (string.ascii_letters + string.digits + string.punctuation)
 senha = ''.join (
     secrets.choice(caracteres) for _ in range(tamanho))
 return senha

print("Bem vindo ao gerador de senhas")
char_num = input("Digite a quantidade de caracterés da sua senha: ")
char_num_int = int(char_num)
print("Senha gerada: ", gerar_senha(char_num_int))
