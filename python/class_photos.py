"""
Create a function which takes in and compares two lists and determines if each index is taller or higher than the
other list. Returns true if one of the lists has all higher values, false otherwise.
"""


def class_photos(red_shirt_heights, blue_shirt_heights):
    red_shirt_heights.sort()
    blue_shirt_heights.sort()

    shirt_color = 'RED' if red_shirt_heights[0] < blue_shirt_heights[0] else 'BLUE'
    tallest_red = red_shirt_heights[-1]
    tallest_blue = blue_shirt_heights[-1]

    if tallest_red == tallest_blue:
        return False

    for idx in range(len(red_shirt_heights)):
        red_shirt_height = red_shirt_heights[idx]
        blue_shirt_height = blue_shirt_heights[idx]

        if abs(red_shirt_height - blue_shirt_height) == 0:
            return False
        elif shirt_color == 'RED' and red_shirt_height >= blue_shirt_height:
            return False
        elif shirt_color == 'BLUE' and blue_shirt_height >= red_shirt_height:
            return False

    return True


if __name__ == '__main__':
    print(class_photos([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))
    print(class_photos([2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6]))
