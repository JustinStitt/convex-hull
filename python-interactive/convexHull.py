class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'({self.x}, {self.y})'


def determinant(A: Point, B: Point, p: Point) -> float:
    return (B.x - A.x)*(p.y - A.y) - (B.y - A.y)*(p.x - A.x)

def distance(A, B):
    return (B.y-A.y)**2 + (B.x-A.x)**2

def convexHull(points: list) -> list:
    '''
    return list of points that construct
    the convex hull from the given list of
    points.
    '''
    hull = []
    for u in points:
        for v in points:
            if u == v: continue
            same_side = True
            for i in range(len(points) - 1):
                d1 = determinant(u, v, points[i])
                d2 = determinant(u, v, points[i+1])
                s1, s2 = d1 >= 0, d2 >= 0
                if s1 ^ s2: same_side = False; break;
            if same_side:
                hull.append((u, v))
    return hull
