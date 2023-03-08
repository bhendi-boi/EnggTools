# Cirlce

This is one of the basic element in 2D Geometry. This represents a Circle in 2D cartesian coordinate system.

- ## Initialization

  You can create a circle by calling the Circle constructor with `radius` and `center` as an arguments. This creates a circle with using the equation `(x-x1)^2 + (y-y1)^2 = r^2`

  ```python
  from geometry import Circle, Point
  center = Point((0,0))
  raduis = 5
  c1 = Circle(raduis, center)
  # Returns a circle object which is equivalent to x^2 + y^2 = 5^2
  ```
