from software_module import processing_function

# Experimental parameters
DATE = "2012-03-04"
DESCRIPTION = 'description'

# Define a relative path to the data -- don't hardcode a path. 
data_location = '../../data/{}_{}'.format(DATE, DESCRIPTION)
processed_data = processing_function(data_dir)

# Save the processed data to the local output directory. 
processed_data.save('output/{}_{}_processed_experimental_data.csv'.format(DATE, DESCRIPTION))

