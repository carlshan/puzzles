import scala.io.Source

val fileName = "day1.in"
val lines = Source.fromFile(fileName).getLines.toList.map(s => s.toInt)

// Part 1

def getFuel(mass: Int) : Int = {
  (mass / 3.0).floor.toInt - 2
}
println(lines.map(getFuel).sum)

// Part 2
def getFuel(mass: Int, acc: Int) : Int = {
  val result = (mass / 3.0).floor.toInt - 2
  if ((result / 3.0).floor.toInt < 2) {
    result + acc
  } else (
    getFuel(result, result + acc)
  )
}

def wrapper(mass: Int) : Int = {
  getFuel(mass, 0)
}

println(lines.map(wrapper).sum)
