# Exemplo de implementação do padrão prototype em Python3.
# ALISSON MORETTO
# Especifique os tipos de objetos para criar usando uma instância prototípica
# e crie novos objetos copiando esse protótipo. 

import copy

def ascii():
    print('''
     ,                    ," e`--o
    ((                   (  | __,'
     \\\\~----------------' \_;/
     (      PROTOTYPE       /
     /) ._______________.  )
    (( (               (( (
     ``-'               ``-''')

class ProtoCao:
    def __init__(self):
        self.truques = []
    
    def addTruque(self, truque):
        self.truques.append(truque)

    pass

cybercao = ProtoCao() 
cybercaoClone = copy.deepcopy(cybercao)

def addTruq(cao, truq):
    if cao == '1':
        cybercao.addTruque(truq)        
        print('\n[*] Novo truque adicionado ao Cybercão Original: %s' % cybercao.truques)
    else:
        cybercaoClone.addTruque(truq)
        print('\n[*] Novo truque adicionado ao Clone do Cybercão: %s' % cybercaoClone.truques)

def main():
    ascii()    
    
    print('\nTruques do Cybercão Original: %s ' % cybercao.truques)

    while True:
        op = input('\nSelecione o cão: \n\n[1] Original \n[2] Clone\n > ')
        truq = input('\nInsira um novo truque para o cão: ')
        addTruq(op, truq)

if __name__ == "__main__":
    main()
