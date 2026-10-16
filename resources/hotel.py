from flask_restful import Resource,reqparse

hoteis = [
    { "hotel_id": "paraiso", "nome": "Hotel Paraiso", "estrelas": 4.6, "diartia":123.99, "cidade": "Porto"},
    { "hotel_id": "fukui", "nome": "Fukui Resort", "estrelas": 4.8, "diartia":225.99, "cidade": "Viena"},
    { "hotel_id": "aguas", "nome": "Hotel Aguas", "estrelas": 4.2, "diartia":193.99, "cidade": "Lisboa"},
]
class Hoteis(Resource):
    def get(self):
        return { "hoteis": hoteis }

#Listar, inserir, atualizar e eliminar um hotel específico
class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument("nome", type=str, help="Nome obrigatório")
    argumentos.add_argument("estrelas", type=float, help="Estrelas obrigatório")
    argumentos.add_argument("diaria", type=float, help="Diária obrigatório")
    argumentos.add_argument("cidade", type=str, help="Cidade obrigatório")

    def get(self,id_hotel):
        for hotel in hoteis:
            if hotel["hotel_id"] == id_hotel:
                return hotel
        return{"message": "Hotel not found"}, 404


    def post(self, id_hotel):
        dados = Hotel.argumentos.parse_args() #Dicionário
        for hotel in hoteis:
            if hotel["hotel_id"] == id_hotel:
                return{ "message": "Hotel with this id already exists"}
        novo_hotel = { "hotel_id": id_hotel, **dados }
        hoteis.append(novo_hotel)
        return novo_hotel, 200
           
