#!/usr/bin/env ruby

pattern = Regexp.new(/^School/)

input = ARGV[0]

if pattern.match(input)
  puts input
else
  puts ""
end
