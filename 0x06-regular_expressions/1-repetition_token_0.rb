#!/usr/bin/env ruby

pattern = Regexp.new(/^(School)(\1+)?$/)

input = ARGV[0]

if pattern.match(input)
  puts input
else
  puts ""
end
