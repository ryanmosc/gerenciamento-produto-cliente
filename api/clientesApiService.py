import requests

url = 'http://localhost:3000/clientes'

class ClientesApiervice:
    # Fazendo a requisição GET
    def buscarClientes(self):
        
        response = requests.get(url)
        
        if response.status_code == 200:
            users = response.json()
            print(users)
            return
        else:
            print('Erro ao acessar a API:', response.status_code)
            
            
    def buscarCliente(self, id=None, nome=None):
        if id is not None and nome is not None:
            response = requests.get(f"{url}?{id}&nome={nome}")
        elif id is not None:
            response = requests.get(f"{url}/{id}") 
        elif nome is not None:
            response = requests.get(f"{url}?nome={nome}")  
        else:
            self.buscarClientes()
            return  
        
        if response.status_code == 200:
            users = response.json()
            print(users)
            return
        else:
            print('Erro ao acessar a API:', response.status_code)
            
    def adicionarCliente(self, nome):
        novo_cliente = {"nome":nome}
        response = requests.post(url, json=novo_cliente)
        
        
        if response.status_code == 200:
            print(f"{nome} foi adicionado a lista de clientes")
        else:
            print('Erro ao adicionar o cliente:', response.status_code)
    
    def alterarCliente(self, id, nome, cpf=None):
        cliente_atualizado = {"nome": nome}
        
        if(cpf is not None):
            cliente_atualizado["cpf"] = cpf
            
        response = requests.put(f"{url}/{id}", json=cliente_atualizado)
        
        if response.status_code == 200:
            print(f"{nome} foi atualizado na lista de clientes")
        else:
            print("Erro ao atualizar o cliente", response.status_code)
            
            
            
    def removerCliente(self, id):
        response = requests.delete(f"{url}/{id}")
        
        if response.status_code == 200:
            print(f"Cliente de código {id} foi removidocom sucesso da list de clientes :)")
        else:
            print("Erro ao remover o cliente:", response.status_code)
                
servico = ClientesApiervice()
#servico.adicionarCliente("Vicente")
#servico.alterarCliente("36a0", "Vicente de Castro", "4444444444445")
#servico.alterarCliente("256", "Vicente de souza")
# servico.buscarCliente(256)
# servico.buscarCliente(None, "Ryan")
# servico.buscarCliente(257, "Thales")
servico.removerCliente("256")