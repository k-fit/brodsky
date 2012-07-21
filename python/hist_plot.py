import matplotlib
matplotlib.use('Agg') #so that plot windows don't pop up 
matplotlib.rcParams.update({'font.size': 8})
import numpy
import matplotlib.dates
import pylab
import matplotlib
import datetime
from pylab import *
#from datetime import *
from matplotlib.dates import num2date
from matplotlib.backends.backend_pdf import PdfPages	


def hist_plot(call):
	no_plots = 0
	no_plots_sent = 0
	now = datetime.datetime.now().date()
	pp = PdfPages('../plots/topsy_' + str(now.month) + '-'+ str(now.day) + '2.pdf')
	for item in call:
		try:
			hist_pl(item)
			pp.savefig()
		except:
			no_plots += 1
		try:
			hist_pl2(item)
			pp.savefig()
		except:
			no_plots_sent += 1

			
	pp.close()
	print "no_plots = " + str(no_plots)
	print "no_plots_sent = " + str(no_plots_sent)

		

def hist_pl(L):
	hold('True')
	#fig = figure()
	ax = pylab.figure().gca()
	#ax = fig.add_subplot(111)
	title(L['target']['url'])
	for item in L['gen_sent:yahoo']:
		dates = item['dates']
		dates_num = [date2num(datetime.datetime.strptime(str(dates[i]), '%Y%m%d')) for i in range(len(dates))]
		ax.plot_date(dates_num, item['neg_ref'], 'b-', label = 'neg_ref')
		ax.plot_date(dates_num, item['pos_ref'], 'y-', label = 'pos_ref')
		ax.plot_date(dates_num, item['ref'], 'g-', label = 'ref')

	#ax.xaxis_date()
	ax.xaxis.set_major_formatter(DateFormatter('%d \n %b'))
	handles, labels = ax.get_legend_handles_labels()
	legend(handles[0:3], labels[0:3])
	

def hist_pl2(L):
	hold('True')
	#fig = figure()
	ax = pylab.figure().gca()
	#ax = fig.add_subplot(111)
	title(L['target']['url'])
	for item in L['gen_sent:yahoo']:
		dates = item['dates']
		dates_num = [date2num(datetime.datetime.strptime(str(dates[i]), '%Y%m%d')) for i in range(len(dates))]
		ax.plot_date(dates_num, item['sentiment'], 'r-', label = 'sentiment')
	#ax.xaxis_date()
	ax.xaxis.set_major_formatter(DateFormatter('%d \n %b'))
	handles, labels = ax.get_legend_handles_labels()
	ylabel('SENTIMENT')
	#legend(handles[0], labels[0])

