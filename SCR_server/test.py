import cherrypy
import json
import numpy as np
import pickle

class App:
	exposed = True
	@cherrypy.tools.json_in()
	def POST(self):
		data = []
		input_json = cherrypy.request.json
		value = input_json['requestKey']
		data = [float(i) for i in value]
		IMG = np.array(data)
		IMG_arr = IMG.reshape(1,-1)
		mlp = pickle.load(open('IMG_MLP.pkl','rb'))
		predicted = mlp.predict_proba(IMG_arr)
		
		return str(predicted)


if __name__ == '__main__':
	app_config = {
		'/' : {'request.dispatch' : cherrypy.dispatch.MethodDispatcher()}
		}
	cherrypy.tree.mount( App(),config= app_config)
	cherrypy.config.update({
		'server.socket_host' : '114.71.219.72',
		'server.socket_porti' : 8080,
	})
	cherrypy.engine.start()
	cherrypy.engine.block()
