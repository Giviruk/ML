dataset = {
    'b_1': [0.97, 0.99, 0.66, 0.73, 0.93, 0.97, 0.93, 0.01, 0.96, 0.53, 0.04, 0.75],
    'b_2': [0.96, 0.98, 0.73, 0.75, 0.9, 0.96, 0.01, 0.94, 0.94, 0.64, 0.02, 0.08],
    'b_3': [1, 1, 0.88, 0.88, 1, 1, 0.77, 0.77, 1, 0.77, 0, 1],
    'b_4': [0.92, 0.96, 0.76, 0.76, 0.8, 1, 0.96, 0.0001, 1, 0.6, 0.08, 0.72],
    'b_5': [0.91, 1, 0.79, 0.86, 0.75, 0.83, 0.03, 0.86, 0.93, 0.41, 0.06, 0.0001],
    'b_6': [1, 1, 0.5, 0.5, 0.5, 0.5, 0.1, 0.0001, 0.5, 0.0001, 0.5, 1],
    'b_7': [1, 1, 0.5, 0.5, 0.5, 0.1, 0.0001, 0.1, 1, 1, 0.0001, 0.5],
    'b_8': [1, 0.7, 1, 0.8, 0.57, 0.85, 0.85, 0.0001, 1, 0.42, 0.0001, 0.85],
    'b_9': [0.9, 1, 0.6, 0.6, 0.4, 0.9, 0.0001, 0.8, 1, 0.6, 0.0001, 0.09]
}

if __name__ == '__main__':
    input_symptoms = [1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0]
    output_probabilities = {}
    for k in dataset.keys():
        probability = 1
        for i in range(len(input_symptoms)):
            if input_symptoms[i] == 0:
                probability = probability * (1 - dataset[k][i])
            else:
                probability = probability * dataset[k][i]
        output_probabilities[k] = probability
    print('Самая вероятная болезнь: ' + max(output_probabilities, key=output_probabilities.get))
    print('Вероятности всех болезней: ')
    for k in output_probabilities.keys():
        print(k + ' ' + str(output_probabilities[k]))
    pass

