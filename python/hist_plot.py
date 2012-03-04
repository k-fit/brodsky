import matplotlib
import numpy
import matplotlib.dates
import pylab
import matplotlib
from pylab import *
from datetime import *
from matplotlib.dates import num2date
from matplotlib.backends.backend_pdf import PdfPages	

def hist_plot(call):
	pp = PdfPages('topsy.pdf')
	for item in call:
		hist_pl(item)
		pp.savefig()
	pp.close()
		

def hist_pl(L):
	hold('True')
	#fig = figure()
	ax = pylab.figure().gca()
	#ax = fig.add_subplot(111)
	title(L['target']['title'])
	for item in L['gen_sent']:
		dates = item['dates']
		dates_num = [date2num(datetime.strptime(str(dates[i]), '%Y%m%d')) for i in range(len(dates))]
		ax.plot_date(dates_num, item['neg_ref'], 'b-', label = 'neg_ref')
		ax.plot_date(dates_num, item['pos_ref'], 'y-', label = 'pos_ref')
		ax.plot_date(dates_num, item['ref'], 'g-', label = 'ref')

	ax.xaxis.set_major_formatter(DateFormatter('%m \n %b'))
	handles, labels = ax.get_legend_handles_labels()
	legend(handles[0:3], labels[0:3])
	
