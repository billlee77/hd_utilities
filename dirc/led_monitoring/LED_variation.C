
///*--------------------------------------------------*/
// North Box

void LED_north_variation(TString file_name){

	TFile *file1 = TFile::Open(file_name);

	TCanvas* c1 = new TCanvas();
	TH1I * north_led_timing = (TH1I*) file1->Get("DIRC_timing/Hit/NorthUpperBox/Hit_LEDRefTdcChannelTimeDiff");

	north_led_timing->Draw();
	
	TSpectrum* s = new TSpectrum();
	s->Search(north_led_timing, 1, "");
	
  	Double_t *mean;

	mean = s->GetPositionX();
  
	Int_t nfound =3;

    long long sizes = nfound;
    long long inds[10];  // need to have static size
    for(int k=0; k<nfound; k++) inds[k] = 0;
    TMath::Sort(sizes,mean,inds,kFALSE);
	

//     for(int j=0; j<nfound; j++) {
// 
//       cout<<mean[inds[j]] << "    " << 	north_led_timing->GetBinContent(north_led_timing->FindBin(mean[inds[j]])) <<endl;
//     }

	TString run_number(file_name(9,5));

	TString time_str = gSystem->GetFromPipe("python rcdb_info.py " + run_number);

	c1->Print(run_number + "_north.png");



//	cout << time_str << endl;	


 	cout << run_number << "   " << time_str << "    ";
 	cout << setprecision(7) << setw(8) << north_led_timing->GetBinContent(north_led_timing->FindBin(mean[inds[0]])) << "   ";
 	cout <<	setw(10) << north_led_timing->GetBinContent(north_led_timing->FindBin(mean[inds[1]])) << "   ";
 	cout <<	setw(10) << north_led_timing->GetBinContent(north_led_timing->FindBin(mean[inds[2]])) << "   ";
 	cout << endl;
 
}

///*--------------------------------------------------*/
// South Box

void LED_south_variation(TString file_name){

	TFile *file1 = TFile::Open(file_name);

	TCanvas* c1 = new TCanvas();
	TH1I * north_led_timing = (TH1I*) file1->Get("DIRC_timing/Hit/SouthLowerBox/Hit_LEDRefTdcChannelTimeDiff");

	north_led_timing->Draw();
	
	TSpectrum* s = new TSpectrum();
	s->Search(north_led_timing, 1, "");
	
  	Double_t *mean;

	mean = s->GetPositionX();
  
	Int_t nfound =3;

    long long sizes = nfound;
    long long inds[10];  // need to have static size
    for(int k=0; k<nfound; k++) inds[k] = 0;
    TMath::Sort(sizes,mean,inds,kFALSE);
    
    for(int j=0; j<nfound; j++) {

      cout<<mean[inds[j]] << "    " << 	north_led_timing->GetBinContent(north_led_timing->FindBin(mean[inds[j]])) <<endl;
    }

	TString run_number(file_name(9,5));

	c1->Print(run_number + "_south.png");

}



