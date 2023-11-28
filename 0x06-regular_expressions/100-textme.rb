#!/usr/bin/env ruby

# Define regular expressions for parsing the log lines
sender_regex = /from:(.+)]/
receiver_regex = /to:(.+)]/
flags_regex = /flags:(.+)]/

# Open the log file for reading
File.open('log.txt', 'r') do |file|
  file.each_line do |line|
    # Extract sender, receiver, and flags using regex
    sender = line.match(sender_regex)[1]
    receiver = line.match(receiver_regex)[1]
    flags = line.match(flags_regex)[1]

    # Format the extracted information
    output = "[#{sender}],[#{receiver}],[#{flags}]"

    # Print the formatted information
    puts output
  end
end
