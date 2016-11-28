def how_eligible(essay):
    eligible = 0
    if '?' in essay:
        eligible += 1
    if '!' in essay:
        eligible += 1
    if '"' in essay:
        eligible += 1   
    if ',' in essay:
        eligible += 1   
        return eligible       