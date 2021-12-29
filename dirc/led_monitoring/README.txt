* This is the readme for the DIRC LED monitoring

Author and contact: Wenliang (Bill) Li
Email: wenliang.billlee@gmail.com

* Purpose of this tool:
	- Produce the monitoring plots for the DIRC LED stability over time

* That is in this tool kit ?




* Name of the HD_recon branch and plugin information.

Branch information: https://github.com/JeffersonLab/halld_recon/tree/bill_dirc

(under https://github.com/JeffersonLab/halld_recon,  with branch name: bill_dirc )

Plugin name: DIRC_timing

Or see pfull path: https://github.com/JeffersonLab/halld_recon/tree/bill_dirc/src/plugins/Calibration/DIRC_timing


/*--------------------------------------------------*/
List of tool kit avaliable

ls_n_plot.sh : Initiating the entire plotting algorithm
LED_variantion.C : Main plotting algorithm
rcdb_info.py : Getting the RCDB information
read.py : For ploting the extracted information on the time scale (axis)
setup_file: contain setup files



/*--------------------------------------------------*/
Job submission script example:


     hd_utilities/dirc/led_monitoring/swif_job_script



/*--------------------------------------------------*/
Instruction:

Setting up the enviroment:

1. For the quik setup, and test  
$ cp set_file ~/ 
$ Source the source ~/setup_diffuser.csh

Important Note: for the custimized configuration going forward, one must build directory: ~/halld_my/halld_recon_diffuser, and modify ~/setup_file/version_diffuser.xml

# Copying over the example data.
	$ cp /work/halld2/billlee/monitoring/LED_test_dir/2020_summer_period_3/hd_root_Run07310*.root .
# In case the data link above doesn't work, try the following
	$ cp /u/group/halld/DIRC_LED_example_data/hd_root_Run07310*.root .

2. Step getting the picks and plotting information:

$ sh ls_n_plot.sh
After product: 1. series of diagnostic plots named "XXXXX_south.png" and "XXXXX_north.png"; 2. south_tmp and north_tmp, note that these files will be used as input for getting the monitoring plots.


3. $ python read.py south_tmp, for generating the monitoring plot 


