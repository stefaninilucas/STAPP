from pyautocad import Autocad, APoint

acad = Autocad()

selecao = acad.get_selection("Selecione o eixo:")

lista = []

for obj in acad.doc.Modelspace:
    lista.append(obj.handle)

for i in acad.iter_objects('Polyline', selecao, dont_cast=True):
    obj_handle = i.handle
    print(obj_handle)
    acad.doc.sendcommand("copy (handent \"" + obj_handle + "\")  D 0,0,0 ")

acad.prompt("Selecione um ponto de quebra:")
p = acad.doc.Utility.GetPoint()
p0 = p[0]
p1 = p[1]

acad.doc.sendcommand("break (handent \"" + obj_handle + "\")  " + str(p0) + "," + str(p1) + " " + str(p0) + "," + str(p1) + " ")

lista2 = []

for obj in acad.doc.Modelspace:
    lista2.append(obj.handle)

acad.prompt(i.length)

print("OK")