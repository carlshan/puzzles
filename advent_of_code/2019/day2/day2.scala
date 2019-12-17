import scala.io.Source
import scala.collection.mutable.ListBuffer

val fileName = "day2.in"
val lines = Source.fromFile(fileName).getLines.toList.head.split(",").map(s => s.toInt).to(ListBuffer)

// To get the type, use the .getClass method
// println(lines)

// Part 1
/*
  1 - adds two numbers and places it in the third
  2 - same, except multiplies two numbers
  99 - end the program
*/

def Op1(pos1: Int, pos2: Int, pos3: Int, data: ListBuffer[Int]) : Unit = {
  val sum = data(pos1) + data(pos2)
  data(pos3) = sum
}

def Op2(pos1: Int, pos2: Int, pos3: Int, data: ListBuffer[Int]) : Unit = {
  val product = data(pos1) * data(pos2)
  data(pos3) = product
}

// var test = ListBuffer(1, 0, 0, 0, 99)
// var test2 = ListBuffer(2,4,4,5,99,0)
// var test3 = ListBuffer(1,1,1,4,99,5,6,0,99)
// Op1(0, 0, 0, test)
// println(test)

lines(1) = 12
lines(2) = 2

def compute(data: ListBuffer[Int]) : Unit = {
  var done = false
  var i = 0
  while(!(done)) {
    var pos1 = data(i+1)
    var pos2 = data(i+2)
    var pos3 = data(i+3)
    if (data(i) == 1) {
      Op1(pos1, pos2, pos3, data)
      i += 4
    } else if (data(i) == 2) {
      Op2(pos1, pos2, pos3, data)
      i += 4
    }
    if (data(i) == 99) {
      done = true
    }
  }
}

// compute(lines)
//
// println(lines)

// Part 2

import util.control.Breaks._

def partTwo(data: ListBuffer[Int]) : (Int, Int) = {
  var result = (0, 0)
  breakable {
    for {
      noun <- 0 to 99
      verb <- 0 to 99
    } {
      var clone = data.clone
      clone(1) = noun
      clone(2) = verb
      compute(clone)
      println(noun, verb)
      if (clone(0) == 19690720) {
        result = (noun, verb)
        break
      }
    }
  }

  result
}

println(partTwo(lines))
