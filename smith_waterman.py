import numpy as np

MATCH = 5
GAP = -4
MISMATCH = -3


def print_score_matrix(score_matrix, sequence1, sequence2):
    def print_row(row):
        for i in range(len(row)):
            print(f'| %-4s ' % row[i], end='')
        print('|')
    temp_seq1 = ' ' + sequence1
    temp_seq2 = ' ' + sequence2
    print_row(' ' + temp_seq1)
    
    for i in range(len(score_matrix)):
        print_row([temp_seq2[i]] + list(score_matrix[i]))

def backtrack(score_matrix, sequence1, sequence2, row_index, col_index):
    aligned_seq1 = ''
    aligned_seq2 = ''
    move = [[0, -1], [-1, 0], [-1, -1]]
    while row_index != 0 and col_index != 0:
        is_match = (sequence1[col_index-1] ==  sequence2[row_index-1])
        if is_match:
            scores = [0, 0, 1]
        else:
            left_score = score_matrix[row_index][col_index-1]
            top_score = score_matrix[row_index-1][col_index]
            diagonal_score = score_matrix[row_index-1][col_index-1]
            scores = [left_score, top_score, diagonal_score]

        maxindex = scores.index(max(scores))
        if maxindex == 0:
            aligned_seq1 += sequence1[col_index-1]
            aligned_seq2 += '-'
        elif maxindex == 1:
            aligned_seq1 += '-'
            aligned_seq2 += sequence2[row_index-1]
        else:
            aligned_seq1 += sequence1[col_index-1]
            aligned_seq2 += sequence2[row_index-1]
        row_index += move[maxindex][0]
        col_index += move[maxindex][1]

    aligned_seq1 = aligned_seq1[::-1]
    aligned_seq2 = aligned_seq2[::-1]

    return aligned_seq1, aligned_seq2

def smith_waterman(sequence1, sequence2):
    no_rows = len(sequence2) + 1
    no_cols = len(sequence1) + 1
    score_matrix = np.zeros((no_rows, no_cols))
    score_matrix[:, 0] = [0 * i for i in range(no_rows)]
    score_matrix[0, :] = [0 * i for i in range(no_cols)]

    max_row_index, max_col_index = 0, 0
    max_value = -9999
    for i in range(1, no_rows):
        for j in range(1, no_cols):
            is_match = (sequence1[j-1] == sequence2[i-1])
            left_score = score_matrix[i][j-1] + GAP
            top_score = score_matrix[i-1][j] + GAP
            diagonal_score = score_matrix[i-1][j-1] + (MATCH if is_match else MISMATCH)
            score = max(diagonal_score, left_score, top_score)
            score_matrix[i][j] = (score if score >= 0 else 0)
            if score_matrix[i][j] > max_value:
                max_value = score_matrix[i][j]
                max_row_index, max_col_index = i, j
    
    aligned_seq1, aligned_seq2 = backtrack(score_matrix, seq1, seq2, max_row_index, max_col_index)

    return aligned_seq1, aligned_seq2


seq1 = 'CGTGAATTCAT'
seq2 = 'GACTTAC'
print('Input Sequence 1', seq1)
print('Input Sequence 2', seq2)
print()
aligned_seq1, aligned_seq2 = smith_waterman(sequence1=seq1, sequence2=seq2)
print('Output Sequence 1', aligned_seq1)
print('Output Sequence 2', aligned_seq2)

