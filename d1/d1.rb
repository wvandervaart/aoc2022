#!/usr/bin/env ruby

sums = []
sum = 0
File.read('./input').lines do |lines|
  if lines != "\n"
    sum += lines.to_i
  else
    sums.push(sum)
    sum = 0
  end
end
sums = sums.sort_by { |int| -int}
puts "Part1: " + sums[0].to_s
puts "Part2: " + (sums[0] + sums[1] + sums[2]).to_s