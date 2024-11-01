class Camera:
    def __init__(self):
        print("i can capture pics and videos")
class Pen(Camera):
    def __init__(self):
        print("i will write")
        super().__init__()
class Phone(Camera):
    def __init__(self):
        print("i will communicate ")
        super().__init__()
        
