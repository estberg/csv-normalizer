# CSV Normalization

## Environment set up
The only library used which is not included in python is pytz, which most people have installed. So, as long as you have python>3.7 and this library you should be able to run this script without any set up. However, I use conda for python
environment and dependency management. If you'd like to match my environment you can do the following:

Set up the environment with dependencies using conda:
```
conda env create -f environment.yml
conda activate csv-normalizer
```

You may need to set up permissions for the python script:
```
chmod +x normalizer.py
```

## Running the script
Run the script with:
```
./normalizer < {input file path} > {output file path}
```

Example:
```
./normalizer < sample-with-broken-utf8.csv > output.csv
```