import scala.io.Source
import scala.collection.mutable.Map
import util.control.Breaks._

object Day10 {

  def parseCoords(asteriods: List[String]) : Map[(Int, Int), Char] = {
    /**
      Returns Map of coords -> element for the input asteriod map.
    **/
    var coords : Map[(Int, Int), Char] = Map()
    for (x <- 0 to asteriods(0).length - 1; y <- 0 to asteriods.length - 1) {
      val elem = asteriods(y)(x)
      coords += ((x, y) -> elem)
    }
    coords.filterInPlace( (coord, elem) => elem == '#') // keeping only coords of asteriods
  }

  def getLine(coord1: (Int, Int), coord2: (Int, Int)) : (Float, Float) = {
    /**
      Returns slope and intercept of the line intersecting two points
    **/
    val slope = (coord2._2 - coord1._2) / (coord2._1 - coord1._1).toFloat
    val intercept = coord1._2 - slope * coord1._1.toFloat
    (slope, intercept)
  }

  def getMagnitude(coord: (Int, Int)) : Double = {
    math.sqrt(math.pow(coord._1, 2) + math.pow(coord._2, 2))
  }

  def getDistanceBetweenTwoCoords(coord1: (Int, Int), coord2: (Int, Int)) : Double = {
    val xComponent = coord1._1 - coord2._1
    val yComponent = coord1._2 - coord2._2

    getMagnitude((xComponent, yComponent))
  }

  def isWithin(start: Int, stop: Int, num: Int) : Boolean = {
    var within = false
    if (start > stop) {
      within = (stop to start).toList.contains(num)
    } else {
      within = (start to stop).toList.contains(num)
    }
    within
  }

  def isBetween(toCheck: (Int, Int), coord1: (Int, Int), coord2: (Int, Int)) : Boolean = {
    var between = false

    if (isWithin(coord1._1, coord2._1, toCheck._1) && isWithin(coord1._2, coord2._2, toCheck._2)) {
      between = true
    }
    between
  }

  def checkObstruction(coord1: (Int, Int), coord2: (Int, Int), checkCoords: List[(Int, Int)]) : Boolean = {
    val (slope, intercept) = getLine(coord1, coord2)
    var obstructed = false
    breakable {
      for (toCheck <- checkCoords) {
        if (getLine(coord1, toCheck) == (slope, intercept) && isBetween(toCheck, coord1, coord2)) {
          println(coord1, " to ", coord2, " is obstructed by ", toCheck)
          obstructed = true
          break
        }
      }
    }
    obstructed
  }

  def countAsteriods(coords: Map[(Int, Int), Char]) : Map[(Int, Int), Int] = {
    val counter = coords.keys.toList.map(coord => (coord, 0)).to(collection.mutable.Map) // hold counts

    // for every OTHER point, check to see if coord1 to otherPoint has the same slope/intercept
    // else at the end of checking all other points, increment the counter for coord1 by 1
    // println(coord1, coord2, slope, intercept)
    for (coord1 <- coords.keys.toList) {
      val otherCoords = coords.keys.toList.filter(coord => coord != coord1)
      for (coord2 <- otherCoords) {
        val checkCoords = otherCoords.filter(coord => coord != coord2)
        val isObstructed = checkObstruction(coord1, coord2, checkCoords)
        if (!isObstructed) {
          counter(coord1) += 1
        }
      }
    }
    counter
  }

  def main(args: Array[String]) : Unit = {
    val inputFile = "day10.in"
    //val inputFile = "test5.in"
    val result = Source.fromFile(inputFile).getLines.toList
    val coords = parseCoords(result)

    val results = countAsteriods(coords)
    println(results.valuesIterator.max)
  }
}
