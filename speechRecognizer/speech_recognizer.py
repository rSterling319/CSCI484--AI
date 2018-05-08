#!/usr/bin/env python3

#Training Dataset:
#http://download.tensorflow.org/data/speech_commands_v0.01.tar.gz
#Citation for dataset:
#"Warden P. Speech Commands: A public dataset for single-word speech recognition, 2017. Available from http://download.tensorflow.org/data/speech_commands_v0.01.tar.gz".


import os
import argparse
import warnings
import random

import time

import pickle


import numpy as np
from scipy.io import wavfile

from hmmlearn import hmm
warnings.filterwarnings("ignore", category=DeprecationWarning)
from python_speech_features import mfcc

outFile = "results.txt"
out = open(outFile, 'a')

#define function to parse input args
def build_arg_parser():
    parser = argparse.ArgumentParser(description='Trains the HMM-based speech \ recognition system')
    parser.add_argument("--input-folder",dest="input_folder",required=True, help="Input folder containing the audio files for training")
    return parser

#define a class to train the HMM (Hidden Markov Models)
class ModelHMM(object):
    def __init__(self, num_components=4, num_iter=1000):
        self.n_components = num_components
        self.n_iter = num_iter
        self.cov_type = 'diag'
        self.model_name = 'GaussianHMM'
        self.models=[]
        self.model = hmm.GaussianHMM(n_components=self.n_components,covariance_type=self.cov_type, n_iter=self.n_iter)

    #method to train model
    def train(self, training_data):
        np.seterr(all='ignore')
        cur_model=self.model.fit(training_data)
        self.models.append(cur_model)

    #methond to compute score for input data
    def compute_score(self, input_data):
        return self.model.score(input_data)

#function to build a model for each word
def build_models(input_folder):
    #init the variable to store all the models
    speech_models=[]

    #parse the input directory
    for dirname in os.listdir(input_folder):
        #get name of the subfolder
        subfolder = os.path.join(input_folder, dirname)
        if not os.path.isdir(subfolder):
            continue

        #extract the label
        label = subfolder[subfolder.rfind('/')+1:]
        
        #init the variables
        X = np.array([])

        #create a list of files to be used for training
        training_files = [x for x in os.listdir(subfolder) if x.endswith('.wav')]

        #Comment to use all
        # try:
        #     training_files = random.sample(training_files, 1000)#chose n files from each to speed things up
        # except ValueError: #if the sample size is bigger than array continue
        #     continue

        #iterate throught the training files and build the models
        for filename in training_files:
            #extract the current filepath
            filepath = os.path.join(subfolder, filename)
            #read the audio signal from the input file
            sampling_freq, signal = wavfile.read(filepath)
            #extract the mfcc features
            with warnings.catch_warnings():
                warnings.simplefilter('ignore')
                features_mfcc = mfcc(signal, sampling_freq)
            #append to var X
            if len(X)==0:
                X = features_mfcc
            else:
                X = np.append(X, features_mfcc, axis=0)
        #create the hmm model
        model = ModelHMM()
        #train the hmm
        model.train(X)
        #save the model for the current word
        speech_models.append((model, label))

        #reset the variable
        model = None

    return speech_models

#Define a function to run tests on input files
def run_tests(test_files):
    #classify input data
    for test_file in test_files:
        #read input files:
        sampling_freq, signal = wavfile.read(test_file)
        #extract mfcc features (Mel Frequency Cepstral Coefficients)
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            features_mfcc = mfcc(signal, sampling_freq)
        #define vars
        max_score = -float('inf')
        output_label = None
        #run the current feature vector through all the hmm models and pick the one with highest score
        allScores =[]
        # print(speech_models[0])

        for item in speech_models:
            model, label = item
            score = model.compute_score(features_mfcc)
            allScores.append((score,label))
            # print(score, label)
            if score > max_score:
                max_score = score
                predicted_label = label
        #sort all the scores
        allScores = sorted(allScores, key=lambda x: (-x[0], x[1]))
        #print top five results
        out.write("Top Five results:\n")
        for i, pair in enumerate(allScores[:5]):
            out.write("%d) %.5f %s\n"%(i, pair[0], pair[1]))

        #print the predicted output
        start_index = test_file.find('/')+1
        end_index = test_file.rfind('/')
        original_label = test_file[start_index:test_file.rfind('.')]
        actual=None
        for i, x in enumerate(allScores):

            if x[1] == original_label[:original_label.rfind('/')]:
                actual =(i,x)
        # try:
        out.write("%s %.5f\n" %(str(actual), allScores[0][0]))
        # except IndexError:
            # out.write("%s  %s" %("Something went wrong with allScores", str(allScores)))
        # try:
        out.write("\nScore off by: %f\n" %(actual[1][0]- allScores[0][0]))
        out.write("Words off by: %d\n" % actual[0])
        # except TypeError:
            # out.write("\nScore off by: %s\n" %("TypeError: something went wrong"))
            # out.write("Words off by: %s %s\n" %("TypeError: Something went wrong:", str(actual)))
        if actual == 0:
            out.write("Correct\n")
        else:
            out.write("Incorrect\n")
        out.write('\nOriginal: %s\n' % original_label)
        out.write('Predicted: %s\n'  %predicted_label)

def printline(ch):
    out.write("%s\n" %(ch*50))

if __name__ == '__main__':
    args = build_arg_parser().parse_args()
    input_folder=args.input_folder



    start = time.time()
    #build on hmm model for each word
    speech_models = build_models(input_folder)
    #pickle.dump(speech_models, open("pickled.sav", "wb"))

    #test files
    test_files = []

    word = None
    while word is '_background_noise_' or word is '.DS_Store' or word is 'fruits' or word is None:
        word = random.choice(os.listdir('data'))
        print(word)
    filepath = random.choice(os.listdir('data/'+word))
    filepath = 'data/'+word+'/'+filepath
    printline('=')
    out.write("Test Word: %s\nFilepath: %s\nTraining Set Size: %s\n" %(word,filepath, "2000+"))
    printline('-')

    test_files.append(filepath)

    run_tests(test_files)
    end = time.time()
    elapsed = end-start
    out.write("hours: %d\nmin:%d\nsec:%d\n" %(elapsed/3600, elapsed/60, elapsed%60))
    # print(word)
    printline('+')