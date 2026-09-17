"""
games_books_6_10.py — Game books 6-10, 42+ pages each.
Reuses helpers from build_games_books.py.
"""

import workbook_games as g
from build_games_books import start, finish


# =====================================================================
# BOOK 6 — Animal Homes Matching Game (matching cards + worksheets)
# =====================================================================
def book6():
    toc = ["Animal Cards", "Home Cards", "Match Animal to Home",
           "Sort: Land, Water, Air", "Habitat Worksheets", "Answer Key", "Certificate"]
    wb = start("Animal Homes Matching Game",
               "Matching Cards and Worksheets for Science", "Ages 5-19", "Science",
               "Matching cards and worksheets", g.GREEN, g.SKY, toc,
               "Builds science knowledge about animals and habitats by matching each animal to the home "
               "where it lives, then sorting by habitat.")
    animals = [("Bee", "Animal"), ("Bird", "Animal"), ("Fish", "Animal"), ("Bear", "Animal"),
               ("Spider", "Animal"), ("Rabbit", "Animal"), ("Bat", "Animal"), ("Ant", "Animal"),
               ("Beaver", "Animal"), ("Fox", "Animal")]
    homes = [("Hive", "Home"), ("Nest", "Home"), ("Water / pond", "Home"), ("Cave / den", "Home"),
             ("Web", "Home"), ("Burrow", "Home"), ("Cave (roosting)", "Home"), ("Anthill", "Home"),
             ("Lodge / dam", "Home"), ("Den", "Home")]
    wb.divider("Part 1: Animal & Home Cards", "Cut them out and find each animal's home.")
    g.cut_out_cards(wb, "Cards", "Animal Cards (Set 1)", animals[:6], sub="Match to a home card.")
    g.cut_out_cards(wb, "Cards", "Animal Cards (Set 2)", animals[6:])
    g.cut_out_cards(wb, "Cards", "Home Cards (Set 1)", homes[:6], sub="Match to an animal card.")
    g.cut_out_cards(wb, "Cards", "Home Cards (Set 2)", homes[6:])
    g.draw_line_matching(wb, "Match", "Match Animal to Home (1)",
                         [a[0] for a in animals[:5]], [h[0] for h in homes[:5]],
                         "Draw a line from each animal to the home it lives in.")
    g.draw_line_matching(wb, "Match", "Match Animal to Home (2)",
                         [a[0] for a in animals[5:]], [h[0] for h in homes[5:]],
                         "Draw a line from each animal to the home it lives in.")
    g.discussion_sort(wb, "Sort", "Where Does It Live? Land, Water, or Air",
                      ["Land", "Water", "Air"],
                      ["Bear", "Fish", "Bird", "Beaver", "Bee", "Frog", "Whale", "Eagle"],
                      "Write 'L' land, 'W' water, or 'A' air. Some live in more than one!")
    p, y, nn = wb.page("Worksheet", "Habitat Worksheet")
    y = wb.intro_box(p, y, "A habitat is where an animal finds food, water, and shelter. For each animal, write "
                           "its home and one thing it needs to live. Older kids: name the habitat type.")
    for a in ["Fish:", "Bird:", "Bear:", "Bee:"]:
        p.set_fill(*wb.accent); p.text(g.MARGIN, y, a, 11.5, bold=True)
        y = wb.write_lines(p, y - 14, 2, spacing=24); y -= 8
        if y < 90: break
    answers = [("Bee", "Hive"), ("Bird", "Nest"), ("Fish", "Water/pond"), ("Bear", "Cave/den"),
               ("Spider", "Web"), ("Rabbit", "Burrow"), ("Ant", "Anthill"), ("Beaver", "Lodge/dam"),
               ("Fox", "Den")]
    return finish(wb, "06_Animal_Homes_Matching_Game.pdf",
                  "for matching animals to their homes!", answers=answers)


# =====================================================================
# BOOK 7 — Community Helpers Role-Play Kit (pretend-play cards)
# =====================================================================
def book7():
    toc = ["Meet the Helpers", "Role-Play Cards", "Tools of the Job Matching",
           "Who Would You Call?", "Pretend-Play Scenarios", "My Helper Journal", "Certificate"]
    wb = start("Community Helpers Role-Play Kit",
               "Pretend-Play Cards for Social Studies", "Ages 5-19", "Social studies",
               "Pretend-play cards", g.BLUE, g.SUN, toc,
               "Builds social-studies knowledge about the people who help our community, through "
               "pretend-play, matching jobs to tools, and knowing who to call for help.")
    wb.divider("Part 1: Community Helpers", "Meet the people who help us every day.")
    g.roleplay_cards(wb, "Role-Play", "Helper Role-Play Cards (Set 1)",
                     [("Doctor / Nurse", "Say: 'Let's check how you feel.' Help someone get better."),
                      ("Firefighter", "Say: 'Stay low and safe!' Put out the pretend fire."),
                      ("Police Officer", "Say: 'How can I help keep you safe?'"),
                      ("Teacher", "Say: 'Let's learn together!' Teach a lesson."),
                      ("Farmer", "Say: 'Time to grow our food.' Plant and harvest."),
                      ("Mail Carrier", "Say: 'Special delivery!' Deliver the letters.")],
                     "Cut out and act out each helper. Take turns being the helper and the person they help.")
    g.roleplay_cards(wb, "Role-Play", "Helper Role-Play Cards (Set 2)",
                     [("Chef", "Say: 'Order up!' Cook a pretend meal."),
                      ("Dentist", "Say: 'Let's keep those teeth healthy!'"),
                      ("Bus Driver", "Say: 'All aboard - buckle up!'"),
                      ("Vet", "Say: 'Let's help this animal feel better.'"),
                      ("Librarian", "Say: 'Let me help you find a book.'"),
                      ("Construction Worker", "Say: 'Hard hats on - let's build!'")],
                     "More helpers to act out. What does each one say and do?")
    g.draw_line_matching(wb, "Match", "Match the Helper to Their Tool",
                         ["Firefighter", "Doctor", "Chef", "Farmer", "Mail Carrier", "Construction Worker"],
                         ["hose", "stethoscope", "cooking pot", "tractor", "letters", "hard hat"],
                         "Draw a line from each helper to a tool they use.")
    g.scenario_match(wb, "Match", "Who Would You Call?",
                     [("There is a fire", "Firefighter"),
                      ("Someone is very sick", "Doctor / Nurse"),
                      ("A pet is hurt", "Vet"),
                      ("You want to learn to read", "Teacher / Librarian"),
                      ("You need a safe ride to school", "Bus Driver"),
                      ("A tooth hurts", "Dentist")],
                     "Situation", "Helper", "Match each situation to the helper who can help.")
    g.discussion_sort(wb, "Sort", "Where Do They Work?",
                      ["Hospital", "School", "Outdoors"],
                      ["Nurse", "Teacher", "Farmer", "Doctor", "Librarian", "Construction Worker"],
                      "Write where each helper usually works. Some can work in more than one place!")
    p, y, nn = wb.page("Journal", "My Community Helper")
    y = wb.intro_box(p, y, "Which helper would you like to be? Draw or write about it. Older kids: what training "
                           "or skills would you need?")
    y = wb.write_lines(p, y, 5, spacing=28)
    answers = [("Firefighter", "hose"), ("Doctor", "stethoscope"), ("Chef", "cooking pot"),
               ("Farmer", "tractor"), ("Fire", "Firefighter"), ("Sick", "Doctor/Nurse"), ("Hurt pet", "Vet")]
    return finish(wb, "07_Community_Helpers_Role-Play_Kit.pdf",
                  "for exploring the helpers in our community!", answers=answers)


# =====================================================================
# BOOK 8 — Kind or Unkind Words? (sorting and discussion game)
# =====================================================================
def book8():
    toc = ["Word Cards to Cut Out", "Kind vs. Unkind Sorting Mat", "Sort & Discuss",
           "Turn Unkind Into Kind", "What Would You Say?", "My Kind Words Journal", "Certificate"]
    wb = start("Kind or Unkind Words?",
               "A Sorting and Discussion Game for Social Skills", "Ages 5-19", "Social skills",
               "Sorting and discussion game", g.ROSE, g.MINT, toc,
               "Builds social skills by sorting words and phrases into kind and unkind, discussing how words "
               "affect others, and practicing kinder ways to speak.")
    kind = ["\"Great job!\"", "\"Can I help you?\"", "\"I'm sorry.\"", "\"You can play too.\"",
            "\"Thank you.\"", "\"I like your idea.\""]
    unkind = ["\"Go away!\"", "\"You're stupid.\"", "\"That's dumb.\"", "\"You can't play.\"",
              "\"I don't care.\"", "\"It's all your fault.\""]
    wb.divider("Part 1: Word Cards", "Cut out the word cards and sort them.")
    g.cut_out_cards(wb, "Cards", "Word Cards (Set 1)",
                    [(w, "Kind or unkind?") for w in kind], sub="Sort onto the kind/unkind mat.")
    g.cut_out_cards(wb, "Cards", "Word Cards (Set 2)",
                    [(w, "Kind or unkind?") for w in unkind])
    g.sorting_mat(wb, "Sort", "Sorting Mat: Kind vs. Unkind Words",
                  ["Kind Words", "Unkind Words"], "Sort your cut-out word cards into the two bins.",
                  items_hint="Use the word cards from the previous pages.")
    g.discussion_sort(wb, "Sort", "Sort & Discuss",
                      ["Kind", "Unkind"],
                      ["\"You did it!\"", "\"Nobody likes you.\"", "\"Want to share?\"",
                       "\"You're too slow.\"", "\"Let me help.\"", "\"That was silly of you.\""],
                      "Write 'K' or 'U'. Then talk: how would each word make someone feel?")
    p, y, nn = wb.page("Reframe", "Turn Unkind Into Kind")
    y = wb.intro_box(p, y, "Rewrite each unkind thing in a kind way. For older kids: talk about how to disagree "
                           "respectfully.")
    for u in ["Unkind: \"You can't sit here.\"   Kind: ______",
              "Unkind: \"That's a dumb drawing.\"   Kind: ______",
              "Unkind: \"Hurry up, you're too slow!\"   Kind: ______",
              "Unkind: \"Go away.\"   Kind: ______"]:
        p.set_fill(*g.INK); p.wrap_text(g.MARGIN, y, u, 11, g.CW, leading=14)
        y = wb.write_lines(p, y - 26, 1, spacing=22); y -= 8
        if y < 90: break
    g.scenario_match(wb, "Say It", "What Would You Say?",
                     [("A friend is new and feels shy", "\"Want to play with us?\""),
                      ("Someone drops their tray", "\"Let me help you.\""),
                      ("A classmate did well", "\"Great job!\""),
                      ("You bump into someone", "\"I'm sorry, are you okay?\""),
                      ("You disagree with an idea", "\"I see it differently - can I share?\""),
                      ("A friend is sad", "\"I'm here for you.\"")],
                     "Situation", "Kind words", "Match each situation to kind words you could say.")
    answers = [("Kind words", "Great job, Can I help, I'm sorry, You can play too, Thank you, I like your idea"),
               ("Unkind words", "Go away, You're stupid, That's dumb, You can't play, I don't care, It's your fault"),
               ("Reframe idea", "'You can't sit here' -> 'There's room over here for you'")]
    return finish(wb, "08_Kind_or_Unkind_Words.pdf",
                  "for choosing kind words!", answers=answers)


# =====================================================================
# BOOK 9 — Bible Story Bingo (30 bingo cards)
# =====================================================================
def book9():
    toc = ["How to Play Bingo", "The Call List", "30 Bingo Cards", "Story Clues to Call",
           "My Bingo Journal", "Certificate"]
    wb = start("Bible Story Bingo",
               "30 Printable Bingo Cards for Bible Recognition", "Ages 5-19", "Bible recognition",
               "30 bingo cards", g.PURPLE, g.GOLD, toc,
               "Builds Bible recognition through a fun bingo game - call out a character, story, or clue, and "
               "players mark the matching square.")
    words = ["Noah", "David", "Moses", "Jonah", "Ruth", "Esther", "Daniel", "Mary",
             "Peter", "Paul", "Joseph", "Abraham", "Sarah", "Adam", "Eve", "Joshua",
             "Samuel", "Solomon", "Elijah", "John", "Luke", "Mark", "Matthew", "Job",
             "Isaac", "Jacob", "Aaron", "Miriam", "Deborah", "Gideon"]
    # how to play
    p, y, n = wb.page("How to Play", "How to Play Bible Story Bingo")
    y = wb.paragraph(p, y, "Give each player a bingo card. A caller reads a name, story, or clue from the call "
                           "list. If a player has that square, they mark it. The first to complete a full row, "
                           "column, or diagonal calls out 'Bingo!' Play again for a full-card blackout.")
    y = wb.subhead(p, y, "Ways to play (any age)")
    wb.checklist(p, y, ["Younger: call out the character's NAME.",
                        "Middle: call a short STORY clue ('built the ark') - players find the name.",
                        "Older: call a VERSE reference and let players connect it to the character.",
                        "Cooperative: play as a team and celebrate every Bingo together."], box=False)
    # call list
    p2, y2, n2 = wb.page("Call List", "The Caller's List (Names & Clues)")
    y2 = wb.intro_box(p2, y2, "Cut this out for the caller. Read the name, or read the clue and let players find "
                              "the name on their card.")
    clues = {
        "Noah": "built the ark", "David": "faced Goliath", "Moses": "parted the sea",
        "Jonah": "the big fish", "Ruth": "loyal to Naomi", "Esther": "the brave queen",
        "Daniel": "the lions' den", "Mary": "mother of Jesus", "Peter": "walked on water",
        "Paul": "wrote many letters", "Joseph": "coat of many colors", "Abraham": "father of nations",
    }
    for name in words:
        clue = clues.get(name, "a person in the Bible")
        p2.set_fill(*wb.accent); p2.text(g.MARGIN, y2, "- ", 10, bold=True)
        p2.set_fill(*g.INK); p2.text(g.MARGIN + 14, y2, f"{name}  -  {clue}", 10.5)
        y2 -= 17
        if y2 < 60: break
    # 30 unique bingo cards
    wb.divider("Part 2: 30 Bingo Cards", "Print and hand out - each card is different.")
    for i in range(1, 31):
        g.bingo_card(wb, f"Bible Story Bingo  -  Card #{i}", words, size=5, seed=1000 + i)
    g.journal_page(wb, "Journal", "My Bingo Journal",
                   ["Which Bible character did you learn something new about?",
                    "What is your favorite Bible story from the game?"])
    return finish(wb, "09_Bible_Story_Bingo.pdf",
                  "for playing Bible Story Bingo!")


# =====================================================================
# BOOK 10 — What Would You Do? Christian Scenario Cards (role-play deck)
# =====================================================================
def book10():
    toc = ["How to Use the Deck", "Kindness Scenario Cards", "Honesty Scenario Cards",
           "Friendship Scenario Cards", "Faith & Courage Cards", "Role-Play & Reflect",
           "My Faith-in-Action Journal", "Certificate"]
    wb = start("What Would You Do? Christian Scenario Cards",
               "A Role-Play Card Deck for Faith-Based Problem-Solving", "Ages 5-19",
               "Faith-based problem-solving", "Role-play card deck", g.TEAL, g.CORAL, toc,
               "Builds faith-based problem-solving by acting out real situations and choosing responses "
               "rooted in kindness, honesty, and faith. Great for families, classes, and youth groups.")
    p, y, n = wb.page("How to Use", "How to Use the Scenario Cards")
    y = wb.paragraph(p, y, "Cut out the scenario cards. One person reads a card aloud, then players talk about "
                           "or act out what they would do. There is often more than one good answer - the goal "
                           "is thoughtful, kind, faith-filled choices, and hearing each other's ideas.")
    y = wb.subhead(p, y, "Ways to use the deck")
    wb.checklist(p, y, ["Talk it out: what would a kind, honest choice look like?",
                        "Act it out: role-play the situation and the good choice.",
                        "Go deeper (older kids): which Bible verse or value guides your choice?",
                        "No wrong answers - explain your thinking and listen to others."], box=False)
    wb.divider("Part 1: Scenario Cards", "Cut out and play. What would you do?")
    g.cut_out_cards(wb, "Kindness", "Kindness Scenario Cards",
                    [("Left out", "A new kid is sitting alone at lunch. What do you do?"),
                     ("Sharing", "You have extra snacks; a friend has none. What do you do?"),
                     ("A hard day", "Someone is crying at school. What do you do?"),
                     ("Chores", "Your family is busy and tired. How can you help?"),
                     ("Teasing", "Kids are teasing someone. What do you do?"),
                     ("A mistake", "Someone drops their things in the hall. What do you do?")],
                    sub="Read a card and talk or act out a kind choice.")
    g.cut_out_cards(wb, "Honesty", "Honesty Scenario Cards",
                    [("Found money", "You find money on the ground. What do you do?"),
                     ("Broke it", "You broke something and no one saw. What do you do?"),
                     ("Test answer", "A friend wants to copy your test. What do you do?"),
                     ("A lie", "You told a small lie and feel bad. What do you do?"),
                     ("Too much change", "A cashier gives you too much change. What do you do?"),
                     ("Blamed", "Someone else is blamed for what you did. What do you do?")],
                    sub="Read a card and choose the honest thing to do.")
    g.cut_out_cards(wb, "Friendship", "Friendship Scenario Cards",
                    [("Peer pressure", "Friends want you to do something wrong. What do you do?"),
                     ("A secret", "A friend shares an unsafe secret. What do you do?"),
                     ("Argument", "You and a friend disagree. How do you make peace?"),
                     ("Jealousy", "A friend gets something you wanted. What do you do?"),
                     ("New friend", "You want to join a group. What do you say?"),
                     ("Forgiveness", "A friend hurt your feelings and said sorry. What now?")],
                    sub="Read a card and role-play a caring, wise choice.")
    g.cut_out_cards(wb, "Faith & Courage", "Faith & Courage Scenario Cards",
                    [("Standing up", "Someone is being treated unfairly. What do you do?"),
                     ("Prayer", "A friend is scared or sad. How could you encourage them?"),
                     ("Different beliefs", "A friend believes differently than you. How do you show respect?"),
                     ("Doing right", "Doing the right thing is hard and unpopular. What do you do?"),
                     ("Gratitude", "Something good happened. How do you give thanks?"),
                     ("Serving", "You see a need in your community. How can you help?")],
                    sub="Read a card and choose a faith-filled, courageous response.")
    p2, y2, n2 = wb.page("Role-Play", "Role-Play & Reflect")
    y2 = wb.intro_box(p2, y2, "Pick a card, act it out, then reflect. Older kids: connect your choice to a value "
                              "or Bible verse.")
    for pr in ["A scenario we acted out was...", "The choice we thought was best was...",
               "Why that choice was kind, honest, or faithful..."]:
        p2.set_fill(*wb.accent); p2.text(g.MARGIN, y2, pr, 11.5, bold=True)
        y2 = wb.write_lines(p2, y2 - 14, 2, spacing=24); y2 -= 8
        if y2 < 90: break
    g.journal_page(wb, "Journal", "My Faith-in-Action Journal",
                   ["A time I made a kind or honest choice was...",
                    "A choice I want to make better next time is...",
                    "How I can help someone this week..."])
    return finish(wb, "10_What_Would_You_Do_Christian_Scenario_Cards.pdf",
                  "for choosing kind, honest, and faithful actions!")


BUILDERS_6_10 = [book6, book7, book8, book9, book10]
