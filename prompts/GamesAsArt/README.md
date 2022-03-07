# Notes

The completions passing the screening are collected in the spreadsheets AllGames_xlsx and AllGames_thinking.xlsx. 

The file names starting with DISCARDED were discarded according to the criteria reported in the methods section.

There were initially three completions that should have been discarded automatically according to our a priori plans, but the games_as_art.py script did not initially catch. These files contained sequences of more than 10 characters repeated at least 2 times consecutively. As was reported in the methods section, we discarded these files and did not consider them for annotation.

The repetitions were checked from all completions with the script GamesAsArt_check_repetitions.py. We found three that did not fulfill the criteria. Thus, we generated new completions to replace these three (these can be found from spreadsheet AllGames_thinking_3extra). The completions containing the repetitions were marked as discarded. 


