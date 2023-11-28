#!/usr/bin/env ruby

pattern = Regexp.new(/^\d{10}$/)

input = ARGV[0]

if pattern.match(input)
  puts input
else
  puts ""
end
