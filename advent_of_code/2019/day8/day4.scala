/*
For example, given an image 3 pixels wide and 2 pixels tall, the image data
123456789012 corresponds to the following image layers:

Layer 1: 123
         456

Layer 2: 789
         012
The image you received is 25 pixels wide and 6 pixels tall.

To make sure the image wasn't corrupted during transmission, the Elves would
like you to find the layer that contains the fewest 0 digits. On that layer,
what is the number of 1 digits multiplied by the number of 2 digits?

*/

import scala.io.Source

val fileName = "day4.in"
val data = Source.fromFile(fileName).getLines.toList.head.toList

// Part 1
val grouped = data.grouped(25 * 6)
val answer = grouped.minBy(elem => elem.count(_ == '0'))

println(answer.count(_ == '1') * answer.count(_ == '2'))

// Part 2
/*
--- Part Two ---
Now you're ready to decode the image. The image is rendered by stacking the
layers and aligning the pixels with the same positions in each layer.
The digits indicate the color of the corresponding pixel:

0 is black, 1 is white, and 2 is transparent.

The layers are rendered with the first layer in front and the last layer in back.
So, if a given position has a transparent pixel in the first and second layers,
a black pixel in the third layer, and a white pixel in the fourth layer, the
final image would have a black pixel at that position.

For example, given an image 2 pixels wide and 2 pixels tall, the image data
0222112222120000 corresponds to the following image layers:

Layer 1: 02
         22

Layer 2: 11
         22

Layer 3: 22
         12

Layer 4: 00
         00
Then, the full image can be found by determining the top visible pixel in each position:

The top-left pixel is black because the top layer is 0.
The top-right pixel is white because the top layer is 2 (transparent), but the second layer is 1.
The bottom-left pixel is white because the top two layers are 2, but the third layer is 1.
The bottom-right pixel is black because the only visible pixel in that position is 0 (from layer 4).
So, the final image looks like this:

01
10
What message is produced after decoding your image?
*/

import scala.collection.mutable.ListBuffer

// We're going to create a final array of 0s and 1s
// To create each element in this final array, we will scan through
// each of the grouped elements until we find the first one that's not a 2 and
// we will put that in the final array and move on.

val message = new ListBuffer[Char]()

for (i <- 0 to 149) {
  message += grouped.find(group => group(i) != '2').get(i)
}

// Now we have to print it 25x6
for (result <- message.grouped(25)) {
  println(result.mkString(" ").replace('1', '#'))
}
/*
0 # # 0 0 0 # # 0 0 # 0 0 # 0 # # # 0 0 # # # # 0
# 0 0 # 0 # 0 0 # 0 # 0 # 0 0 # 0 0 # 0 0 0 0 # 0
# 0 0 # 0 # 0 0 0 0 # # 0 0 0 # 0 0 # 0 0 0 # 0 0
# # # # 0 # 0 0 0 0 # 0 # 0 0 # # # 0 0 0 # 0 0 0
# 0 0 # 0 # 0 0 # 0 # 0 # 0 0 # 0 0 0 0 # 0 0 0 0
# 0 0 # 0 0 # # 0 0 # 0 0 # 0 # 0 0 0 0 # # # # 0
*/
