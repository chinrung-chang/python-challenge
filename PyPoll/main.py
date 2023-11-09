import csv


#total votes
total_votes = 0
#dictionary to store candidate's votes
votes_by_candidate = {}
#dictionary to store candidate's summary info (condidates's votes and percentage)
summary_by_candidate = {}

# read csv file
csvpath = './Resources/election_data.csv'
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
       
    # Read each row of data after the header
    for row in csvreader:           
        total_votes = total_votes + 1
        #get candidate's name
        candidate = row[2]        
        # if find the candidate's name in the dictionary votes_by_candidate, increment the total votes, else start from 1
        if (votes_by_candidate.get(candidate, None) != None):
            votes_by_candidate[candidate]= votes_by_candidate.get(candidate) + 1            
        else:
            votes_by_candidate[candidate] = 1    

#store votes and percentage(candidate's votes divide total votes)
for key in votes_by_candidate:
  summary_by_candidate[key] = {"votes": votes_by_candidate[key], "pct": round(votes_by_candidate[key]/total_votes, 5) }

#use max function to get the key with max votes in the dictionary
winner  = max(votes_by_candidate, key=votes_by_candidate.get)

#put the output by lines in a list
outputLines = [
    "Election Results",
    "-------------------------",
    f"Total Votes: {total_votes}",
    "-------------------------"]
for key, value in summary_by_candidate.items():
    outputLines.append(f"{key}: {value['pct']:.3%} ({value['votes']})")

outputLines.append("-------------------------")
outputLines.append(f"Winner:{winner}")
outputLines.append("-------------------------")

#print the list
for line in outputLines:
    print(line + "\n")

# output the list to output.txt in sub folder analysis
outputPath = './analysis/output.txt'
with open(outputPath, 'w') as f:
    for line in outputLines:
        f.write(line + "\n")    


