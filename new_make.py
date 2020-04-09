
import re
###################################################
#####        ###            #######################
##### Author ### Promontana #######################
#####        ###            #######################
###################################################
#####        ###            #######################
##### Github ### saeziae    #######################
#####        ###            #######################
###################################################
#####         ###                                 #
##### License ### GNU General Public License v3.0 #
#####         ###                                 #
###################################################
with open("in.txt","r") as f:
    global orignal
    original = f.read().replace("\n","").replace("\r","").replace("\t","").replace(" ","").replace("|","")

def conv(txt):
    """
    make 123 into CDE, eg.
    """
    tones = [  #C
        ["4", "F4"],
        ["1", "C4"],
        ["2", "D4"],
        ["3", "E4"],
        ["5", "G4"],
        ["6", "A4"],
        ["7", "B4"],

        ["4,", "3"],
        ["3,", "2"],
        ["2,", "1"],
        ["4.", "5"],
        ["5.", "6"],
        ["6.", "7"],
        ["7.", "8"],
    ]
    '''
    tones = [  #bE
        ["4", "bA4"],
        ["1", "bE4"],
        ["2", "F4"],
        ["3", "G4"],
        ["5", "bB4"],
        ["6", "C5"],
        ["7", "D5"],

        ["4,", "3"],
        ["3,", "2"],
        ["2,", "1"],
        ["4.", "5"],
        ["5.", "6"],
        ["6.", "7"],
        ["7.", "8"],
    ]
    '''
    for i in tones:
        txt = txt.replace(i[0], i[1])

    return txt

listo=[]

to_beat={
    "-": "2",
    "--": "3",
    "---": "4",
    "_": "0.5",
    "__": "0.25",
    "___": "0.125",
    "_>": "0.75",
    "__>": "0.375",
    "___>": "0.1875",
    ">": "1.5",
    
}
    
listo = []
pattern = re.compile(r'\d[^\d]*')
pattern1 = re.compile(r'[_\->]+')
result1 = pattern.findall(original)
for result in result1:
    result2="1"
    find = pattern1.findall(result)
    if find:
        result2 = to_beat[find[0]]
        result=result.rstrip('_->')
    listo.append((result,result2))
    
a = '\n'.join([conv(i[0])+" "+i[1] for i in listo])

with open("music.txt","w") as f:
    f.write(a)