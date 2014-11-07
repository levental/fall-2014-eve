def fi(numbers, a, b, index, limit):
    a, b = b, a + b
    numbers.append(a)
    index += index ** index
    if (index < limit):
        return fi(numbers, a, b, index, index)
    else:
        return

numbers = []
fi(numbers, 1, 1, 0, 9)
print numbers


http://www.yesmail.com/sites/default/files/Mid_Level_Images/trigger_intelligence_mid-level_image.jpg