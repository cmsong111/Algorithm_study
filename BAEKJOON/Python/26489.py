standard_input = """gum gum for jay jay
gum gum for jay jay
gum gum for jay jay
gum gum for jay jay
gum gum for jay jay
gum gum for jay jay
gum gum for jay jay
gum gum for jay jay
gum gum for jay jay
gum gum for jay jay
gum gum for jay jay
"""

result = 0


while True:
    try:
        input()
        result += 1
    except EOFError:
        print(result)
        break
