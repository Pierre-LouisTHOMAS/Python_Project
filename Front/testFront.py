import random

def monte_carlo_pi(estimations):
    points_dans_cercle = 0

    for _ in range(estimations):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        distance = x**2 + y**2

        if distance <= 1:
            points_dans_cercle += 1

    return (points_dans_cercle / estimations) * 4

# Exemple d'utilisation avec 1 million d'estimations
resultat_pi = monte_carlo_pi(1000000)
print("Estimation de π:", resultat_pi)
