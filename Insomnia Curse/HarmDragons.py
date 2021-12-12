def harm_dragons(k, l, m, n, d):
    healthyDargons = 0

    for i in range(1, d + 1):
        if i%k != 0 and i%l != 0 and i%m != 0 and i%n != 0:
            healthyDargons += 1
    
    return d - healthyDargons