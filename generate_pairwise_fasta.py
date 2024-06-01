import os
from pprint import pprint 
from pathlib import Path

fragments = './fragments.txt'
savepath = './fasta_files'

Path(savepath).mkdir(parents=True, exist_ok=True)

all_lines = []
with open(fragments) as f:
    while line := f.readline():
        a = line.rstrip()
        if a != '':
            all_lines.append(a)
           
#pprint(all_lines)

prot_dict = {}
head_count = []

all_text = '__'.join(all_lines)

#print(all_text)

separate_proteins = all_text.split('>')
separate_proteins = list(filter(None, separate_proteins))
for p in separate_proteins:
    p_list = p.split('__')
    p_list = list(filter(None, p_list))
#    print(p_list)
    prot_dict[p_list[0].partition('_')[0]] = {}
    for i in range(0, len(p_list)):
        if ':' in p_list[i]:
            prot_dict[p_list[0].partition('_')[0]][p_list[i][:-1]] = p_list[i+1]

for k1, v1 in prot_dict.items():
    for k2, v2 in prot_dict.items():
        #if k1 != k2:
            for res_range1, res1 in v1.items():
                for res_range2, res2 in v2.items():
                    
                    fasta_head = k1 + '_' + res_range1.replace("-", "_") + "_" + k2 + '_' + res_range2.replace("-", "_")
                    fasta_alternate_head = k2 + '_' + res_range2.replace("-", "_") + "_" + k1 + '_' + res_range1.replace("-", "_")
                    fasta_content_1 =  res1 + ':' + '\n'
                    fasta_content_2 = res2
                    fastafiles_lst = []
                    for fastafiles in os.listdir(savepath):
                        fastafiles_lst.append(fastafiles.partition('.')[0])
                    if fasta_alternate_head not in fastafiles_lst:
                        with open(os.path.join(savepath,'{fname}.fasta').format(fname = fasta_head), 'w') as g:
                            g.writelines(['>'+fasta_head + '\n', fasta_content_1, fasta_content_2])
#print(fasta_head, fasta_content_1)
