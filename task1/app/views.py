from django.shortcuts import render
import pandas as pd
import csv
from app.settings import INFLATION_LIST
import pandas as pd

def inflation_view(request):
    template_name = 'inflation.html'
    list_of_data = []
    df = pd.read_csv('C:/inflation_russia.csv', delimiter=';')
    with open(INFLATION_LIST, encoding='utf-8') as text:
        read = csv.reader(text, delimiter=';')
        for row in read:
            list_of_data.append(row)
    common_list = []
    common_list.append(['Год', 'Январь', 'Февраль', 'Март', 'Апрель', 'Май',
                        'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь', 'Суммарно'])
    for line in list_of_data[1:]:
        new_list = []
        for i in line:
            if i:
                new_list.append(float(i))
            else:
                new_list.append(i)
            new_list[0] = int(new_list[0])
        common_list.append(new_list)

    context = {'data': common_list}

    return render(request, template_name,
                  context)


