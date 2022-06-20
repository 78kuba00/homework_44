from django.shortcuts import render
from .game import Game


def play(request):
    secret_number = [1, 2, 3, 4]
    if request.method == "GET":
        return render(request, "index.html")
    else:
        numbers_str = str(request.POST.get('numbers')).split()
        if not Game.is_valid_count(numbers_str):
            context = {
                "success": False,
                "message": "Please enter 4 number spearated by space",
            }
        elif not Game.is_unique_numbers(numbers_str):
            context = {
                "success": False,
                "message": "Numbers are not unique",
            }
        elif not Game.is_valid_range(numbers_str):
            context = {
                "success": False,
                "message": "Numbers must be 1-9",
            }
        else:
            result = Game.play(numbers_str, secret_number)
            context = {
                "success": True,
                "message": f"Cows {len(result[0])} Bulls {len(result[1])}",
            }

    return render(request, 'index.html', context)
