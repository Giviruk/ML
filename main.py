import random as rnd
import sys


def make_child(population):
    first_index = rnd.randint(0, len(population)-1)
    second_index = rnd.randint(0, len(population)-1)
    while first_index == second_index:
        second_index = rnd.randint(0, len(population)-1)
    first_parent = population[first_index]
    second_parent = population[second_index]
    child = []
    for i in range(0, len(first_parent)):
        p = rnd.randint(0, 1)
        if p == 0:
            child.append(first_parent[i])
        else:
            child.append(second_parent[i])
    return child


def make_mutation(population):
    count = rnd.randint(0, 5)
    was_mutation = []
    for i in range(0, count):
        index = rnd.randint(0, len(population)-1)
        was_mutation.append(index)
        mutation_index = rnd.randint(0, len(population[index])-1)
        population[index][mutation_index] += rnd.randint(0, 10)

    return population


def fitness(population, coefficients, answer):
    q = {}
    for j in range(len(population)):
        ind = population[j]
        ans = 0
        for i in range(len(ind)):
            ans += ind[i]*coefficients[i]
        ans += coefficients[len(coefficients)-1]
        if ans == answer:
            return ind
        q[j] = abs(answer - ans)
    arr = []
    for i in range(len(q)):
        for j in range(0, q[i]):
            arr.append(i)
    values_for_delete = []
    for i in range(0, 5):
        index = rnd.randint(0, len(arr)-1)
        el = arr[index]
        values_for_delete.append(population[el])
        while el in arr:
            arr.remove(el)
    for item in values_for_delete:
        population.remove(item)
    for i in range(0, 5):
        population.append(make_child(population))
    return make_mutation(population)


def calculate_ans(individ, coeffs, ans):
    local_ans = 0
    for i in range(0, len(coeffs)-1):
        local_ans += individ[i]*coeffs[i]
    local_ans += coeffs[len(coeffs)-1]
    return abs(ans-local_ans)


if __name__ == '__main__':
    count_variables = int(input())
    coefficients = []
    for i in range(0, count_variables+1):
        coefficient = int(input())
        coefficients.append(coefficient)
    answer = int(input())
    max = max(max(coefficients), answer)
    population = []
    answer_was_found = False
    for i in range(10):
        new_age = []
        for i in range(0, count_variables):
            new_age.append(rnd.randint(1, max))
        population.append(new_age)
    for i in range(0, 100):
        population = fitness(population, coefficients, answer)
        for individ in population:
            ans = calculate_ans(individ, coefficients, answer)
            if ans == 0 and not answer_was_found:
                print('answer = ')
                print(individ)
                answer_was_found = True
    if not answer_was_found:
        min_ans = sys.maxsize
        ind = []
        for individ in population:
            if calculate_ans(individ, coefficients, answer) < min_ans:
                min_ans = calculate_ans(individ, coefficients, answer)
                ind = individ
        print(ind)
        print(min_ans)

    print("end pg")
    a = 1
