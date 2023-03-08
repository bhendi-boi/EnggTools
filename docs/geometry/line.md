# Line

This is one of the basic element in 2D Geometry. This represents a line in 2D cartesian coordinate system.

- ## Initialization

  You can create a line by calling the Line constructor with a tuple say `(a,b,c)` as an argument. Here a,b,c represents the xcoefficient, ycooefficent and constant of the line l when written in the form `ax+by+c = 0`.

  ```python
  from geometry import Line
  l = Line((1,1,-3))
  ```

  From two points on a line

  ```python
  from geometry import Line, Point

  p1 = Point((1,2))
  p2 = Point(2,2)

  l = Line(p1,p2)
  # returns a line pasing through points p1 and p2
  # i.e. y-2=0
  ```

  From specifying line equation in the form of a string

  ```python
  from geometry import Line

  line1 = Line.initFromString("2x - 3y = 0")
  # returns a line object which represents 2x - 3y = 0
  ```

- ## containsPoint

  Use this method to find whether a point is present on a line.

  - params : Point
  - return type: bool

  ```python
  from geometry import Line, Point

  p1 = Point((1,2))
  p2 = Point((2,2))
  l = Line(p1,p2)

  lcontainsp1 = l.containsPoint(p1)
  # returns True cuz l passes through p1

  p3 = Point((1,0))
  lcontainsp3 = l.containsPoint(p3)
  # retuns False cuz l does not pass through p3
  ```

- ## onSameSide

  Use this method to find whether a point is present on a line.

  - params : Point, Point
  - return type: bool

  ```python
  from geometry import Line, Point

  l = Line((1,0,0))
  p1 = Point((2,0))
  p2 = Point((2,8))

  p1p2OnSameSideOfL = l.onSameSide(p1,p2)
  # returns True cuz p1, p2 are on the same side of line l.

  p3 = Point((-1,3))
  p1p3OnSameSideOfL = l.onSameSide(p1,p3)
  # retuns False cuz p1 and p3 doesnot fall on the same side of line l.
  ```

- ## passesThroughOrigin

  Use this method to find whether a line passes through origin or not.

  - params : none
  - return type: bool

  ```python
  from geometry import Line

  l = Line((1,2,0))
  lPassesThroughOrigin = l.passesThroughOrigin()
  # returns True cuz line l passes throught origin

  l2 = Line((1,2,3))
  lPassesThroughOrigin = l2.passesThroughOrigin()
  # retuns False cuz l2 doesnot pass through origin
  ```

  **Note**
  You can use `containsPoint` method to find whether a line passes through origin or not. But we recommend you to use `passesThroughOrigin` instead because it is faster when compared to `containsPoint`.

- ## isParallelTo

  Use this method to find whether a line is parallel to another line or not.

  - params : Line
  - return type: bool

  ```python
  from geometry import Line

  l1 = Line((2,4,0))
  l2 = Line((1,4,3))

  l1IsParallelToL2 = l1.isParallelTo(l2)
  # retuns False cuz l2 is not parallel to l1

  l3= Line((1,2,3))
  l1IsParallelToL3 = l1.isParallelTo(l3)
  # retuns True cuz l3 is parallel to l1
  ```

- ## isPerpendicularTo

  Use this method to find whether a line is perpendicular to another line or not.

  - params : Line
  - return type: bool

  ```python
  from geometry import Line

  l1 = Line((2,4,0))
  l2 = Line((1,4,3))

  l1IsPerpendicularToL2 = l1.isPerpendicularlTo(l2)
  # retuns False cuz l2 is not parallel to l1

  l3 = Line((-2,1,3))
  l1IsPerpendicularToL3 = l1.isPerpendicularlTo(l3)
  # retuns True cuz l3 is parallel to l1
  ```

- ## isIntersectingWith

  Use this method to find whether a line is intersecting with another line or not.

  - params : Line
  - return type: bool

  ```python
  from geometry import Line

  l1 = Line((2,4,0))
  l2 = Line((1,2,0))

  l1IntersectsWithL2 = l1.isIntersectingWith(l2)
  # retuns False cuz l2 is not intersecting with L2

  l3 = Line((-2,1,3))
  l1IntersectsWithL3 = l1.isIntersectingWith(l3)
  # retuns True cuz l3 is intersecting with L3
  ```

- ## intersectsAt

  Use this method to find the intersection point of a line with other.
  `intersectsAt` will return False if both lines do not intersect.

  - params : Line
  - return type: Point | bool

  ```python
  from geometry import Line

  l1 = Line((2,4,0))
  l2 = Line((1,2,0))

  l1IntersectsWithL2 = l1.isIntersectingWith(l2)
  # retuns False cuz l2 is not intersecting with L2

  l3 = Line((0,1,0))
  l1IntersectsWithL3 = l1.isIntersectingWith(l3)
  # retuns (2,0) cuz l3 is intersecting with L3
  ```
