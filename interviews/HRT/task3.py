def solution(S, Y, Z):
    errMsg = S[Y]

    # Prepend at most Z characters to error.
    i = Y - 1
    numLines = 0
    while i >= 0 and (Y - i) <= Z:
        if S[i] == '\n':
            numLines += 1
        # Don't want to prepend a newline, so we break if there's another line above.
        if numLines > 1:
            break

        errMsg = S[i] + errMsg
        i -= 1

    i = Y + 1
    if errMsg[-1] != '\n':
        while i < len(S) and S[i] != '\n' and (i - Y) <= Z:
            errMsg += S[i]
            i += 1

        errMsg += '\n'

    # Calculate the number of spaces needed before caret.
    j = Y - 1
    numSpaces = 0
    while j >= 0 and S[j] != '\n' and (Y - j) <= Z:
        numSpaces += 1
        j -= 1

    errMsg += ' '*numSpaces + '^'

    if i < len(S) and S[i] != '\n':
        errMsg += '\n'

    # Append at most Z characters to error after caret.
    numLines = 0
    while i < len(S) and numLines < 2 and (i - Y) <= Z:
        if S[i] == '\n':
            numLines += 1

        errMsg += S[i]
        i += 1

    return errMsg


print(solution('// comment\nint main() {\n    return 0\n}\n', 36, 126))

print(solution('Hello\n', 3, 1000))

print(solution('123', 1, 0))

print(solution('abcde\nfghij\nklmno\n', 8, 5))

print(solution('abcde\nfghij\nk\nmno\n', 8, 5))
