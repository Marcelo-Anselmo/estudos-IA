import math

input = 1
output_desire = 0

input_weight = 0.5

learning_rate = 0.1

def activation(sum):
    if sum >= 0:
        return 1
    else:
        return 0

print("entrada", input, "desejado", output_desire)

error = math.inf

interation = 0

bias = 1
bias_weight = 0.5

while not error == 0:
    interation += 1
    print("######## Interação: ", interation)
    print("peso", input_weight)
    sum = (input * input_weight) + (bias * bias_weight)

    output = activation(sum)

    error = output_desire - output

    print("saida", output)
    print("erro", error)

    if not error == 0:
        input_weight = input_weight + (learning_rate * input * error)
        bias_weight = bias_weight + (learning_rate * bias * error)

print("A rede aprendeu Querid@!!")