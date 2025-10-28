def tower_of_hanoi(n, source, auxilary, destination):
    if n == 1:
        print(f"move disk 1 from {source} -> {destination}")
        return
    tower_of_hanoi(n-1,source,destination,auxilary)
    print(f"move disk {n} from {source} -> {destination}")
    tower_of_hanoi(n-1,auxilary,source,destination)

tower_of_hanoi(3, 'A', 'B', 'C')