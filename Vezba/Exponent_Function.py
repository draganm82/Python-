def rais_to_power(base_num, pow_number):
    result = 1
    for index in range(pow_number):
        result = result * base_num
        return result


print (rais_to_power(3, 4))

