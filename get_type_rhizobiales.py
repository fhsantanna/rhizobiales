#/usr/bin/env python

#Author: Dr. Fernando Hayashi Sant'Anna
#Date: 03/28/2018

#Captura código das linhagens e número acesso de espécies do gênero de interesse a partir do LPSN.
#This script accesses bacterio.net(LPSN), captures type strain codes and 16S rRNA accession numbers from species of a genus of interest, generating a table as output.

#Usage: python get_type_rhizobiales.py

import re
from bs4 import BeautifulSoup
import requests

#strain = sys.argv[1]
outfile_name = "strains_rhizobiales_lpsn.txt"
outfile = open(outfile_name, "a")
outfile.write("Species" + "\t" + "Strain" + "\t" + "Accession number" + "\n")

lista_rhizobiales = ["Afifella", "Afipia", "Agrobacterium", "Albibacter", "Aliihoeflea", "Alsobacter", "Aminobacter", "Amorphomonas", "Amorphus", "Ancalomicrobium", "Ancylobacter", "Anderseniella", "Angulomicrobium", "Aquabacter", "Aquamicrobium", "Arsenicitalea", "Aurantimonas", "Aureimonas", "Azorhizobium", "Bartonella", "Bauldia", "Beijerinckia", "Blastobacter", "Blastochloris", "Bosea", "Bradyrhizobium", "Breoghania", "Brucella", "Camelimonas", "Carbophilus", "Chelativorans", "Chelatococcus", "Chenggangzhangella", "Chthonobacter", "Ciceribacter", "Cohaesibacter", "Consotaella", "Corticibacterium", "Cucumibacter", "Daeguia", "Devosia", "Dichotomicrobium", "Ensifer", "Enterovirga", "Falsochrobactrum", "Filomicrobium", "Fulvimarina", "Gellertiella", "Hansschlegelia", "Hartmannibacter", "Hoeflea", "Hyphomicrobium", "Jiella", "Kaistia", "Labrys", "Lentilitoribacter", "Liberibacter", "Lutibaculum", "Mabikibacter", "Maritalea", "Martelella", "Mesorhizobium", "Methylobacterium", "Methylobrevis", "Methylocapsa", "Methyloceanibacter", "Methylocella", "Methylocystis", "Methyloferula", "Methyloligella", "Methylopila", "Methylorhabdus", "Methylorosula", "Methylosinus", "Methylosporovibrio", "Methylosulfonomonas", "Methyloterrigena", "Methylovirgula", "Microvirga", "Mongoliimonas", "Mycoplana", "Neomegalonema", "Nitratireductor", "Nitrobacter", "Nordella", "Notoacmeibacter", "Ochrobactrum", "Oharaeibacter", "Oligotropha", "Oricola", "Paenochrobactrum", "Paradevosia", "Paramesorhizobium", "Parvibaculum", "Pedomicrobium", "Pelagibacterium", "Photorhizobium", "Phyllobacterium", "Pleomorphomonas", "Polyprosthecobacterium", "Prosthecomicrobium", "Pseudahrensia", "Pseudaminobacter", "Pseudochelatococcus", "Pseudochrobactrum", "Pseudohoeflea", "Pseudolabrys", "Pseudorhodoplanes", "Pseudoxanthobacter", "Psychroglaciecola", "Pyruvatibacter", "Qingshengfania", "Reichenowia", "Rhizobium", "Rhodobium", "Rhodoblastus", "Rhodoligotrophos", "Rhodomicrobium", "Rhodoplanes", "Rhodopseudomonas", "Robiginosimarina", "Roseiarcus", "Roseitalea", "Roseospirillum", "Salinarimonas", "Seliberia", "Shinella", "Sinorhizobium", "Solomonas", "Starkeya", "Tardiphaga", "Tepidamorphus", "Tepidicaulis", "Terasakiella", "Thalassocella", "Thalassocola", "Tianweitania", "Variibacter", "Xanthobacter", "Youhaiella"]


for genus in range(0,len(lista_rhizobiales)):
	url = "http://bacterio.net/" + lista_rhizobiales[genus].lower() + ".html"

	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	text = soup.get_text()
	text_ed = text.replace("\r\n","\n")

	pattern = " *({0}.+)\n.*\n *Type.+\.net\) *(.+)\..*\n.*\n *Sequence.+\: *(.+)\.".format(lista_rhizobiales[genus].title())
	lista = re.findall(pattern, text_ed)

	for species in (range(0,len(lista))):
	    strains = lista[species][1].split("=")
	    anumber16S = lista[species][2]
	    for n in range(0,len(strains)):
	        name_split = lista[species][0].split(" ")
	        strain = strains[n]
	        if name_split[2] != "subsp.":
	            sname = " ".join(name_split[0:2])
	        else:
	            sname = " ".join(name_split[0:4])
	        outfile.write(sname + "\t" + strain + "\t" + anumber16S + "\n")

outfile.close()