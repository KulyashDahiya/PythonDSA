def avrg(lst, n):
    sum = 0
    for i in range(n):
        sum += lst[i]
    return sum/n

lst1 = []
n = int(input("Enter number of Elements in lst: "))
print('Enter Values:')
for i in range(n):
    ele = int(input())
    lst1.append(ele)
print('Average is {}', avrg(lst1, n))










# winners = {1931: ['Norman Taurog'], 1932: ['Frank Borzage'], 1933: ['Frank Lloyd'], 1934: ['Frank Capra'], 1935: ['John Ford'], 1936: ['Frank Capra'], 1937: ['Leo McCarey'], 1938: ['Frank Capra'], 1939: ['Victor Fleming'], 1940: ['John Ford'], 1941: ['John Ford'], 1942: ['William Wyler'], 1943: ['Michael Curtiz'], 1944: ['Leo McCarey'], 1945: ['Billy Wilder'], 1946: ['William Wyler'], 1947: ['Elia Kazan'], 1948: ['John Huston'], 1949: ['Joseph L. Mankiewicz'], 1950: ['Joseph L. Mankiewicz'], 1951: ['George Stevens'], 1952: ['John Ford'], 1953: ['Fred Zinnemann'], 1954: ['Elia Kazan'], 1955: ['Delbert Mann'], 1956: ['George Stevens'], 1957: ['David Lean'], 1958: ['Vincente Minnelli'], 1959: ['William Wyler'], 1960: ['Billy Wilder'], 1961: ['Jerome Robbins', 'Robert Wise'], 1962: ['David Lean'], 1963: ['Tony Richardson'], 1964: ['George Cukor'], 1965: ['Robert Wise'], 1966: ['Fred Zinnemann'], 1967: ['Mike Nichols'], 1968: ['Carol Reed'], 1969: ['John Schlesinger'], 1970: ['Franklin J. Schaffner'], 1971: ['William Friedkin'], 1972: ['Bob Fosse'], 1973: ['George Roy Hill'], 1974: ['Francis Ford Coppola'], 1975: ['Milos Forman'], 1976: ['John G. Avildsen'], 1977: ['Woody Allen'], 1978: ['Michael Cimino'], 1979: ['Robert Benton'], 1980: ['Robert Redford'], 1981: ['Warren Beatty'], 1982: ['Richard Attenborough'], 1983: ['James L. Brooks'], 1984: ['Milos Forman'], 1985: ['Sydney Pollack'], 1986: ['Oliver Stone'], 1987: ['Bernardo Bertolucci'], 1988: ['Barry Levinson'], 1989: ['Oliver Stone'], 1990: ['Kevin Costner'], 1991: ['Jonathan Demme'], 1992: ['Clint Eastwood'], 1993: ['Steven Spielberg'], 1994: ['Robert Zemeckis'], 1995: ['Mel Gibson'], 1996: ['Anthony Minghella'], 1997: ['James Cameron'], 1998: ['Steven Spielberg'], 1999: ['Sam Mendes'], 2000: ['Steven Soderbergh'], 2001: ['Ron Howard'], 2002: ['Roman Polanski'], 2003: ['Peter Jackson'], 2004: ['Clint Eastwood'], 2005: ['Ang Lee'], 2006: ['Martin Scorsese'], 2007: ['Ethan Coen', 'Joel Coen'], 2008: ['Danny Boyle'], 2009: ['Kathryn Bigelow'], 2010: ['Tom Hooper']}
#
# ### For Question 2: Please provide a list with the name(s) of the director(s) with
# ### the most Oscar wins. The list can hold the names of multiple directors,
# ### since there can be more than 1 director tied with the most Oscar wins.
#
# most_win_director = []
# # Add your code here
# win_count_dict = {}
# for year, winnerlist in winners.items():
#     for winner in winnerlist:
#         win_count_dict[winner] = win_count_dict.get(winner, 0) + 1
#
# # count = {}
# # for year, director_list in winners.items():
# #     for director in director_list:
# #         if director not in count:
# #             count[director] = 1
# #         else:
# #             count[director] += 1
#
# ## METHOD 1
# # highest_count = 0
# # for key, value in win_count_dict.items():
# #     if value > highest_count:
# #         highest_count = value
# #         most_win_director.clear()
# #         most_win_director.append(key)
# #     elif value == highest_count:
# #         most_win_director.append(key)
# #     else:
# #         continue
#
# ## METHOD 2
# # max_val = 0
# # for key in count.keys():
# #     if count[key] > max_val:
# #         max_val = count[key]
# #
# # for key in count.keys():
# #     if count[key] == max_val:
# #         most_win_director.append(key)
#
# ## METHOD 3
# highest_count = max(win_count_dict.values())
# most_win_director = [key for key, value in win_count_dict.items() if value == highest_count]
#
# print("most_win_director = {}".format(most_win_director))













# nominated = {1931: ['Norman Taurog', 'Wesley Ruggles', 'Clarence Brown', 'Lewis Milestone', 'Josef Von Sternberg'], 1932: ['Frank Borzage', 'King Vidor', 'Josef Von Sternberg'], 1933: ['Frank Lloyd', 'Frank Capra', 'George Cukor'], 1934: ['Frank Capra', 'Victor Schertzinger', 'W. S. Van Dyke'], 1935: ['John Ford', 'Michael Curtiz', 'Henry Hathaway', 'Frank Lloyd'], 1936: ['Frank Capra', 'William Wyler', 'Robert Z. Leonard', 'Gregory La Cava', 'W. S. Van Dyke'], 1937: ['Leo McCarey', 'Sidney Franklin', 'William Dieterle', 'Gregory La Cava', 'William Wellman'], 1938: ['Frank Capra', 'Michael Curtiz', 'Norman Taurog', 'King Vidor', 'Michael Curtiz'], 1939: ['Sam Wood', 'Frank Capra', 'John Ford', 'William Wyler', 'Victor Fleming'], 1940: ['John Ford', 'Sam Wood', 'William Wyler', 'George Cukor', 'Alfred Hitchcock'], 1941: ['John Ford', 'Orson Welles', 'Alexander Hall', 'William Wyler', 'Howard Hawks'], 1942: ['Sam Wood', 'Mervyn LeRoy', 'John Farrow', 'Michael Curtiz', 'William Wyler'], 1943: ['Michael Curtiz', 'Ernst Lubitsch', 'Clarence Brown', 'George Stevens', 'Henry King'], 1944: ['Leo McCarey', 'Billy Wilder', 'Otto Preminger', 'Alfred Hitchcock', 'Henry King'], 1945: ['Billy Wilder', 'Leo McCarey', 'Clarence Brown', 'Jean Renoir', 'Alfred Hitchcock'], 1946: ['David Lean', 'Frank Capra', 'Robert Siodmak', 'Clarence Brown', 'William Wyler'], 1947: ['Elia Kazan', 'Henry Koster', 'Edward Dmytryk', 'George Cukor', 'David Lean'], 1948: ['John Huston', 'Laurence Olivier', 'Jean Negulesco', 'Fred Zinnemann', 'Anatole Litvak'], 1949: ['Joseph L. Mankiewicz', 'Robert Rossen', 'William A. Wellman', 'Carol Reed', 'William Wyler'], 1950: ['Joseph L. Mankiewicz', 'John Huston', 'George Cukor', 'Billy Wilder', 'Carol Reed'], 1951: ['George Stevens', 'John Huston', 'Vincente Minnelli', 'William Wyler', 'Elia Kazan'], 1952: ['John Ford', 'Joseph L. Mankiewicz', 'Cecil B. DeMille', 'Fred Zinnemann', 'John Huston'], 1953: ['Fred Zinnemann', 'Charles Walters', 'William Wyler', 'George Stevens', 'Billy Wilder'], 1954: ['Elia Kazan', 'George Seaton', 'William Wellman', 'Alfred Hitchcock', 'Billy Wilder'], 1955: ['Delbert Mann', 'John Sturges', 'Elia Kazan', 'Joshua Logan', 'David Lean'], 1956: ['George Stevens', 'Michael Anderson', 'William Wyler', 'Walter Lang', 'King Vidor'], 1957: ['David Lean', 'Mark Robson', 'Joshua Logan', 'Sidney Lumet', 'Billy Wilder'], 1958: ['Richard Brooks', 'Stanley Kramer', 'Robert Wise', 'Mark Robson', 'Vincente Minnelli'], 1959: ['George Stevens', 'Fred Zinnemann', 'Jack Clayton', 'Billy Wilder', 'William Wyler'], 1960: ['Billy Wilder', 'Jules Dassin', 'Alfred Hitchcock', 'Jack Cardiff', 'Fred Zinnemann'], 1961: ['J. Lee Thompson', 'Robert Rossen', 'Stanley Kramer', 'Federico Fellini', 'Robert Wise', 'Jerome Robbins'], 1962: ['David Lean', 'Frank Perry', 'Pietro Germi', 'Arthur Penn', 'Robert Mulligan'], 1963: ['Elia Kazan', 'Otto Preminger', 'Federico Fellini', 'Martin Ritt', 'Tony Richardson'], 1964: ['George Cukor', 'Peter Glenville', 'Stanley Kubrick', 'Robert Stevenson', 'Michael Cacoyannis'], 1965: ['William Wyler', 'John Schlesinger', 'David Lean', 'Hiroshi Teshigahara', 'Robert Wise'], 1966: ['Fred Zinnemann', 'Michelangelo Antonioni', 'Claude Lelouch', 'Richard Brooks', 'Mike Nichols'], 1967: ['Arthur Penn', 'Stanley Kramer', 'Richard Brooks', 'Norman Jewison', 'Mike Nichols'], 1968: ['Carol Reed', 'Gillo Pontecorvo', 'Anthony Harvey', 'Franco Zeffirelli', 'Stanley Kubrick'], 1969: ['John Schlesinger', 'Arthur Penn', 'George Roy Hill', 'Sydney Pollack', 'Costa-Gavras'], 1970: ['Franklin J. Schaffner', 'Federico Fellini', 'Arthur Hiller', 'Robert Altman', 'Ken Russell'], 1971: ['Stanley Kubrick', 'Norman Jewison', 'Peter Bogdanovich', 'John Schlesinger', 'William Friedkin'], 1972: ['Bob Fosse', 'John Boorman', 'Jan Troell', 'Francis Ford Coppola', 'Joseph L. Mankiewicz'], 1973: ['George Roy Hill', 'George Lucas', 'Ingmar Bergman', 'William Friedkin', 'Bernardo Bertolucci'], 1974: ['Francis Ford Coppola', 'Roman Polanski', 'Francois Truffaut', 'Bob Fosse', 'John Cassavetes'], 1975: ['Federico Fellini', 'Stanley Kubrick', 'Sidney Lumet', 'Robert Altman', 'Milos Forman'], 1976: ['Alan J. Pakula', 'Ingmar Bergman', 'Sidney Lumet', 'Lina Wertmuller', 'John G. Avildsen'], 1977: ['Steven Spielberg', 'Fred Zinnemann', 'George Lucas', 'Herbert Ross', 'Woody Allen'], 1978: ['Hal Ashby', 'Warren Beatty', 'Buck Henry', 'Woody Allen', 'Alan Parker', 'Michael Cimino'], 1979: ['Bob Fosse', 'Francis Coppola', 'Peter Yates', 'Edouard Molinaro', 'Robert Benton'], 1980: ['David Lynch', 'Martin Scorsese', 'Richard Rush', 'Roman Polanski', 'Robert Redford'], 1981: ['Louis Malle', 'Hugh Hudson', 'Mark Rydell', 'Steven Spielberg', 'Warren Beatty'], 1982: ['Wolfgang Petersen', 'Steven Spielberg', 'Sydney Pollack', 'Sidney Lumet', 'Richard Attenborough'], 1983: ['Peter Yates', 'Ingmar Bergman', 'Mike Nichols', 'Bruce Beresford', 'James L. Brooks'], 1984: ['Woody Allen', 'Roland Joffe', 'David Lean', 'Robert Benton', 'Milos Forman'], 1985: ['Hector Babenco', 'John Huston', 'Akira Kurosawa', 'Peter Weir', 'Sydney Pollack'], 1986: ['David Lynch', 'Woody Allen', 'Roland Joffe', 'James Ivory', 'Oliver Stone'], 1987: ['Bernardo Bertolucci', 'Adrian Lyne', 'John Boorman', 'Norman Jewison', 'Lasse Hallstrom'], 1988: ['Barry Levinson', 'Charles Crichton', 'Martin Scorsese', 'Alan Parker', 'Mike Nichols'], 1989: ['Woody Allen', 'Peter Weir', 'Kenneth Branagh', 'Jim Sheridan', 'Oliver Stone'], 1990: ['Francis Ford Coppola', 'Martin Scorsese', 'Stephen Frears', 'Barbet Schroeder', 'Kevin Costner'], 1991: ['John Singleton', 'Barry Levinson', 'Oliver Stone', 'Ridley Scott', 'Jonathan Demme'], 1992: ['Clint Eastwood', 'Neil Jordan', 'James Ivory', 'Robert Altman', 'Martin Brest'], 1993: ['Jim Sheridan', 'Jane Campion', 'James Ivory', 'Robert Altman', 'Steven Spielberg'], 1994: ['Woody Allen', 'Quentin Tarantino', 'Robert Redford', 'Krzysztof Kieslowski', 'Robert Zemeckis'], 1995: ['Chris Noonan', 'Tim Robbins', 'Mike Figgis', 'Michael Radford', 'Mel Gibson'], 1996: ['Anthony Minghella', 'Joel Coen', 'Milos Forman', 'Mike Leigh', 'Scott Hicks'], 1997: ['Peter Cattaneo', 'Gus Van Sant', 'Curtis Hanson', 'Atom Egoyan', 'James Cameron'], 1998: ['Roberto Benigni', 'John Madden', 'Terrence Malick', 'Peter Weir', 'Steven Spielberg'], 1999: ['Spike Jonze', 'Lasse Hallstrom', 'Michael Mann', 'M. Night Shyamalan', 'Sam Mendes'], 2000: ['Stephen Daldry', 'Ang Lee', 'Steven Soderbergh', 'Ridley Scott', 'Steven Soderbergh'], 2001: ['Ridley Scott', 'Robert Altman', 'Peter Jackson', 'David Lynch', 'Ron Howard'], 2002: ['Rob Marshall', 'Martin Scorsese', 'Stephen Daldry', 'Pedro Almodovar', 'Roman Polanski'], 2003: ['Fernando Meirelles', 'Sofia Coppola', 'Peter Weir', 'Clint Eastwood', 'Peter Jackson'], 2004: ['Martin Scorsese', 'Taylor Hackford', 'Alexander Payne', 'Mike Leigh', 'Clint Eastwood'], 2005: ['Ang Lee', 'Bennett Miller', 'Paul Haggis', 'George Clooney', 'Steven Spielberg'], 2006: ['Alejandro Gonzaalez Inarritu', 'Clint Eastwood', 'Stephen Frears', 'Paul Greengrass', 'Martin Scorsese'], 2007: ['Julian Schnabel', 'Jason Reitman', 'Tony Gilroy', 'Paul Thomas Anderson', 'Joel Coen', 'Ethan Coen'], 2008: ['David Fincher', 'Ron Howard', 'Gus Van Sant', 'Stephen Daldry', 'Danny Boyle'], 2009: ['James Cameron', 'Quentin Tarantino', 'Lee Daniels', 'Jason Reitman', 'Kathryn Bigelow'], 2010: ['Darren Aronofsky', 'David O. Russell', 'David Fincher', 'Ethan Coen', 'Joel Coen', 'Tom Hooper']}
# winners = {1931: ['Norman Taurog'], 1932: ['Frank Borzage'], 1933: ['Frank Lloyd'], 1934: ['Frank Capra'], 1935: ['John Ford'], 1936: ['Frank Capra'], 1937: ['Leo McCarey'], 1938: ['Frank Capra'], 1939: ['Victor Fleming'], 1940: ['John Ford'], 1941: ['John Ford'], 1942: ['William Wyler'], 1943: ['Michael Curtiz'], 1944: ['Leo McCarey'], 1945: ['Billy Wilder'], 1946: ['William Wyler'], 1947: ['Elia Kazan'], 1948: ['John Huston'], 1949: ['Joseph L. Mankiewicz'], 1950: ['Joseph L. Mankiewicz'], 1951: ['George Stevens'], 1952: ['John Ford'], 1953: ['Fred Zinnemann'], 1954: ['Elia Kazan'], 1955: ['Delbert Mann'], 1956: ['George Stevens'], 1957: ['David Lean'], 1958: ['Vincente Minnelli'], 1959: ['William Wyler'], 1960: ['Billy Wilder'], 1961: ['Jerome Robbins', 'Robert Wise'], 1962: ['David Lean'], 1963: ['Tony Richardson'], 1964: ['George Cukor'], 1965: ['Robert Wise'], 1966: ['Fred Zinnemann'], 1967: ['Mike Nichols'], 1968: ['Carol Reed'], 1969: ['John Schlesinger'], 1970: ['Franklin J. Schaffner'], 1971: ['William Friedkin'], 1972: ['Bob Fosse'], 1973: ['George Roy Hill'], 1974: ['Francis Ford Coppola'], 1975: ['Milos Forman'], 1976: ['John G. Avildsen'], 1977: ['Woody Allen'], 1978: ['Michael Cimino'], 1979: ['Robert Benton'], 1980: ['Robert Redford'], 1981: ['Warren Beatty'], 1982: ['Richard Attenborough'], 1983: ['James L. Brooks'], 1984: ['Milos Forman'], 1985: ['Sydney Pollack'], 1986: ['Oliver Stone'], 1987: ['Bernardo Bertolucci'], 1988: ['Barry Levinson'], 1989: ['Oliver Stone'], 1990: ['Kevin Costner'], 1991: ['Jonathan Demme'], 1992: ['Clint Eastwood'], 1993: ['Steven Spielberg'], 1994: ['Robert Zemeckis'], 1995: ['Mel Gibson'], 1996: ['Anthony Minghella'], 1997: ['James Cameron'], 1998: ['Steven Spielberg'], 1999: ['Sam Mendes'], 2000: ['Steven Soderbergh'], 2001: ['Ron Howard'], 2002: ['Roman Polanski'], 2003: ['Peter Jackson'], 2004: ['Clint Eastwood'], 2005: ['Ang Lee'], 2006: ['Martin Scorsese'], 2007: ['Ethan Coen', 'Joel Coen'], 2008: ['Danny Boyle'], 2009: ['Kathryn Bigelow'], 2010: ['Tom Hooper']}
#
# ### Question 1A: Create dictionary with the count of Oscar nominations for each director
# nom_count_dict = {}
# # Add your solution code below before line 10. Add more lines for your code as needed.
# for year, list_director in nominated.items():
#     for director in list_director:
#         if director not in nom_count_dict:
#             nom_count_dict[director] = 1
#         else:
#             nom_count_dict[director] += 1
#
# print("nom_count_dict = {}\n".format(nom_count_dict))
# ###################################################################################################################
#
# ### Question 1B: Create dictionary with the count of Oscar wins for each director
# win_count_dict = {}
# # Add your solution code below before line 20. Add more lines for your code as needed.
#
# ## METHOD 1
# for year, winner_list in winners.items():
#     for winner in winner_list:
#         win_count_dict[winner] = win_count_dict.get(winner, 0) + 1
#
# ## METHOD 2
# # for year, winner_list in winners.items():
# #     for winner in winner_list:
# #         if winner not in win_count_dict:
# #             win_count_dict[winner] = 1
# #         else:
# #             win_count_dict[winner] += 1
# ## METHOD 3
# # for year, director in winners.items():
# #     if director[0] not in win_count_dict:
# #         win_count_dict[director[0]] = 1
# #     else:
# #         win_count_dict[director[0]] += 1
#
# print("win_count_dict = {}".format(win_count_dict))











# scores = {
#              "Rick Sanchez": 70,
#              "Morty Smith": 35,
#              "Summer Smith": 82,
#              "Jerry Smith": 23,
#              "Beth Smith": 98
#           }
#
# passed = [name for name in scores if scores[name] >= 65]
# print(passed)





# names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
#
# first_names = [name.split(' ')[0].lower() for name in names]
# print(first_names)









# cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
# heights = [72, 68, 72, 66, 76]
#
# # write your for loop here
# for i, char in enumerate(cast):
#     cast[i] = char + " " + str(heights[i])
#
# print(cast)








# cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))
#
# # define names and heights here
# names, heights = zip(*cast)
#
# print(names)
# print(heights)








# cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))
#
# # define names and heights here
# names, heights = zip(*cast)
#
# print(names)
# print(heights)









# x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
# y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
# z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
# labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]
#
# points = []
# # write your for loop here
# for point in zip(labels, x_coord, y_coord, z_coord):
#     points.append("{}: {}, {}, {}".format(*point))
#
# for point in points:
#     print(point)









# x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
# y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
# z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
# labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]
#
# points = {}
# points = dict(zip(labels, list(zip(x_coord, y_coord, z_coord))))
#
# for i in points :
#     print("{}: {}".format(i, points[i]))









# ## Your code should check if each number in the list is a prime number
# check_prime = [26, 39, 51, 53, 57, 79, 85]
#
# ## write your code here
# ## HINT: You can use the modulo operator to find a factor
# for item in check_prime:
#     for i in range(2, item):
#         if item%i == 0:
#             print("{} is NOT a prime number, because {} is a factor of {}".format(item, i, item))
#             break
#         elif i == item - 1:
#             print("{} is a prime number".format(item))








# # HINT: modify the headlines list to verify your loop works with different inputs
# headlines = ["Local Bear Eaten by Man",
#              "Legislature Announces New Laws",
#              "Peasant Discovers Violence Inherent in System",
#              "Cat Rescues Fireman Stuck in Tree",
#              "Brave Knight Runs Away",
#              "Papperbok Review: Totally Triffic"]
#
# news_ticker = ""
# # write your loop here
# for headline in headlines:
#     if len(news_ticker) >= 140:
#         print("Length is more than 140")
#         news_ticker = news_ticker[:140]
#         break
#     else:
#         news_ticker += headline + " "
#
# print(news_ticker, "\n", len(news_ticker))











# num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
# count, sum, i = 0, 0, 0
# odd_nums = []
#
# while count < 5 and i < len(num_list):
#     if num_list[i] % 2 == 1:
#         odd_nums.append(num_list[i])
#         sum += num_list[i]
#         count += 1
#     i += 1
#
# print(sum)
# print(odd_nums)









# limit, num = 40, 0
#
# while (num+1)**2 < limit:
#     num += 1
#
# nearest_square = num*num
# print(nearest_square)






# limit = 40
# squared, num = 1, 1
# # write your while loop here
# while squared < 40:
#     nearest_square = squared
#     squared = num * num
#     num += 1
#
# print(nearest_square)








# start_num = 0
# end_num = 21
# count_by = 2
#
# # write a condition to check that end_num is larger than start_num before looping
# # write a while loop that uses break_num as the ongoing number to
# #   check against end_num
#
# if start_num > end_num:
#     print("Oops! Looks like your start value is greater than the end value. Please try again.")
# else:
#     break_num = start_num
#     while break_num < end_num:
#         break_num += count_by
#
#     result = break_num
#
# print(result)







# start_num = 0
# end_num = 21
# count_by = 2
# break_num = 0
#
# # write a while loop that uses break_num as the ongoing number to
# #   check against end_num
# while start_num <= end_num:
#     break_num += 2
#     start_num += count_by
#
#
# print(break_num)








# # You would like to count the number of fruits in your basket.
# # In order to do this, you have the following dictionary and list of
# # fruits.  Use the dictionary and list to count the total number
# # of fruits and not_fruits.
#
# basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
# fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']
#
# #Iterate through the dictionary
# #if the key is in the list of fruits, add to fruit_count.
# #if the key is not in the list, then add to the not_fruit_count
#
# def countfruits():
#     sum = 0
#     for key, value in basket_items.items():
#         if key in fruits:
#             sum += value
#     return sum
#
# def not_fruitcount():
#     sum = 0
#     for key, value in basket_items.items():
#         if key not in fruits:
#             sum += value
#     return sum
#
#
# fruit_count = countfruits()
# not_fruit_count = not_fruitcount()
#
# print(fruit_count, not_fruit_count)




# basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
# fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']
#
#
# def count_fruits():
#     sum = 0
#     for key, value in basket_items.items():
#         if key in fruits:
#             sum += value
#     return sum
#
#
# result = count_fruits()
# print(result)



# cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]
#
# # def is_short(name):
# #     return len(name) < 10
#
# short_cities = list(filter(lambda x: len(x) < 10, cities))
# print(short_cities)




# numbers = [
#               [34, 63, 88, 71, 29],
#               [90, 78, 51, 27, 45],
#               [63, 37, 85, 46, 22],
#               [51, 22, 34, 11, 18]
#            ]
#
# # def mean(num_list):
# #     return sum(num_list) / len(num_list)
#
# averages = list(map(lambda x: sum(x)/ len(x), numbers))
# print(averages)



# print(list(range(0,-5)))



# items = ['first string', 'second string']
# html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
#                      # the characters that are after it in html_str are on the next line
#
# # write your code here
# for item in items:
#     html_str += "<li>{}</li>\n".format(item)
#
# # for i in range(len(items)):
# #     html_str = html_str + "<li>" + items[i] + "</li>\n"
#
# html_str += "</ul>"
# print(html_str)




# tokens = ['<greeting>', 'Hello World!', '</greeting>']
# count = 0
#
# # write your for loop here
# for token in tokens:
#     if token[0] == '<' and token[-1] == '>':
#         count += 1
#
# print(count)




# names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
#
# for name in names:
#     name = name.lower().replace(" ", "_")
#
# print(names)




# names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
# usernames = []
#
# # write your for loop here
# for name in names:
#     usernames.append(name.replace(" ", "_").lower())
#
# print(usernames)




# # write your function here
# def readable_timedelta(days):
#     weeks = days//7
#     remainder = days%7
#     return "{} week(s) and {} day(s).".format(weeks, remainder)
#
# # test your function
# print(readable_timedelta(10))




# # Write a for loop using range() to print out multiples of 5 up to 30 inclusive
# for i in range(1, 31):
#     if i%5 == 0:
#         print(i)
# # OR
# for i in range(5, 31, 5):
#     print(i)




# sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]
#
# # Write a for loop to print out each word in the sentence list, one word per line
# for word in sentence:
#     print(word)




# points = 150  # use this as input for your submission
#
# # establish the default prize value to None
# prize = None
#
# # use the points value to assign prizes to the correct prize names
# if points <= 50:
#     prize = "wooden rabbit"
# elif 151 <= points <= 180:
#     prize = "wafer-thin mint"
# else:
#     prize = "penguin"
#
# # use the truth value of prize to assign result to the correct prize
# if prize:
#     result = "Congratulations! You won a {}!".format(prize)
# else:
#     result = "Oh dear, no prize this time."
#
# print(result)




# sf_population, sf_area = 864816, 231.89
# rio_population, rio_area = 6453682, 486.5
#
# san_francisco_pop_density = sf_population/sf_area
# rio_de_janeiro_pop_density = rio_population/rio_area
#
# answer = san_francisco_pop_density > rio_de_janeiro_pop_density
# print(answer)
#
# mon_sales = "121"
# tues_sales = "105"
# wed_sales = "110"
# thurs_sales = "98"
# fri_sales = "95"
#
# total = int(mon_sales) + int(tues_sales) + int(wed_sales) + int(thurs_sales) + int(fri_sales)
