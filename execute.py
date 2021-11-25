import parse, sys

result, error = parse.execute('<stdin>', f"run(\"{sys.argv[1]}\")")

if error:
    print(error.as_string())
elif result:
    if len(result.elements) == 1:
        print(repr(result.elements[0]))
    else:
        print(repr(result))