from django.shortcuts import render, reverse

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
    pages = {
        'Омлет': reverse('omlet'),
        'Паста': reverse('pasta'),
        'Бутерброд': reverse('buter')
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context = context)

def omlet_view(request):
    omlet = 'omlet'
    if omlet in DATA:
        ingridients_omlet = DATA[omlet]
        servings = request.GET.get('servings')
        if servings:
            summa_ingridients = {}
            for keys_omlet,value_omlet in ingridients_omlet.items():
                new_value = value_omlet*int(servings)
                summa_ingridients[keys_omlet] = new_value
                context = {
                    'omlet': omlet,
                    'recipe': summa_ingridients
                 }
        else:
            context = {
                'omlet': omlet,
                'recipe': ingridients_omlet
            }

    else:
        context = None
    return render(request, template_name='calculator/index.html', context=context)

def pasta_view(request):
    pasta = 'pasta'
    if pasta in DATA:
        ingridients_pasta = DATA[pasta]
        servings = request.GET.get('servings')
        if servings:
            summa_ingridients = {}
            for keys, value in ingridients_pasta.items():
                new_value = value * int(servings)
                summa_ingridients[keys] = new_value
                context = {
                    'pasta': pasta,
                    'recipe': summa_ingridients
                }
        else:
            context = {
                'pasta': pasta,
                'recipe': ingridients_pasta
            }

    else:
        context = None
    return render(request, template_name='calculator/index.html', context=context)

def buter_view(request):
    buter = 'buter'
    if buter in DATA:
        ingridients_buter = DATA[buter]
        servings = request.GET.get('servings')
        if servings:
            summa_ingridients = {}
            for keys, value in ingridients_buter.items():
                new_value = value * int(servings)
                summa_ingridients[keys] = new_value
                context = {
                    'buter': buter,
                    'recipe': summa_ingridients
                }
        else:
            context = {
                'buter': buter,
                'recipe': ingridients_buter
            }

    else:
        context = None
    return render(request, template_name='calculator/index.html', context=context)

