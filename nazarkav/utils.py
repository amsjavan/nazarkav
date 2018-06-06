import logging
import os
import signal
import sys
from PyQt4.QtCore import QTimer
from PyQt4.QtGui import QApplication
from nazarkav import webkit2png

# Technically, this is a QtGui application, because QWebPage requires it
# to be. But because we will have no user interaction, and rendering can
# not start before 'app.exec_()' is called, we have to trigger our "main"
# by a timer event.


LOG_FILENAME = 'webkit2png.log'
logger = logging.getLogger('webkit2png')


def init_qtgui(display=None, style=None, qtargs=None):
    """Initiates the QApplication environment using the given args."""
    if QApplication.instance():
        logger.debug("QApplication has already been instantiated. \
                        Ignoring given arguments and returning existing QApplication.")
        return QApplication.instance()

    qtargs2 = [sys.argv[0]]
    return QApplication(qtargs2)


def __main_qt(width, height):
    # Render the page.
    # If this method times out or loading failed, a
    # RuntimeException is thrown
    try:
        # Initialize WebkitRenderer object
        renderer = webkit2png.WebkitRenderer()
        renderer.logger = logger
        renderer.width = width
        renderer.height = height
        out = open('table.png', 'bw')
        renderer.render_to_file(res='table.html', file_object=out)
        out.close()
        QApplication.exit(0)
    except RuntimeError as e:
        logger.error("main: %s" % e)
        print(sys.stderr, e)
        QApplication.exit(1)

# Initialize Qt-Application
# If we execute this in the dataframe2png,
# we will get error in executing more than once in ipython notebook
app = init_qtgui()

def dataframe2png(df, width=0, height=0):
    style = """
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8" />
    <style>
    table, td, th {
        border: 1px solid black;
        text-align: center;
    }
    table {
        border-collapse: collapse;
        width: 100%;
    }
    th {
        font-family: Nazanin, Tahoma;
        background-color: #f2f2f2;
    }
    </style>
    </head>
    """

    with open('table.html', 'w', encoding='utf8') as file:
        file.write(style + df.to_html())

    global app
    QTimer.singleShot(0, lambda: __main_qt(width, height))
    app.exec_()
    from PIL import Image
    img = Image.open('table.png')
    #os.remove('table.html')
    return img

