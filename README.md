# Election-Analysis

## Overview
   The Colorado Board of Elections entrusted us with the audit and analysis of their congressional elections. We perfmored the audit with Python assisted programming

## Analysis
County Votes:
- Jefferson: 10.5% (38855)
- Denver: 82.8% (306055)
- Arapahoe: 6.7% (24801)

Candidate Results:
- Charles Casper Stockham received 23.0% of the vote(85,213)
- Diana DeGette received 73.8%  of the vote (272,892)
- Raymon Anthony Doan received 3.1% of the vote (11,606)

In total, 369,711 votes had been cast.

The winner is Dianna Degette, with a commanding 73.8% of the popular vote.

We found these results through a combination of iterating for loops using lists and dictionaries for both the counties and candidates.

    for county_name in county_options:

        # Retrieve the county vote count.
        cvotes = county_votes.get(county_name)

        # Calculate the percentage of votes for the county.
        cvote_percentage = float(cvotes) / float(total_votes) * 100
        
         # Print the county results 
        county_results = f"{county_name}: {cvote_percentage:.1f}% ({cvotes})\n"

        print(county_results)
         
        # Save the county votes to a text file.
        txt_file.write(county_results)

         # Determine the winning county and get its vote count.
        if (cvotes > highest_vote) and (cvote_percentage > highest_percentage):
            highest_vote = cvotes
            highest_percentage = cvote_percentage
            highest_county = county_name
 
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

## Summary

By looping through the data this way we are able to quickly count votes for both the candidates and the counties to get the data we need to perform out analysis. This loop can be used for any future elections by simply changing the variables to match the description of the data. The name retrieval function is not limited to 3 places. The code will simply count each vote individually based on the data point we choose. We can reuse this code to anlayse many different voting categories.

## Resources
- Data Source: election_results.csv
- Software: Python, Visual Studio Code
