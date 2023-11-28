#!/usr/bin/env ruby

# Define regular expressions for parsing the log lines
sender_regex = /from:(.+)]/
receiver_regex = /to:(.+)]/
flags_regex = /flags:(.+)]/

# Open the log file for reading
File.open('log.txt', 'r') do |file|
  file.each_line do |line|
    # Initialize variables to handle potential missing values
    sender = nil
    receiver = nil
    flags = nil

    # Extract sender, receiver, and flags using regex
    begin
      sender = line.match(sender_regex)[1]
    rescue NoMethodError
      # Sender information not found
    end

    begin
      receiver = line.match(receiver_regex)[1]
    rescue NoMethodError
      # Receiver information not found
    end

    begin
      flags = line.match(flags_regex)[1]
    rescue NoMethodError
      # Flags information not found
    end

    # Format the extracted information, handling potential missing values
    output = "[#{sender || 'Unknown'},#{receiver || 'Unknown'},#{flags || 'Unknown'}]"

    # Print the formatted information
    puts output
  end
end
