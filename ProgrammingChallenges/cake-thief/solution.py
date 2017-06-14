
cake_tuples = [(7, 160), (3, 90), (2, 15)]
capacity    = 20

def max_duffel_bag_value(tps, cap):
    champ = 0
    for choice in tps:
        if choice[0] <= cap:
            max_duffel_bag_value(tps, cap-choice[0])

    pass

def main():
    max_duffel_bag_value(cake_tuples, capacity)

if __name__ == "__main__":
    main()
