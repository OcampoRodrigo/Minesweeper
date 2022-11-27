import settings

#Function to calculate how much percentage of our height we want to
#use
def height_prct(percentage):
    return (settings.HEIGHT/100) * percentage
def width_prct(percentage):
    return  (settings.WIDTH/100) * percentage