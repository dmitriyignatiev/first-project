
def main():
    import csv
    # import dates from CSV file into list with dicts

    with open('c://Python/soccer_players.csv') as csvfile:
        my_file = csv.DictReader(csvfile)
        player_list = list(my_file)
        #print(player_list)

    # create 3 teams, each company - the list with the dicts

    Dragons = []
    Sharks = []
    Raptors = []

    # Create a logic which divide players into 3 teams

    for players in player_list:
        if players['Soccer Experience'] == 'YES': # Choose players who has a practice
           if len(Dragons)< 3:
               Dragons.append(players)
           if len(Sharks)<3 and players not in Dragons:
               Sharks.append(players)
           if  players not in Dragons and players not in Sharks:
               Raptors.append(players)

    for players in player_list:
        if players['Soccer Experience'] == 'NO': # Choose players who hasn't any practice
            if len(Dragons) < 6:
                Dragons.append(players)
            if len(Sharks) < 6 and players not in Dragons:
                Sharks.append(players)
            if players not in Dragons and players not in Sharks:
                Raptors.append(players)

    # create additional dict for each team with information of first day of practice

    start_date_Dragon = {'date': 'March 17, 1 pm', 'team': 'Dragon'}
    start_date_Sharks = {'date': 'March 17, 3 pm', 'team': 'Sharks'}
    start_date_Raptors = {'date': 'March 18, 1 pm', 'team': 'Raptors'}

    # Adding dict start_date(Dragon, Sharks, Raptors) for each list with the dict

    for item in Dragons:
        item.update(start_date_Dragon)

    for item in Sharks:
        item.update(start_date_Sharks)

    for item in Raptors:
        item.update(start_date_Raptors)

    # just for checking is everything is correct print below
    print(Dragons)
    print(Sharks)
    print(Raptors)

    # create 6 files for letters for each player in Dragons team
    file_Dragons = ["joe_smith.txt", "jill_tanner.txt", "bill_bon.txt",
                           "eva_gordon.txt", "matt_gill.txt", "kimmy_stein.txt"]

    #create 6 files for letters for each player in Sharks team
    file_Sharks = ["karl_saygan.txt", "suzane_greenberg.txt", "diego_soto.txt",
                         "letter_10.txt", "sammy_adams.txt", "joe_kavalier.txt"]

    #create 6 file for letter for each players in Raptors team
    file_Raptors = ["phillip_helm.txt", "les_clay.txt", "herschel_krustofski.txt",
                          "ben_finkelstein.txt", "chloe_alaska.txt", "arnold_willis.txt"]



    # create list with sentences for each player for Dragon, Sharks, Raptors team
    sentences_list_Dragons = []
    sentences_list_Sharks = []
    sentences_list_Raptors = []

    # create dict for Dragons players  to perform sentense for each player using {}.format
    dict_for__Dragons = {}
    for players in Dragons:
            dict_for__Dragons = players
            letter_for_Dragons = "Dear's {Guardian Name(s)} my name is {Name}, my team is {team} first start day is {date}".format(**dict_for__Dragons )
            sentences_list_Dragons.append(letter_for_Dragons)

    # create dict for Sharks players  to perform sentense for each player using {}.format
    dict_for_Sharks = {}
    for players in Sharks:
            dict_for__Sharks = players
            letter_for_Sharks = "Dear's {Guardian Name(s)} my name is {Name}, my team is {team} first start day is {date}".format(**dict_for__Sharks )
            sentences_list_Sharks.append(letter_for_Sharks)

    # create dict for Sharks players  to perform sentense for each player using {}.format
    dict_for_Raptors = {}
    for players in Raptors:
            dict_for__Raptors = players
            letter_for_Raptors = "Dear's {Guardian Name(s)} my name is {Name}, my team is {team} first start day is {date}".format(**dict_for__Raptors)
            sentences_list_Raptors.append(letter_for_Raptors)


    #just for checking print(sentences)
    print(sentences_list_Dragons)
    print(sentences_list_Sharks)
    print(sentences_list_Raptors)

    # Create and writing files  with sentences for each player for each team

    for sentences, file in zip(sentences_list_Dragons, file_Dragons):
        with open(file, "w") as output:
            output.write(sentences + '\n')

    for sentences, file in zip(sentences_list_Sharks, file_Sharks):
        with open(file, "w") as output:
            output.write(sentences + '\n')

    for sentences, file in zip(sentences_list_Raptors, file_Raptors):
        with open(file, "w") as output:
            output.write(sentences + '\n')
if __name__ == '__main__':
    main()