from math import log

# The trick was to take the log of both sides and then compare
def prob99():
    base_exp_file = open('base_exp.txt', 'r')
    max_pair = 0
    line_num_max = 0
    for line_num, line in enumerate(base_exp_file.readlines()):
        base_exp = line.split(',')
        pair = int(base_exp[1]) * log(int(base_exp[0]))
        if pair > max_pair:
            max_pair = pair
            line_num_max = line_num

    base_exp_file.close()
    return line_num_max

def main():
    # Note: ProjectEuler started counting line numbers from 1 not 0
    # so you have to add 1 to the return value
    print(prob99())

if __name__ == '__main__':
    main()
