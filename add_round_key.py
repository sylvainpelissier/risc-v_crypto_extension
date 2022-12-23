from Crypto.Util.strxor import strxor

def add_round_key(s, k):
    result = []
    for i in range(4):
        result.append(list(strxor(bytes(s[i]), bytes(k[i]))))

    return result

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    return bytes([item for sublist in matrix for item in sublist])

if __name__ == "__main__":
    state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
    ]

    round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
    ]
    matrix = add_round_key(state, round_key)
    print(matrix)
    print(matrix2bytes(matrix))