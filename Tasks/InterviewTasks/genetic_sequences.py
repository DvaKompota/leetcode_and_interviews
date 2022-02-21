# Given this:
# ["ACAAA", "TTGTA", "GGTGT", "CTCCC", "GAACG", "GACCC", "TAAAC", "TTCTG", "AGCTT", "AGTGA", "TCCCT", "GCCAT"]

# You'd want to return this:
# ["NCAAA", "NNGTA", "NNNGT", "NNNNC", "NNNNN", "GNNNN", "TANNN", "TTCNN", "AGCTN", "AGTGA", "NCCCT", "NNCAT"]


def correct_sequence(sequence, replace_char="N", starting_position=1, going_forward=True):
    gene_length = len(sequence[0])
    position = starting_position
    going_forward = going_forward
    output_list = []
    for i in range(len(sequence)):
        if going_forward:
            elem = replace_char * position + sequence[i][position:]
            output_list.append(elem)
            going_forward = False if position == gene_length - 1 else True
            position += 1 if position < gene_length else -1
        elif not going_forward:
            elem = sequence[i][:gene_length - position] + replace_char * position
            output_list.append(elem)
            going_forward = True if position == 0 else False
            position -= 1 if position > 0 else -1
    return output_list


if __name__ == '__main__':
    seq = ["ACAAA", "TTGTA", "GGTGT", "CTCCC", "GAACG", "GACCC", "TAAAC", "TTCTG", "AGCTT", "AGTGA", "TCCCT", "GCCAT"]
    result = correct_sequence(seq)
    print(result)
