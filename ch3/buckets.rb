require 'csv'

# Tableau Speak - Measures
grades = [83,95,91,87,70,0,85,82,100,67,73,77,0]

# Tableau Speak - Dimensions
histogram = Hash.new
decile = ->(grade) { (grade / 10 * 10).floor }
grades.each do |grade|
  histogram[decile.call(grade)] = grade
end

CSV.open("buckets.csv", "wb") do |csv|
  i = 0
  csv << %w( row_id grade )
  grades.each do |grade|
    csv << [i+1, grade]
    i += 1
  end
end
