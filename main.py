while True:
    light.set_brightness(10)
    light.set_pixel_color(0, light.rgb(255,100, 0))
    pause(300)
    light.set_pixel_color(1, light.rgb(255,255,0))
    pause(300)
    light.set_pixel_color(2, light.rgb(0,255,0))
    pause(300)
    light.set_pixel_color(3, light.rgb(0,255,255))
    pause(300)
    light.set_pixel_color(4, light.rgb(0,100,235))
    pause(300)
    light.set_pixel_color(5, light.rgb(0,0,255))
    pause(300)
    light.set_pixel_color(6, light.rgb(0,0,100))
    pause(300)
    light.set_pixel_color(7, light.rgb(100,0,255))
    pause(300)
    light.set_pixel_color(8, light.rgb(200,0,255))
    pause(300)
    light.set_pixel_color(9, light.rgb(255,0,0))
    pause(300)
    pause(1000) #pause for 3 seconds
    light.clear()
    pause(1000) #pause for 2 seconds

   