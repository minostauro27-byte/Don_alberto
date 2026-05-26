from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)

inventario =[
	"Bujias de iridio",
	"Filtro de aceite",
	"Aceite motul 7100"
]

peritajes =[
	{"placa":"MDT-276"},
	{"placa":"HNM-672"}
]



@app.route('/api/registros', methods=['GET'])
def registros():
	return jsonify({
	 "status":"online",
	 "servidor":"Ubuntu de Torres Maikoll:",
 	 "hora_servidor":str(datetime.datetime.now()),
	 "inventario": inventario
	})



@app.route('/api/peritajes', methods=['GET'])
def get_peritajes():
	return jsonify({
	"cantidad":len(peritajes),
	"peritajes": peritajes
	})

@app.route('/api/peritajes', methods=['POST'])
def post_peritajes():
	data = request.get_json()

	if not  data or "placa" not in data:
		return jsonify({
			"error":"Debes enviar la placa ej Json"
		}), 400
	
	nuevo = {
		"placa": data["placa"],
		"hora": str(datetime.datetime.now())
	}

	peritajes.append(nuevo)

	return jsonify({
		"mensaje":"Peritaje registrado",
		"peritaje": nuevo
		}), 201


if __name__ == "__main__":
	app.run()
