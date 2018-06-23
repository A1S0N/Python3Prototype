# Python3Prototype
Exemplo de implementação do padrão prototype em Python3

### PROTOTYPE

O padrão de projeto PROTOTYPE permite criar novos objetos clonando um objeto prototípico original. 


### O padrão é utilizado para:


* Evitar que as subclasses que criam objetos funcionem como o padrão abstract factory.
* Evitar criar um novo objeto utilizando a palavra new, o que diminui o custo de memória.


O padrão Prototype é principalmente utilizado quando existe a necessidade de copiar um objeto. Dessa forma,  pode-se dizer que sua aplicação realiza cópias exatas de algum objeto em tempo de execução e este padrão é altamente recomendado. Também pode ser utilizado em sistemas que precisam ser independentes da forma como os seus componentes são criados, compostos e representados.


### Vantagens:

* Economia de memória.

* Pode realizar cópias em tempo de execução.


### Desvantagens:

* Deve-se ter cuidado com o uso da concorrência.


### EXEMPLO DE UTILIZAÇÃO EM PYTHON 3


É necessário importar a biblioteca COPY, a qual permite fazer cópias de objetos de duas formas: cópia superficial(copy) e cópia profunda(deepcopy).


copy : constrói um novo objeto composto e, na medida do possível, insere referências nele aos objetos encontrados no original.


deepcopy: constrói um novo objeto composto e, recursivamente, insere cópias nele dos objetos encontrados no original.


Em código:

```
import copy
```

Cria-se uma classe prototípica que será copiada mais tarde.

```
class ProtoCao:

    pass
```

Adicionemos nossas funções de exemplo:

```
    def __init__(self):       # Inicia uma lista vazia quando o objeto é instanciado
    
        self.truques = [ ]
    
    def add Truque(self, truque): # Permite que itens sejam adicionados à lista   
    
        self.truques.append(truque)
```

A classe prototípica de exemplo ficará assim:

```
class ProtoCao:

        def __init__(self):       # Inicia uma lista vazia quando o objeto é instanciado
        
            self.truques = [ ]

         def add Truque(self, truque): # Permite que itens sejam adicionados à lista   
         
             self.truques.append(truque)

    pass
```

Agora definimos uma função principal para o código, a qual conterá o código responsável pela instanciação do objeto e implementação do padrão:

```
def main():

    cybercao = ProtoCao()  # Instancia-se um objeto
    
    cybercaoClone = copy.deepcopy(cybercao) # O objeto anterior é clonado
    
    cybercao.addTruque('Raio laser') # Insere itens a lista do original
    
    cybercaoClone.addTruque('Lança chamas') # Insere itens a lista do clone
    
    # Exibe os itens da lista do objeto original e do clone
    
    print('\nTruques do Cybercão: %s ' % cybercao.truques)
    
    print('\nTruques do Clone do Cybercão: %s\n' % cybercaoClone.truques)

```

Com isso criamos um objeto e seu clone.


![Original](https://github.com/A1S0N/Python3Prototype/blob/master/cyberdog.jpeg)
![Clone](https://github.com/A1S0N/Python3Prototype/blob/master/cyberdog.jpeg)


Por fim chamamos a função principal tendo em vista boas práticas de python:

```
if __name__ == “__main__”:

    main()
```
