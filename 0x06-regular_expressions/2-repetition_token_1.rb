#!/usr/bin/env ruby

pattern = Regexp.new(/(\w+)a(\w+)\w+a(\w+)a(\w+)/)

input = ARGV[0]

if pattern.match(input)
  puts input
else
  puts ""
end
