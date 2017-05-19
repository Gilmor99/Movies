import fresh_tomatoes_oscar
import media_oscar


""" Nominated for Best Movies """

la_la_land = media_oscar.Movie("La La Land",
                        "The story of Mia, an aspiring actress, and Sebastian, a dedicated jazz musician, struggling to make ends meet while pursuing their dreams in a city known for destroying hopes and breaking hearts.",
                        "http://t2.gstatic.com/images?q=tbn:ANd9GcRhFtgdSYQ89vUMjMJal2D8H39qBCkh9ptCEoZEsafOzkeQPTu2",
                        "https://youtu.be/Dwcbk808dQE",
                        "Damien Chazelle",
                        "December 9, 2016",
                        )
arrival = media_oscar.Movie("Arrival",
                            "When mysterious spacecrafts touch down across the globe, an elite team - lead by expert linguist Louise Banks - is brought together to investigate.",
                            "http://cdn3-www.comingsoon.net/assets/uploads/gallery/arrival/arrivalposter.jpg",
                            "https://youtu.be/wu8_5TGwr90",
                            "Denis Villeneuve",
                            "November 11, 2016",
                            )
lion = media_oscar.Movie("Lion",
                            "Five year old Saroo gets lost on a train which takes him thousands of miles across India, away from home and family. Saroo must learn to survive alone in Kolkata, before ultimately being adopted by an Australian couple. Twenty five years later, armed with only a handful of memories, his unwavering determination, he sets out to find his lost family and finally return to his first home.",
                            "http://t0.gstatic.com/images?q=tbn:ANd9GcTVuFTo4qf9v0c91rhTcSn25dsQygPhIRdivLe8Z1HdZNiPCj2F",
                            "https://youtu.be/lGSlfuOq7-s",
                            "Garth Davis",
                            "November 25, 2016",
                            )
hell_or_high_water = media_oscar.Movie("Hell or High Water",
                                        "Two brothers -- Toby, a straight-living, divorced father trying to make a better life for his son; and Tanner, a short-tempered ex-con with a loose trigger finger -- come together to rob branch after branch of the bank that is foreclosing on their family land. The hold-ups are part of a last-ditch scheme to take back a future that powerful forces beyond their control have stolen from under their feet",
                                        "http://t1.gstatic.com/images?q=tbn:ANd9GcRYPGO1eXsOXccVk-YmuR5XBUsr9Cjf7PrrAdc-KngRAptlynNl",
                                        "https://youtu.be/Wi25oqajc3A",
                                        "David Mackenzie",
                                        "August 12, 2016",
                                        )
hidden_figures = media_oscar.Movie("HIDDEN FIGURES ",
                                    "The incredible untold story of Katherine G. Johnson, Dorothy Vaughan and Mary Jackson - brilliant African-American women working at NASA, who served as the brains behind one of the greatest operations in history: the launch of astronaut John Glenn into orbit, a stunning achievement that restored the nation's confidence, turned around the Space Race, and galvanized the world. The visionary trio crossed all gender and race lines to inspire generations to dream big.",
                                    "http://t1.gstatic.com/images?q=tbn:ANd9GcRqU2FbN7Zp0ELl-sX4lO8XO0pTjpmdJcpos_fnP9wM9DQHYgFq",
                                    "https://youtu.be/WnZRw8juTsQ",
                                    "Theodore Melfi",
                                    "December 25, 2016",
                                    )
moonlight = media_oscar.Movie("Moonlight",
                                "At once a vital portrait of contemporary African American life and an intensely personal and poetic meditation on identity, family, friendship, and love, MOONLIGHT is a groundbreaking piece of cinema that reverberates with deep compassion and universal truths. Anchored by extraordinary performances from a tremendous ensemble cast, Barry Jenkins's staggering, singular vision is profoundly moving in its portrayal of the moments, people, and unknowable forces that shape our lives and make us who we are.",
                                "http://t3.gstatic.com/images?q=tbn:ANd9GcT53B_Wizqekgv5U9fetXZc_7FmMFzp5MpeEodcyTOiugrjV7iP",
                                "https://youtu.be/2gCc6kGpXdw",
                                "Barry Jenkins",
                                "October 21, 2016",
                                )
hacksaw_ridge = media_oscar.Movie("Hacksaw Ridge",
                                    "The extraordinary true story of conscientious objector Desmond T. Doss who saved 75 men in Okinawa, during the bloodiest battle of WWII, without firing a single shot. Believing that the war was just but killing was nevertheless wrong, he was the only American soldier in WWII to fight on the front lines without a weapon.",
                                    "http://t1.gstatic.com/images?q=tbn:ANd9GcQkB0TuKruaG_PylU3qlUC2BkFKj3R4aUgN2MMDkc7hmSXrPTsy",
                                    "https://youtu.be/5V-o9SBcSI4",
                                    "Mel Gibson",
                                    "November 2, 2016",
                                    )
manchester_by_the_sea = media_oscar.Movie("Manchester by the Sea",
                                    "Lee Chandler is a brooding, irritable loner who works as a handyman for a Boston apartment block. One damp winter day he gets a call summoning him to his hometown, north of the city. His brother's heart has given out suddenly, and he's been named guardian to his 16-year-old nephew. As if losing his only sibling and doubts about raising a teenager weren't enough, his return to the past re-opens an unspeakable tragedy.",
                                    "http://t3.gstatic.com/images?q=tbn:ANd9GcS5-FlTo1iYdLeCeTN09lbE6seUjxO1jksMN8y5dpz3vJdRgFig",
                                    "https://youtu.be/0rnBRkeByvY",
                                    "Kenneth Lonergan",
                                    "November 18, 2016",
                                    )
fences = media_oscar.Movie("Fences",
                            "Fences is the story of Troy Maxson, a mid-century Pittsburgh sanitation worker who once dreamed of a baseball career, but was too old when the major leagues began admitting black players. He tries to be a good husband and father, but his lost dream of glory eats at him, and causes him to make a decision that threatens to tear his family apart.",
                            "http://t0.gstatic.com/images?q=tbn:ANd9GcRt-j2EYdJQHgR4kf077h3lHPz_h6-JHBIDYv7v-sB1x5lD6rj6",
                            "https://youtu.be/RWIW9Jmoh90",
                            "Denzel Washington",
                            "December 25, 2016",
                            )

movies = [la_la_land, arrival, lion, hell_or_high_water, hidden_figures,
            moonlight, hacksaw_ridge, manchester_by_the_sea, fences]

fresh_tomatoes_oscar.open_movies_page(movies)
