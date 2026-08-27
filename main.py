from flask import Flask, make_response, jsonify, request
from bd import usuarios

app = Flask(__name__)

@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    return make_response (jsonify (usuarios), 200)



@app.route('/usuarios', methods=['POST'])
def create_usuario():
    usuario = request.json
   
    if 'email' not in usuario:
        return make_response(
            jsonify({"erro": "O campo email é obrigatório"}), 
            400
        )

    usuarios.append(usuario)
    return make_response(jsonify(usuario), 201)

@app.route('/usuarios/<int:id>', methods=['PUT'])
def editar_usuario_por_id(id):
    usuario_alterado = request.get_json()
    for indice,usuario in enumerate(usuarios):
        if usuario.get('id') == id:
            usuarios[indice].update(usuario_alterado)
            return jsonify(usuarios[indice])

@app.route('/usuarios/<int:id>', methods=['GET'])
def obter_usuario_por_id(id):
    for usuario in usuarios:
        if usuario.get('id') == id:
            return jsonify(usuario)

    return make_response(   
        jsonify({"erro": "Usuário não encontrado"}), 
        404
    )


        
       
app.run()

