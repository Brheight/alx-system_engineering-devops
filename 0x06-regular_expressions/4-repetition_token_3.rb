#!/usr/bin/env ruby

pattern = Regexp.new(/a([^\\s]+)a(\w+)a(\w+)a/)

input = ARGV[0]

if pattern.match(input)
  puts input
else
  puts ""
end
