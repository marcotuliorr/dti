import csv
from wiki_survey_entry import *

def readDataFromFile():
    with open('data/wiki4HE.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        # Skip header.
        next(reader)
        wiki_entries = []
        for raw_row in reader:
            # Cast digits to int and replace '?'s with None.
            row = [int(c) if c.isdigit() else None for c in raw_row]
            data = [
                Professor(*row[0:10]),
                Usefulness(*row[10:13]),
                EaseOfUse(*row[13:16]),
                Enjoyment(*row[16:18]),
                Quality(*row[18:23]),
                Visibility(*row[23:26]),
                SocialImage(*row[26:29]),
                SharingAttitude(*row[29:32]),
                UseBehaviour(*row[32:37]),
                Profile(*row[37:40]),
                JobRelevance(*row[40:42]),
                BehavioralIntention(*row[42:44]),
                Incentives(*row[44:48]),
                Experience(*row[48:53]),
            ]
            data_dict = {type(e).__name__: e for e in data}
            wiki_entry = WikiSurveyEntry(**data_dict)
            wiki_entries.append(wiki_entry)
        return wiki_entries

def main():
    entries = readDataFromFile()
    

if __name__ == '__main__':
    main()
