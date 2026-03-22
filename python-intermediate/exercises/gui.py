#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

def show_tree():
    for sub_array in picture:
        line = ''
        for item in sub_array:
            if item == 1:
                line += '*'
            elif item == 0:
                line += ' '
        print(line)

show_tree()
show_tree()
print(show_tree) # just show the location of this function in memory