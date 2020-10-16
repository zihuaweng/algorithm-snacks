import math

def main(instances, cpus):
    idx = 0
    n = len(cpus)
    while idx < n:
        if cpus[idx] < 25:
            if instances == 1:
                idx += 1
            else:
                instances = math.ceil(instances / 2.0)
                idx += 10
        elif cpus[idx] > 60:
            if instances * 2 < 2 * 10**8:
                instances *= 2
                idx += 10
            else:
                idx += 1
        else:
            idx += 1
    
    return instances

print(main(2, [25,23,1,2,3,4,5,6,7,8,9,10,76,80]))
print(main(1, [5,10,80]))
print(main(5, [30,5,4,8,19,89]))

