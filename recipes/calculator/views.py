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


def menu(request):
    recipe = request.GET.get('recipe')
    amount = int(request.GET.get('amount', 1))
    context = {'recipe': {meal: amount * count for meal, count in DATA[recipe].items()}}
    print(context)
    return render(request, 'calculator/index.html', context)
