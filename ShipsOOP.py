####Ship oop
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import math

class Ship:
	def __init__(self, name, film, length, width, crew, maxSpeed):
		self.name = name
		self.length = length
		self.film = film
		self.crew = crew #maximum capacity
		self.maxSpeed= maxSpeed ##m/s
		self.width= width
		self.area=self.length*self.width
		self.density=self.area/self.crew

####enter data

##
galactica=Ship("Galactica\nBattlestar Galactica","Battlestar Galactica",1414,536.84,5000,22.799)
pegasis=Ship("Pegasus","Battlestar Galactica",1789,732.2,1750,24.72)
falcon=Ship("Millennium Falcon","Star Wars",34.75,24.8,5,291.68)
eD=Ship("USS Enterprise D","Star Trek: The Next Generation",842.5,463.73,1014,941.19*10**9)
serenity=Ship("Serenity", "Firefly",82,52,18,178816)
voyager=Ship("USS Voyager","Star Trek: Voyager",345,116,150,992*10**9)
disco=Ship("USS Discovery","Star Trek: Discovery",683,420,136,125*10**9)
cylonB=Ship("Cylon Basestar","Battlestar Galactica",856.1,1030.69,1500,22.8)
endurance=Ship("Endurace","Interstellar",64,64,6,35*10**3)
ussDiscOne=Ship("USS Discovery One","2001:A Space Odyssey",140.1,16.7,2,38585)
nostromo=Ship("Nostromo","Alien",334,215,7,13140046296.3) ##https://speculativeidentities.com/research/uscss-nostromo
prometheus=Ship("Prometheus","Prometheus",130,48.75,17,4.4*10**9)



### append into list
ListOfShipNames=[galactica,pegasis,falcon,eD,serenity,voyager,disco,cylonB,endurance,ussDiscOne,nostromo,prometheus]

x=ListOfShipNames
x.sort(key=lambda x: x.length)
plt1name = [ship.name + "\n" + ship.film for ship in x]
plt1length = [ship.length for ship in x]
ypos = np.arange(len(plt1name))
fig1 = plt.figure(figsize=(5,5))
plt.bar(ypos,plt1length,align='center',alpha=0.5)
plt.xticks(ypos,plt1name,rotation=30)
plt.ylabel('Length of ship [m]')
plt.xlabel('Name of Ship')
plt.title('Favourite Sci-Fi ships in order of length')
plt.legend()
plt.show()

##comparisons
##ship name vs length
##sort via ship lenth
#sort via speed
#sort via crew
##weight vs speed
#ship name vs area
#ship name with max speed vs area
