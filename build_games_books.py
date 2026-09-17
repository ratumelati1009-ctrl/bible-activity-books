"""
build_games_books.py — 10 interactive matching/sorting/role-play/game books.
Ages 5-19. Each 42+ pages. Writer: Daniel Tesfamariam.
Run: python3 build_games_books.py   ->  games-books/*.pdf
"""

import os
import re
import workbook_games as g

OUT = "games-books"
os.makedirs(OUT, exist_ok=True)


def report(path):
    d = open(path, "rb").read()
    pages = len(re.findall(rb"/Type\s*/Page[^s]", d))
    ok = d[:8] == b"%PDF-1.4" and d.rstrip().endswith(b"%%EOF") and pages >= 42
    print(f"[{'OK ' if ok else 'BAD'}] {path}  pages={pages}  bytes={len(d):,}")
    return ok


TIPS = [
    "Print on card stock if you can, so the cut-out cards last longer.",
    "Cut out the cards together along the dashed lines - it builds fine-motor skills.",
    "Play each game more than once; repetition is where the learning sticks.",
    "For older kids, ask 'why?' after every answer to deepen thinking.",
    "Keep it playful - praise trying, not just getting it right.",
]


def start(title, subtitle, ages, skill, fmt, accent, accent2, toc, teaches):
    wb = g.GameBook(title, subtitle, ages, skill, fmt, accent=accent, accent2=accent2)
    wb.cover()
    wb.how_to_play(teaches, TIPS)
    wb.toc = toc
    wb.contents()
    return wb


def _pad(wb, extra=None):
    order = list(extra or [])
    order += [
        lambda: g.journal_page(wb, "Reflect", "What I Learned",
                               ["My favorite game in this book was...",
                                "One new thing I learned was..."]),
        lambda: g.journal_page(wb, "Draw It", "Draw Your Own",
                               ["Draw or design your own card or game for this topic."]),
        lambda: g.journal_page(wb, "Talk", "Talk About It",
                               ["What did this book make you think about?",
                                "How could you use it with a friend or family member?"]),
    ]
    i = 0; guard = 0
    while wb._pageno < 44 and guard < 30:
        order[i % len(order)](); i += 1; guard += 1


def finish(wb, filename, cert_line, answers=None, extra_pad=None):
    if answers:
        g.answer_key(wb, "For Grown-Ups", "Answer Key", answers)
    g.journal_page(wb, "Reflect", "Playing & Learning Journal",
                   ["Which game did you play the most?",
                    "What was tricky at first but got easier?",
                    "What do you want to try next?"])
    _pad(wb, extra_pad)
    g.certificate(wb, cert_line)
    path = os.path.join(OUT, filename)
    wb.save(path)
    return path


# =====================================================================
# BOOK 1 — Match the Bible Character to the Story (matching cards)
# =====================================================================
def book1():
    toc = ["Matching Cards: Characters", "Matching Cards: Stories", "Draw-a-Line Matching",
           "Who Am I? Clues", "Sorting: Old & New Testament", "Answer Key", "Certificate"]
    wb = start("Match the Bible Character to the Story",
               "A Matching-Card Game for Bible Knowledge", "Ages 5-19", "Bible knowledge",
               "Matching cards", g.INDIGO, g.SUN, toc,
               "Builds Bible knowledge by matching well-known characters to their stories - great for "
               "memory, recall, and family Bible time.")
    wb.divider("Part 1: Character & Story Cards", "Cut them out and find the pairs.")
    chars = [
        ("Noah", "Character card"), ("David", "Character card"), ("Moses", "Character card"),
        ("Jonah", "Character card"), ("Ruth", "Character card"), ("Esther", "Character card"),
        ("Daniel", "Character card"), ("Mary", "Character card"), ("Peter", "Character card"),
        ("Paul", "Character card"), ("Joseph", "Character card"), ("Abraham", "Character card"),
    ]
    stories = [
        ("Built the ark", "Story of Noah"), ("Faced the giant Goliath", "Story of David"),
        ("Led God's people out of Egypt", "Story of Moses"), ("Swallowed by a big fish", "Story of Jonah"),
        ("Loyal to Naomi", "Story of Ruth"), ("Brave queen who saved her people", "Story of Esther"),
        ("Prayed in the lions' den", "Story of Daniel"), ("Mother of Jesus", "Story of Mary"),
        ("Walked on water toward Jesus", "Story of Peter"), ("Wrote many New Testament letters", "Story of Paul"),
        ("Coat of many colors; forgave his brothers", "Story of Joseph"), ("Father of many nations", "Story of Abraham"),
    ]
    g.cut_out_cards(wb, "Cards", "Character Cards (Set 1)", chars[:6], sub="Match each to its story card.")
    g.cut_out_cards(wb, "Cards", "Character Cards (Set 2)", chars[6:])
    g.cut_out_cards(wb, "Cards", "Story Cards (Set 1)", stories[:6], sub="Match each to its character card.")
    g.cut_out_cards(wb, "Cards", "Story Cards (Set 2)", stories[6:])
    g.draw_line_matching(wb, "Match", "Draw a Line: Character to Story (1)",
                         [c[0] for c in chars[:6]], [s[0] for s in stories[:6]],
                         "Draw a line from each Bible character to their story.")
    g.draw_line_matching(wb, "Match", "Draw a Line: Character to Story (2)",
                         [c[0] for c in chars[6:]], [s[0] for s in stories[6:]],
                         "Draw a line from each Bible character to their story.")
    p, y, n = wb.page("Who Am I?", "Who Am I? Clue Cards")
    y = wb.intro_box(p, y, "Read each clue and write the character's name. For older kids: add a verse or a "
                           "lesson the story teaches.")
    clues = ["I obeyed God and built a giant boat. Who am I?",
             "I was small but I trusted God to defeat a giant. Who am I?",
             "God spoke to me from a burning bush. Who am I?",
             "I ran from God and ended up inside a big fish. Who am I?",
             "I became queen and bravely saved my people. Who am I?",
             "I stayed loyal to my mother-in-law, Naomi. Who am I?"]
    for c in clues:
        p.set_fill(*wb.accent); p.text(g.MARGIN, y, "-", 11, bold=True)
        p.set_fill(*g.INK); endy = p.wrap_text(g.MARGIN + 16, y, c, 11, g.CW - 16, leading=14)
        y = wb.write_lines(p, endy - 6, 1, spacing=22, indent=16); y -= 8
        if y < 90: break
    g.discussion_sort(wb, "Sort", "Old or New Testament?", ["Old Testament", "New Testament"],
                      ["Noah", "Moses", "David", "Jonah", "Mary", "Peter", "Paul", "Esther"],
                      "Write 'O' for Old Testament or 'N' for New Testament beside each name.")
    answers = [("Noah", "Built the ark"), ("David", "Faced Goliath"), ("Moses", "Led people out of Egypt"),
               ("Jonah", "Big fish"), ("Ruth", "Loyal to Naomi"), ("Esther", "Brave queen"),
               ("Daniel", "Lions' den"), ("Mary", "Mother of Jesus"), ("Peter", "Walked on water"),
               ("Paul", "Wrote letters"), ("Testament sort", "Mary, Peter, Paul are New Testament; the rest Old")]
    return finish(wb, "01_Match_the_Bible_Character_to_the_Story.pdf",
                  "for matching Bible characters to their stories!", answers=answers)


# =====================================================================
# BOOK 2 — Creation Days Sequencing Game (seven-day sorting)
# =====================================================================
def book2():
    toc = ["Seven Days Cards", "Sequencing: Order the Days", "Day & Creation Matching",
           "Sorting: Which Day?", "Draw the Days", "Answer Key", "Certificate"]
    wb = start("Creation Days Sequencing Game",
               "A Seven-Day Sorting & Sequencing Activity", "Ages 5-19", "Sequencing",
               "Seven-day sorting activity", g.TEAL, g.GOLD, toc,
               "Teaches sequencing and the order of the seven days of creation - building memory, order, "
               "and Bible knowledge.")
    days = [
        ("Day 1", "God made light - day and night."),
        ("Day 2", "God made the sky and the waters."),
        ("Day 3", "God made land, seas, and plants."),
        ("Day 4", "God made the sun, moon, and stars."),
        ("Day 5", "God made fish and birds."),
        ("Day 6", "God made animals and people."),
        ("Day 7", "God rested and blessed the day."),
    ]
    wb.divider("Part 1: The Seven Days", "Cut out the day cards and put them in order.")
    g.cut_out_cards(wb, "Cards", "Creation Day Cards (1-4)", days[:4], cols=2, rows=2,
                    sub="Cut out and arrange in order, Day 1 to Day 7.")
    g.cut_out_cards(wb, "Cards", "Creation Day Cards (5-7)", days[4:], cols=2, rows=2)
    g.sequencing_page(wb, "Sequence", "Put the Days in Order",
                      [d[1] for d in days], "Number each creation event 1-7 in the order it happened.")
    g.draw_line_matching(wb, "Match", "Match the Day to What God Made",
                         [d[0] for d in days], [d[1].split(' - ')[0].replace('God made ', '').rstrip('.') for d in days],
                         "Draw a line from each day to what God made.")
    g.discussion_sort(wb, "Sort", "Living or Not Living?", ["Living", "Not Living"],
                      ["Light", "Plants", "Sun", "Fish", "Birds", "Animals", "People", "Sky"],
                      "Sort each creation into Living or Not Living. Write 'L' or 'N'.")
    p, y, n = wb.page("Draw", "Draw the Seven Days")
    y = wb.intro_box(p, y, "Draw a picture for each day of creation. Older kids can add the matching Bible verse "
                           "from Genesis 1.")
    for d in days[:5]:
        p.set_fill(*wb.accent); p.text(g.MARGIN, y, d[0] + ":", 11.5, bold=True)
        p.set_stroke(*g.RULE); p.set_line_width(1); p.round_rect(g.MARGIN + 70, y - 34, g.CW - 70, 40, 6, fill=False, stroke=True)
        y -= 50
        if y < 80: break
    answers = [("Order", "Day 1 light, 2 sky/water, 3 land/plants, 4 sun/moon/stars, 5 fish/birds, 6 animals/people, 7 rest"),
               ("Living", "Plants, fish, birds, animals, people"),
               ("Not living", "Light, sun, sky")]
    return finish(wb, "02_Creation_Days_Sequencing_Game.pdf",
                  "for learning the order of the seven days of creation!", answers=answers)


# =====================================================================
# BOOK 3 — Good Choice or Poor Choice? (sorting cards)
# =====================================================================
def book3():
    toc = ["Choice Cards to Cut Out", "Sorting Mat", "Good or Poor? Sort",
           "What Happens Next?", "Draw-a-Line: Choice to Result", "Answer Key", "Certificate"]
    wb = start("Good Choice or Poor Choice?",
               "A Sorting-Card Game for Decision-Making", "Ages 5-19", "Decision-making",
               "Sorting cards", g.GREEN, g.CORAL, toc,
               "Builds decision-making by sorting everyday actions into good and poor choices, then talking "
               "about the results of each.")
    good = ["Sharing your snack with a friend", "Telling the truth", "Helping clean up",
            "Saying sorry when you're wrong", "Waiting your turn", "Doing your homework"]
    poor = ["Hitting when you're angry", "Telling a lie", "Taking without asking",
            "Cutting in line", "Ignoring the rules", "Being mean online"]
    wb.divider("Part 1: Choice Cards", "Cut them out and sort them.")
    g.cut_out_cards(wb, "Cards", "Choice Cards (Set 1)",
                    [(c, "Good or poor choice?") for c in good], sub="Sort onto the mat.")
    g.cut_out_cards(wb, "Cards", "Choice Cards (Set 2)",
                    [(c, "Good or poor choice?") for c in poor])
    g.sorting_mat(wb, "Sort", "Sorting Mat: Good vs. Poor Choices",
                  ["Good Choice", "Poor Choice"], "Sort your cut-out choice cards into the two bins.",
                  items_hint="Use the cards from the previous pages.")
    g.discussion_sort(wb, "Sort", "Good or Poor? Write It",
                      ["Good", "Poor"],
                      ["Share your toys", "Push to the front", "Say thank you", "Break a promise",
                       "Help a friend up", "Laugh at a mistake"],
                      "Write 'G' for good or 'P' for poor. Then talk about why.")
    g.scenario_match(wb, "Match", "What Happens Next?",
                     [("You tell the truth", "people trust you"),
                      ("You share", "you make a friend"),
                      ("You cut in line", "others feel upset"),
                      ("You help clean up", "the room gets done faster"),
                      ("You break a rule", "someone could get hurt"),
                      ("You say sorry", "you can make things right")],
                     "Choice", "Result", "Match each choice to what might happen next.")
    p, y, nn = wb.page("Decide", "Make the Choice")
    y = wb.intro_box(p, y, "Read each situation. Write a GOOD choice you could make. For older kids: explain the "
                           "consequences of a poor choice too.")
    for s in ["Your friend drops their books in the hallway...",
              "You really want a turn but someone else is using it...",
              "You broke something by accident and no one saw..."]:
        p.set_fill(*wb.accent); p.text(g.MARGIN, y, "-", 11, bold=True)
        p.set_fill(*g.INK); endy = p.wrap_text(g.MARGIN + 16, y, s, 11, g.CW - 16, leading=14)
        y = wb.write_lines(p, endy - 6, 2, spacing=24, indent=16); y -= 8
        if y < 90: break
    answers = [("Good choices", "Sharing, truth, helping, apologizing, waiting, doing homework"),
               ("Poor choices", "Hitting, lying, taking, cutting in line, ignoring rules, being mean")]
    return finish(wb, "03_Good_Choice_or_Poor_Choice.pdf",
                  "for learning to make good choices!", answers=answers)


# =====================================================================
# BOOK 4 — Match the Emotion to the Situation (scenario-matching)
# =====================================================================
def book4():
    toc = ["Emotion Cards", "Situation Cards", "Scenario Matching Game",
           "Emotion Faces Sort", "What Would Help?", "Answer Key", "Certificate"]
    wb = start("Match the Emotion to the Situation",
               "A Scenario-Matching Game for Emotional Literacy", "Ages 5-19", "Emotional literacy",
               "Scenario-matching game", g.CORAL, g.SKY, toc,
               "Builds emotional literacy by matching feelings to the situations that cause them - naming "
               "emotions is the first step to managing them.")
    emotions = ["Happy", "Sad", "Angry", "Scared", "Excited", "Nervous",
                "Proud", "Jealous", "Embarrassed", "Grateful", "Lonely", "Surprised"]
    wb.divider("Part 1: Emotion & Situation Cards", "Cut them out and find the matches.")
    g.cut_out_cards(wb, "Cards", "Emotion Cards (Set 1)",
                    [(e, "How does it feel?") for e in emotions[:6]], sub="Match to a situation card.")
    g.cut_out_cards(wb, "Cards", "Emotion Cards (Set 2)",
                    [(e, "How does it feel?") for e in emotions[6:]])
    sits = [("You get a surprise gift", "Excited"),
            ("Your pet is sick", "Sad"),
            ("Someone breaks your toy on purpose", "Angry"),
            ("You have to speak in front of the class", "Nervous"),
            ("You finish a hard puzzle by yourself", "Proud"),
            ("You're home alone and hear a strange noise", "Scared")]
    g.cut_out_cards(wb, "Cards", "Situation Cards",
                    [(s[0], "Which emotion fits?") for s in sits])
    g.scenario_match(wb, "Match", "Match Emotion to Situation (1)",
                     sits, "Situation", "Emotion", "Draw a line from each situation to the emotion it might cause.")
    g.scenario_match(wb, "Match", "Match Emotion to Situation (2)",
                     [("A friend won't share and you wanted it too", "Jealous"),
                      ("You trip in front of everyone", "Embarrassed"),
                      ("Someone helps you when you needed it", "Grateful"),
                      ("You have no one to play with", "Lonely"),
                      ("You win first place", "Happy"),
                      ("A loud clap surprises you", "Surprised")],
                     "Situation", "Emotion", "Match each situation to the feeling it might cause.")
    p, y, nn = wb.page("Help", "What Would Help?")
    y = wb.intro_box(p, y, "Big feelings are okay. For each feeling, write one thing that could help. Older kids "
                           "can name a healthy coping skill.")
    for e in ["When I feel angry, it helps to...", "When I feel nervous, it helps to...",
              "When I feel sad, it helps to...", "When I feel jealous, it helps to..."]:
        p.set_fill(*wb.accent); p.text(g.MARGIN, y, e, 11.5, bold=True)
        y = wb.write_lines(p, y - 14, 1, spacing=22); y -= 10
        if y < 90: break
    answers = [(s[0], s[1]) for s in sits]
    return finish(wb, "04_Match_the_Emotion_to_the_Situation.pdf",
                  "for learning to name feelings and match them to situations!", answers=answers)


# =====================================================================
# BOOK 5 — Fruits and Vegetables Color Sorting (busy-book)
# =====================================================================
def book5():
    toc = ["Color Sorting Mats", "Cut-Out Food Tokens", "Red & Green Sort",
           "Fruit or Vegetable?", "Match Food to Color", "Answer Key", "Certificate"]
    wb = start("Fruits and Vegetables Color Sorting",
               "A Busy-Book Activity for Colors and Vocabulary", "Ages 5-19", "Colors and vocabulary",
               "Busy-book activity", g.ORANGE, g.MINT, toc,
               "Builds color recognition and food vocabulary through hands-on sorting - great for early "
               "learners and for building categories and vocabulary in older kids.")
    wb.divider("Part 1: Color Sorting", "Sort the foods by their color.")
    g.busy_color_sort(wb, "Sort", "Sort by Color (1)",
                      [("Red", g.CORAL, ["apple", "tomato", "strawberry", "cherry"]),
                       ("Yellow", g.GOLD, ["banana", "corn", "lemon", "pepper"])],
                      "Cut out each food and place it under the matching color.")
    g.busy_color_sort(wb, "Sort", "Sort by Color (2)",
                      [("Green", g.MINT, ["pea", "lettuce", "lime", "broccoli"]),
                       ("Orange", g.ORANGE, ["carrot", "orange", "pumpkin", "mango"])],
                      "Cut out each food and place it under the matching color.")
    g.busy_color_sort(wb, "Sort", "Sort by Color (3)",
                      [("Purple", g.PURPLE, ["grape", "eggplant", "plum", "beet"]),
                       ("White", g.SLATE, ["onion", "garlic", "cauliflower", "mushroom"])],
                      "Cut out each food and place it under the matching color.")
    g.discussion_sort(wb, "Sort", "Fruit or Vegetable?",
                      ["Fruit", "Vegetable"],
                      ["Apple", "Carrot", "Banana", "Broccoli", "Grape", "Potato", "Orange", "Pea"],
                      "Write 'F' for fruit or 'V' for vegetable. Talk about how they grow.")
    g.draw_line_matching(wb, "Match", "Match the Food to Its Color",
                         ["Banana", "Tomato", "Pea", "Grape", "Carrot"],
                         ["yellow", "red", "green", "purple", "orange"],
                         "Draw a line from each food to its color.")
    p, y, nn = wb.page("Vocabulary", "My Favorite Foods")
    y = wb.intro_box(p, y, "Draw or write your favorite fruit and vegetable of each color. Older kids: add where "
                           "each food comes from.")
    for c in ["A red food I like:", "A green food I like:", "A yellow food I like:", "An orange food I like:"]:
        p.set_fill(*wb.accent); p.text(g.MARGIN, y, c, 11.5, bold=True)
        y = wb.write_lines(p, y - 14, 1, spacing=22); y -= 10
        if y < 90: break
    answers = [("Fruit", "Apple, Banana, Grape, Orange"), ("Vegetable", "Carrot, Broccoli, Potato, Pea"),
               ("Note", "A tomato is technically a fruit - a fun talking point!")]
    return finish(wb, "05_Fruits_and_Vegetables_Color_Sorting.pdf",
                  "for sorting fruits and vegetables by color!", answers=answers)


BUILDERS = [book1, book2, book3, book4, book5]

if __name__ == "__main__":
    from games_books_6_10 import BUILDERS_6_10
    ok = True
    for b in BUILDERS + BUILDERS_6_10:
        ok &= report(b())
    print("\n" + ("ALL >=42 & VALID" if ok else "SOME FAILED"))
