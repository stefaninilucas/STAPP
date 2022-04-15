from pyautocad import Autocad, APoint
acad = Autocad()

selecao = acad.get_selection("Selecione círculos para alterá-los para polyline:")
for i in acad.iter_objects('Circle', selecao, dont_cast=True):
    centro = APoint(i.center)
    raio = i.radius
    pi = 3.14159265358979

    arco1 = acad.model.addArc(centro, raio, 0, pi / 2)
    arco2 = acad.model.addArc(centro, raio, pi / 2, pi)
    arco3 = acad.model.addArc(centro, raio, pi, 3 * pi / 2)
    arco4 = acad.model.addArc(centro, raio, 3 * pi / 2, 2 * pi)

    handle1 = arco1.handle
    handle2 = arco2.handle
    handle3 = arco3.handle
    handle4 = arco4.handle

    acad.doc.SendCommand('pedit (handent "' + handle1 + '")   ')
    acad.doc.SendCommand('pedit (handent "' + handle2 + '")   ')
    acad.doc.SendCommand('pedit (handent "' + handle3 + '")   ')
    acad.doc.SendCommand('pedit (handent "' + handle4 + '")  J ALL   ')

acad.prompt("Concluído\n")
