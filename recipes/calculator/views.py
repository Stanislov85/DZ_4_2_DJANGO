from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def home_view(request):
    template_name = 'calculator/home.html'
    recept_list = list(DATA.keys())
    pages = {k: (k+'/') for k in recept_list}
    context = {
        'pages': pages
    }
    return render(request, template_name, context = context)

def recept_view(request, recept):
    if recept in DATA:
        ingridients = DATA[recept]
        servings = request.GET.get('servings')
        if servings:
            summa_ingridients = {}
            for keys,value in ingridients.items():
                new_value = value*int(servings)
                summa_ingridients[keys] = new_value
                context = {
                    'recept': recept,
                    'recipe': summa_ingridients
                 }
        else:
            context = {
                'recept': recept,
                'recipe': ingridients
            }

    else:
        context = None
    return render(request, template_name='calculator/index.html', context=context)
