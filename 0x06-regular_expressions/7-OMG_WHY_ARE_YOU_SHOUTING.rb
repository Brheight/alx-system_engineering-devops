#!/usr/bin/env ruby

pattern = Regexp.new(/[A-Z]+/)

input = ARGV[0]

if pattern.match(input)
  puts input
else
  puts ""
end
