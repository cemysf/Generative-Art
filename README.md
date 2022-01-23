# Generative-Art
Create generative art in Python!

See dependencies in requirements.txt (tested with python3.9)

To run this program, execute the main file from the command line using <code>python main.py</code>.

Included in this repo are a handful of utilities and example functions to generate a couple styles of Perlin-Noise based art drawn with PyQt.QPainter. Uncomment whatever drawing you'd like to make from the <code>main.py</code> file to generate output images!

## Run GUI
- Implement a new experiment class in `gui_experiments`
- Set `FUNCTION_IN_USE` to desired class
- Run `python gui.py`
- Mouse-click to create a new image

## TODO:
- Make saving image optional
- Add right click save on gui
- Possible performance optimizations
- Add linter to project