class Marker:
    def __init__(self, color='Red'):
        self.color = color


class MarkerBox:
    def __init__(self, markers=[]):
        self.markers = markers

    def add_marker(self, marker):
        self.markers.append(marker)

    def remove_marker(self, color):
        for marker in self.markers:
            if marker.color == color:
                self.markers.remove(marker)
                return marker
        return None


if __name__ == "__main__":
    mest_markers = MarkerBox()
    mest_markers.add_marker(Marker(color="blue"))
    mest_markers.add_marker(Marker(color="black"))
    #mest_markers.remove_marker(color="blue")

count = 0
for Mark in mest_markers.markers:
    count += 1
    print Mark.color
print "We have {} color ".format(count)