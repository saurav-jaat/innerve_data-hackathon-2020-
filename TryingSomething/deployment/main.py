import os
import sys
import pandas as pd
from pickle import load


if __name__ == "__main__":
	arguments = sys.argv
	if len(arguments) != 2:
		print('syntax: python main.py <from-to>')
		print('example: python main.py 151-1661')
	else:
		if '-' in arguments[1]:
			test = pd.DataFrame({'from-to': [arguments[1], ]})
			test.to_csv('test.csv')
			# Loading Features
			os.system('python featureGenerator.py')
			features = pd.read_csv('test_features.csv')
			print('features---')
			features.drop(['from-to', 'Unnamed: 0', 'userA_id', 'userB_id'], axis=1, inplace=True)
			#
			# Loading Model
			print('prediction---')
			model = load(open('model_DT.pkl', 'rb'))
			print(f'Compatibility: {model.predict(features)}')

			# Predicting Value
