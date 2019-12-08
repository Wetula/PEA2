import os
import sys
import utils
from Graph import Graph


def main():
    print("TSP Application - Task 2")
    if len(sys.argv) > 1:
        fn = sys.argv[1]
        if os.path.exists(fn):
            print("Path to file to load: " + fn)
        else:
            print("File does not exist.")
            sys.exit("Incorrect path.")
    else:
        print("Pass the file name to use.")
        sys.exit("No file given.")

    file, extension = os.path.splitext(fn)

    if extension == '.tsp':
        graph = utils.tsp_reader(fn)
    elif extension == '.atsp':
        graph = utils.atsp_reader(fn)
    else:
        sys.exit("Unsupported file type: " + extension)

    select = 0

    while select == 0:
        print("Select method for solution: \n"
              "T - Taboo Search\n"
              "S - Simulated Annealing\n")

        method = input("Selection: ")

        if method.capitalize() == 'T':  # Brute Force
            select = 1
            tour, cost, time = BruteForce(graph).solve()
            pass
        elif method.capitalize() == 'S':  # Dynamic Programming
            select = 2
            tour, cost, time = DynamicProgramming(graph).solve()
            pass
        else:
            print("Wrong selection")
            pass

    print("The solution is:")
    print(tour)
    print("The cost is:")
    print(str(cost))
    print("Solving took " + str(time) + " seconds.")


if __name__ == "__main__":
    main()
