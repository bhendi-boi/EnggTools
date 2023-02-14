# EnggTools

A Repo comprising math and physics tools for folks pursuing bachelors.

## DaBoyz

DaBoyz is the organization that maintains this repo.
Members include

- [Vibhav Gopal](https://github.com/Vibhav-Gopal)
- [Jyothikrishna](https://github.com/bhendi-boi)
- [Praneeth](https://github.com/ProfessorZoom023)
- [Advaita kartikeya](https://github.com/addukar28)

Want to know how to use this amazing tool, follow along to find out!

## Geometry

There is a folder by name `geometry` in the root of this repo. As the name suggests this folder consists of tools related to geometry.

## 2D Geometry

There is a file by name `twodim.py` in `geometry` folder. Use this file to access any 2D element like point, line, circle etc.

### Point

This is one of the basic element in 2D Geometry. This represents a point in 2D cartesian coordinate system.

- ### Initialization

  You can create a point by calling the Point constructor with a tuple say `(x,y)` as an argument. Here x,y represents the xcoordinate and ycoordinate of the point p.

  ```python
  from geometry.twodim import Point
  p = Point((1,2))
  ```

- ### Distance from Origin

  Use this method to find the distance between origin and a point.

  - arguments : none
  - return type : float

  ```python
  from geometry.twodim import Line

  p = Point(2,0)
  print(p.dist2origin())
  # it will return 2.0
  ```

- ### Distance from a point

  Use this method to find the distance between two points.

  - arguments : Point
  - return type : float

  ```python
  from geometry.twodim import Line

  p1 = Point(2,0)
  p2 = Point(1,0)
  print(p2.dist2point((1,0)))
  # it will return 1.0
  ```

### Line

This is one of the basic element in 2D Geometry. This represents a line in 2D cartesian coordinate system.

- ### Initialization

  You can create a line by calling the Line constructor with a tuple say `(a,b,c)` as an argument. Here a,b,c represents the xcoefficient, ycooefficent and constant of the line l when written in the form `ax+by+c = 0`.

  ```python
  from geometry.twodim import Line
  l = Line((1,1,-3))
  ```

  From two points on a line

  ```python
  from geometry.twodim import Line, Point
  p1 = Point((1,2))
  p2 = Point(2,2)
  l = Line(p1,p2)
  # returns a line pasing through points p1 and p2
  # i.e. y-2=0
  ```

- ### containsPoint
  Use this method to find whether a point is present on a line.
  - params : Point
  - return type: bool
  ```python
  from geometry.twodim import Line, Point
  p1 = Point((1,2))
  p2 = Point((2,2))
  l = Line(p1,p2)
  lcontainsp1 = l.containsPoint(p1)
  # returns True cuz l passes through p1
  p3 = Point((1,0))
  lcontainsp3 = l.containsPoint(p3)
  # retuns False cuz l does not pass through p3
  ```
- ### onSameSide
  Use this method to find whether a point is present on a line.
  - params : Point, Point
  - return type: bool
  ```python
  from geometry.twodim import Line, Point
  l = Line((1,0,0))
  p1 = Point((2,0))
  p2 = Point((2,8))
  p1p2OnSameSideOfL = l.onSameSide(p1,p2)
  # returns True cuz p1, p2 are on the same side of line l.
  p3 = Point((-1,3))
  p1p3OnSameSideOfL = l.onSameSide(p1,p3)
  # retuns False cuz p1 and p3 doesnot fall on the same side of line l.
  ```
- ### passesThroughOrigin

  Use this method to find whether a line passes through origin or not.

  - params : none
  - return type: bool

  ```python
  from geometry.twodim import Line
  l = Line((1,2,0))
  lPassesThroughOrigin = l.passesThroughOrigin()
  # returns True cuz line l passes throught origin
  l2 = Line((1,2,3))
  lPassesThroughOrigin = l2.passesThroughOrigin()
  # retuns False cuz l2 doesnot pass through origin
  ```

  **Note**
  You can use `containsPoint` method to find whether a line passes through origin or not. But we recommend you to use `passesThroughOrigin` instead because it is faster when compared to `containsPoint`.
