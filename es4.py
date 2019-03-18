vet=[   {"todo": "call John for AmI project organization", "urgent": True},
        {"todo": "buy a new mouse", "urgent": True},
        {"todo": "find a present for Angelina’s birthday", "urgent": False},
        {"todo": "organize mega party (last week of April)", "urgent": False},
        {"todo": "book summer holidays", "urgent": False},
        {"todo": "whatsapp Mary for a coffee", "urgent": False}  ]
ris=[]

for gigi in vet:
    if gigi["urgent"]:
        ris.append(gigi)

print(ris)