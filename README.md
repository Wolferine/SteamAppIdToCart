# steamAppToCart

1. extractAllVisibleAppIdsFromSearch.js extracts all links currently shown games from https://store.steampowered.com/search/ (data mine tool to get app id). 
Simply run in browser console and copy

2. convertAppidToSubid.py converts an in.txt file to out.txt file (in.txt format is one id each line)

3. createJsCommands.py makes copy paste ready js commands to paste on steam store page with at least one dlc (will add them to cart but its only way i found to bulk add steam game)