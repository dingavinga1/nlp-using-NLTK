"""
##########################
#DISCRETE PROJECT PHASE 2#
#ABDULLAH IRFAN 20I-2702##
#AISHA IRFAN 20I-1851#####
#MUHAMMAD HUZAIFA 20I-0604
#SAMEEL AHMED 20I-0527####
#####CYBER SECURITY-T#####
"""

##################################
##################################
##################################

# PREREQUISITES FOR THIS PROGRAM #
# $pip install matplotlib
# $pip install nltk
# $pip install bs4
# $pip install requests
# $pip install networkx
# $pip install scipy
##################################

########### GUIDELINES ###########
# This program extracts data from
# 5 webpages each from the websites
# of NUCES, NUST and LUMS
##################################
# This program uses alot of 
# computational power and was 
# tested of a system running 
# windows 10 on 32gb of RAM and 
# Core i9-9900K
# If your system does not match the
# requirements, this program might 
# cause your system to crash or
# take an unusual amount of time 
# to run. 
# Please be patient and wait for
# the results


import requests #library for web scrapping
from bs4 import BeautifulSoup #library for html parsing
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize #library for tokenizing text
import matplotlib.pyplot as plt #library for visualisation using graphs
import networkx as nx #library for plotting connected graphs
import networkx as nx
from networkx.utils.decorators import not_implemented_for
from networkx.algorithms.shortest_paths import single_source_shortest_path_length as sp_length
import scipy as sp

print("\n\n\n\n\n\n\n\n\n\n\nPLEASE WAIT...\nTHERE IS TOO MUCH DATA BEING HANDLED SO IT MIGHT TAKE A WHILE")

#####################################
#VARIOUS FUNCTIONS FOR WEB SCRAPPING#
#####################################

def webScrape(url):
    stringx=requests.get(url)
    stringy=stringx.content
    return stringy #returns raw html content from url

def getContent(stringy):
    soup=BeautifulSoup(stringy, 'html.parser')
    return soup #returns parsed data from html content

def convertText(soup):
    return soup.get_text() #returns all text (removing all tags)

################################
#EXTRACTING TEXT FROM WEBSTITES#
################################

#making a string of all text from 5 webpages of nu.edu.pk
l=convertText(getContent(webScrape("http://nu.edu.pk")))
l=l+convertText(getContent(webScrape("http://nu.edu.pk/vision-and-mission")))
l=l+convertText(getContent(webScrape("http://nu.edu.pk/University/History")))
l=l+convertText(getContent(webScrape("http://nu.edu.pk/Oric")))
l=l+convertText(getContent(webScrape("http://nu.edu.pk/University/Foundation")))

#making a string of all text from 5 webpages of lums.edu.pk
m=convertText(getContent(webScrape("https://lums.edu.pk/")))
m=m+convertText(getContent(webScrape("https://lums.edu.pk/aboutlums")))
m=m+convertText(getContent(webScrape("https://lums.edu.pk/ranking-accreditation")))
m=m+convertText(getContent(webScrape("https://sdsb.lums.edu.pk/")))
m=m+convertText(getContent(webScrape("https://sbasse.lums.edu.pk/")))

#making a string of all text from 5 webpages of nust.edu.pk
n=convertText(getContent(webScrape("https://nust.edu.pk/")))
n=n+convertText(getContent(webScrape("https://nust.edu.pk/about-us")))
n=n+convertText(getContent(webScrape("https://seecs.nust.edu.pk/about-us/history/")))
n=n+convertText(getContent(webScrape("https://seecs.nust.edu.pk/about-us/why-seecs/")))
n=n+convertText(getContent(webScrape("https://scme.nust.edu.pk/welcome-to-seecs/")))

##########################
#EXTRACTING POS FROM TEXT#
##########################

#extracting tokens from strings created before
ltokens=word_tokenize(l)
mtokens=word_tokenize(m)
ntokens=word_tokenize(n)

#counting number of each pos from token lists

lnouns=[]
lncount=0
lvcount=0
lacount=0
for i in ltokens:
    if(nltk.pos_tag([i])[0][1]=="NN" or nltk.pos_tag([i])[0][1]=="NNS" or nltk.pos_tag([i])[0][1]=="NNP" or nltk.pos_tag([i])[0][1]=="NNPS"): #checking if word is noun
        lnouns.append(nltk.pos_tag([i])[0][0])
        lncount+=1
    if(nltk.pos_tag([i])[0][1]=="VB" or nltk.pos_tag([i])[0][1]=="VBD" or nltk.pos_tag([i])[0][1]=="VBG" or nltk.pos_tag([i])[0][1]=="VBN" or nltk.pos_tag([i])[0][1]=="VBP" or nltk.pos_tag([i])[0][1]=="VBZ"): #checking if word is a verb
        lvcount+=1
    if(nltk.pos_tag([i])[0][1]=="JJ" or nltk.pos_tag([i])[0][1]=="JJR" or nltk.pos_tag([i])[0][1]=="JJS"): #checking if word is an adjective
        lacount+=1
    if(nltk.pos_tag([i])[0][1]=="."):
        lnouns.append(".")

mnouns=[]
mncount=0
mvcount=0
macount=0
for i in mtokens:
    if(nltk.pos_tag([i])[0][1]=="NN" or nltk.pos_tag([i])[0][1]=="NNS" or nltk.pos_tag([i])[0][1]=="NNP" or nltk.pos_tag([i])[0][1]=="NNPS"): #checking if word is noun
        mnouns.append(nltk.pos_tag([i])[0][0])
        mncount+=1
    if(nltk.pos_tag([i])[0][1]=="VB" or nltk.pos_tag([i])[0][1]=="VBD" or nltk.pos_tag([i])[0][1]=="VBG" or nltk.pos_tag([i])[0][1]=="VBN" or nltk.pos_tag([i])[0][1]=="VBP" or nltk.pos_tag([i])[0][1]=="VBZ"): #checking if word is a verb
        mvcount+=1
    if(nltk.pos_tag([i])[0][1]=="JJ" or nltk.pos_tag([i])[0][1]=="JJR" or nltk.pos_tag([i])[0][1]=="JJS"): #checking if word is an adjective
        macount+=1
    if(nltk.pos_tag([i])[0][1]=="."):
        mnouns.append(".")

nnouns=[]
nncount=0
nvcount=0
nacount=0
for i in ntokens:
    if(nltk.pos_tag([i])[0][1]=="NN" or nltk.pos_tag([i])[0][1]=="NNS" or nltk.pos_tag([i])[0][1]=="NNP" or nltk.pos_tag([i])[0][1]=="NNPS"): #checking if word is noun
        nnouns.append(nltk.pos_tag([i])[0][0])
        nncount+=1
    if(nltk.pos_tag([i])[0][1]=="VB" or nltk.pos_tag([i])[0][1]=="VBD" or nltk.pos_tag([i])[0][1]=="VBG" or nltk.pos_tag([i])[0][1]=="VBN" or nltk.pos_tag([i])[0][1]=="VBP" or nltk.pos_tag([i])[0][1]=="VBZ"): #checking if word is a verb
        nvcount+=1
    if(nltk.pos_tag([i])[0][1]=="JJ" or nltk.pos_tag([i])[0][1]=="JJR" or nltk.pos_tag([i])[0][1]=="JJS"): #checking if word is an adjective
        nacount+=1
    if(nltk.pos_tag([i])[0][1]=="."):
        nnouns.append(".") 

#print(lnouns)
#exit()

#################################################
#CREATING VISUALISATION OF ALL POS AS COMPARISON#
#################################################

#creating x axis
uni=['NUCES', 'LUMS', 'NUST']

#creating y axis for nouns chart
pnouns=[lncount, mncount, nncount]

#plotting bar graph for nouns
plt.bar(uni, pnouns)
plt.title('University vs Nouns')
plt.xlabel('University')
plt.ylabel('Nouns')
plt.show()

#creating y axis for verbs chart
pverbs=[lvcount, mvcount, nvcount]

#plotting bar graph for verbs
plt.bar(uni, pverbs)
plt.title('University vs Verbs')
plt.xlabel('University')
plt.ylabel('Verbs')
plt.show()

#creating y axis for adjectives chart
padjs=[lacount, macount, nacount]

#plotting bar graph for adjectives
plt.bar(uni, padjs)
plt.title('University vs Adjectives')
plt.xlabel('University')
plt.ylabel('Adjectives')
plt.show()

#######################################
#MAKING A CONNECTED GRAPH OF ALL NOUNS#
#######################################

g=nx.Graph() #creating an undirected graph

#adding nouns of first website
for z in range(0, len(lnouns)):
    for i in range(z, len(lnouns)):
        if lnouns[i]=='.':
            z+=1
            break
        g.add_node(lnouns[i])
        for j in range(z, len(lnouns)):
            if i is not j:
                if lnouns[j]=='.':
                    break
                g.add_node(lnouns[j])
                g.add_edge(lnouns[i], lnouns[j])
        z+=1
        if z>10:
            break
"""
#adding nouns of second website
for z in range(0, len(mnouns)):
    for i in range(z, len(mnouns)):
        if mnouns[i]=='.':
            z+=1
            break
        g.add_node(mnouns[i])
        for j in range(z, len(mnouns)):
            if i is not j:
                if mnouns[j]=='.':
                    break
                g.add_node(mnouns[j])
                g.add_edge(mnouns[i], mnouns[j])
        z+=1

#adding nouns of third website
for z in range(0, len(nnouns)):
    for i in range(z, len(nnouns)):
        if nnouns[i]=='.':
            z+=1
            break
        g.add_node(nnouns[i])
        for j in range(z, len(nnouns)):
            if i is not j:
                if nnouns[j]=='.':
                    break
                g.add_node(nnouns[j])
                g.add_edge(nnouns[i], nnouns[j])
        z+=1 
        """

print("\n" for i in range(100))

################################################
#FINDING OUT THE NUMBER OF CONNECTED COMPONENTS#
################################################

connectedComps=nx.number_connected_components(g)
print("Number of connected components:", end=" ")
print(connectedComps)

print("\n\n")

#########################################
#PRINTING TOP 10 NOUNS AND THEIR DEGREES#
#########################################

max=[-1 for i in range(10)] #list to store degrees of top nouns
topnouns=['' for i in range(10)] #list to store top nouns

#looking for and storing top 10 nouns and their degrees
for i in range(10):
    for j in g.nodes():
        if j not in topnouns:
            if g.degree(j)>max[i]:
                max[i]=g.degree(j)
                topnouns[i]=j

#printing
print("TOP 10 NOUNS AND DEGREES")
for i in range(10):
    print("Noun:", end=" ")
    print(topnouns[i], end="\t")
    print("Degree: ", end=" ")
    print(max[i])

print("\n\n")

#################################################
#PRINTING ALL NOUNS FROM DISTANCE<5 FROM QUALITY#
#################################################

print("Nouns adjacent to quality\n")
dicts=nx.single_source_shortest_path(g, "quality", 5) #gets all paths of length<5 
print(set(dicts.keys())) #displays all nouns on those paths


##########################
#VISUALISING NOUN NETWORK#
##########################

plt.title("Connected graph of all nouns")
plt.axis('off')
nx.draw_networkx(g)
plt.show()