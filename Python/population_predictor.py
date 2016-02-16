import json
import functools, operator, collections
from tsne_fit import fit_tSNE, fit_PCA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

reference_file = '/Users/nickdeveaux/Dev/ThirdParty/ethnicity_population_data.json'
sample_file = '/Users/nickdeveaux/Dev/Data/genome_Nicholas_De_Veaux_Full_20160216093048.txt'

class UnexpectedMutationException(Exception):
    pass

# Returns 0, 0.5, 1, or UnexpectedMutationException
def get_value(reference_allele, alternate_allele, sample_genotype):
    if reference_allele * 2 == sample_genotype:
        return 0.0
    elif alternate_allele * 2 == sample_genotype:
        return 1.0
    elif reference_allele in sample_genotype and alternate_allele in sample_genotype:
        return 0.5
    else:
        raise UnexpectedMutationException(' '.join([reference_allele, alternate_allele, sample_genotype]))

# Annotate plot code from Stack Overflow: http://stackoverflow.com/questions/5147112/matplotlib-how-to-put-individual-tags-for-a-scatter-plot
def annotate(plot, keys, x, y):
    for label, x_v, y_v in zip(keys, x, y):
        plot.annotate(
            label, 
            xy = (x_v, y_v), xytext = (-20, 20),
            textcoords = 'offset points', ha = 'right', va = 'bottom',
            bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
            arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))


ref = json.load(open(reference_file))
sample_data = {}
lines = [line.strip() for line in open(sample_file)]
for l in lines:
    if not l.startswith('#'):
        splits = l.split('\t')
        if len(splits) > 1:
            sample_data[splits[0]] = splits[1:]

#Contents: [u'genomic_coordinates', u'allele_count_denominator', u'allele_frequency_afr', u'allele_frequency_eur', u'rs_id', u'allele_count', u'alternate_allele', u'allele_frequency_amr', u'reference_allele', u'_sbid', u'allele_frequency_eas', u'is_reference_allele', u'homozygote_count', u'allele_frequency', u'allele', u'variant_id', u'allele_frequency_sas', u'population']

rsids = [x['rs_id'] for x in ref]
match = set(rsids).intersection(sample_data.keys())

# Compute Ethnicity by L2 distance

# Initialize distances
distances = {}
vectors = {}
vectors['sample'] = []

for rsid in match:
    genotype = sample_data[rsid][2]
    ref_data = filter(lambda x: x['rs_id'] == rsid and x['is_reference_allele'] == True, ref)[0]
    try:
        distances[rsid] = {}
        coefficient = get_value(ref_data['reference_allele'], ref_data['alternate_allele'][0], genotype)
        vectors['sample'].append(coefficient)
        weightedness = sum([1.0 - pop['allele_frequency'] for pop in ref_data['population']])
        for pop in ref_data['population']:
            distances[rsid][pop['code']] = (((1.0 - pop['allele_frequency']) - coefficient) ** 2)
            if pop['code'] not in vectors:
                vectors[pop['code']] = []
            vectors[pop['code']].append(1.0 - pop['allele_frequency'])
    except UnexpectedMutationException as e:
        print e.message
sum_dict = functools.reduce(operator.add, map(collections.Counter, distances.values()))
print sum_dict
X = np.array([vector for vector in vectors.values()])
Y = fit_PCA(X, 10)
models = fit_tSNE(Y)
colors = np.random.rand(len(models))
x = [100*model[0] for model in models]
y = [100*model[1] for model in models]
plt.scatter(x, y, c=colors, s=50)

annotate(plt,vectors.keys(), x, y)

plt.show() #, labels=vectors.keys())

models = fit_PCA(X)
x = [100*model[0] for model in models]
y = [100*model[1] for model in models]
plt.scatter(x, y, c=colors, s=50)

annotate(plt,vectors.keys(), x, y)

plt.show() 
    
models = fit_PCA(X, 3)
x = [100*model[0] for model in models]
y = [100*model[1] for model in models]
z = [100*model[2] for model in models]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, c=colors)
plt.show() 
