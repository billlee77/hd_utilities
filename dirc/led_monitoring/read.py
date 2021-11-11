from ROOT import gROOT, TCanvas, TF1, TPython, TNtuple, TGraph, TDatime, TLegend, gStyle, gPad, TGaxis
import numpy as np
import sys

gROOT.Reset()
c1 = TCanvas( 'c1', 'LED intensity', 200, 10, 700, 500 )
c2 = TCanvas( 'c2', 'Pressure', 200, 10, 700, 500 )

da = TDatime(2020,1,1,19,00,00) ;
gStyle.SetTimeOffset(da.Convert());

#n1 = TNtuple("nt1","nt1", "run_num/C:date/C:time/C:pressure/C:led1/C:led2/C:led3/C")

#n1.ReadFile("test_digit.txt")


#y = np.loadtxt("test_digit.txt")

#print (y)

# f = open('test_digit.txt', 'r')
# f.read()
# 
# #for line in f.readlines():
# 
# for line in f:
# 	print line
# #	print(repr(line))

# with open('test_digit.txt', 'r') as f:
#     # do things with your file
#     data = f.read()
# 
# type(data)
# 
# 
# #
# # Create a one dimensional function and draw it
# #
#fun1 = TF1( 'fun1', 'abs(sin(x)/x)', 0, 10 )
#c1.SetGridx()
#c1.SetGridy()
#fun1.Draw()
#c1.Update()
# 
#  

#TPython.Prompt()
#run_number = defaultdict(list)
run_number = []
date = []
time = []
pressure = []
led1 = []
led2 = []
led3 = []

f = open(str(sys.argv[1]), 'r') 
#lines = f.readline()
#print lines,

for line in f:
#	print line,
	x = line.split()
#	print(x) 
	run_number.append(x[0])
	date.append(x[1])
	time.append(x[2])
	pressure.append(x[3])
	led1.append(float(x[4]))
	led2.append(float(x[5]))
	led3.append(float(x[6]))
	
f.close()


print run_number
print date
print time
print led1
print led2
print led3

ratio_21 = []
ratio_23 = []
ratio_13 = []

for x in range(np.size(run_number)):
	ratio_13.append(led1[x]/led3[x])
	ratio_21.append(led2[x]/led1[x])
	ratio_23.append(led2[x]/led3[x])


# print ratio_23

gr_13 = TGraph(np.size(run_number))
gr_21 = TGraph(np.size(run_number))
gr_23 = TGraph(np.size(run_number))

gr_pressure = TGraph(np.size(run_number))

data_arr=[]
# Convert time

for x in range(np.size(run_number)):
	date_split = date[x].split("-")
	time_split = time[x].split(":")

#	print date_split
#	print time_split[x]
	
#	print date_split[0], date_split[1], date_split[2], time_split[0], time_split[1], time_split[2] 

	date_time = TDatime(int(date_split[0]), int(date_split[1]), int(date_split[2]), int(time_split[0]), int(time_split[1]), int(time_split[2]))
	data_arr.append(date_time)

#	date_111 = TDatime(2020, 11, 12, 0, 0, 0)




for x in range(np.size(run_number)):
	gr_21.SetPoint(x, data_arr[x].Convert(), float(ratio_21[x]))
	gr_23.SetPoint(x, data_arr[x].Convert(), float(ratio_23[x]))
	gr_13.SetPoint(x, data_arr[x].Convert(), float(ratio_13[x]))
	gr_pressure.SetPoint(x, data_arr[x].Convert(), float(pressure[x]))


c1.cd()

gr_13.SetMarkerStyle(20);
gr_21.SetMarkerStyle(21);
gr_23.SetMarkerStyle(22);
gr_pressure.SetMarkerStyle(4);

gr_21.SetMarkerColor(2);
gr_23.SetMarkerColor(3);

gr_13.GetHistogram().SetMaximum(1.5);
gr_13.GetHistogram().SetMinimum(0);
  	
gr_13.SetTitle("North Upper Box LED Signal Ratio");

gr_13.Draw("Ap")
gr_13.GetXaxis().SetTimeDisplay(1);
gr_13.GetXaxis().SetNdivisions(510);
gr_13.GetXaxis().SetTimeFormat("#splitline{%m-%d}{%H:%M}");

gr_13.SetName("gr_13")
gr_21.SetName("gr_21")
gr_23.SetName("gr_23")

gr_21.Draw("psame");
gr_23.Draw("psame");




c1.Update();


c2.cd()

pres_min=98
pres_max=105

gr_pressure.GetHistogram().SetMaximum(pres_max);
gr_pressure.GetHistogram().SetMinimum(pres_min);

gr_pressure.Draw("ap");
gr_pressure.GetXaxis().SetTimeDisplay(1);
gr_pressure.GetXaxis().SetNdivisions(510);
gr_pressure.GetXaxis().SetTimeFormat("#splitline{%m-%d}{%H:%M}");


c2.Update();


c1.cd()

gr_pressure.SetName("gr_pres");

#rightmax = 1.1*gr_pressure.GetHistogram().GetMaximum()
scale = (gr_pressure.GetHistogram().GetMaximum() - gr_pressure.GetHistogram().GetMinimum())/gr_13.GetHistogram().GetMaximum()

#print gPad.GetUymax(), rightmax

gr_pressure.SetMarkerColor(6)
for x in range(np.size(run_number)):
	gr_pressure.GetY()[x] = (gr_pressure.GetY()[x] - 98)/scale
	print gr_pressure.GetY()[x], scale

gr_pressure.Draw("p")

axis = TGaxis(gPad.GetUxmax(),gPad.GetUymin(), gPad.GetUxmax(), gPad.GetUymax(), pres_min,pres_max,510,"+L");
axis.SetLineColor(2);
axis.SetTextColor(2);
axis.Draw();



legend = TLegend(0.1,0.7,0.48,0.9);
legend.AddEntry("gr_13","LED 1/LED 3 Ratio","p");
legend.AddEntry("gr_21","LED 2/LED 1 Ratio","p");
legend.AddEntry("gr_23","LED 2/LED 3 Ratio","p");
legend.AddEntry("gr_pres", "CDC Gas Pressure","p");
legend.Draw();

c1.Update()



TPython.Prompt()

