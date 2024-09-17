from django.shortcuts import render
import random

participants = []

def assign_secret_santa(participants):
    shuffled_participants = participants[:]
    while True:
        random.shuffle(shuffled_participants)
        # Check if anyone is assigned to themselves
        if all(santa != recipient for santa, recipient in zip(participants, shuffled_participants)):
            break
    return [(santa, recipient) for santa, recipient in zip(participants, shuffled_participants)]

def secret_santa(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            participants.append(name)
        if 'clear_list' in request.POST:
            participants.clear()
        if 'randomize' in request.POST:
            if len(participants) < 2:
                result = []
            else:
                result = assign_secret_santa(participants)

            return render(request, "secret_santa/secret_santa.html", {'participants': participants, 'result': result})

    return render(request, "secret_santa/secret_santa.html", {'participants': participants})
