import mph
import pandas as pd
import numpy as np
import os

os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OMP_MAX_ACTIVE_LEVELS"] = "1"

client = mph.start()
pymodel = client.load("D:\\Kagome.mph")
model = pymodel.java


def run_mph_simulation(a1, a2, a3, a4, b1, b2, b3, b4):
    model.param().set("a1", str(a1))
    model.param().set("a2", str(a2))
    model.param().set("a3", str(a3))
    model.param().set("a4", str(a4))
    model.param().set("b1", str(b1))
    model.param().set("b2", str(b2))
    model.param().set("b3", str(b3))
    model.param().set("b4", str(b4))

    model.study("std1").run()

    model.result().table("tbl1").clearTableData()
    model.result().table("tbl2").clearTableData()
    model.result().table("tbl3").clearTableData()
    model.result().table("tbl4").clearTableData()

    model.result().numerical("int1").set("table", "tbl1")
    model.result().numerical("int1").setResult()
    model.result().table("tbl1").save("D:\\DATA-DKR\\彩虹\\RL\\RL-rainbow-corner\\table1.csv")
    model.result().numerical("int2").set("table", "tbl2")
    model.result().numerical("int2").setResult()
    model.result().table("tbl2").save("D:\\DATA-DKR\\彩虹\\RL\\RL-rainbow-corner\\table2.csv")
    model.result().numerical("int3").set("table", "tbl3")
    model.result().numerical("int3").setResult()
    model.result().table("tbl3").save("D:\\DATA-DKR\\彩虹\\RL\\RL-rainbow-corner\\table3.csv")
    model.result().numerical("int4").set("table", "tbl4")
    model.result().numerical("int4").setResult()
    model.result().table("tbl4").save("D:\\DATA-DKR\\彩虹\\RL\\RL-rainbow-corner\\table4.csv")

    file_paths = [
        "D:\\table1.csv",
        "D:\\table2.csv",
        "D:\\table3.csv",
        "D:\\table4.csv"
    ]

    max_values = []
    for path in file_paths:
        data = pd.read_csv(path, header=None)
        values = pd.to_numeric(data.iloc[5:17, 1], errors="coerce")
        max_value = values.max()
        max_values.append(max_value)

 
    average_max = np.mean(max_values)

    model.result().table("tbl1").clearTableData()
    model.result().table("tbl2").clearTableData()
    model.result().table("tbl3").clearTableData()
    model.result().table("tbl4").clearTableData()

    return average_max



