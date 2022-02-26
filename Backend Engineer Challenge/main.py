def getServers():
    servers = {
            "region-2":{
                "server1":{
                    "capacity": "10"
                }
            },
            "region-2":{
                "server2":{
                    "capacity": "8"
                },
                "server3":{
                    "capacity": "10"
                }
            },
    }
    return servers
    
def getServerBan(server):
    server_ban = {"server1":["Luis"]}
    if(server_ban[server]):
        return server_ban[server]
    else:
        return null

def getPlayerBan(player):
    player_ban = {"Arturo":["Luis"]}
    if(player_ban[player]):
        return player_ban[player]
    else:
        return null

def getPlayersRegionBan(region):
    players = {
            "region-1":{"Arturo"},
            "region-2":["Luis", "Jorge"]
    }
    if(players[region]):
        return players[region]
    else:
        return null

def sync(player):
    player_ban = getPlayerBan(player)
    serversRegions = getServers()
    
    print(player_ban)
    print(serversRegions)

    for region in serversRegions.keys():
        regionBan = getPlayersRegionBan(region)
        
        print(regionBan)
        if(player in regionBan):
            print("baneado")
            continue

        for serverRegion in serversRegions[region]:
            #trae el servidor
            #al traer el servidor valida si esta baneado en ese server function getServerBan
            #obtiene el servidor, region y capacidad
            #dado que  no tenemos quienes estan en el server no se valida la capacidad y cuantos jugadores hay dentro de ese server
            #de igual manera al no saber que jugadores estan en el server no podemos validar si sus usuarios bloqueados se encuentran conectado en el servidor

        

    



sync("Arturo")

