def function(chart, actual_state, actual_letter):
    for posibility in chart:
        if actual_state==posibility[0] and actual_letter==posibility[1]:
            return posibility[2]


# "Deterministic finite automaton- parameters"

states=[str(x) for x in input("Enter all the states of the automaton: ").strip().split()]
alfabet=[str(x) for x in input("Enter all the letters of the automaton: ").strip().split()]
chart=[]
for state in states:
    for letter in alfabet:
        equivalent_state = str(input(f"f({state},{letter})= ").strip())
        chart.append((state, letter, equivalent_state))
initial_state=str(input("Enter the initial state of the automaton: ").strip())
final_state=[str(x) for x in input("Enter all the final states of the automaton: ").strip().split()]


word=str(input("Type the word you want to check for compatibility:  "))

actual_state=initial_state
route=[actual_state]
for index in range(len(word)):
    actual_state=function(chart, actual_state, word[index])
    route.append(actual_state)


if actual_state not in final_state:
    print("The word is not accepted.")
else:
    print("The word is accepted.")
    for state in route:
        print(f"{state} -> ", end="")
    print("IESIRE",end="")