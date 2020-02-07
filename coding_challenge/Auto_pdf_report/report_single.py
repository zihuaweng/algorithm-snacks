# -*- coding: utf-8 -*-
"""
	This script is to :
		generate single report for urinary_project individual to specific out_dir

	Usafe:
		python script.py [qiime_file_dir] [phynotype.file] [sample.id] [out_dir_new]

"""
import sys
import os
import commands
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import re
import json
import datetime
from jinja2 import Template, Environment, FileSystemLoader
import os
import pdfkit
from slugify import slugify

if __name__ == "__main__":
	if len(sys.argv) != 5:
		print __doc__
		sys.exit()

script, dir, phy, query_id, output_dir = sys.argv

reload(sys)
sys.setdefaultencoding('utf-8')

all_data = {}
all_data['part_1'] = {}
all_data['part_2'] = {}
all_data['part_3_1'] = {}
all_data['part_3_2'] = {}

#mkdir output dirs
#upper_dir = os.path.dirname(dir)
dir = os.path.abspath(dir)

#a_diversity = '/share/apps/miniconda2/envs/qiime1/bin/alpha_diversity.py'
#css = "/share/data2/wengzh/python/Urinary_report/report.css"
css = "report.css"
script_dir = os.path.dirname(os.path.abspath(__file__))

#==============================================================================
def trans(value):
	try:
    		unicode(value, "ascii")
	except UnicodeDecodeError:
    		value = unicode(value, "utf-8")
	else:
    		# value was valid ASCII data
    		pass

def check_mkdir(path):
	if not os.path.exists(path):
		os.mkdir(path)

def mkdir_part_file(outdir,file):
	path = outdir + '/' + file
	if not os.path.exists(path):
		os.mkdir(path)

def find_file(dir,suffix):
	command = 'find ' + dir + ' -name "*' + suffix + '"'
	path = commands.getoutput(command)
	return path

def find_file_open_col(dir, suffix):
	command = 'find ' + dir + ' -name "*' + suffix + '"'
	path = commands.getoutput(command)
	file = pd.read_table(path, index_col = 0)
	head = list(file.columns.values)
	return file, head

def replace_taxa2new(df, series, col_name):
	new_col = []
	for anno in series:
		a = re.sub('.*g__', '', anno, count=0, flags=0)
		a = re.sub('.*o__', 'o__', a, count=0, flags=0)
		a = re.sub(';s__', ' ', a, count=0, flags=0)
		new_col.append(a)
	df[col_name] = pd.Series(new_col, index=df.index)

def report_part_2(hgenus,sample):
	plt.figure(figsize=(8,8))
	labels = sorted(hgenus, key=hgenus.__getitem__, reverse=True)
	sizes = []
	for key in labels:
		sizes.append(hgenus[key])
	labels.append('others')
	sizes.append(others[sample])
	n = len(labels)
	#colors = ['%f' % (i/float(n)) for i in range(n)]
	colors = np.repeat('lightgray',n)
	explode = (list(np.repeat(0.05,n)))
	patches,l_text,p_text = plt.pie(sizes,
									#explode=explode,
									labels=labels,
									colors=colors,
									labeldistance = 1.1,
									autopct = '%3.1f%%',
									shadow = False,
									startangle = 90,
									pctdistance = 0.9,
									#radius=0.8,
									wedgeprops = { 'linewidth' : 1 , 'edgecolor' : 'black'}
									)
	#db = ['', '/', 'o', '+', '*', '.', '-', '|', 'x', '0', '/', 'o', '+', '*', '.', '|', 'x', '0', '/', 'o', '+', '*', '.']
	#hatching = db[:n]
	#for j, patch in enumerate(patches): patch.set_hatch(hatching[j])
	#change text size
	for t in range(n):
		l_text[t].set_fontsize(12)
		p_text[t].set_fontsize(12)

	#axis=equal so that pie chat will show as a circle
	plt.axis('equal')
	plt.subplots_adjust(right=0.8)
	#plt.tight_layout()
	#plt.legend()
	plt.savefig(out_dir + '/all_data_fig/' + sample + '.png')
	plt.close()

def report_part_3(hpa, sample):
	warning = {}
	all_data['part_3_1'][sample] = {}
	all_data['part_3_2'][sample] = {}
	species = hpa.keys()
	num = len(species)
	if num == 0:
		result = '您的尿液中没有检测出泌尿系统感染常见致病菌'
		#all_data['part_3_1'][sample] = trans(result)
		all_data['part_3_1'][sample] = result
	else:
		result = '您的尿液中检测出' + str(num) + '种泌尿系统感染常见致病菌'
		c_warn = 0
		for s,abun in hpa.items():
			if abun > 0.5:
				c_warn =+ 1
				warning[s] = 1
		if c_warn == 0:
			result_1 = '，但含量并未超标:'
			result_2 = result + result_1
			#all_data['part_3_1'][sample] = trans(result_2)
			all_data['part_3_1'][sample] = result_2
		elif c_warn > 0:
			result_1 = ',其中有' + str(c_warn) + '种超标，需引起您的注意：'
			result_2 = result + result_1
			#all_data['part_3_1'][sample] = trans(result_2)
			all_data['part_3_1'][sample] = result_2

	for s in species:
		all_data['part_3_2'][sample][s] = {}
		all_data['part_3_2'][sample][s]['gram'] = hgram[s]
		all_data['part_3_2'][sample][s]['zname'] = hzname[s]
		if s in warning.keys():
			all_data['part_3_2'][sample][s]['abun'] = \
			str(float('%.2f' %(float(hpa[s])*100))) + '%' + '(*)'
		else:
			all_data['part_3_2'][sample][s]['abun'] = \
			str(float('%.2f' %(float(hpa[s])*100))) + '%'

def to_json(dict):
	with open(out_dir + '/all_data_json/' + 'all_data.json','w') as f:
		json.dump(dict, f, ensure_ascii=False, sort_keys=True)

def toHtml(data, info, id, path):
#	fn = slugify(id + " " + datetime.date.today().strftime('%m/%d/%y'))
	fn = id
	jenv = Environment(loader=FileSystemLoader(script_dir), trim_blocks=True)
	tmpl = jenv.get_template('report.html')
	out = tmpl.render(data=data, info=info, id=id, path=path)
	with open(out_dir + '/report_pdf/' + fn + '.html', "wb") as fh:
		#fh.write(out.encode('utf-8'))
		fh.write(out)
	pdfkit.from_string(out, out_dir + '/report_pdf/' + fn + '.pdf', css=css)

#==============================================================================
#make dir for all_output
check_mkdir(output_dir)	
out_dir = os.path.abspath(output_dir)
mkdir_part_file(out_dir,'all_data_json')
mkdir_part_file(out_dir,'all_data_fig')
mkdir_part_file(out_dir,'report_pdf')

#==============================================================================
#import pynotype file
hphy = {}

with open(phy, 'r') as info:
	phy = info.readlines()
	head = phy[0]
	head = head.strip('\n').split('\t')
	col = len(head)
	for line in phy[1:]:
		line = line.strip('\n').split('\t')
		hphy[line[0]] = {}
		for i in range(1,col):
			hphy[line[0]][head[i]] = line[i]

#==============================================================================
#generate out_count file : 1st part of reports

#####count observed otu by qiime script.py
#command = 'find ' + dir + ' -name *otu_prof.biom'
#prof_file = commands.getoutput(command)
#command = ['python', a_diversity, '-i', prof_file, '-m observed_otus', '-o', out_dir+'/out_count']
#command = ' '.join(command)
#os.system(command)

#####count observed otu without using any scripts
hc_otu = {}

prof, samples = find_file_open_col(dir, 'otu_prof')
for id in samples:
	hc_otu[id] = len(prof[prof[id]>0][id])
	all_data['part_1'][id] = hc_otu[id]    ##dict for json file

#==============================================================================
#draw bacteria composition pie-chat
hgenus_otu = {}
others = {}

genus_path = dir + '/profile'

g_prof, samples = find_file_open_col(genus_path, 'genus.prof')

replace_taxa2new(g_prof, g_prof.index, 'index')
g_prof = g_prof.set_index('index')

for id in samples:
	if id == query_id:
		all_data['part_2'][id] = {}
		series = g_prof[g_prof[id]>=0.03][id]
		hgenus_otu = dict(series)
		other = g_prof[g_prof[id]<0.03][id].sum()
		others[id] = other
		report_part_2(hgenus_otu, id)
		##dict for json file
		for g in hgenus_otu.keys():
			all_data['part_2'][id][g] = hgenus_otu[g]
		all_data['part_2'][id]['others'] = other

#==============================================================================
#return a pathogen list as report part_3
#read pathogen.list
hlist = {}
hzname = {}
hgram = {}

file = open(script_dir + '/pathogen.list', 'r')
pa_list = file.readlines()
for line in pa_list:

	line = line.strip('\n').split('\t')
	hlist[line[0]] = 1
	hzname[line[1]] = line[2]
	hgram[line[1]] = line[3]

label_path = dir + '/otus/rdp_assigned_taxonomy'
path = find_file(label_path, 'txt')
anno = pd.read_table(path, header = None, index_col = 0)

otu, sample = find_file_open_col(genus_path, 'otu_prof.even')
#merge anno and otu dataframe according to df.index
anno_otu = pd.merge(anno, otu, left_index=True, right_index=True, how = 'inner')
r_total = anno_otu.sum(axis=0)[3]   #total reads for even file are the same, 3 represents the index of the first sample

#pick pathgen otu from df
df = anno_otu[anno_otu.iloc[:,0].str.contains(hlist.keys()[0]) == True]
hlist.pop(hlist.keys()[0])
for key in hlist.keys():
	l = anno_otu[anno_otu.iloc[:,0].str.contains(key) == True]
#	if len(l.index) != 0:
#		hgram[l.iloc[0,0]] = hgram[key]
#		hzname[l.iloc[0,0]] = hzname[key]
	df = pd.concat([df, l], axis=0)

replace_taxa2new(df, df.iloc[:,0], 'index')
#sum rows according to annotation
df.drop(df.columns[[0,1]], axis=1, inplace=True)
df = df.groupby(df['index']).sum()
#calculate ralative_abun
df = df.apply(lambda x : (x/float(r_total)))

hpa_abun = {}
for id in sample:
	if id == query_id:
		series = df[df[id]>0][id]
		hpa_abun = dict(series)
		report_part_3(hpa_abun, id)

#==============================================================================
#generate json file
to_json(all_data)

#==============================================================================
#trans of Chinese encoding for part_3_1
json.dumps(all_data).decode("unicode-escape")

#==============================================================================
#generate pdf file
for id in sample:
	if id == query_id:
		path = out_dir + '/all_data_fig/' + id + '.png'
		toHtml(all_data, hphy, id, path)
