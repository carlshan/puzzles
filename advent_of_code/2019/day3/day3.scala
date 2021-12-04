import scala.io.Source
import scala.collection.mutable.ListBuffer

val wire1Name = "./wire1.in"
val wire2Name = "./wire2.in"


def getInstruc(instruc: String) : (Char, Int) = {
  val dir = instruc.head
  val value = instruc.tail.toInt
  (dir, value)
}

// val wire1Name = "./test1.in"
// val wire2Name = "./test2.in"

val wire1 = Source.fromFile(wire1Name).getLines.toList.head.split(",").map(getInstruc)
val wire2 = Source.fromFile(wire2Name).getLines.toList.head.split(",").map(getInstruc)

def coordsHelper(current: List[Int], dir: Char, value: Int) : Array[List[Int]] = {
  var new_coords = Array.empty[List[Int]]
  if (dir == 'U') {
    val beg = current(1) + 1
    val end = current(1) + value
    for (y <- beg to end) {
      val new_coord = Array(List(current(0), y))
      new_coords = new_coords ++ new_coord
    }
  } else if (dir == 'D') {
    val beg = current(1) - 1
    val end = current(1) - value
    for (y <- beg to end by -1) {
      val new_coord = Array(List(current(0), y))
      new_coords = new_coords ++ new_coord
    }
  } else if (dir == 'L') {
    val beg = current(0) - 1
    val end = current(0) - value
    for (x <- beg to end by -1) {
      val new_coord = Array(List(x, current(1)))
      new_coords = new_coords ++ new_coord
    }
  } else if (dir == 'R') {
    val beg = current(0) + 1
    val end = current(0) + value
    for (x <- beg to end) {
      val new_coord = Array(List(x, current(1)))
      new_coords = new_coords ++ new_coord
    }
  }
  new_coords
}



// Define a function that takes an array of instructions and returns an Array of all coordinates the instructions 'walk through'
def getCoords(instructions: Array[(Char, Int)]) : Array[List[Int]] = {
  var coords = Array(List(0, 0))
  var current_pos = coords(0)
  for (instruc <- instructions) {
    val dir = instruc._1
    val value = instruc._2
    var new_coords = coordsHelper(current_pos, dir, value)
    coords = coords ++ new_coords
    current_pos = coords.last // this needs to be the last thing in coords
  }
  coords
}

def manhattan(coords: List[Int]) : Int = {
  coords.map(math.abs).sum
}

def compare(a1: Array[List[Int]], a2: Array[List[Int]]) : Array[List[Int]] = {
  List(a1, a2).reduce((a, b) => a intersect b)
}

val w1coords = getCoords(wire1)
val w2coords = getCoords(wire2)

val intersection = compare(w1coords, w2coords)

val sorted = intersection.sortWith((c1, c2) => manhattan(c1) < manhattan(c2)) // 38

// Part 2
/*
It turns out that this circuit is very timing-sensitive; you actually need to minimize the signal delay.

To do this, calculate the number of steps each wire takes to reach each intersection; choose the intersection where the sum of both wires' steps is lowest. If a wire visits a position on the grid multiple times, use the steps value from the first time it visits that position when calculating the total value of a specific intersection.

The number of steps a wire takes is the total number of grid squares the wire has entered to get to that location, including the intersection being considered. Again consider the example from above:

...........
.+-----+...
.|.....|...
.|..+--X-+.
.|..|..|.|.
.|.-X--+.|.
.|..|....|.
.|.......|.
.o-------+.
...........
In the above example, the intersection closest to the central port is reached after 8+5+5+2 = 20 steps by the first wire and 7+6+4+3 = 20 steps by the second wire for a total of 20+20 = 40 steps.

However, the top-right intersection is better: the first wire takes only 8+5+2 = 15 and the second wire takes only 7+6+2 = 15, a total of 15+15 = 30 steps.

Here are the best steps for the extra examples from above:

R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83 = 610 steps
R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = 410 steps
What is the fewest combined steps the wires must take to reach an intersection?

*/
val options = sorted.tail // excluding (0, 0)
// go through options and find how many instructions and steps needed to follow to hit it for both w1 and w2

def counter(coords: Array[List[Int]], compare: List[Int]) : Int = {
  var c = 0
  for (coord <- coords) {
    c += 1
    if (coord sameElements compare) {
      return c
    }
  }
  c
}

def minCounter(coords1: Array[List[Int]], coords2: Array[List[Int]], options: Array[List[Int]]) : (List[Int], Int) = {
  var min = 9999999
  var best_option = List(0, 0)
  for (option <- options) {
    val w1cost = counter(coords1.tail, option)
    val w2cost = counter(coords2.tail, option)
    val total_cost = w1cost + w2cost
    if (total_cost < min) {
      min = total_cost
      best_option = option
    }
  }
  (best_option, min)
}

val (best_option, cost) = minCounter(w1coords, w2coords, options)
println(best_option, cost)
