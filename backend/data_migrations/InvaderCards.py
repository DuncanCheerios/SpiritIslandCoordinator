from itertools import combinations
from game.models import InvaderCard

land_types = ["Wetlands", "Mountains", "Desert", "Jungle"]

for stage in [1, 2]:
    for land in land_types:
        InvaderCard.objects.get_or_create(name=land, stage=stage, escalation=stage==2)

InvaderCard.objects.get_or_create(name="Coasts", stage=2, escalation=False)

for land_type_pair in combinations(land_types, 2):
    name = land_type_pair[0] + " and " + land_type_pair[1]
    InvaderCard.objects.get_or_create(name=name, stage=3, escalation=False)


