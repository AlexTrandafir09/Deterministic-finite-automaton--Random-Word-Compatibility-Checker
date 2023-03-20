def function(chart, actual_state, actual_letter):
    for posibility in chart:
        if actual_state==posibility[0] and actual_letter==posibility[1]:
            return posibility[2]

print(" Deterministic finite automaton- Parameters")
states=[str(x) for x in input("Type all the states of the automaton: ").strip().split()]
alfabet=[str(x) for x in input("Type all the letters of the automaton: ").strip().split()]
chart=[]
for state in states:
    for letter in alfabet:
        equivalent_state = str(input(f"f({state},{letter})=").strip())
        chart.append((state, letter, equivalent_state))
initial_state=str(input("Type the initial state: ").strip())
final_states=[str(x) for x in input("Type all the final states: ").strip().split()]
print("Word")
word=str(input("Word= "))

actual_state=initial_state
route=[actual_state]
for index in range(len(word)):
    actual_state=function(chart, actual_state, word[index])
    route.append(actual_state)


if actual_state not in final_states:
    print("Not acceptable.")
else:
    print("Acceptable.")
    for state in route:
        print(f"{state} -> ", end="")
    print("exit",end="")