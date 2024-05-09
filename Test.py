def pig_it(text):
    words = text.split()
    res = ""
    for word in words:
        res += word[1:]
        res += word[0]
        if word [-1] in ["A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h","I","i","J","j","K","k","L","l","M","m","N","n","O","o","P","p","Q","q","R","r","S","s","T","t","U","u","V","v","W","w","X","x","Y","y","Z","z"]:
            res += "ay"
        res += " "
    res = res[:-1]
    return res
print (pig_it("Pig latin is cool for arfasfas asdas ... asdawd ?? AWADA! ! ! ! asfdasdasdawf safg Afaf shg dsafafrd ghgj  q23t5  1q qe3t3q1t "))