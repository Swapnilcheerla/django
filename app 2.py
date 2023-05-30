import matplotlib.pyplot as plt
import numpy as np
import os
from datetime import datetime


@app.route('/')
def index():
    return render_template("index.html")
