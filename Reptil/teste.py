from Jacare import Jacare
from Camaleao import Camaleao
from Cobra import Cobra

print("------------------------Os Jacarés------------------------")

j1 = Jacare("jacaretinga", "verde", 5, 32)
print(j1.tomar_sol())
print(j1.botar_ovo())
print(j1.atacar())
print(j1.dormir())

print("------------------------Os Jacarés------------------------")

j1 = Jacare("jacaretinga", "verde", 1, 10)
print(j1.tomar_sol())
print(j1.botar_ovo())
print(j1.atacar())
print(j1.dormir())

print("------------------------Os Camaleoes------------------------")

c1 = Camaleao("Chamaeleo jacksonii", "verde", 3, "barata")
print(c1.tomar_sol())
print(c1.botar_ovo())
print(c1.mudar_de_cor())
print(c1.comer_inseto())

print("------------------------As cobras------------------------")

co = Cobra("Jiboia", "verde", 3, False, False)
print(co.tomar_sol())
print(co.botar_ovo())
print(co.rastejar())
print(co.trocar_pele())

print("------------------------As cobras------------------------")

co = Cobra("coral", "vermelha", 2, False, True)
print(co.tomar_sol())
print(co.botar_ovo())
print(co.rastejar())
print(co.trocar_pele())

