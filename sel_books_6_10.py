"""
sel_books_6_10.py — Content for SEL books 6-10 (ages 5-17), 42+ pages each.
Reuses the shared parts/helpers from build_sel_books.py.
"""

import workbook_sel as s
from build_sel_books import (
    start, finish, part_understand_feelings, part_calm_tools, part_scenarios,
    part_coloring_reflect, DEFAULT_SCENES, BREATHS,
)


# =====================================================================
# BOOK 6 — My Calm Corner: Printable SEL Toolkit
# =====================================================================
def book6():
    toc = ["Getting to Know Feelings", "Building My Calm Corner", "My Calm-Down Tools",
           "Making Calm Choices", "Calm & Reflect", "My Calm-Down Plan", "Gratitude"]
    wb = start("My Calm Corner",
               "A Printable SEL Toolkit for Building Your Own Calm-Down Space",
               s.LAVEN, s.MINT, toc)
    part_understand_feelings(wb)
    # calm corner building part
    wb.divider("Part 2: Building My Calm Corner",
               "A cozy spot to reset big feelings.", mood="calm")
    p, y, n = wb.page("Design", "What Goes in a Calm Corner?")
    y = wb.intro_box(p, y, "A calm corner is a safe spot you can go to when feelings get big. It is NOT a "
                           "time-out or punishment - it is a place to reset. Let's design yours!")
    y = wb.checklist(p, y, ["Something soft (pillow, blanket, stuffed animal)",
                            "Something to squeeze (stress ball, putty)",
                            "Something to look at (calm pictures, glitter jar)",
                            "Something to listen to (calm music, headphones)",
                            "This book and a pencil",
                            "A feelings chart or thermometer"], box=True)
    p2, y2, n2 = wb.page("Design", "My Calm Corner Plan")
    y2 = wb.subhead(p2, y2, "Where will my calm corner be?")
    y2 = wb.write_lines(p2, y2, 2, spacing=26)
    y2 = wb.subhead(p2, y2, "What will I put in it?")
    y2 = wb.write_lines(p2, y2, 3, spacing=26)
    wb.draw_box(p2, y2, "Draw your calm corner:", min(y2 - 80, 150))
    part_calm_tools(wb, breaths=(0, 1))
    # printable signs
    p3, y3, n3 = wb.page("Printables", "Calm Corner Signs to Color")
    y3 = wb.instruction(p3, y3, "Color these signs and hang them in your calm corner.")
    for label in ["MY CALM CORNER", "TAKE A BREATH", "YOU ARE SAFE HERE"]:
        p3.set_fill(*s.CARD); p3.round_rect(s.MARGIN, y3 - 60, s.CW, 56, 12, fill=True, stroke=False)
        p3.set_stroke(*wb.accent); p3.set_line_width(1.6)
        p3.round_rect(s.MARGIN, y3 - 60, s.CW, 56, 12, fill=False, stroke=True)
        p3.set_fill(*wb.accent); p3.text_center(s.PW/2, y3 - 38, label, 20, bold=True)
        y3 -= 72
    part_scenarios(wb,
                   ["You feel a big feeling building up at home.",
                    "You need a break but there are people around.",
                    "Your calm corner is busy - what else can you do?"],
                   ["You feel overwhelmed and want to be alone for a bit.",
                    "You're at school and can't go to your calm corner.",
                    "A friend wants to use calm-down tools with you."])
    part_coloring_reflect(wb, DEFAULT_SCENES)
    return finish(wb, "06_My_Calm_Corner_Printable_SEL_Toolkit.pdf")


# =====================================================================
# BOOK 7 — Feelings Detective: Social-Emotional Learning Activity Book
# =====================================================================
def book7():
    toc = ["Becoming a Feelings Detective", "Clues in the Body", "Reading Others' Feelings",
           "Calm-Down Tools", "Solving Feeling Mysteries", "Calm & Reflect", "My Plan", "Gratitude"]
    wb = start("Feelings Detective",
               "A Social-Emotional Learning Activity Book - Investigate, Name & Solve Big Feelings",
               s.OCEAN, s.GOLD, toc)
    wb.divider("Part 1: Becoming a Feelings Detective",
               "Every feeling leaves clues.", mood="surprised")
    p, y, n = wb.page("Case File", "Your Detective Badge")
    y = wb.paragraph(p, y, "Detectives look for clues to solve mysteries. YOU can be a Feelings Detective! "
                           "Your job is to notice the clues that tell you what you (and others) are feeling - "
                           "then figure out what would help.")
    # badge
    p.set_stroke(*wb.accent); p.set_line_width(2)
    wb._star(p, s.PW/2, y - 80, 60)
    p.set_fill(*wb.accent); p.text_center(s.PW/2, y - 84, "FEELINGS", 12, bold=True)
    p.text_center(s.PW/2, y - 100, "DETECTIVE", 12, bold=True)
    y -= 170
    wb.subhead(p, y, "Detective's oath")
    wb.intro_box(p, y - 22, "I promise to look for clues, name feelings kindly, and use what I learn to help "
                            "myself and others feel calmer and safer.")
    s.feelings_faces_color(wb, "Clues", "Face Clues to Investigate",
                           [("happy", "Happy"), ("sad", "Sad"), ("angry", "Angry"),
                            ("worried", "Worried"), ("surprised", "Surprised"), ("calm", "Calm")])
    s.body_scan(wb)
    p2, y2, n2 = wb.page("Clues", "Body Clue Chart")
    y2 = wb.intro_box(p2, y2, "Feelings leave clues in the body. Match the clue to the feeling it often means.")
    y2 = wb.checklist(p2, y2, ["Hot face, clenched fists -> often ANGER",
                               "Butterflies, fast heart -> often WORRY",
                               "Heavy body, tears -> often SADNESS",
                               "Big smile, bouncy body -> often JOY",
                               "Slow breathing, loose shoulders -> often CALM"], box=False)
    y2 = wb.subhead(p2, y2, "My own body clues are...")
    wb.write_lines(p2, y2, 3, spacing=26)
    # reading others
    wb.divider("Part 2: Reading Others' Feelings",
               "Great detectives notice other people too.", mood="calm")
    s.feelings_faces_color(wb, "Investigate", "What Might They Feel?",
                           [("sad", "left out"), ("worried", "nervous"), ("angry", "frustrated"),
                            ("happy", "proud"), ("surprised", "shocked"), ("calm", "content")])
    s.matching_page(wb, "Investigate", "Match the Clue to the Feeling",
                    ["Crossed arms, frown", "Wide eyes, gasp", "Slumped shoulders", "Jumping, cheering"],
                    ["angry", "surprised", "sad", "excited"],
                    "Draw a line from each clue to the feeling it might mean.")
    part_calm_tools(wb, breaths=(0, 3))
    # feeling mysteries = scenarios
    wb.divider("Part 3: Solving Feeling Mysteries",
               "Use your clues to choose calm.", mood="worried")
    s.scenario_page(wb, "Case", "Mystery Cases (1)",
                    ["A classmate is quiet and won't play today. What might they feel? What could you do?",
                     "You feel grumpy but don't know why. What clues can you check?",
                     "A friend suddenly gets angry during a game. What might be going on?"])
    s.scenario_page(wb, "Case", "Mystery Cases (2)",
                    ["You feel nervous but excited before a big event. Name both feelings.",
                     "Someone online seems upset. How can you tell, and what can you do?",
                     "You snapped at someone. What feeling was underneath it?"])
    part_coloring_reflect(wb, DEFAULT_SCENES)
    return finish(wb, "07_Feelings_Detective_SEL_Activity_Book.pdf")


# =====================================================================
# BOOK 8 — What Should I Do? Kids' Social Skills Scenario Cards
# =====================================================================
def book8():
    toc = ["Getting to Know Feelings", "Social Skills Basics", "Scenario Cards",
           "Making Calm Choices", "Calm-Down Tools", "Calm & Reflect", "My Plan", "Gratitude"]
    wb = start("What Should I Do?",
               "Kids' Social Skills Scenario Cards - Practice Real Situations and Kind Choices",
               s.GREEN, s.CORAL, toc)
    part_understand_feelings(wb)
    # social skills basics
    wb.divider("Part 2: Social Skills Basics",
               "Skills for getting along and feeling good together.", mood="happy")
    p, y, n = wb.page("Skills", "Social Skills Toolbox")
    y = wb.intro_box(p, y, "Social skills help us make friends, solve problems, and feel good with others. "
                           "Here are some of the most useful ones.")
    y = wb.checklist(p, y, ["Listening without interrupting",
                            "Taking turns and sharing",
                            "Using a calm voice and kind words",
                            "Asking to join in",
                            "Saying sorry and making it right",
                            "Standing up for myself respectfully",
                            "Reading the room - noticing how others feel"], box=True)
    s.matching_page(wb, "Skills", "Match the Skill to the Situation",
                    ["Someone is talking", "You made a mistake", "You want to play",
                     "A friend is sad"],
                    ["listen carefully", "say sorry", "ask to join", "show you care"],
                    "Draw a line from each situation to a helpful skill.")
    # lots of scenario "cards"
    wb.divider("Part 3: Scenario Cards",
               "Think it through before you act.", mood="worried")
    scenario_sets = [
        ("Friendship Cards",
         ["A friend doesn't want to play what you want to play.",
          "Two friends are arguing and both want you to take their side.",
          "You want to join a group that's already playing."]),
        ("Fairness Cards",
         ["Someone cuts in line in front of you.",
          "You think a rule or grade is unfair.",
          "A teammate isn't doing their part in a group project."]),
        ("Tricky Talk Cards",
         ["Someone says something that hurts your feelings.",
          "You need to tell a friend 'no' without being mean.",
          "You have to apologize to someone you wronged."]),
        ("Online & Group Cards",
         ["You see someone being teased in a group chat.",
          "You feel left out when others make plans without you.",
          "Someone pressures you to do something you don't want to do."]),
    ]
    for title, sc in scenario_sets:
        s.scenario_page(wb, "Card Set", title, sc)
    part_calm_tools(wb, breaths=(0, 1))
    part_coloring_reflect(wb, DEFAULT_SCENES)
    return finish(wb, "08_What_Should_I_Do_Kids_Social_Skills_Scenario_Cards.pdf")


# =====================================================================
# BOOK 9 — Brave Feelings: Coping Skills Activity Book for Kids
# =====================================================================
def book9():
    toc = ["Getting to Know Feelings", "Brave vs. Scared", "Coping Skills",
           "Facing Worries", "Making Calm Choices", "Calm & Reflect", "My Plan", "Gratitude"]
    wb = start("Brave Feelings",
               "A Coping Skills Activity Book for Kids - Facing Worry, Fear & Hard Days With Courage",
               s.INDIGO, s.GOLD, toc)
    part_understand_feelings(wb)
    # brave vs scared
    wb.divider("Part 2: Brave vs. Scared",
               "Brave doesn't mean not scared - it means going on anyway.", mood="worried")
    p, y, n = wb.page("Learn", "What Does Brave Really Mean?")
    y = wb.paragraph(p, y, "Being brave doesn't mean you never feel scared or worried. Brave means feeling the "
                           "fear AND doing the hard thing anyway - sometimes in tiny steps. Everyone feels "
                           "afraid sometimes. Courage is a skill you can grow.")
    y = wb.subhead(p, y, "Worry vs. real danger")
    wb.intro_box(p, y, "Sometimes our worry alarm goes off even when we're safe - like a smoke alarm beeping "
                       "at burnt toast. Learning to check 'Am I really in danger, or is this a worry alarm?' "
                       "helps us feel braver.")
    s.feelings_faces_color(wb, "Feelings", "Faces of Worry & Courage",
                           [("worried", "Worried"), ("worried", "Nervous"), ("sad", "Scared"),
                            ("calm", "Calm"), ("happy", "Brave"), ("excited", "Proud")])
    s.feelings_thermometer(wb, kicker="Worry Meter", heading="My Worry Thermometer")
    # coping skills
    wb.divider("Part 3: Coping Skills",
               "Tools for worry, fear, and hard days.", mood="calm")
    for idx in (0, 2):
        k, nm, st, sh = BREATHS[idx]
        s.breathing_exercise(wb, "Breathe", k, nm, st, shape=sh)
    s.calm_strategy_cards(wb, "Toolkit", "Brave Coping Cards", [
        ("Name the Worry", "Say exactly what you're worried about."),
        ("Check the Facts", "Ask: is this a real danger or a worry alarm?"),
        ("Brave Step", "Break it into one tiny step you can do."),
        ("Worry Time", "Save worries for a set 10-minute 'worry time.'"),
        ("Talk It Out", "Share the worry with a safe person."),
        ("Brave Self-Talk", "Say: 'I can do hard things.'"),
    ])
    s.tracing_affirmations(wb, "Words", "Brave Words",
                           ["I can do hard things.", "I am braver than my worry.", "One small step."])
    # facing worries
    p2, y2, n2 = wb.page("Practice", "My Worry Ladder")
    y2 = wb.intro_box(p2, y2, "A worry ladder breaks a scary thing into small steps, from easiest at the bottom "
                              "to hardest at the top. You climb one rung at a time.")
    y2 = wb.subhead(p2, y2, "Something I want to feel braver about:")
    y2 = wb.write_lines(p2, y2, 1, spacing=24)
    y2 -= 6
    for rung in ["Top step (hardest):", "Middle step:", "Middle step:", "First step (easiest):"]:
        p2.set_fill(*wb.accent); p2.text(s.MARGIN, y2, rung, 11, bold=True)
        y2 = wb.write_lines(p2, y2 - 12, 1, spacing=22)
        y2 -= 8
    part_scenarios(wb,
                   ["You feel scared to try something new, like a class or a sport.",
                    "You have a worry that keeps coming back at bedtime.",
                    "You feel afraid to ask for help."],
                   ["You're anxious about a big test or performance.",
                    "You feel nervous about a hard conversation.",
                    "A worry is making it hard to focus or sleep."])
    part_coloring_reflect(wb, DEFAULT_SCENES)
    return finish(wb, "09_Brave_Feelings_Coping_Skills_Activity_Book_for_Kids.pdf")


# =====================================================================
# BOOK 10 — One Breath, One Step: Classroom Calm Kit
# =====================================================================
def book10():
    toc = ["Getting to Know Feelings", "Whole-Class Calm", "Breathing & Movement Breaks",
           "Making Calm Choices Together", "Calm & Reflect", "Class Calm Plan", "Gratitude"]
    wb = start("One Breath, One Step",
               "A Classroom Calm Kit - Group Breathing, Calm Breaks & SEL Routines for Any Class",
               s.TEAL, s.ORANGE, toc)
    # teacher note
    p, y, n = wb.page("For Teachers", "Using This Classroom Kit")
    y = wb.paragraph(p, y, "This kit gives you ready-to-use, low-prep calm routines for the whole class. Use a "
                           "breathing break to start the day, reset after recess, or settle nerves before a "
                           "test. Every page is reproducible and works for a wide age range - simplify the "
                           "language for younger students and add reflection for older ones.")
    y = wb.subhead(p, y, "Quick tips")
    wb.checklist(p, y, ["Do the routines WITH students - your calm sets the tone.",
                        "Keep breaks short (1-3 minutes) and predictable.",
                        "Post a class feelings chart where everyone can see it.",
                        "Praise effort and calm choices, not just quiet."], box=False)
    part_understand_feelings(wb)
    # whole-class calm
    wb.divider("Part 2: Whole-Class Calm",
               "Calm is easier when we do it together.", mood="calm")
    p2, y2, n2 = wb.page("Routine", "Class Feelings Check-In")
    y2 = wb.intro_box(p2, y2, "Start the day by having each student show or say how they feel. It builds "
                              "belonging and helps you spot who might need support.")
    s.feelings_faces_color(wb, "Check-In", "Point to How You Feel", [
        ("happy", "Good"), ("calm", "Calm"), ("worried", "Worried"),
        ("sad", "Sad"), ("angry", "Frustrated"), ("excited", "Excited")])
    p3, y3, n3 = wb.page("Routine", "Class Calm Signals")
    y3 = wb.intro_box(p3, y3, "Agree on quiet signals the whole class knows, so anyone can ask for calm without "
                              "words. Design yours together.")
    y3 = wb.checklist(p3, y3, ["A hand signal that means 'I need a breath.'",
                               "A signal for 'the class needs a reset.'",
                               "A calm word or chime that starts a breathing break.",
                               "A signal for 'I need to use the calm corner.'"], box=True)
    y3 = wb.subhead(p3, y3, "Our class signals are...")
    wb.write_lines(p3, y3, 3, spacing=26)
    # breathing & movement
    wb.divider("Part 3: Breathing & Movement Breaks",
               "Short resets for busy minds.", mood="happy")
    for idx in (0, 1, 2):
        k, nm, st, sh = BREATHS[idx]
        s.breathing_exercise(wb, "Break", k, nm, st, shape=sh)
    p4, y4, n4 = wb.page("Break", "Movement Reset Cards")
    y4 = wb.intro_box(p4, y4, "Movement helps release big energy and feelings. Try one for 60 seconds.")
    y4 = wb.checklist(p4, y4, ["Stand and stretch tall like a tree, then fold down slow.",
                               "Shake out your hands, arms, and legs for 10 seconds.",
                               "March in place slowly, then faster, then slow again.",
                               "Push your palms together, hold, and release.",
                               "Roll your shoulders back five times.",
                               "Take five slow breaths together as a class."], box=True)
    # calm choices together
    wb.divider("Part 4: Calm Choices Together",
               "We help each other stay calm and kind.", mood="happy")
    s.scenario_page(wb, "Class", "Class Situations (1)",
                    ["The class is getting loud and wound up before a lesson.",
                     "Two classmates are arguing and others are taking sides.",
                     "Someone is having a big feeling and needs space."])
    s.scenario_page(wb, "Class", "Class Situations (2)",
                    ["The whole class feels nervous before a test.",
                     "A change in plans upsets several students.",
                     "Someone new joins and feels left out."])
    s.checklist_page(wb, "Agreement", "Our Class Calm Agreement",
                     "Create shared promises for how your class handles big feelings. Tick the ones you agree on.",
                     ["We treat all feelings with respect.",
                      "We use calm voices and kind words.",
                      "We give each other space when needed.",
                      "We use our calm-down tools before reacting.",
                      "We ask for help when feelings are too big.",
                      "We welcome and include everyone."])
    part_coloring_reflect(wb, DEFAULT_SCENES)
    return finish(wb, "10_One_Breath_One_Step_Classroom_Calm_Kit.pdf")


BUILDERS_6_10 = [book6, book7, book8, book9, book10]
