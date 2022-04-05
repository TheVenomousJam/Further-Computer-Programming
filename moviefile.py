import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as manimation
n = 1000
x = np.linspace(0, 6*np.pi, n)
y = np.sin(x)


FFMpegWriter = manimation.writers['ffmpeg']
metadata = dict(title='Movie Test', artist='Matplotlib',
                comment='a red circle following a blue sine wave')
writer = FFMpegWriter(fps=15, metadata=metadata)


fig = plt.figure()


sine_line, = plt.plot(x, y, 'b')
red_circle, = plt.plot([0], [0], 'x', markersize = 30, linewidth = 50)
blue_triangle, = plt.plot([0], [0], '>', markersize = 15)
plt.xlabel('x')
plt.ylabel('sin(x)')


with writer.saving(fig, "writer_test.mp4", 100):
    for i in range(n):
        x0 = x[i]
        y0 = y[i]
        red_circle.set_data(x0, y0)
        blue_triangle.set_data(x0, y0)
        writer.grab_frame()