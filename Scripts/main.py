"""

"""
import os
import shutil
import json
from flask import Blueprint
import random

from flask import request
from werkzeug.utils import secure_filename

import os
from flask import request, render_template, jsonify
from Scripts.Utility import utils
from Scripts.Services.Calculation import calc


exception_message = '{"status":False, "status":"Server error, please contact your administrator"}'
method_error_message = '{"status": False, "message": "Method not supported!"}'

preqin_main = Blueprint("preqin_main", __name__)


@preqin_main.route("/", methods=["GET", "POST"])
def random_calculation():
    if request.method == "GET":
        try:

            random_float_list = []
            # Set a length of the list to 10
            for i in range(0, 500):
                # any random float between 50.50 to 500.50
                # don't use round() if you need number as it is
                x = round(random.uniform(50.50, 500.50), 2)
                random_float_list.append(x)

            print(random_float_list)

            return {
                "data": json.dumps(random_float_list)
            }

        except Exception as e:
            utils.logger.exception("__Error__" + str(e))


@preqin_main.route("/calculate", methods=["GET", "POST"])
def algebraic_calculator():
    if request.method == "POST":
        try:
            data = request.get_json()
            calc_obj = calc.AlgebraicCalculation()
            x, y = float(data['x']), float(data['y'])

            res = {}

            match data['operation'].lower():
                case "add":
                    res['val'] = calc_obj.add(x, y)
                case "subtract":
                    res['val'] = calc_obj.subtract(x, y)
                case "multiply":
                    res['val'] = calc_obj.multiply(x, y)
                case "divide":
                    res['val'] = calc_obj.divide(x, y)
                case _:
                    res["message"] = "Operation Not Matched"
                    res["val"] = None
                    print(res['message'])

            return {
                "data": json.dumps(res['val'])
            }

        except Exception as e:
            utils.logger.exception("__Error__" + str(e))