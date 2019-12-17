def coordsHelper(current: (Int, Int), dir: Char, value: Int) : Array[Array[Int]] = {
  var new_coords = Array(Array(current._1, current._2))
  if (dir == 'U') {
    // add all the tuples between current_pos._2 to current_pos._2 + val to coords
    val beg = current._2 + 1
    val end = current._2 + value
    for (y <- beg to end) {
      val new_coord = Array(Array(current._1, y))
      new_coords = new_coords ++ new_coord
    }
  } else if (dir == 'D') {
    val beg = current._2 - 1
    val end = current._2 - value
    for (y <- beg to end) {
      val new_coord = Array(Array(current._1, y))
      new_coords = new_coords ++ new_coord
    }
  } else if (dir == 'L') {
    val beg = current._1 - 1
    val end = current._1 - value
    for (x <- beg to end) {
      val new_coord = Array(Array(x, current._2))
      new_coords = new_coords ++ new_coord
    }
  } else if (dir == 'R') {
    val beg = current._1 + 1
    val end = current._1 + value
    for (x <- beg to end) {
      val new_coord = Array(Array(x, current._2))
      new_coords = new_coords ++ new_coord
    }
  }
  new_coords
}

var current = (0, 0)
var dir = 'U'
val value = 5

coordsHelper(current, dir, value).foreach(elem => println(elem(1)))
