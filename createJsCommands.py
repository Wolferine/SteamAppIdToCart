idText = ""
with open('out.txt', 'r') as f:
    inTxt = f.readlines()

    
counter = 0
preText = 'var listToAdd = ['
afterText = '];listToAdd.forEach(id => {document.getElementsByClassName("gameDlcBlocks")[0].insertAdjacentHTML("afterend","<a> <input type=\\\"hidden\\\" name=\\\"subid[]\\\" value=\"+id+\"> </a>\");}); addAllDlcToCart();'

with open('jsCommands.txt', 'w') as f:
    for line in inTxt:
        idText += line.strip()
        counter += 1
        if counter % 90 == 0:
            out = preText + idText + afterText
            out += "\n"
            out += "\n"
            f.write(out)
            f.flush()
            idText = ""
        
    out = preText + idText + afterText
    f.write(out)
    f.flush()

print("done")
input("Press Enter to continue...")



