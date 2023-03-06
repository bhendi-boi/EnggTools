# Point

This is one of the basic element in 2D Geometry. This represents a point in 2D cartesian coordinate system.

- # Initialization

  You can create a point by calling the Point constructor with a tuple say `(x,y)` as an argument. Here x,y represents the xcoordinate and ycoordinate of the point p.

  ```python
  from geometry import Point

  p = Point((1,2))
  ```

- ## Distance from Origin

  Use this method to find the distance between origin and a point.

  - arguments : none
  - return type : float

    ```python
    from geometry import Point

    p = Point(2,0)

    print(p.dist2origin())
    # it will return 2.0
    ```

- ## Distance from a point

  Use this method to find the distance between two points.

  - arguments : Point
  - return type : float

  ```python
  from geometry import Point

  p1 = Point(2,0)
  p2 = Point(1,0)

  print(p2.dist2point((1,0)))
  # it will return 1.0
  ```
