
from MFIS_Read_Functions import *
import matplotlib.pyplot as plt


def main():
    #Realizo listas y diccionarios con los que trabajar
    InputFuzzy = readFuzzySetsFile('Files/InputVarSets.txt')
    Outputfuzzy = readFuzzySetsFile('Files/Risks.txt')
    Apps = readApplicationsFile()
    Rule = readRulesFile()

    #Abro el archivo
    resultados = open('Files/Results.txt', 'w')

    #Calculo el resultado para cada aplicación
    for App in Apps:
        centroid = procesapp(App, InputFuzzy, Outputfuzzy, Rule) #Funcion que calcula el riesgo
        resultados.write("Resultado_Aplicacion_" + App.appId + " = "+ str(centroid) + "\n") #Escribo el resultado en el archivo

    #Cierro el archivo
    resultados.close()
def procesapp(app, input, output, rule):
    #inicializo variable de salida
    salidax = output['Risk=LowR'].x.copy()
    saliday = [0.0]*101

    #borrosificacion
    fuzzy(app, input)

    #2 inferencia
    for r in rule:

        eval_antecedente(r, input)

        #Evaluacion del consecuente
        if r.consequent == 'Risk=LowR':
            r.consequentY = output['Risk=LowR'].y.copy()
        elif r.consequent == 'Risk=MediumR':
            r.consequentY = output['Risk=MediumR'].y.copy()
        elif r.consequent == 'Risk=HighR':
            r.consequentY = output['Risk=HighR'].y.copy()
        for j in range(len(salidax)):
            #Agregacion parcial
            if r.strength < r.consequentY[j]:
                r.consequentY[j]= r.strength
            #Agregacion completa
            if saliday[j] < r.consequentY[j]:
                saliday[j] = r.consequentY[j]

    #plt.plot(salidax, saliday)
    #plt.show()
    #Calculo el centroide con las dos listas de datos
    return skf.centroid(salidax, saliday)

def fuzzy (app, input):
    for i in input.values():
        if i.var == 'Age':
            i.memDegree = i.y[app.data[0][1]]
        elif i.var == 'IncomeLevel':
            i.memDegree = i.y[app.data[1][1]]
        elif i.var == 'Assets':
            i.memDegree = i.y[app.data[2][1]]
        elif i.var == 'Amount':
            i.memDegree = i.y[app.data[3][1]]
        elif i.var == 'Job':
            i.memDegree = i.y[app.data[4][1]]
        else:
            i.memDegree = i.y[app.data[5][1]]
def eval_antecedente(r, input):
    riesgo_parcial = []
    for i in r.antecedent:
        riesgo_parcial.append(input[i].memDegree)
    r.strength = min(riesgo_parcial)

if __name__ == "__main__":
    main()
