require 'csv'

# Tableau Speak - Dimensions
years = [ 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020 ]

# Tableau Speak - Measures
gdp = [ 300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3, 12983.3 ]

CSV.open("plot.csv", "wb") do |csv|
  csv << %w( row_id year gdp )

  i = 0
  years.each do |y|
    csv << [i+1, Date.new(y).to_s, gdp[i]]
    i += 1
  end
end
