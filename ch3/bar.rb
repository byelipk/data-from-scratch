require 'csv'

# Tableau Speak - Dimensions
movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]

# Tableau Speak - Measures
num_oscars = [5, 11, 3, 8, 10]

CSV.open("bar.csv", "wb") do |csv|
  csv << %w( row_id movie num_oscars)

  i = 0
  movies.each do |y|
    csv << [i+1, y, num_oscars[i]]
    i += 1
  end
end
