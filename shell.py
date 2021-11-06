import purse
while True:
    text = input(f"parse > ")
    if not text == "":
        result, error = purse.run('<stdin>', text)

        if error: print(error.as_string())
        elif result: print(result)
