"""
build_story_books.py — 10 illustrated social-story + activity books.
Each 42+ pages. Writer: Daniel Tesfamariam.
Run: python3 build_story_books.py   ->  social-stories/*.pdf
"""

import os
import re
import workbook_story as w

OUT = "social-stories"
os.makedirs(OUT, exist_ok=True)


def report(path):
    d = open(path, "rb").read()
    pages = len(re.findall(rb"/Type\s*/Page[^s]", d))
    ok = d[:8] == b"%PDF-1.4" and d.rstrip().endswith(b"%%EOF") and pages >= 42
    print(f"[{'OK ' if ok else 'BAD'}] {path}  pages={pages}  bytes={len(d):,}")
    return ok


HOW_TO_USE = [
    "Read the story slowly and out loud, pointing at the pictures.",
    "Read it again on calm days - not only in the hard moment.",
    "Pause to let your child color, answer, or act out the pages.",
    "Praise effort and calm tries, not perfection.",
    "Use the calm-down tools together so they feel familiar later.",
]


def start(title, subtitle, ages, fmt, accent, accent2, toc):
    wb = w.StoryBook(title, subtitle, ages, fmt, accent=accent, accent2=accent2)
    wb.cover()
    wb.for_grownups(
        "This book helps a child understand the feeling, see that it is normal, and practice calm, "
        "kind choices - before the real moment happens.", HOW_TO_USE)
    wb.toc = toc
    wb.contents()
    return wb


# meaningful pages used to round each book up to 44+
def _pad(wb):
    order = [
        lambda: w.journal_page(wb, "Journal", "My Feelings Journal",
                               ["A time I felt this feeling was...", "What helped me feel better was..."]),
        lambda: w.coloring_page(wb, "Color", "My Calm Place", "Draw and color a place where you feel calm and safe.",
                                w.scene_calm_place),
        lambda: w.tracing_page(wb, "Words", "Calm Words to Trace",
                               ["I am safe.", "I can ask for help.", "This will pass."]),
        lambda: w.journal_page(wb, "Journal", "People Who Help Me",
                               ["Who are my safe grown-ups?", "How can they help me?"]),
        lambda: w.coloring_page(wb, "Color", "Happy Together", "Color two friends being kind to each other.",
                                w.scene_two_friends),
    ]
    i = 0; guard = 0
    while wb._pageno < 44 and guard < 30:
        order[i % len(order)](); i += 1; guard += 1


def finish(wb, filename, cert_line):
    w.toolkit_page(wb)
    w.journal_page(wb, "All About Me", "What I Learned",
                   ["The most helpful thing I learned was...", "One thing I will try next time is..."])
    _pad(wb)
    w.certificate(wb, "name", cert_line)
    path = os.path.join(OUT, filename)
    wb.save(path)
    return path


# tiny illustration helpers built from kid()/face()
def _one_kid(mood, color=None):
    def draw(wb, p, cx, cy):
        wb.kid(p, cx, cy, 34, mood, color=color)
    return draw


def _two_kids(m1, m2):
    def draw(wb, p, cx, cy):
        wb.kid(p, cx - 70, cy, 30, m1)
        wb.kid(p, cx + 70, cy, 30, m2)
        p.set_stroke(0.13, 0.14, 0.17); p.set_line_width(1.4)
        p.line(cx - 150, cy - 78, cx + 150, cy - 78)
    return draw


def _kid_and_adult(mood):
    def draw(wb, p, cx, cy):
        wb.kid(p, cx - 60, cy - 6, 26, mood)
        wb.kid(p, cx + 70, cy + 6, 40, "calm")  # bigger = adult
        p.set_stroke(0.13, 0.14, 0.17); p.set_line_width(1.4)
        p.line(cx - 150, cy - 90, cx + 150, cy - 90)
    return draw


# =====================================================================
# BOOK 1 — What to Do When I Feel Angry (4-8) : story + calming cards
# =====================================================================
def book1():
    toc = ["The Story: When I Feel Angry", "My Feelings Faces", "Calming Cards",
           "Balloon Breathing", "What Would You Do?", "My Calm-Down Toolkit", "My Certificate"]
    wb = start("What to Do When I Feel Angry",
               "A Social Story With Calming Cards", "Ages 4-8",
               "Social story + calming cards", w.CORAL, w.SUN, toc)
    wb.section("The Story", "When I Feel Angry", mood="angry")
    wb.story(_one_kid("happy"), ["Hi! My name is Sam.", "Most of the time I feel just fine."])
    wb.story(_one_kid("angry"), ["But sometimes I feel ANGRY.",
                                 "Anger is a normal feeling. Everybody feels it sometimes."])
    wb.story(_one_kid("angry"), ["When I get angry, my face feels hot.",
                                 "My hands squeeze into tight fists. My tummy feels tight too."])
    wb.story(_one_kid("angry"), ["Sometimes I want to yell, or hit, or throw things.",
                                 "But those choices can hurt me or other people."])
    wb.story(_one_kid("worried"), ["Anger is okay to FEEL.",
                                    "It is not okay to hurt myself or others. So I have a better plan."])
    wb.story(_one_kid("calm"), ["First, I STOP.",
                                "I notice my angry body and I do not act right away."])
    wb.story(_one_kid("calm"), ["Then I take a big, slow breath.",
                                "I breathe in slowly... and out even slower. My body starts to cool down."])
    wb.story(_one_kid("calm"), ["I can also count to ten, ask for a hug, or take a break.",
                                "I can tell a grown-up, 'I feel angry.'"])
    wb.story(_one_kid("happy"), ["When I am calm again, I can use my words.",
                                 "I can say what is wrong and ask for help fixing it."])
    wb.story(_two_kids("happy", "happy"), ["I am the boss of my body.",
                                           "I can feel angry AND still make a calm, kind choice. I can do it!"])
    w.feelings_faces(wb, "Feelings", "How Does Anger Feel?",
                     [("calm", "Calm"), ("worried", "Annoyed"), ("angry", "Frustrated"),
                      ("angry", "Angry"), ("sad", "Hurt"), ("happy", "Happy Again")])
    w.cards_page(wb, "Calming Cards", "My Calming Cards (Set 1)",
                 "Cut out these cards. Keep them close for when you feel angry.",
                 [("Stop", "Freeze and notice your angry body."),
                  ("Breathe", "Take 3 big, slow belly breaths."),
                  ("Count", "Count slowly to ten."),
                  ("Walk Away", "Step away to a calm spot to cool off.")])
    w.cards_page(wb, "Calming Cards", "My Calming Cards (Set 2)",
                 "More calming cards to try.",
                 [("Squeeze", "Squeeze a pillow or push your hands together."),
                  ("Ask for Help", "Tell a grown-up, 'I feel angry.'"),
                  ("Use Words", "Say, 'I feel angry because...'"),
                  ("Get a Drink", "Sip some cool water and reset.")])
    w.breathing_card(wb, "Balloon Breathing",
                     ["Breathe in slowly and fill your belly like a balloon.",
                      "Hold for a moment.", "Breathe out slowly and let the balloon go soft.",
                      "Do it 3-5 times until you feel calmer."], shape="square")
    w.scenario_page(wb, "Think It Through", "What Would You Do?",
                    ["Your block tower falls down right before it was finished.",
                     "Your brother changes the TV channel while you were watching.",
                     "You lose a game and feel like giving up."])
    w.scenario_page(wb, "Think It Through", "More Angry Moments",
                    ["Someone cuts in front of you in line.",
                     "You get told 'no' when you really wanted a yes.",
                     "A friend accidentally knocks over your drawing."])
    return finish(wb, "01_What_to_Do_When_I_Feel_Angry.pdf",
                  "for learning calm, kind ways to handle angry feelings!")


# =====================================================================
# BOOK 2 — My First Day of School Feelings (4-7) : story + feelings workbook
# =====================================================================
def book2():
    toc = ["The Story: My First Day", "My Feelings Faces", "Feelings Workbook",
           "Bumblebee Breathing", "What Would You Do?", "All About My Day", "My Certificate"]
    wb = start("My First Day of School Feelings",
               "A Social Story With a Feelings Workbook", "Ages 4-7",
               "Story + feelings workbook", w.SKY, w.SUN, toc)
    wb.section("The Story", "My First Day of School", mood="worried")
    wb.story(_one_kid("worried"), ["Tomorrow is my first day of school.",
                                   "My tummy feels wiggly and my thoughts are busy."])
    wb.story(_one_kid("worried"), ["I feel lots of feelings at once.",
                                   "A little excited. A little worried. That is okay - feelings can mix."])
    wb.story(_kid_and_adult("worried"), ["My grown-up says, 'It is normal to feel nervous about something new.'",
                                         "'I will bring you and pick you up. You are safe.'"])
    wb.story(_one_kid("calm"), ["In the morning, I take a slow breath.",
                                "I remember: new things get easier once I try them."])
    wb.story(_kid_and_adult("calm"), ["At school, my teacher smiles and says hello.",
                                      "She shows me where to put my bag and where I will sit."])
    wb.story(_two_kids("calm", "happy"), ["I see other kids. Some look nervous too.",
                                          "I am not the only one with big feelings today."])
    wb.story(_one_kid("worried"), ["I miss my grown-up a little.",
                                   "When I feel that way, I take a breath and remember they will come back."])
    wb.story(_two_kids("happy", "happy"), ["I find a friend to play with.",
                                           "We build blocks and read a story together."])
    wb.story(_one_kid("happy"), ["The day goes by faster than I thought.",
                                 "I did lots of new things - and I was brave."])
    wb.story(_kid_and_adult("happy"), ["My grown-up comes back, just like they promised.",
                                       "I tell them all about my first day. I did it!"])
    w.feelings_faces(wb, "Feelings", "First-Day Feelings",
                     [("excited", "Excited"), ("worried", "Nervous"), ("sad", "Missing Home"),
                      ("surprised", "Surprised"), ("calm", "Calm"), ("happy", "Proud")])
    w.matching(wb, "Workbook", "Match the Feeling to What Helps",
               ["Nervous", "Missing my grown-up", "Excited", "Shy"],
               ["take a slow breath", "remember they'll come back", "share the good news", "say a quiet hello"],
               "Draw a line from each feeling to something that can help.")
    w.journal_page(wb, "Workbook", "How I Feel About School",
                   ["Something I feel excited about is...",
                    "Something I feel nervous about is...",
                    "Something that will help me be brave is..."])
    w.breathing_card(wb, "Bumblebee Breathing",
                     ["Breathe in slowly through your nose.",
                      "Breathe out with a soft humming 'mmm' like a bee.",
                      "Feel the buzz calm your body.",
                      "Do it a few times before school."], shape="flower")
    w.scenario_page(wb, "Think It Through", "What Would You Do?",
                    ["You do not know where to sit on the first day.",
                     "You feel shy about saying hello to a new kid.",
                     "You miss your grown-up in the middle of the day."])
    w.journal_page(wb, "All About Me", "All About My Day",
                   ["The best part of my day was...",
                    "A grown-up who helps me at school is...",
                    "Something new I want to try is..."])
    return finish(wb, "02_My_First_Day_of_School_Feelings.pdf",
                  "for being brave on the first day of school!")


# =====================================================================
# BOOK 3 — Coping With Separation Anxiety (4-8) : printable story + activities
# =====================================================================
def book3():
    toc = ["The Story: Saying Goodbye", "My Feelings Faces", "Goodbye Plan",
           "Star Breathing", "What Would You Do?", "My Comfort List", "My Certificate"]
    wb = start("Coping With Separation Anxiety",
               "A Printable Social Story With Activities", "Ages 4-8",
               "Printable story + activities", w.LAVEN, w.PEACH, toc)
    wb.section("The Story", "Saying Goodbye for Now", mood="sad")
    wb.story(_kid_and_adult("sad"), ["When my grown-up says goodbye, my chest feels tight.",
                                     "I do not want them to go. This feeling is hard."])
    wb.story(_one_kid("worried"), ["This feeling has a name: worry about being apart.",
                                   "Lots of kids feel it. I am not the only one."])
    wb.story(_kid_and_adult("calm"), ["My grown-up always comes back.",
                                      "Goodbye is not forever - it is just 'see you later.'"])
    wb.story(_one_kid("calm"), ["We make a goodbye plan.",
                                "A quick hug, a wave, and a special word: 'See you soon!'"])
    wb.story(_one_kid("worried"), ["When I feel the worry, I take a slow breath.",
                                   "I hold my comfort item and remember our plan."])
    wb.story(_one_kid("calm"), ["I keep my hands and mind busy.",
                                "Playing and doing things makes the time go faster."])
    wb.story(_kid_and_adult("happy"), ["And then - my grown-up comes back!",
                                       "Just like they promised. I knew they would."])
    wb.story(_one_kid("happy"), ["Each time, saying goodbye gets a little easier.",
                                 "I am learning that I am safe, even when we are apart."])
    w.feelings_faces(wb, "Feelings", "How Goodbye Feels",
                     [("sad", "Sad"), ("worried", "Worried"), ("angry", "Upset"),
                      ("calm", "Calmer"), ("happy", "Happy Again"), ("excited", "Excited to Reunite")])
    w.journal_page(wb, "My Plan", "Our Goodbye Plan",
                   ["Our special goodbye is... (hug, wave, secret word)",
                    "My comfort item is...",
                    "My grown-up comes back at..."])
    w.breathing_card(wb, "Star Breathing",
                     ["Trace up a point of the star as you breathe in.",
                      "Trace down as you breathe out.",
                      "Go slowly around all five points.",
                      "Finish with one big, calm breath."], shape="star")
    w.scenario_page(wb, "Think It Through", "What Would You Do?",
                    ["Your grown-up drops you off and you feel like crying.",
                     "You feel worried in the middle of the day.",
                     "You have a new babysitter you do not know well."])
    w.journal_page(wb, "Comfort", "My Comfort List",
                   ["Things that make me feel safe are...",
                    "People I can talk to when I feel worried are...",
                    "Something fun I can do while I wait is..."])
    return finish(wb, "03_Coping_With_Separation_Anxiety.pdf",
                  "for being brave when saying goodbye for now!")


# =====================================================================
# BOOK 4 — One Breath, One Step: Managing Overwhelm (5-9) : SEL workbook + breathing cards
# =====================================================================
def book4():
    toc = ["The Story: Too Much at Once", "My Feelings Faces", "One Step at a Time",
           "Breathing Cards", "What Would You Do?", "My Overwhelm Plan", "My Certificate"]
    wb = start("One Breath, One Step",
               "Managing Overwhelm - An SEL Workbook With Breathing Cards", "Ages 5-9",
               "SEL workbook + breathing cards", w.AQUA, w.ORANGE, toc)
    wb.section("The Story", "When Everything Feels Like Too Much", mood="worried")
    wb.story(_one_kid("worried"), ["Sometimes I have SO much to do.",
                                   "My thoughts get loud and everything feels like too much at once."])
    wb.story(_one_kid("worried"), ["This big feeling is called being overwhelmed.",
                                   "My body might feel tight, tired, or like I want to give up."])
    wb.story(_one_kid("calm"), ["When I feel that way, I stop and take ONE breath.",
                                "One slow breath tells my body, 'You are safe. You can handle this.'"])
    wb.story(_one_kid("calm"), ["Then I take ONE small step.",
                                "I do not have to do everything at once - just the next small thing."])
    wb.story(_one_kid("calm"), ["Big things feel smaller when I break them into pieces.",
                                "One breath. One step. Then another."])
    wb.story(_one_kid("happy"), ["If it is still too much, I ask for help.",
                                 "Asking for help is a smart and brave thing to do."])
    wb.story(_one_kid("happy"), ["Little by little, I get it done.",
                                 "I feel proud. One breath and one step at a time really works."])
    w.feelings_faces(wb, "Feelings", "Overwhelmed Feelings",
                     [("worried", "Overwhelmed"), ("sad", "Tired"), ("angry", "Frustrated"),
                      ("calm", "Calmer"), ("happy", "Capable"), ("excited", "Proud")])
    w.journal_page(wb, "One Step", "One Step at a Time",
                   ["Something that feels like too much right now is...",
                    "The very first small step I can take is...",
                    "Who can help me if I need it?"])
    w.breathing_card(wb, "Square Breathing",
                     ["Breathe in for 4 as you trace up.", "Hold for 4 across the top.",
                      "Breathe out for 4 down the side.", "Hold for 4 across the bottom."], shape="square")
    w.breathing_card(wb, "Triangle Breathing",
                     ["Breathe in as you trace the first side.",
                      "Hold as you trace the second side.",
                      "Breathe out as you trace the last side.",
                      "Go around slowly a few times."], shape="triangle")
    w.scenario_page(wb, "Think It Through", "What Would You Do?",
                    ["You have homework, chores, and practice all in one evening.",
                     "Your room is a huge mess and you don't know where to start.",
                     "Too many kids are talking to you at once and it feels loud."])
    w.journal_page(wb, "My Plan", "My Overwhelm Plan",
                   ["When I feel overwhelmed, my first move is...",
                    "My favorite breathing tool is...",
                    "How I break big things into small steps..."])
    return finish(wb, "04_One_Breath_One_Step_Managing_Overwhelm.pdf",
                  "for learning to take one breath and one step at a time!")


# =====================================================================
# BOOK 5 — How to Ask an Adult for Help (4-8) : social story + role-play cards
# =====================================================================
def book5():
    toc = ["The Story: Asking for Help", "Safe Grown-Ups", "Role-Play Cards",
           "Practice Words", "What Would You Do?", "My Help Plan", "My Certificate"]
    wb = start("How to Ask an Adult for Help",
               "A Social Story With Role-Play Cards", "Ages 4-8",
               "Social story + role-play cards", w.GREEN, w.SUN, toc)
    wb.section("The Story", "It's Okay to Ask for Help", mood="worried")
    wb.story(_one_kid("worried"), ["Sometimes I get stuck, or hurt, or scared.",
                                   "I might not know what to do all by myself."])
    wb.story(_one_kid("worried"), ["I used to think asking for help meant I wasn't big.",
                                   "But that is not true at all."])
    wb.story(_kid_and_adult("calm"), ["Asking for help is a SMART and BRAVE thing to do.",
                                      "Even grown-ups ask each other for help."])
    wb.story(_kid_and_adult("calm"), ["First, I find a safe grown-up.",
                                      "That could be a parent, teacher, coach, or helper."])
    wb.story(_kid_and_adult("worried"), ["I get their attention politely.",
                                         "I can say their name, or say, 'Excuse me, can you help me?'"])
    wb.story(_kid_and_adult("calm"), ["Then I tell them what I need in a few words.",
                                      "'I feel...' or 'I need help with...' or 'Something happened.'"])
    wb.story(_kid_and_adult("happy"), ["The grown-up listens and helps.",
                                       "I feel so much better once I ask."])
    wb.story(_one_kid("happy"), ["If the first grown-up can't help right away, I can try another.",
                                 "I keep asking until I get the help I need."])
    w.journal_page(wb, "My People", "My Safe Grown-Ups",
                   ["Safe grown-ups at home are...",
                    "Safe grown-ups at school are...",
                    "Other helpers I can find are..."])
    w.cards_page(wb, "Role-Play Cards", "Role-Play Cards",
                 "Act these out with a grown-up. Take turns being the helper.",
                 [("I'm hurt", "Practice: 'I fell and my knee hurts.'"),
                  ("I'm stuck", "Practice: 'I can't reach it. Can you help?'"),
                  ("I'm scared", "Practice: 'Something scared me. I need you.'"),
                  ("I'm lost", "Practice: 'I can't find my grown-up.'"),
                  ("Someone's unkind", "Practice: 'Someone is being mean to me.'"),
                  ("I don't understand", "Practice: 'Can you show me how?'")], cardh=88)
    w.tracing_page(wb, "Practice", "Helping Words to Trace",
                   ["Can you help me?", "Excuse me.", "I need help."])
    w.scenario_page(wb, "Think It Through", "What Would You Do?",
                    ["You fall on the playground and your knee hurts.",
                     "You can't open your lunch and you're hungry.",
                     "You feel scared but the grown-up is busy."])
    w.journal_page(wb, "My Plan", "My Help Plan",
                   ["When I need help, the words I can say are...",
                    "If one grown-up is busy, I can ask...",
                    "A time I asked for help and it went well was..."])
    return finish(wb, "05_How_to_Ask_an_Adult_for_Help.pdf",
                  "for learning to ask a safe grown-up for help!")


BUILDERS = [book1, book2, book3, book4, book5]

if __name__ == "__main__":
    from story_books_6_10 import BUILDERS_6_10
    ok = True
    for b in BUILDERS + BUILDERS_6_10:
        ok &= report(b())
    print("\n" + ("ALL >=42 & VALID" if ok else "SOME FAILED"))
