{"filter":false,"title":"calc_weight_json.py","tooltip":"/calc_weight_json.py","ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":23,"column":126},"end":{"row":23,"column":126},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"hash":"1b89fe11b889e932558e36d298198bf1a04d0665","undoManager":{"mark":37,"position":37,"stack":[[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":["i"],"id":2},{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"insert","lines":["m"]},{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"insert","lines":["p"]},{"start":{"row":0,"column":3},"end":{"row":0,"column":4},"action":"insert","lines":["o"]},{"start":{"row":0,"column":4},"end":{"row":0,"column":5},"action":"insert","lines":["r"]},{"start":{"row":0,"column":5},"end":{"row":0,"column":6},"action":"insert","lines":["t"]}],[{"start":{"row":0,"column":6},"end":{"row":0,"column":7},"action":"insert","lines":[" "],"id":3},{"start":{"row":0,"column":7},"end":{"row":0,"column":8},"action":"insert","lines":["j"]},{"start":{"row":0,"column":8},"end":{"row":0,"column":9},"action":"insert","lines":["s"]},{"start":{"row":0,"column":9},"end":{"row":0,"column":10},"action":"insert","lines":["o"]}],[{"start":{"row":0,"column":10},"end":{"row":0,"column":11},"action":"insert","lines":["n"],"id":4},{"start":{"row":0,"column":11},"end":{"row":0,"column":12},"action":"insert","lines":["F"]},{"start":{"row":0,"column":12},"end":{"row":0,"column":13},"action":"insert","lines":["i"]},{"start":{"row":0,"column":13},"end":{"row":0,"column":14},"action":"insert","lines":["l"]},{"start":{"row":0,"column":14},"end":{"row":0,"column":15},"action":"insert","lines":["e"]}],[{"start":{"row":0,"column":15},"end":{"row":0,"column":16},"action":"insert","lines":["H"],"id":5},{"start":{"row":0,"column":16},"end":{"row":0,"column":17},"action":"insert","lines":["n"]},{"start":{"row":0,"column":17},"end":{"row":0,"column":18},"action":"insert","lines":["a"]},{"start":{"row":0,"column":18},"end":{"row":0,"column":19},"action":"insert","lines":["d"]},{"start":{"row":0,"column":19},"end":{"row":0,"column":20},"action":"insert","lines":["l"]}],[{"start":{"row":0,"column":19},"end":{"row":0,"column":20},"action":"remove","lines":["l"],"id":6},{"start":{"row":0,"column":18},"end":{"row":0,"column":19},"action":"remove","lines":["d"]},{"start":{"row":0,"column":17},"end":{"row":0,"column":18},"action":"remove","lines":["a"]},{"start":{"row":0,"column":16},"end":{"row":0,"column":17},"action":"remove","lines":["n"]}],[{"start":{"row":0,"column":16},"end":{"row":0,"column":17},"action":"insert","lines":["a"],"id":7},{"start":{"row":0,"column":17},"end":{"row":0,"column":18},"action":"insert","lines":["n"]},{"start":{"row":0,"column":18},"end":{"row":0,"column":19},"action":"insert","lines":["d"]},{"start":{"row":0,"column":19},"end":{"row":0,"column":20},"action":"insert","lines":["l"]},{"start":{"row":0,"column":20},"end":{"row":0,"column":21},"action":"insert","lines":["e"]},{"start":{"row":0,"column":21},"end":{"row":0,"column":22},"action":"insert","lines":["e"]},{"start":{"row":0,"column":22},"end":{"row":0,"column":23},"action":"insert","lines":["r"]}],[{"start":{"row":0,"column":22},"end":{"row":0,"column":23},"action":"remove","lines":["r"],"id":8},{"start":{"row":0,"column":21},"end":{"row":0,"column":22},"action":"remove","lines":["e"]}],[{"start":{"row":0,"column":21},"end":{"row":0,"column":22},"action":"insert","lines":["r"],"id":9}],[{"start":{"row":0,"column":22},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":10},{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":57},"action":"insert","lines":["data = jsonFileHandler.readJsonFile('files/insulin.json')"],"id":11}],[{"start":{"row":2,"column":57},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":12},{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"insert","lines":["",""]},{"start":{"row":4,"column":0},"end":{"row":5,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":5,"column":0},"end":{"row":14,"column":35},"action":"insert","lines":["if data != \"\" :","    bInsulin = data['molecules']['bInsulin']","    aInsulin = data['molecules']['aInsulin']","    insulin = bInsulin + aInsulin","    molecularWeightInsulinActual = data['molecularWeightInsulinActual']","    print('bInsulin: ' + bInsulin)","    print('aInsulin: ' + aInsulin)","    print('molecularWeightInsulinActual: ' + str(molecularWeightInsulinActual))","else:","    print(\"Error. Exiting program\")"],"id":13}],[{"start":{"row":12,"column":79},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":14},{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"remove","lines":["    "],"id":16},{"start":{"row":12,"column":79},"end":{"row":13,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":12,"column":79},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":18},{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"insert","lines":["    "]},{"start":{"row":13,"column":4},"end":{"row":14,"column":0},"action":"insert","lines":["",""]},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "]},{"start":{"row":14,"column":4},"end":{"row":15,"column":0},"action":"insert","lines":["",""]},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":13,"column":4},"end":{"row":14,"column":4},"action":"remove","lines":["","    "],"id":19}],[{"start":{"row":13,"column":4},"end":{"row":23,"column":122},"action":"insert","lines":["# Calculating the molecular weight of insulin  ","# Getting a list of the amino acid (AA) weights  ","aaWeights = data['weights']","# Count the number of each amino acids  ","aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A','C','D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T','V', 'W', 'Y']})  ","# Multiply the count by the weights  ","molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in","['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T', 'V', 'W', 'Y']}.values())  ","print(\"The rough molecular weight of insulin: \" +","str(molecularWeightInsulin))","print(\"Percent error: \" + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))"],"id":20}],[{"start":{"row":13,"column":51},"end":{"row":14,"column":0},"action":"remove","lines":["",""],"id":21}],[{"start":{"row":13,"column":51},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":22},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":14,"column":53},"end":{"row":15,"column":0},"action":"remove","lines":["",""],"id":23}],[{"start":{"row":14,"column":53},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":24},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":15,"column":31},"end":{"row":16,"column":0},"action":"remove","lines":["",""],"id":25}],[{"start":{"row":15,"column":31},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":26},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":16,"column":44},"end":{"row":17,"column":0},"action":"remove","lines":["",""],"id":27}],[{"start":{"row":16,"column":44},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":28},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":17,"column":167},"end":{"row":18,"column":0},"action":"remove","lines":["",""],"id":29}],[{"start":{"row":17,"column":167},"end":{"row":18,"column":0},"action":"insert","lines":["",""],"id":30},{"start":{"row":18,"column":0},"end":{"row":18,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":18,"column":41},"end":{"row":19,"column":0},"action":"remove","lines":["",""],"id":31}],[{"start":{"row":18,"column":41},"end":{"row":19,"column":0},"action":"insert","lines":["",""],"id":32},{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":19,"column":78},"end":{"row":20,"column":0},"action":"remove","lines":["",""],"id":33}],[{"start":{"row":19,"column":78},"end":{"row":20,"column":0},"action":"insert","lines":["",""],"id":34},{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":20,"column":116},"end":{"row":21,"column":0},"action":"remove","lines":["",""],"id":35}],[{"start":{"row":20,"column":116},"end":{"row":21,"column":0},"action":"insert","lines":["",""],"id":36},{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":21,"column":53},"end":{"row":22,"column":0},"action":"remove","lines":["",""],"id":37}],[{"start":{"row":21,"column":53},"end":{"row":22,"column":0},"action":"insert","lines":["",""],"id":38},{"start":{"row":22,"column":0},"end":{"row":22,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":22,"column":32},"end":{"row":23,"column":0},"action":"remove","lines":["",""],"id":39}],[{"start":{"row":22,"column":32},"end":{"row":23,"column":0},"action":"insert","lines":["",""],"id":40},{"start":{"row":23,"column":0},"end":{"row":23,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":24,"column":0},"end":{"row":24,"column":4},"action":"remove","lines":["    "],"id":41},{"start":{"row":23,"column":126},"end":{"row":24,"column":0},"action":"remove","lines":["",""]}]]},"timestamp":1696908224614}