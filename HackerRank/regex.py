# match the string "hackerrank" (this is case sensitive)
r'hackerrank'

# matches only and exactly strings of form: abc.def.ghi.jkx
# where each variable can be any single character except the newline
r"^(...)\.(...)\.(...)\.(...)$"

# match the pattern xxXxxXxxxx where denotes x a digit character
# and X denotes a non-digit character
r"(\d\d)\D(\d\d)\D(\d\d\d\d)"

# match the pattern XXxXXxXX where x denotes whitespace characters ([\r\n\t\f])
# and X denotes non-white space characters
r"(\S\S)\s(\S\S)\s(\S\S)"

# match the pattern xxxXxxxxxxxxxxXxxx where x denotes any word character (a-z, A-Z, 0-9, _)
# and X denotes any non-word character
r"(\w\w\w)\W(\w\w\w\w\w\w\w\w\w\w)\W(\w\w\w)"

# match the pattern Xxxxx. where x denotes a word character and X denotes a digit.
# The string must start with X and end with . and be just 6 characters long
r"^\d\w\w\w\w\.$"

# match S with following conditions:
# 1) S must be of length 6
# 2) 1st character: 1, 2, or 3
# 3) 2nd character: 1, 2, or 0
# 4) 3rd character: x, s, or 0
# 5) 4th character: 3, 0, A, or a
# 6) 5th character: x, s, or u
# 7) 6th character: . or ,
r'^[123][120][xs0][30Aa][xsu][\.,]$'

# match S with following conditions:
# 1) S must be of length 6
# 2) 1st character: not a digit
# 3) 2nd character: not a lowercase vowel
# 4) 3rd character: not b, c, D, or F
# 5) 4th character: not a whitespace character
# 6) 5th character: not a uppercase vowel
# 7) 6th character: not a . or ,
r'^[^\d][^aeiou][^bcDF][^\s][^AEIOU][^\.,]$'

# match S with following conditions:
# 1) S must be of length >= 5
# 2) 1st character: a lowercase character
# 3) 2nd character: a positive digit (i.e., not including 0)
# 4) 3rd character: not a lowercase character
# 5) 4th character: not an uppercase character
# 6) 5th character: an uppercase character
r'^[a-z][1-9][^a-z][^A-Z][A-Z]'

# match S with following conditions:
# 1) S must be of length 45
# 2) 1st characters: consist of letters (both lowercase and uppercase) or of even digits
# 3) last characters: consist of odd digits or whitespace characters
r'^[a-zA-Z02468]{40}[\s13579]{5}$'

# match S with following conditions:
# 1) begin with 1 or 2 digits
# 2) after that, should have 3 or more letters (both lowercase and uppercase)
# 3) then should end with up to 3 . symbol(s) (could be 0 to 3, inclusively)
r'^\d{1,2}[a-zA-Z]{3,}\.{0,3}$'

# match S with following conditions:
# 1) begin with 2 or more digits
# 2) after that, should have 0 or more lowercase letters
# 3) then should end with 0 or more uppercase letters
r'^\d{2,}[a-z]*[A-Z]*$'

# match S with following conditions:
# 1) begin with 1 or more digits
# 2) after that, should have 1 or more uppercase letters
# 3) then should end with 1 or more lowercase letters
r'^\d+[A-Z]+[a-z]+$'

# match S with following conditions:
# 1) consist of only lowercase and uppercase letters
# 2) should end in s
r'^[a-zA-Z]*s$'

# Three different positions qualify for word boundaries:
# 1) Before the first character in the string, if the first character is a word character.
# 2) Between two characters in the string, where one is a word character and the other is not.
# 3) After the last character in the string, if the last character is a word character.

# match word:
# 1) starting with vowel (a,e,i,o, u, A, E, I , O, or U)
# 2) the matched word can be of any length
# 3) the matched word consist of letters (lowercase and uppercase) only
# 4) the matched word must start and end with a word boundary
r'\b[aeiouAEIOU][a-zA-Z]*\b'

# match S that has 3 or more consecutive repetitions of 'ok'
r'(ok){3,}'

# match S with following conditions:
# 1) start with Mr., Mrs., Ms., Dr., or Er.
# 2) after that, must contain only 1 or more letters (lowercase and uppercase)
r'^(Mr\.|Mrs\.|Ms\.|Dr\.|Er\.)([a-z]|[A-Z])+$'

# match S with following conditions:
# 1) S must be of length 20
# 2) 1st character: lowercase letter
# 3) 2nd character: word character
# 4) 3rd character: whitespace character
# 5) 4th character: non-word character
# 6) 5th character: digit
# 7) 6th character: non-digit
# 8) 7th character: uppercase letter
# 9) 8th character: letter (either lowercase or uppercase)
# 10) 9th character: vowel (a, e, i , o , u, A, E, I, O, or U)
# 11) 10th character: non-whitespace character
# 12) 11th character: same as 1st character
# 13) 12th character: same as 2nd
# 14) 13th character: same as 3rd
# 15) 14th character: same as 4th
# 16) 15th character: same as 5th
# 17) 16th character: same as 6th
# 18) 17th character: same as 7th
# 19) 18th character: same as 8th
# 20) 19th character: same as 9th
# 21) 20th character: same as 10th
r'^([a-z])(\w)(\s)(\W)(\d)(\D)([A-Z])([a-zA-Z])([aeiouAEIOU])(\S)\1\2\3\4\5\6\7\8\9\10$'

# match S with following conditions:
# 1) contains 8 digits
# 2) may or may not have "-" separator such that S gets divided in 4 parts,
# with each part having exactly 2 digits (e.g., 12-34-56-78)
# **NOTE**: r"^(\d\d)(-)?(\d\d)\2(\d\d)\2(\d\d)$" does NOT work!
# (though this works in Javascript's flavor of regex) this is because the backreference (\1) fails
# to match but when the backreference is optional (? means 0 or 1 so (b?) then b is optional) then
# it's fine that the backreference fails to match
r"^(\d\d)(-?)(\d\d)\2(\d\d)\2(\d\d)$"

# match all occurrences of 'o' followed immediately by 'oo'
r'o(?=oo)'

# match all characters which are not immediately followed by that same character
r"(.)(?!\1)"

# match all the occurences of digit which are immediately preceded by odd digit
r"(?<=[13579])\d"

# match all the occurences of characters which are not immediately preceded by vowels (a, e, i, u, o, A, E, I, O, U)
r"(?<![aeiouAEIOU])."
