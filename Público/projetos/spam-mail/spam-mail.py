#!/usr/bin/env python3.6
# encoding: utf-8

import webbrowser
import os, time
import smtplib
import getpass
 
 
def frase():
    print("""
 
       .d88888b                     8888ba.88ba           oo dP
       88.    "'                    88  `8b  `8b             88
       `Y88888b.  88d888b. .d8888b. 88   88   88 .d8888b. dP 88
             `8b  88'  `88 88'  `88 88   88   88 88'  `88 88 88
       d8'   .8P  88.  .88 88.  .88 88   88   88 88.  .88 88 88
        Y88888P   88Y888P' `88888P8 dP   dP   dP `88888P8 dP dP
       oooooooooo~88~ooooooooooooooooooooooooooooooooooooooooooo
                  dP    
 
       [+] Funcional :  @gmail.com, @hotmail.com
           [!] Seus dados não serão comprometidos, e nem roubados.
           [!] Ative a opção "Aplicativos menos seguro" para seguir o script.
                               (Apenas no gmail)
                   >> https://myaccount.google.com/lesssecureapps <<
       [+]Na escolha de arquivos, algumas extensões não são válidas.
 
   """)
 
x = 0
def win():
        x = 0
        frase()
        # Escolha entre gmail e hotmail
        print('[1]GMAIL   [2]HOTMAIL')
        escolha = int(input('>>> '))
        if escolha == 1:
            email = input('{+}Seu E-mail : ')
            if '@gmail.com' not in email:
                print('{--}Faltando Parametros.')
                exit()
            ## Entrada de senha
            senha = getpass.getpass('{+}Senha de ' + email + ': ')
            time.sleep(2)
            os.system('cls')
            frase()
            try:
                smtp = smtplib.SMTP('smtp.gmail.com', 587)
                smtp.starttls()
                # Logando
                smtp.login(email, senha)
            except Exception as erro:
                print('{--}Erro na senha/e-mail[--]')
                exit()
            # email alvo
            para = input('{+}E-mail Alvo : ')
            if '@gmail.com' not in para:
                print('{--}Faltando Parametros.[--]')
                exit()
            ### Escolha em opçoes
            print('\n[1]MENSAGEM-TEXTO   [2]CONTEUDO DE ARQUIVO')
            escolha = int(input('>>> '))
            print('\n')
            #
            if escolha == 1:
                x = 0
                msg = input('{+} Mensagem : ')
                vezes = int(input('{+} Quantidade Vezes : '))
                print('\n')
                while x < vezes:
                    x += 1
                    smtp.sendmail(email, para, msg)
                    print('[.]Enviando o %d ° e-mail[.]'%(x))
                   
                   
                try:
 
                    print("""
 
                   [!]Seu E-mail : %s
 
                   [!]E-mail Alvo : %s
                       
                   [!]Mensagem : %s
                       
                   [!]Envio de Texto
 
 
                           """ % (email, para, msg))
                except:
                    print('Erro')
                #
            if escolha == 2:
                print('{+}Arquivo pode ser escolhido no diretorio : '+os.getcwd())
                try:
                    msg = input('{+} Arquivo : ')
                    p = open(msg,'r')
                    z = p.read()
                except:
                    print('{-}Erro no arquivo/nome/extensão')
                    exit()
                vezes = int(input('{+} Quantidade Vezes : '))
                x = 1
                while x <= vezes:
                    smtp.sendmail(email, para, z)
                    print('{.}Enviando %d ° E-mail[.]'%(x))
                    x += 1
                   
                       
                try:
 
                    print("""
 
                   [!]Seu E-mail : %s
 
                   [!]E-mail Alvo : %s
 
                   [!]Arquivo : %s
                                             
                   [!]Envio de Arquivo.
 
 
                           """ % (email, para, msg))
                except KeyboardInterrupt:
                    print('[!]Voce cancelou.')
                except:
                    print('Erro')
                #Se for maior ou menor
            if escolha > 2 or escolha < 1:
                print('{--}Erro na escolha.{--}')
                exit()
 
 
                ############################################################################
                    #  PARTE  2 (HOTMAIL)#############
        elif escolha == 2:
                email = input('{+}Seu E-mail : ')
                x = 0
                if '@hotmail.com' not in email:
                    print('{--}Faltando Parametros.')
                    exit()
                ## Entrada de senha
                senha = input('{+}Senha de ' + email + ': ')
                time.sleep(2)
                os.system('cls')
                frase()
                try:
                    smtp = smtplib.SMTP('smtp.live.com', 587)
                    smtp.starttls()
                    # Logando
                    smtp.login(email, senha)
                except Exception as erro:
                    print('{--}Erro na senha/e-mail{--}')
                    exit()
                # email alvo
                para = input('{+}E-mail Alvo : ')
                if '@hotmail.com' not in para:
                    print('{--}Faltando Parametros.{--}')
                    exit()
                ### Escolha em opçoes
                print('\n[1]MENSAGEM-TEXTO   [2]CONTEUDO DE ARQUIVO')
                escolha = int(input('>>> '))
                print('\n')
                # Caso escolha 1
                if escolha == 1:
                    msg = input('{+} Mensagem : ')
                    vezes = int(input('{+} Quantidade Vezes : '))
                    print('\n')
                    x = 1
                    while x <= vezes:
                        smtp.sendmail(email, para, msg)
                        print('{.}Enviando o %d ° e-mail{.}'%(x))
                        x += 1
                    try:
 
                        print("""
 
               [!]Seu E-mail : %s
 
               [!]E-mail Alvo : %s
                               
               [!]Mensagem : %s
                               
               [!]Envio de Texto
 
 
                       """ % (email, para, msg))
                    except:
                        print('Erro')
                # caso escolha 2
                elif escolha == 2:
                    print('{+}Arquivo pode ser escolhido no diretorio : '+os.getcwd())
                    try:
                        x = 1
                        msg = input('{+} Arquivo : ')
                        p = open(msg,'r')
                        z = p.read()
                    except Exception as erro:
                        print(erro)
                    vezes = int(input('{+} Quantidade Vezes : '))
                    print('\n')
                    while x <= vezes:
                        smtp.sendmail(email, para, z)
                        print('{.}Enviando %d ° E-mail{.}'%(x))
                        x += 1
                       
                    try:
                        print("""
 
                   [!]Seu E-mail : %s
 
                   [!]E-mail Alvo : %s
 
                   [!]Arquivo : %s
                                                 
                   [!]Envio de Arquivo.
 
 
                           """ % (email, para, msg))
                    except KeyboardInterrupt:
                        print('[!]Voce cancelou.')
                    except:
                        print('Erro')
                                   
        elif escolha > 2 or escolha < 1:
            print('{--}Escolha incorreta.{--}')
            exit()
win()