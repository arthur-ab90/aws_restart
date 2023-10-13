{"filter":false,"title":"debug-caesar-2.py","tooltip":"/debug-caesar-2.py","undoManager":{"mark":14,"position":14,"stack":[[{"start":{"row":2,"column":3},"end":{"row":3,"column":0},"action":"remove","lines":["",""],"id":1},{"start":{"row":2,"column":2},"end":{"row":2,"column":3},"action":"remove","lines":["\""]},{"start":{"row":2,"column":1},"end":{"row":2,"column":2},"action":"remove","lines":["\""]},{"start":{"row":2,"column":0},"end":{"row":2,"column":1},"action":"remove","lines":["\""]},{"start":{"row":1,"column":23},"end":{"row":2,"column":0},"action":"remove","lines":["",""]},{"start":{"row":1,"column":22},"end":{"row":1,"column":23},"action":"remove","lines":["n"]},{"start":{"row":1,"column":21},"end":{"row":1,"column":22},"action":"remove","lines":["o"]},{"start":{"row":1,"column":20},"end":{"row":1,"column":21},"action":"remove","lines":["i"]},{"start":{"row":1,"column":19},"end":{"row":1,"column":20},"action":"remove","lines":["t"]},{"start":{"row":1,"column":18},"end":{"row":1,"column":19},"action":"remove","lines":["p"]},{"start":{"row":1,"column":17},"end":{"row":1,"column":18},"action":"remove","lines":["i"]},{"start":{"row":1,"column":16},"end":{"row":1,"column":17},"action":"remove","lines":["r"]},{"start":{"row":1,"column":15},"end":{"row":1,"column":16},"action":"remove","lines":["c"]},{"start":{"row":1,"column":14},"end":{"row":1,"column":15},"action":"remove","lines":["s"]},{"start":{"row":1,"column":13},"end":{"row":1,"column":14},"action":"remove","lines":["e"]},{"start":{"row":1,"column":12},"end":{"row":1,"column":13},"action":"remove","lines":["d"]},{"start":{"row":1,"column":11},"end":{"row":1,"column":12},"action":"remove","lines":[" "]},{"start":{"row":1,"column":10},"end":{"row":1,"column":11},"action":"remove","lines":["e"]},{"start":{"row":1,"column":9},"end":{"row":1,"column":10},"action":"remove","lines":["l"]},{"start":{"row":1,"column":8},"end":{"row":1,"column":9},"action":"remove","lines":["u"]},{"start":{"row":1,"column":7},"end":{"row":1,"column":8},"action":"remove","lines":["d"]},{"start":{"row":1,"column":6},"end":{"row":1,"column":7},"action":"remove","lines":["o"]},{"start":{"row":1,"column":5},"end":{"row":1,"column":6},"action":"remove","lines":["m"]},{"start":{"row":1,"column":4},"end":{"row":1,"column":5},"action":"remove","lines":[" "]},{"start":{"row":1,"column":3},"end":{"row":1,"column":4},"action":"remove","lines":["r"]},{"start":{"row":1,"column":2},"end":{"row":1,"column":3},"action":"remove","lines":["u"]},{"start":{"row":1,"column":1},"end":{"row":1,"column":2},"action":"remove","lines":["o"]},{"start":{"row":1,"column":0},"end":{"row":1,"column":1},"action":"remove","lines":["Y"]},{"start":{"row":0,"column":3},"end":{"row":1,"column":0},"action":"remove","lines":["",""]},{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"remove","lines":["\""]},{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"remove","lines":["\""]},{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"remove","lines":["\""]},{"start":{"row":0,"column":0},"end":{"row":55,"column":21},"action":"insert","lines":["# Module Lab: Caesar Cipher Program Bug #2","#","# In a previous lab, you created a Caesar cipher program. This version of","# the program is buggy. Use a debugger to find the bug and fix it.","","# Double the given alphabet","def getDoubleAlphabet(alphabet):","    doubleAlphabet = alphabet + alphabet","    return doubleAlphabet","","# Get a message to encrypt","def getMessage():","    stringToEncrypt = input(\"Please enter a message to encrypt: \")","    return stringToEncrypt","","# Get a cipher key","def getCipherKey():","    shiftAmount = input(\"Please enter a key (whole number from 1-25): \")","    return shiftAmount","","# Encrypt message","def encryptMessage(message, cipherKey, alphabet):","    encryptedMessage = \"\"","    uppercaseMessage = \"\"","    uppercaseMessage = message","    for currentCharacter in uppercaseMessage:","        position = alphabet.find(currentCharacter)","        newPosition = position + int(cipherKey)","        if currentCharacter in alphabet:","            encryptedMessage = encryptedMessage + alphabet[newPosition]","        else:","            encryptedMessage = encryptedMessage + currentCharacter","    return encryptedMessage","","# Decrypt message","def decryptMessage(message, cipherKey, alphabet):","    decryptKey = -1 * int(cipherKey)","    return encryptMessage(message, decryptKey, alphabet)","","# Main program logic","def runCaesarCipherProgram():","    myAlphabet=\"ABCDEFGHIJKLMNOPQRSTUVWXYZ\"","    print(f'Alphabet: {myAlphabet}')","    myAlphabet2 = getDoubleAlphabet(myAlphabet)","    print(f'Alphabet2: {myAlphabet2}')","    myMessage = getMessage()","    print(myMessage)","    myCipherKey = getCipherKey()","    print(myCipherKey)","    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)","    print(f'Encrypted Message: {myEncryptedMessage}')","    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)","    print(f'Decrypted Message: {myDecryptedMessage}')","","# Main logic","runCaesarCipherProgra"]}],[{"start":{"row":55,"column":21},"end":{"row":55,"column":22},"action":"insert","lines":["M"],"id":2}],[{"start":{"row":55,"column":21},"end":{"row":55,"column":22},"action":"remove","lines":["M"],"id":3}],[{"start":{"row":55,"column":21},"end":{"row":55,"column":22},"action":"insert","lines":["M"],"id":4}],[{"start":{"row":55,"column":22},"end":{"row":55,"column":24},"action":"insert","lines":["()"],"id":5}],[{"start":{"row":55,"column":21},"end":{"row":55,"column":22},"action":"remove","lines":["M"],"id":6}],[{"start":{"row":55,"column":21},"end":{"row":55,"column":22},"action":"insert","lines":["m"],"id":7}],[{"start":{"row":24,"column":30},"end":{"row":24,"column":31},"action":"insert","lines":["."],"id":8},{"start":{"row":24,"column":31},"end":{"row":24,"column":32},"action":"insert","lines":["u"]},{"start":{"row":24,"column":32},"end":{"row":24,"column":33},"action":"insert","lines":["p"]},{"start":{"row":24,"column":33},"end":{"row":24,"column":34},"action":"insert","lines":["p"]},{"start":{"row":24,"column":34},"end":{"row":24,"column":35},"action":"insert","lines":["e"]},{"start":{"row":24,"column":35},"end":{"row":24,"column":36},"action":"insert","lines":["r"]}],[{"start":{"row":24,"column":36},"end":{"row":24,"column":38},"action":"insert","lines":["()"],"id":9}],[{"start":{"row":24,"column":37},"end":{"row":24,"column":38},"action":"remove","lines":[")"],"id":10},{"start":{"row":24,"column":36},"end":{"row":24,"column":37},"action":"remove","lines":["("]},{"start":{"row":24,"column":35},"end":{"row":24,"column":36},"action":"remove","lines":["r"]},{"start":{"row":24,"column":34},"end":{"row":24,"column":35},"action":"remove","lines":["e"]},{"start":{"row":24,"column":33},"end":{"row":24,"column":34},"action":"remove","lines":["p"]},{"start":{"row":24,"column":32},"end":{"row":24,"column":33},"action":"remove","lines":["p"]},{"start":{"row":24,"column":31},"end":{"row":24,"column":32},"action":"remove","lines":["u"]},{"start":{"row":24,"column":30},"end":{"row":24,"column":31},"action":"remove","lines":["."]}],[{"start":{"row":24,"column":30},"end":{"row":24,"column":31},"action":"insert","lines":["."],"id":11},{"start":{"row":24,"column":31},"end":{"row":24,"column":32},"action":"insert","lines":["u"]},{"start":{"row":24,"column":32},"end":{"row":24,"column":33},"action":"insert","lines":["p"]},{"start":{"row":24,"column":33},"end":{"row":24,"column":34},"action":"insert","lines":["p"]},{"start":{"row":24,"column":34},"end":{"row":24,"column":35},"action":"insert","lines":["e"]},{"start":{"row":24,"column":35},"end":{"row":24,"column":36},"action":"insert","lines":["r"]}],[{"start":{"row":24,"column":36},"end":{"row":24,"column":38},"action":"insert","lines":["()"],"id":12}],[{"start":{"row":24,"column":37},"end":{"row":24,"column":38},"action":"remove","lines":[")"],"id":13},{"start":{"row":24,"column":36},"end":{"row":24,"column":37},"action":"remove","lines":["("]},{"start":{"row":24,"column":35},"end":{"row":24,"column":36},"action":"remove","lines":["r"]},{"start":{"row":24,"column":34},"end":{"row":24,"column":35},"action":"remove","lines":["e"]},{"start":{"row":24,"column":33},"end":{"row":24,"column":34},"action":"remove","lines":["p"]},{"start":{"row":24,"column":32},"end":{"row":24,"column":33},"action":"remove","lines":["p"]},{"start":{"row":24,"column":31},"end":{"row":24,"column":32},"action":"remove","lines":["u"]},{"start":{"row":24,"column":30},"end":{"row":24,"column":31},"action":"remove","lines":["."]}],[{"start":{"row":24,"column":30},"end":{"row":24,"column":31},"action":"insert","lines":["."],"id":14},{"start":{"row":24,"column":31},"end":{"row":24,"column":32},"action":"insert","lines":["u"]},{"start":{"row":24,"column":32},"end":{"row":24,"column":33},"action":"insert","lines":["p"]},{"start":{"row":24,"column":33},"end":{"row":24,"column":34},"action":"insert","lines":["p"]},{"start":{"row":24,"column":34},"end":{"row":24,"column":35},"action":"insert","lines":["e"]},{"start":{"row":24,"column":35},"end":{"row":24,"column":36},"action":"insert","lines":["r"]}],[{"start":{"row":24,"column":36},"end":{"row":24,"column":38},"action":"insert","lines":["()"],"id":15}]]},"ace":{"folds":[],"scrolltop":125.1572265625,"scrollleft":0,"selection":{"start":{"row":55,"column":0},"end":{"row":55,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":29,"state":"start","mode":"ace/mode/python"}},"hash":"3b622ebf84dc30c529848160f341d00b5b2b4686"}