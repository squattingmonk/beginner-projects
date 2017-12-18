# 99_bottles.rb: prnts the lyrics to "99 Bottles of Beer on the Wall".
# This project is from https://www.redd.it/19kxre.

def bottles(num)
  if num == 1
    '1 bottle'
  else
    num.to_s + ' bottles'
  end
end

99.downto(1) do |num|
  puts bottles(num) + ' of beer on the wall'
  puts bottles(num) + ' of beer'
  puts 'Take one down'
  puts 'Pass it around'
  puts bottles(num - 1) + ' of beer on the wall!'
  puts unless num == 1
end
