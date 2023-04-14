import string
from collections import Counter


def frequency_counter():
    print("letter freq from given text:")
    with open('encrypted.txt', 'r') as f:
        raw = Counter(f.read())
        print(raw)


def decrypt(text, key):
    print(text.translate(str.maketrans(key, string.ascii_lowercase)))


def main():
    Input = input("Input the text u want to count freq: ")
    frequency_counter()
    print("letter freq from english: ")
    print("ETAOINSRHDLUCMFYWGPBVKXQJZ")
    print("First guess: ")
    print("by freq: cnsdzovjufylqrgkxthiewbpma")
    print("by order: siqfcgtuzmwyrdhpjvnlexbka")
    print("FIRST decode: ")
    key = "siqfcgtuzmwyrodhpjvnlexbka"
    decrypt(Input, key)
    """
    o wad wtalonb inry dsiled anh a rinb drttkth e dsole. o sah my moula licv dsitd in my gtte, anh my csarv 
    fab hanbronb ae my facv, fue ni salntdd, anh nie tktn a donbrt calafontl. on int picvte o pue a gtw crog 
    voh xfald, my gakiloet mureo poecs dnacv, anh o gorrth a cirrapdofrt gradv woes afiue a esolh ig a roetl 
    ig waetl. o pue esae on my iestl picvte, esiubs oe purrth my dsiled hiwn a roeert. fue o vntw oe wiurh eavt 
    mt a gtw siuld ei cromf est liuet, anh o hoh nie wane ei ft palcsth fy est eomt o ltacsth est salh poecstd up 
    sobs. a pacv wad iue ig est qutdeoin, palery ftcaudt ig arr est csomntyd on est mohhrt ig est liuet, fue maonry 
    ftcaudt est cromfonb wad salh tniubs esae o hoh nie wane any tjela wtobse in my fihy.
    """
    print("second guess: ")
    print("by freq: cnszdofjuvylqrgkxthiewbpma")
    print("by order: siqvcgtudmwyrozhpjfnlexbka")
    print("Second decode: ")
    key = "siqvcgtudmwyrozhpjfnlexbka"
    decrypt(Input, key)
    """
    i was wtalinb onry sdoles anh a ronb srttkth e sdile. i dah my miula locv sdots on my gtte, anh my cdarv fab 
    hanbrinb ae my facv, fue no dalntss, anh noe tktn a sinbrt calafintl. in ont pocvte i pue a gtw crig vih xfals, 
    my gakoliet murei piecd snacv, anh i girrth a corrapsifrt grasv wied afoue a edilh og a rietl og waetl. i pue 
    edae in my oedtl pocvte, edoubd ie purrth my sdoles hown a rieert. fue i vntw ie wourh eavt mt a gtw douls eo 
    crimf edt louet, anh i hih noe wane eo ft palcdth fy edt eimt i ltacdth edt dalh piecdts up dibd. a pacv was oue 
    og edt qutseion, palery ftcaust og arr edt cdimntys in edt mihhrt og edt louet, fue mainry ftcaust edt crimfinb 
    was dalh tnoubd edae i hih noe wane any tjela wtibde on my fohy.
    """
    print("third guess: ")
    print("by freq: ncszdofjuvylqrgkxthiewbpma")
    print("by order: siqvngtudmwyrozhpjfclexbka")
    print("third decode: ")
    key = "siqvngtudmwyrozhpjfclexbka"
    decrypt(Input, key)
    """
    i was wealinb onry sdolts anh a ronb sreekeh t sdilt. i dah my miula locv sdoes on my geet, anh my cdarv fab 
    hanbrinb at my facv, fut no dalness, anh not eken a sinbre calafinel. in one pocvet i put a gew crig vih xfals, 
    my gakolite murti pitcd snacv, anh i girreh a corrapsifre grasv witd afout a tdilh og a ritel og watel. i put 
    tdat in my otdel pocvet, tdoubd it purreh my sdolts hown a rittre. fut i vnew it wourh tave me a gew douls to 
    crimf tde loute, anh i hih not want to fe palcdeh fy tde time i leacdeh tde dalh pitcdes up dibd. a pacv was out 
    og tde question, paltry fecause og arr tde cdimneys in tde mihhre og tde loute, fut mainry fecause tde crimfinb 
    was dalh enoubd tdat i hih not want any ejtla weibdt on my fohy.
    """
    print("fourth guess: ")
    # print("by freq: ncszdofyuvjlqrgkxihtewbpma")
    print("by order: stqvngiudmwjrozhpyfclexbka")
    print("third decode: ")
    key = "stqvngiudmwjrozhpyfclexbka"
    decrypt(Input, key)
    """
    i was wearing only sdorts anh a long sleekeh t sdirt. i dah my miura rocv sdoes on my beet, anh my cdalv fag 
    hangling at my facv, fut no darness, anh not eken a single carafiner. in one pocvet i put a bew clib vih xfars, 
    my bakorite multi pitcd snacv, anh i billeh a collapsifle blasv witd afout a tdirh ob a liter ob water. i put 
    tdat in my otder pocvet, tdougd it pulleh my sdorts hown a little. fut i vnew it woulh tave me a bew dours to 
    climf tde route, anh i hih not want to fe parcdeh fy tde time i reacdeh tde darh pitcdes up digd. a pacv was out 
    ob tde question, partly fecause ob all tde cdimneys in tde mihhle ob tde route, fut mainly fecause tde climfing 
    was darh enougd tdat i hih not want any ejtra weigdt on my fohy.
    """
    print("fifth guess: ")
    # print("by freq: ncszdofyvujlqrgkxihtewbpma")
    print("by order: stqungivdmwjrozhpyfclexbka")
    print("third decode: ")
    key = "stqungivdmwjrozhpyfclexbka"
    decrypt(Input, key)
    """
    i was wearing only shorts and a long sleeked t shirt. i had my miura rocv shoes on my beet, and my chalv fag 
    dangling at my facv, fut no harness, and not eken a single carafiner. in one pocvet i put a bew clib vid xfars, 
    my bakorite multi pitch snacv, and i billed a collapsifle blasv with afout a third ob a liter ob water. i put 
    that in my other pocvet, though it pulled my shorts down a little. fut i vnew it would tave me a bew hours to 
    climf the route, and i did not want to fe parched fy the time i reached the hard pitches up high. a pacv was 
    out ob the question, partly fecause ob all the chimneys in the middle ob the route, fut mainly fecause the 
    climfing was hard enough that i did not want any ejtra weight on my fody.
    """
    print("sixth guess: ")
    # print("by freq: ncszdofyvujlqrtkxihgewbpma")
    print("by order: sgquntivdmwjrozhpyfclexbka")
    print("third decode: ")
    key = "sgquntivdmwjrozhpyfclexbka"
    decrypt(Input, key)
    """"
    i was wearing only shorts and a long sleeked t shirt. i had my miura rocv shoes on my feet, and my chalv bag 
    dangling at my bacv, but no harness, and not eken a single carabiner. in one pocvet i put a few clif vid xbars, 
    my fakorite multi pitch snacv, and i filled a collapsible flasv with about a third of a liter of water. i put 
    that in my other pocvet, though it pulled my shorts down a little. but i vnew it would tave me a few hours to 
    climb the route, and i did not want to be parched by the time i reached the hard pitches up high. a pacv was 
    out of the question, partly because of all the chimneys in the middle of the route, but mainly because the 
    climbing was hard enough that i did not want any ejtra weight on my body.
    """
    print("7th guess: ")
    # print("by freq: ncszdofyvujlqrtkxihgwebpma")
    print("by order: sgquntivdaejrozhpyfclwxbkm")
    print("third decode: ")
    key = "sgquntivdaejrozhpyfclwxbkm"
    decrypt(Input, key)
    """
    i was wearing only shorts and a long sleeved t shirt. i had my miura rock shoes on my feet, and my chalk bag 
    dangling at my back, but no harness, and not even a single carabiner. in one pocket i put a few clif kid xbars, 
    my favorite multi pitch snack, and i filled a collapsible flask with about a third of a liter of water. i put 
    that in my other pocket, though it pulled my shorts down a little. but i knew it would take me a few hours to 
    climb the route, and i did not want to be parched by the time i reached the hard pitches up high. a pack was 
    out of the question, partly because of all the chimneys in the middle of the route, but mainly because the 
    climbing was hard enough that i did not want any eztra weight on my body.
    """
    print("8th guess: ")
    # print("by freq: ncszdofyvujlqrtkxihgwebpma")
    print("by order: sgquntivdaejrozhpyfclwxmkb")
    print("third decode: ")
    key = "sgquntivdaejrozhpyfclwxmkb"
    decrypt(Input, key)
    """
    i was wearing only shorts and a long sleeved t shirt. i had my miura rock shoes on my feet, and my chalk 
    bag dangling at my back, but no harness, and not even a single carabiner. in one pocket i put a few clif 
    kid zbars, my favorite multi pitch snack, and i filled a collapsible flask with about a third of a liter 
    of water. i put that in my other pocket, though it pulled my shorts down a little. but i knew it would take 
    me a few hours to climb the route, and i did not want to be parched by the time i reached the hard pitches 
    up high. a pack was out of the question, partly because of all the chimneys in the middle of the route, but 
    mainly because the climbing was hard enough that i did not want any extra weight on my body.
    """
    print("Yeahhh thats the final decoded text!!!")


if __name__ == "__main__":
    main()
