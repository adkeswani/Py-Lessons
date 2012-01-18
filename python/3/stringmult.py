lengths = [1, 2, 3, 4, 5]
strings = ["foo", "bar", "baz", "quz", "quuz"]

final = []
for i in range(0, len(lengths)):
    final.append(lengths[i] * strings[i])

print final
