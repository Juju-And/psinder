# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import random

from django.shortcuts import render, redirect
from django.views import View

from matchingapp.models import Dog, DogMatch


class MainView(View):
    def get(self, request):
        return render(request, "base.html")


class MatchView(View):
    def get(self, request):
        all_dogs = Dog.objects.all()
        current_dog = Dog.objects.filter(id=2).first()

        random_dog = generate_random_dog(all_dogs, current_dog)
        return render(request, "matching_view.html", {"dog": random_dog})

    def post(self, request):
        current_dog = Dog.objects.filter(id=2).first()
        data = json.loads(request.body)
        answer = data["answer"]
        data_id = data["data-id"]
        print(answer, data_id)
        if answer == "accepted":
            dog_to_match = Dog.objects.filter(id=data_id).first()
            DogMatch.objects.create(
                dog_like_sender=current_dog, dog_like_receiver=dog_to_match
            )
            return redirect("/matching/")
        else:
            return redirect("/matching/")


def generate_random_dog(all_dogs, current_dog):
    choices = DogMatch.objects.filter(dog_like_sender=current_dog)

    list_of_choices = [current_dog.id]
    for choice in choices:
        list_of_choices.append(choice.dog_like_receiver.id)

    random_dog_id = random.choice(
        [i for i in range(2, len(all_dogs)) if i not in list_of_choices]
    )

    return Dog.objects.filter(id=random_dog_id).first()

    # matches = DogMatch.objects.filter(dog_like_receiver=current_dog)
    # list_of_matches = [current_dog.id]
    # for match in matches:
    #     list_of_matches.append(match.dog_like_sender.id)
    #
    # # print(random_dog.id, likers)
    # random_dog_id = random.choice(
    #     [i for i in range(2, len(all_dogs)) if i not in list_of_matches]
    # )
