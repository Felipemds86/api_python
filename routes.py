from flask import Flask , request
from main import insertUsuario

app= Flask("youtube")

@app.route("/olamundo", methods=["Get"])
def olaMundo():
    return{"ola mundo"}
@app.route("/cadastra/usuario", methods=["Post"])
def cadastraUsuario():
    
    body= request.get_json()
    
    if("nome" not is body):
        return{"status": 400, "mensagem": "o parametro nomee obrigatorio"}
    
     if("email" not is body):
            return{"status": 400, "mensagem": "o parametro email e obrigatorio"}
    
     if("senha" not is body):
            return geraResponse(400,  "o parametro senha  e obrigatorio")
    
    usuario = insertUsuario(body["nome"], body["email", body["senha"])
                            
    return geraResponse(200,"usuario criado", "User" , usuario)
    
    def geraResponse(status, mensagem , nome_do_conteudo ,, conteudo): 
        response={}
        response["status"]= status
        response["mensagem"]= mensagem 
        
        if(nome_do_conteudo and conteudo): 
            response[nome_do_conteudo]= conteudo 
            
        return response
    
app.run()