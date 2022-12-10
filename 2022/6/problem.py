with open('input.txt', 'r') as f:
    input_string = f.read()

marker_detector = []
for i, letter in enumerate(input_string):    
    marker_detector.append(letter)

    if marker_detector.__len__() == 4:
        if len(set(marker_detector)) == len(marker_detector):
            print({'part1': i+1})
            break
        marker_detector.pop(0)

marker_detector.clear()
for i, letter in enumerate(input_string):    
    marker_detector.append(letter)

    if marker_detector.__len__() == 14:
        if len(set(marker_detector)) == len(marker_detector):
            print({'part2': i+1})
            break
        marker_detector.pop(0)







