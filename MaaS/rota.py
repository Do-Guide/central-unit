import geocoder
import googlemaps
from geopy.geocoders import Nominatim
from datetime import datetime
from .utils import rota_json

class MaaS(object):
    # self.gmaps = None
    def __init__(self):
        self.gmaps2 = googlemaps.Client(key='API_KEY')

    @classmethod
    def local_partida(self):
        partida = geocoder.ip('me')
        coordenadas_partida = tuple(partida.latlng)
        # coordenadas_partida = (latitude, longitude) # Setar local de Partida caso precisão esteja equivocada
        return coordenadas_partida
    
    def destino(self, local):
        
        # local = 'Park Shopping Brasília'
        self.local = local
        destino = self.gmaps2.geocode(local)
        coordenadas_destino = (destino[0]["geometry"]["location"]['lat'], destino[0]["geometry"]["location"]['lng'])
        coordenadas_destino

        return coordenadas_destino
    
    @classmethod # API alternativa ao GoogleMaps
    def destino_alternativo(self, local):
        # local = "UnB FGA Gama"
        loc = Nominatim(user_agent="GetLoc")
        local = loc.geocode(local)
        coordenadas_destino =(local.latitude, local.longitude)

        return coordenadas_destino

    
    def instrucao_percurso(self, coordenadas_partida, coordenadas_destino):
        now = datetime.now()
        rota = self.gmaps2.directions(coordenadas_partida,coordenadas_destino,mode="walking",departure_time=now,language='pt-BR')
        rota_json(self.local, rota)
        return rota

# instancia_rota = MaaS()

# partida = instancia_rota.local_partida()
# local = 'UBS 5 Riacho Fundo 2' ## Definir local de Destino
# destino = instancia_rota.destino(local)
# caminho = instancia_rota.instrucao_percurso(partida, destino)

# instrucoes_percurso = instrucao_texto(caminho) # Lista de comandos para reprodução
# print(*instrucoes_percurso, sep='\n')