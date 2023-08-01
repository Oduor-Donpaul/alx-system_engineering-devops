#!/usr/bin/env ruby

def match_school(exp)
  regex = /School/

  matches = exp.scan(regex)

  matches.join

end

exp = ARGV[0]

if exp.nil?
  puts "Usage: #{PROGRAM_NAME} <exp>"
  exit 1
end


result = match_school(exp)

puts result
