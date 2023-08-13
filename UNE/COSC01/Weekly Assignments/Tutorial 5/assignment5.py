weight = {'pencil': 10, 'pen': 20, 'paper': 4,'eraser': 80}
available = {'pen': 3, 'pencil': 5, 'eraser': 2, 'paper': 10}


overall_weight = sum(weight[i] * available[i] for i in weight)

print(overall_weight)

    







