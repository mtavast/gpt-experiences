#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 14:35:35 2021

"""
import openai
from gpt_psych import log_game

##################################################
#################### SETTINGS ####################
##################################################
openai.api_key = open("key.txt", "r").read() # To reproduce the code, you need to create a txt file with your openai key
start = 117
end = 119
engine = "davinci"
experiment_name = 'GamesAsArt'
logfile = f'{experiment_name}_{engine}.log'
thinkgame = False
#################################################

for i in range(end):
    if i >= start:                    # to keep track how many events have been created
        prompt=open("prompts/games_as_art.txt", "r").read()
        # Add "Participant: I'm thinking of the game"
        if thinkgame == True:
            prompt = prompt + " I'm thinking of the game"
        #query a completion
        response = openai.Completion.create(engine=engine, prompt=prompt, max_tokens=500,
                                            #these are the default OpenAI playground parameters
                                            temperature=0.7,
                                            top_p=1.0,
                                            frequency_penalty=0,
                                            presence_penalty=0,
                                            best_of=1)
        response=response["choices"][0]["text"]
        
        log_game(prompt, logfile, response)
        
        #trim the completion
        response2=response[0:response.find("Researcher:")]  #stop the response if the model started to create another question
        finalresponse=response[:response2.find("\n")]  #stop the response after a single paragraph
       
        NumOfWords = finalresponse.split()   # How many words in the final response
        # Discard responses with less than 10 words
        if len(NumOfWords) < 10:
            print('Less than 10 words: ', finalresponse)
            if thinkgame == True:
                with open(f'prompts/GamesAsArt/DISCARDED_thinking_game_{i}_{engine}.txt', mode='w') as f:
                    f.writelines(finalresponse) 
            else:
                with open(f'prompts/GamesAsArt/DISCARDED_game_{i}_{engine}.txt', mode='w') as f:
                    f.writelines(finalresponse) 
        else:
            print('Over 10 words:', finalresponse)
            if thinkgame == True:
                with open(f'prompts/GamesAsArt/thinking_game_{i}_{engine}.txt', mode='w') as f:
                    f.writelines(finalresponse) 
            else:
                with open(f'prompts/GamesAsArt/game_{i}_{engine}.txt', mode='w') as f:
                    f.writelines(finalresponse) 
        