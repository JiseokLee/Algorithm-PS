ship_names = ['SHIP NAME', 'N2 Bomber', 'J-Type 327', 'NX Cruiser', 'N1 Starfighter', 'Royal Cruiser']
classes = ['CLASS', 'Heavy Fighter', 'Light Combat', 'Medium Fighter', 'Medium Fighter', 'Light Combat']
deployments = ['DEPLOYMENT', 'Limited', 'Unlimited', 'Limited', 'Unlimited', 'Limited']
in_service = ['IN SERVICE', '21', '1', '18', '25', '4']

for i in range(0, 6):
    print(ship_names[i].ljust(15) + classes[i].ljust(15) + deployments[i].ljust(11) + in_service[i].ljust(10))