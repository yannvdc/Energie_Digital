from django.shortcuts import render
from bokeh.plotting import figure
from bokeh.embed import components
import numpy as np

def chart(request):
    if request.POST: # wenn "Enter" gedrückt wird
        dic = request.POST # Werte von Page übernehmen
        print('mal sehen was das ist: ' + str(dic))
        nCycle = int(dic['nCycle'])
    else:
        nCycle = int(1)

    chart = makeChart(nCycle)
    return render(request, 'home.html', {'nCycle': nCycle, 'chart': chart})

def makeChart(nCycle):
    x = np.linspace(0,100,100)
    y = np.sin(x/100*2*3.1415*nCycle)
    p1 = figure(plot_width=460, plot_height=200)
    p1.line(x, y)
    p1.toolbar.logo = None

    script, div = components(p1)
    chart = script + div
    return chart