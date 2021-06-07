
def get_binary_gap(number):
    try:
        binary_number = format(number, 'b').strip('0')
        binary_number = binary_number.split('1')
        return len(max(binary_number))
    except Exception as e:
        print("ERROR", e)


binary_gap = get_binary_gap(5)
print(binary_gap)
