import os, sys
sys.path.append(os.path.dirname(__file__))

from pathfinder import app


if __name__ == '__main__':
    app.run(debug=True)
