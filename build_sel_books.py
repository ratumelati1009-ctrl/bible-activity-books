"""
build_sel_books.py — Generate 10 SEL / emotional-regulation activity books.
Ages 5-17, each 42+ pages. Writer: Daniel Tesfamariam.
Run: python3 build_sel_books.py   ->  sel-books/*.pdf
"""

import os
import re
import workbook_sel as s

OUT = "sel-books"
os.makedirs(OUT, exist_ok=True)


# ---- shared front/back matter ----
WELCOME = [
    "Welcome! This book helps kids and teens understand big feelings and learn calm, kind ways to "
    "handle them. Feelings are not good or bad - they are messengers. This book builds the skills to "
    "listen to them and choose what to do next.",
    "Every page is printable and reproducible for your home or classroom. Go at the reader's pace, and "
    "celebrate effort more than 'right answers.'",
]
FOR_GROWNUPS = [
    "Do the activities alongside the child when you can - your calm helps them feel safe.",
    "Name feelings out loud together; naming a feeling helps shrink it.",
    "Never punish a feeling. Coach the choice that comes after it.",
    "Revisit favorite pages often - skills grow with practice, not one-time reading.",
]


def report(path):
    d = open(path, "rb").read()
    pages = len(re.findall(rb"/Type\s*/Page[^s]", d))
    ok = d[:8] == b"%PDF-1.4" and d.rstrip().endswith(b"%%EOF") and pages >= 42
    print(f"[{'OK ' if ok else 'BAD'}] {path}  pages={pages}  bytes={len(d):,}")
    return ok


def start(title, subtitle, accent, accent2, toc):
    wb = s.SELBook(title, subtitle, accent=accent, accent2=accent2)
    wb.cover()
    wb.welcome(WELCOME, FOR_GROWNUPS)
    wb.how_it_scales()
    wb.toc = toc
    wb.contents()
    return wb


def part_practice_week(wb):
    """A week of daily feelings check-ins + a review. ~6 pages."""
    wb.divider("Part 5: My Practice Week",
               "Practice makes calm feel natural.", mood="happy")
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Weekend"]
    # two days per page -> 3 pages
    for i in range(0, len(days), 2):
        p, y, n = wb.page("Daily Check-In", f"{days[i]} & {days[i+1]}")
        for d in (days[i], days[i + 1]):
            p.set_fill(*wb.accent)
            p.text(s.MARGIN, y, d, 13, bold=True)
            p.set_stroke(*wb.accent2); p.set_line_width(2)
            p.line(s.MARGIN, y - 6, s.MARGIN + 46, y - 6)
            y -= 20
            # tiny mood faces to circle
            moods = [("happy", "good"), ("calm", "calm"), ("worried", "worried"),
                     ("sad", "sad"), ("angry", "angry")]
            fx = s.MARGIN + 20
            for (m, lab) in moods:
                wb.face(p, fx, y - 14, 14, m)
                p.set_fill(*s.INK); p.text_center(fx, y - 40, lab, 8)
                fx += (s.CW - 40) / 5
            y -= 56
            p.set_fill(*wb.accent); p.text(s.MARGIN, y, "One thing that helped me today:", 10.5, bold=True)
            y = wb.write_lines(p, y - 12, 1, spacing=22)
            y -= 16
    s.journal_page(wb, "Review", "My Practice Week Review",
                   ["Which calm-down tool did I use the most?",
                    "Which tool worked best for me?",
                    "What do I want to keep practicing next week?"])


def part_toolkit_summary(wb):
    """'My Toolkit' summary + coping review. ~2 pages."""
    p, y, n = wb.page("My Toolkit", "My Top Calm-Down Tools")
    y = wb.intro_box(p, y, "Out of everything you tried, which tools help YOU most? Write your personal top tools "
                           "so you remember them when a big feeling shows up.")
    for i in range(1, 6):
        p.set_fill(*wb.accent); p.circle(s.MARGIN + 9, y + 3, 10, fill=True, stroke=False)
        p.set_fill(1, 1, 1); p.text_center(s.MARGIN + 9, y - 0.5, str(i), 10, bold=True)
        p.set_stroke(*s.RULE); p.set_line_width(0.7)
        p.line(s.MARGIN + 28, y - 3, s.PW - s.MARGIN, y - 3)
        y -= 30
    y -= 6
    y = wb.subhead(p, y, "When I feel calm, I can help others by...")
    wb.write_lines(p, y, 3, spacing=26)
    s.checklist_page(wb, "Check", "How Far I've Come",
                     "Look how much you've learned! Tick everything you can do now (or are practicing).",
                     ["I can name my feelings.",
                      "I can notice feelings in my body.",
                      "I know my warning signs for big feelings.",
                      "I have calm-down tools I can use.",
                      "I can make calmer choices.",
                      "I can ask for help when I need it.",
                      "I can be kind to myself when things are hard."])


EXTRA_SCENES = [
    ("Starry Night", "A peaceful, starry sky to unwind under", s.scene_star_night),
    ("Flower Garden", "A calm garden bursting with flowers", s.scene_garden),
    ("Cozy Corner", "A safe, comfy place to rest", s.scene_cozy_room),
    ("Calm Beach", "Gentle waves on a quiet shore", s.scene_calm_beach),
]

EXTRA_JOURNALS = [
    ("Reflect", "Letter to Myself", [
        "Write a kind letter to yourself for a day you feel a big feeling.",
        "What do you want to remember?",
        "What would you tell a friend feeling the same way?"]),
    ("Reflect", "My Growing Skills", [
        "One feeling I understand better now is...",
        "One thing I can do when it gets big is...",
        "I feel proud that I can..."]),
    ("Mindful", "Slowing Down My Mind", [
        "When my mind feels busy, I can...",
        "A quiet thing I enjoy is...",
        "One slow, calm thing I will do today is..."]),
]


def finish(wb, filename, practice_week=True):
    # shared later parts to reach 42+ pages
    if practice_week:
        part_practice_week(wb)
    part_toolkit_summary(wb)
    # universal back matter
    s.coping_plan(wb)
    s.gratitude_page(wb)
    # auto-pad with meaningful pages until >= 44 (buffer over the 42 minimum)
    pad_scene = list(EXTRA_SCENES)
    pad_journal = list(EXTRA_JOURNALS)
    guard = 0
    while wb._pageno < 44 and guard < 20:
        guard += 1
        if pad_journal:
            k, h, pr = pad_journal.pop(0)
            s.journal_page(wb, k, h, pr)
        elif pad_scene:
            k, cap, sc = pad_scene.pop(0)
            s.coloring_calm(wb, "Color", k, cap, sc)
        else:
            s.notes_page(wb)
    s.notes_page(wb)
    s.notes_page(wb)
    path = os.path.join(OUT, filename)
    wb.save(path)
    return path


# common feelings sets
FACES_BASIC = [("happy", "Happy"), ("sad", "Sad"), ("angry", "Angry"),
               ("worried", "Worried"), ("calm", "Calm"), ("excited", "Excited")]
FACES_MORE = [("surprised", "Surprised"), ("worried", "Nervous"), ("sad", "Lonely"),
              ("happy", "Proud"), ("calm", "Relaxed"), ("angry", "Frustrated")]

BREATHS = [
    ("Square (Box) Breathing", "Box Breathing",
     ["Trace up one side as you breathe IN for 4.",
      "Trace across the top as you HOLD for 4.",
      "Trace down as you breathe OUT for 4.",
      "Trace across the bottom as you HOLD for 4.",
      "Repeat 3-5 times until you feel calmer."], "square"),
    ("Triangle Breathing", "Triangle Breathing",
     ["Breathe IN as you trace the first side (count 3).",
      "HOLD as you trace the second side (count 3).",
      "Breathe OUT as you trace the last side (count 3).",
      "Go around the triangle slowly 4 times."], "triangle"),
    ("Flower & Candle Breathing", "Flower Breathing",
     ["Pretend to smell a flower - breathe IN through your nose.",
      "Pretend to cool soup or blow a candle - breathe OUT slowly through your mouth.",
      "Trace each petal as you breathe.",
      "Notice your shoulders drop as you relax."], "flower"),
    ("Star Breathing", "Star Breathing",
     ["Trace up a point as you breathe IN.",
      "Trace down as you breathe OUT.",
      "Keep going around all five points slowly.",
      "Finish with one big calm breath."], "star"),
]


def part_understand_feelings(wb):
    wb.divider("Part 1: Getting to Know Feelings",
               "Every feeling has a name and a message.", mood="happy")
    s.feelings_faces_color(wb, "Feelings", "Faces We Make", FACES_BASIC)
    s.feelings_faces_color(wb, "Feelings", "More Feelings We Have", FACES_MORE)
    s.matching_page(wb, "Match", "Match the Feeling to What Helps",
                    ["Angry", "Worried", "Sad", "Excited"],
                    ["take deep breaths", "talk to someone", "get a hug", "share the good news"],
                    "Draw a line from each feeling to one thing that can help.")
    s.feelings_thermometer(wb)
    s.body_scan(wb)
    s.journal_page(wb, "Journal", "My Feelings Today",
                   ["A feeling I felt today was...",
                    "It showed up in my body like this...",
                    "What I did about it was..."])


def part_calm_tools(wb, breaths=(0, 1)):
    wb.divider("Part 2: My Calm-Down Tools",
               "Small tools for big feelings.", mood="calm")
    for idx in breaths:
        name_kick, name, steps, shape = BREATHS[idx]
        s.breathing_exercise(wb, "Breathe", name_kick, name, steps, shape=shape)
    s.calm_strategy_cards(wb, "Toolkit", "Calm-Down Cards (Set 1)", [
        ("Deep Breaths", "Slow belly breaths - in for 4, out for 6."),
        ("Count to 10", "Count slowly and unclench your hands."),
        ("Cold Water", "Splash your face or hold something cool."),
        ("Push the Wall", "Press your hands on a wall for 10 seconds."),
        ("Name 5 Things", "Name 5 things you can see right now."),
        ("Ask for a Break", "Say: 'I need a minute to calm down.'"),
    ])
    s.calm_strategy_cards(wb, "Toolkit", "Calm-Down Cards (Set 2)", [
        ("Squeeze & Release", "Tense muscles for 5, then let go."),
        ("Draw It Out", "Draw or scribble how you feel."),
        ("Move Your Body", "Stretch, jump, or take a walk."),
        ("Safe Person", "Talk to someone you trust."),
        ("Calm Words", "Say: 'This is hard, but it will pass.'"),
        ("Calm Corner", "Go to your calm spot for a reset."),
    ])
    s.tracing_affirmations(wb, "Words", "Calming Words to Trace",
                           ["I am safe.", "I can handle this.", "This feeling will pass."])
    s.matching_page(wb, "Match", "Match the Tool to the Moment",
                    ["Feeling angry", "Feeling worried", "Feeling restless", "Feeling sad"],
                    ["take slow breaths", "talk to someone", "move your body", "get a hug or rest"],
                    "Draw a line from each moment to a tool that can help.")
    s.journal_page(wb, "My Tools", "Trying Out My Tools",
                   ["A calm-down tool I want to try is...",
                    "When I could use it is...",
                    "How I hope it will help me..."])


def part_scenarios(wb, scenarios1, scenarios2):
    wb.divider("Part 3: Making Calm Choices",
               "Feelings happen to us - choices are up to us.", mood="worried")
    s.scenario_page(wb, "Think It Through", "What Would You Do? (1)", scenarios1)
    s.scenario_page(wb, "Think It Through", "What Would You Do? (2)", scenarios2)
    s.checklist_page(wb, "Check", "My Calm Choice Checklist",
                     "Before I react, I can check this list. Tick the ones you want to remember.",
                     ["I take a breath before I speak or act.",
                      "I name what I'm feeling.",
                      "I ask myself: will this help or hurt?",
                      "I use a calm-down tool if the feeling is big.",
                      "I ask for help if I need it.",
                      "I try again - mistakes are okay."])
    s.journal_page(wb, "Reflect", "A Time I Made a Calm Choice",
                   ["Describe a time you handled a big feeling well.",
                    "What did you do? How did it turn out?",
                    "What will you try next time?"])


def part_coloring_reflect(wb, scenes):
    wb.divider("Part 4: Calm & Reflect",
               "Rest your mind and notice the good.", mood="calm")
    for (kick, cap, scene) in scenes:
        s.coloring_calm(wb, "Color", kick, cap, scene)
    s.journal_page(wb, "Reflect", "My Calm Place",
                   ["Describe or draw a place where you feel calm.",
                    "What do you see, hear, and feel there?"],
                   box_label="Draw your calm place:", box_h=150)


DEFAULT_SCENES = [
    ("Calm Beach", "A quiet place by the gentle sea", s.scene_calm_beach),
    ("Peaceful Mountains", "Breathe in the fresh mountain air", s.scene_mountain),
    ("Cozy Corner", "A safe, comfy place to rest", s.scene_cozy_room),
]


# =====================================================================
# BOOK 1 — Dazzle's Calm-Down Adventure SEL Toolkit
# =====================================================================
def book1():
    toc = ["Getting to Know Feelings", "Dazzle's Calm-Down Tools", "Making Calm Choices",
           "Calm & Reflect", "My Calm-Down Plan", "Good Things & Gratitude"]
    wb = start("Dazzle's Calm-Down Adventure",
               "An SEL Toolkit Starring Dazzle the Dragon - Learn to Cool Big Feelings",
               s.PURPLE, s.SUN, toc)
    # story-flavored intro
    p, y, n = wb.page("Meet Dazzle", "Dazzle the Feelings Dragon")
    y = wb.paragraph(p, y, "Meet Dazzle! Dazzle is a young dragon who feels BIG feelings. When Dazzle gets "
                           "angry, smoke puffs out. When Dazzle worries, the wings get shaky. Dazzle is "
                           "learning to cool down those big feelings - and Dazzle will teach you how too!")
    wb.face(p, s.PW/2, y-70, 46, "excited", color=s.PURPLE)
    y -= 150
    y = wb.subhead(p, y, "Dazzle's Big Idea")
    wb.intro_box(p, y, "Even a fire-breathing dragon can learn to calm down. If Dazzle can do it, so can you! "
                       "Every time your feeling gets hot, you can cool it with a calm-down tool.")
    part_understand_feelings(wb)
    part_calm_tools(wb, breaths=(0, 2))
    part_scenarios(wb,
                   ["Dazzle's tower of blocks falls down. Dazzle feels like roaring.",
                    "A friend laughs at Dazzle's drawing. Dazzle feels hurt.",
                    "Dazzle has to wait a long time for a turn on the slide."],
                   ["You feel angry because your game got turned off.",
                    "Someone budges in front of you in line.",
                    "You made a mistake on your homework and feel like giving up."])
    part_coloring_reflect(wb, [
        ("Dazzle's Calm Cave", "Dazzle's cozy cave for cooling down", s.scene_cozy_room),
        ("Starry Night", "A peaceful, starry sky", s.scene_star_night),
        ("Dazzle's Garden", "A calm garden full of flowers", s.scene_garden),
    ])
    return finish(wb, "01_Dazzles_Calm-Down_Adventure_SEL_Toolkit.pdf")


# =====================================================================
# BOOK 2 — I Can Calm My Body: Emotional Regulation Activity Book
# =====================================================================
def book2():
    toc = ["Getting to Know Feelings", "My Calm-Down Tools", "Calming My Body",
           "Making Calm Choices", "Calm & Reflect", "My Calm-Down Plan", "Gratitude"]
    wb = start("I Can Calm My Body",
               "An Emotional Regulation Activity Book - Breathing, Grounding & Body-Based Calm",
               s.AQUA, s.PEACH, toc)
    part_understand_feelings(wb)
    part_calm_tools(wb, breaths=(0, 1))
    # extra body-focused part
    wb.divider("Part 2b: Calming My Body",
               "When the body settles, the mind follows.", mood="calm")
    _k, _nm, _st, _sh = BREATHS[3]
    s.breathing_exercise(wb, "Breathe", _k, _nm, _st, shape=_sh)
    p, y, n = wb.page("Grounding", "5-4-3-2-1 Grounding")
    y = wb.intro_box(p, y, "When feelings feel too big, grounding brings you back to right now using your senses.")
    for label, cnt in [("5 things I can SEE", 5), ("4 things I can TOUCH", 4),
                       ("3 things I can HEAR", 3), ("2 things I can SMELL", 2),
                       ("1 slow BREATH I can take", 1)]:
        p.set_fill(*wb.accent); p.text(s.MARGIN, y, label, 12, bold=True)
        y = wb.write_lines(p, y - 14, 1 if cnt > 1 else 1, spacing=22)
        y -= 6
    p2, y2, n2 = wb.page("Relax", "Melting Muscle Relaxation")
    y2 = wb.intro_box(p2, y2, "Tense each body part for 5 seconds, then let it go loose like cooked spaghetti. "
                              "Notice the difference between tight and relaxed.")
    y2 = wb.checklist(p2, y2, ["Scrunch your face, then release.",
                               "Shrug your shoulders up, then drop them.",
                               "Make fists, then open your hands.",
                               "Squeeze your tummy, then relax.",
                               "Curl your toes, then let them go.",
                               "Take one big breath and sigh it out."], box=True)
    part_scenarios(wb,
                   ["Your heart is racing before a test or a big game.",
                    "You feel your face getting hot because you're angry.",
                    "You can't fall asleep because your mind is busy."],
                   ["You feel butterflies before speaking in front of the class.",
                    "You feel shaky after an argument.",
                    "You feel restless and can't sit still."])
    part_coloring_reflect(wb, DEFAULT_SCENES)
    return finish(wb, "02_I_Can_Calm_My_Body_Emotional_Regulation_Activity_Book.pdf")


# =====================================================================
# BOOK 3 — When I Feel Angry: Kids' Calm-Down Activity Pack
# =====================================================================
def book3():
    toc = ["Understanding Anger", "My Anger Signals", "Cool-Down Tools",
           "Making Calm Choices", "Calm & Reflect", "My Anger Plan", "Gratitude"]
    wb = start("When I Feel Angry",
               "A Kids' Calm-Down Activity Pack for Understanding and Cooling Anger",
               s.CORAL, s.GOLD, toc)
    wb.divider("Part 1: Understanding Anger",
               "Anger is normal - it's what we do with it that matters.", mood="angry")
    p, y, n = wb.page("Learn", "Anger Is a Normal Feeling")
    y = wb.paragraph(p, y, "Everybody feels angry sometimes - even grown-ups. Anger often shows up when "
                           "something feels unfair, when we're hurt, or when we don't get what we want. "
                           "Anger isn't 'bad.' It's a signal. The goal isn't to never feel angry; it's to "
                           "handle anger in ways that don't hurt ourselves or others.")
    y = wb.subhead(p, y, "Anger is like a volcano")
    wb.intro_box(p, y, "Anger can build up slowly like a volcano. If we notice the early rumbles, we can cool "
                       "down before we erupt. This book helps you spot your rumbles and cool them.")
    s.feelings_faces_color(wb, "Feelings", "Faces of Anger & Calm",
                           [("angry", "Angry"), ("angry", "Frustrated"), ("worried", "Annoyed"),
                            ("calm", "Calm"), ("happy", "Peaceful"), ("calm", "Relaxed")])
    # anger signals
    p2, y2, n2 = wb.page("Signals", "My Anger Warning Signs")
    y2 = wb.intro_box(p2, y2, "Your body warns you before anger boils over. Circle or write the signs you notice.")
    y2 = wb.checklist(p2, y2, ["Hot face or ears", "Clenched fists or jaw", "Fast heartbeat",
                               "Loud voice", "Tight tummy", "Wanting to hit, throw, or yell"], box=True)
    y2 = wb.subhead(p2, y2, "My personal warning signs are...")
    wb.write_lines(p2, y2, 3, spacing=26)
    s.feelings_thermometer(wb, kicker="Anger Meter", heading="My Anger Thermometer")
    s.body_scan(wb)
    wb.divider("Part 2: Cool-Down Tools",
               "Cool the heat before you act.", mood="calm")
    for idx in (0, 1):
        k, nm, st, sh = BREATHS[idx]
        s.breathing_exercise(wb, "Breathe", k, nm, st, shape=sh)
    s.calm_strategy_cards(wb, "Toolkit", "Anger Cool-Down Cards", [
        ("Stop & Breathe", "Freeze, then take 3 slow breaths."),
        ("Walk Away", "Leave the situation to cool off safely."),
        ("Push or Squeeze", "Push a wall or squeeze a pillow."),
        ("Count Backwards", "Count down from 10 slowly."),
        ("Use Words", "Say 'I feel angry because...'"),
        ("Cool Water", "Get a drink or splash cool water."),
    ])
    s.tracing_affirmations(wb, "Words", "Cool-Down Words",
                           ["I can cool down.", "I am the boss of my body.", "I can use my words."])
    part_scenarios(wb,
                   ["Your sibling breaks something of yours on purpose.",
                    "You get blamed for something you didn't do.",
                    "You lose a game and want to flip the board."],
                   ["Someone says something mean about you online.",
                    "A teacher gives you a rule that feels unfair.",
                    "Your plans get cancelled at the last minute."])
    part_coloring_reflect(wb, [
        ("Cool Blue Ocean", "Cool, calm waves to soothe the heat", s.scene_calm_beach),
        ("Quiet Mountains", "A calm, cool mountain view", s.scene_mountain),
        ("Peaceful Garden", "A gentle garden to relax in", s.scene_garden),
    ])
    return finish(wb, "03_When_I_Feel_Angry_Kids_Calm-Down_Activity_Pack.pdf")


# =====================================================================
# BOOK 4 — Big Feelings, Calm Choices: SEL Workbook for Kids
# =====================================================================
def book4():
    toc = ["Getting to Know Feelings", "My Calm-Down Tools", "Making Calm Choices",
           "Kindness & Empathy", "Calm & Reflect", "My Calm-Down Plan", "Gratitude"]
    wb = start("Big Feelings, Calm Choices",
               "A Social-Emotional Learning Workbook for Kids - Feel It, Name It, Choose It",
               s.BLUE, s.PEACH, toc)
    part_understand_feelings(wb)
    part_calm_tools(wb, breaths=(0, 3))
    part_scenarios(wb,
                   ["You feel jealous when a friend gets something you wanted.",
                    "You feel embarrassed after tripping in front of others.",
                    "You feel disappointed when a trip is cancelled."],
                   ["You feel left out of a group chat or plan.",
                    "You feel overwhelmed by too much homework.",
                    "You feel nervous about making a new friend."])
    # empathy part
    wb.divider("Part 3b: Kindness & Empathy",
               "Big feelings are easier when we care for each other.", mood="happy")
    p, y, n = wb.page("Empathy", "Reading Others' Feelings")
    y = wb.intro_box(p, y, "Empathy means noticing how someone else might feel and caring about it. "
                           "Look at the faces and guess the feeling.")
    s.feelings_faces_color(wb, "Empathy", "How Might They Feel?",
                           [("sad", "left out"), ("worried", "nervous"), ("angry", "frustrated"),
                            ("happy", "proud"), ("surprised", "surprised"), ("calm", "content")])
    s.journal_page(wb, "Kindness", "Caring for Others",
                   ["A time someone was kind to me when I had a big feeling...",
                    "A way I can help a friend who feels upset...",
                    "Kind words I can say to someone who is sad..."])
    part_coloring_reflect(wb, DEFAULT_SCENES)
    return finish(wb, "04_Big_Feelings_Calm_Choices_SEL_Workbook_for_Kids.pdf")


# =====================================================================
# BOOK 5 — I Can Wait! Patience & Waiting Skills Activity Pack
# =====================================================================
def book5():
    toc = ["Why Waiting Is Hard", "Feelings While Waiting", "Waiting Tools",
           "Making Calm Choices", "Calm & Reflect", "My Waiting Plan", "Gratitude"]
    wb = start("I Can Wait!",
               "A Patience & Waiting Skills Activity Pack - Handling the Hard Feeling of Waiting",
               s.MINT, s.ORANGE, toc)
    wb.divider("Part 1: Why Waiting Is Hard",
               "Waiting brings big feelings too.", mood="worried")
    p, y, n = wb.page("Learn", "Waiting Is a Skill")
    y = wb.paragraph(p, y, "Waiting is hard for everyone - our brains like things NOW! But waiting is a skill "
                           "we can grow, just like a muscle. When we practice waiting, big feelings like "
                           "frustration and boredom get easier to handle.")
    y = wb.subhead(p, y, "What waiting can feel like")
    wb.intro_box(p, y, "Waiting can feel boring, wiggly, frustrating, or even worried. All of those are okay. "
                       "The trick is having something to DO with your body and mind while you wait.")
    s.feelings_faces_color(wb, "Feelings", "Feelings While I Wait",
                           [("worried", "Impatient"), ("angry", "Frustrated"), ("sad", "Bored"),
                            ("calm", "Patient"), ("happy", "Hopeful"), ("excited", "Excited")])
    s.feelings_thermometer(wb, kicker="Wait Meter", heading="My Impatience Thermometer")
    wb.divider("Part 2: Waiting Tools",
               "Fill the wait with calm.", mood="calm")
    for idx in (1, 2):
        k, nm, st, sh = BREATHS[idx]
        s.breathing_exercise(wb, "Breathe", k, nm, st, shape=sh)
    s.calm_strategy_cards(wb, "Toolkit", "Waiting Tools", [
        ("Count or Sing", "Count slowly or hum a song in your head."),
        ("Fidget Quietly", "Wiggle fingers or toes, squeeze your hands."),
        ("Look Around", "Notice colors, shapes, or patterns nearby."),
        ("Imagine", "Picture something fun in your mind."),
        ("Ask How Long", "Ask when your turn will come."),
        ("Deep Breaths", "Breathe slowly until it's time."),
    ])
    s.tracing_affirmations(wb, "Words", "Patience Words",
                           ["I can wait.", "My turn will come.", "Waiting gets easier."])
    p2, y2, n2 = wb.page("Practice", "First / Then Planning")
    y2 = wb.intro_box(p2, y2, "Waiting is easier when we know what comes next. Fill in 'First I wait for..., "
                              "then I get to...' to help your brain relax.")
    for _ in range(4):
        p2.set_fill(*wb.accent); p2.text(s.MARGIN, y2, "First I wait for:", 11.5, bold=True)
        y2 = wb.write_lines(p2, y2 - 14, 1, spacing=22)
        p2.set_fill(*wb.accent); p2.text(s.MARGIN, y2, "Then I get to:", 11.5, bold=True)
        y2 = wb.write_lines(p2, y2 - 14, 1, spacing=22)
        y2 -= 10
    part_scenarios(wb,
                   ["You're waiting for your turn on the swings.",
                    "Dinner isn't ready yet and you're hungry.",
                    "You have to wait in a long line."],
                   ["You're waiting for test results or a reply to a message.",
                    "You want something now but have to save up for it.",
                    "You're stuck waiting during a long, boring trip."])
    part_coloring_reflect(wb, DEFAULT_SCENES)
    return finish(wb, "05_I_Can_Wait_Patience_and_Waiting_Skills_Activity_Pack.pdf")


BUILDERS = [book1, book2, book3, book4, book5]

if __name__ == "__main__":
    # Import books 6-10 here (after this module is fully defined) to avoid a
    # circular import, since sel_books_6_10 imports helpers from this module.
    from sel_books_6_10 import BUILDERS_6_10
    ok = True
    for b in BUILDERS + BUILDERS_6_10:
        ok &= report(b())
    print("\n" + ("ALL >=42 & VALID" if ok else "SOME FAILED"))
