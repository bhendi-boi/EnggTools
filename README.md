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

### 2D Geometry

There is a file by name `twodim.py` in `geometry` folder. Use this file to access any 2D element like point, line, circle etc.

#### Point

This is one of the basic element in 2D Geometry. This represents a point in 2D cartesian coordinate system.

- ##### Initialization
  You can create a point by calling the Point constructor with a tuple say `(x,y)` as an argument. Here x,y represents the xcoordinate and ycoordinate of the point p.

```python
from geometry.twodim import Point
p = Point((1,2))
```

- ##### Distance from Origin
  Use this method to find the distance between origin and a point.
  - arguments : none
  - return type : float

```python
from geometry.twodim import Line

p = Point(2,0)
print(p.dist2origin())
# it will return 2.0
```

- ##### Distance from a point
  Use this method to find the distance between two points.
  - arguments : point
  - return type : float

```python
from geometry.twodim import Line

p1 = Point(2,0)
p2 = Point(1,0)
print(p2.dist2point((1,0)))
# it will return 1.0
```

#### Line

This is one of the basic element in 2D Geometry. This represents a line in 2D cartesian coordinate system.

- ##### Initialization
  You can create a line by calling the Line constructor with a tuple say `(a,b,c)` as an argument. Here a,b,c represents the xcoefficient, ycooefficent and constant of the line l when written in the form `ax+by+c = 0`.

```python
from geometry.twodim import Line
l = Line((1,1,-3))
```
