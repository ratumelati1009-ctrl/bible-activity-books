"""
build_sel_teen_books.py — 10 teen/young-adult SEL activity books (ages 10-19).
Each 42+ pages. Writer: Daniel Tesfamariam.
Run: python3 build_sel_teen_books.py   ->  sel-teen-books/*.pdf
"""

import os
import re
import workbook_sel as s
import workbook_sel_teen as t

OUT = "sel-teen-books"
os.makedirs(OUT, exist_ok=True)

WRITER = "Daniel Tesfamariam"

WELCOME = [
    "This workbook is made for ages 10 to 19 - a stage packed with change, pressure, and big "
    "emotions. It won't talk down to you. Instead, it gives you real tools, honest questions, and "
    "space to think for yourself.",
    "There are no grades and no wrong answers. Work at your own pace, be honest in the writing "
    "spaces, and come back to the pages that help most. Skills grow with practice.",
]
FOR_GROWNUPS = [
    "Give privacy - journaling is more honest when it isn't graded or read without permission.",
    "Offer to talk, but don't force it; being available matters more than pushing.",
    "Model the skills yourself - teens notice what adults actually do.",
    "If big feelings feel unmanageable, connect the teen with a counselor or trusted professional.",
]

DISCLAIMER = ("This activity book supports everyday social-emotional learning and self-reflection. "
              "It is not therapy or medical advice. If you are struggling with your safety or mental "
              "health, please talk to a trusted adult, a counselor, or a local helpline right away.")


def report(path):
    d = open(path, "rb").read()
    pages = len(re.findall(rb"/Type\s*/Page[^s]", d))
    ok = d[:8] == b"%PDF-1.4" and d.rstrip().endswith(b"%%EOF") and pages >= 42
    print(f"[{'OK ' if ok else 'BAD'}] {path}  pages={pages}  bytes={len(d):,}")
    return ok


def start(title, subtitle, accent, accent2, toc):
    wb = s.SELBook(title, subtitle, ages="Ages 10-19", accent=accent, accent2=accent2,
                   writer=WRITER, series="Teen Wellbeing SEL Series")
    wb.cover()
    wb.welcome(WELCOME, FOR_GROWNUPS)
    # a short "how this book works" + disclaimer page
    p, y, n = wb.page("Before You Start", "How This Book Works")
    y = wb.paragraph(p, y, "Each part mixes three things: short explanations of what's going on in your brain and "
                           "body, self-checks to notice your own patterns, and tools plus reflection to help you "
                           "respond in ways you feel good about.")
    y = wb.subhead(p, y, "Getting the most from it")
    y = wb.checklist(p, y, ["Be honest - this is for you, not for show.",
                            "Try the tools more than once before deciding if they help.",
                            "Use the trackers to spot patterns over a week or two.",
                            "Revisit the plans and update them as you learn."], box=False)
    y = wb.intro_box(p, y, DISCLAIMER)
    wb.toc = toc
    wb.contents()
    return wb


# reusable back-matter fillers (meaningful, not filler)
def _pad_pages(wb):
    # Meaningful, varied SEL pages (not filler) used to round each book up to 44+.
    order = [
        lambda: t.values_goals(wb),
        lambda: t.reflection_journal(wb, "Reflect", "Checking In With Myself",
                                     ["What's one thing I'm handling better than I used to?",
                                      "What still feels hard, and what might help?"]),
        lambda: t.boundaries_scripts(wb),
        lambda: t.reflection_journal(wb, "Reflect", "A Letter to Future Me",
                                     ["Write a short letter to yourself six months from now.",
                                      "What do you hope is different? What do you want to remember?"]),
        lambda: s.gratitude_page(wb, kicker="Good Stuff", heading="Good Things Worth Noticing"),
        lambda: s.notes_page(wb, kicker="Notes", heading="My Notes & Reflections"),
    ]
    i = 0
    guard = 0
    while wb._pageno < 44 and guard < 40:
        order[i % len(order)]()
        i += 1
        guard += 1


def finish(wb, filename):
    t.action_plan(wb, "My Plan", "My Personal Wellbeing Plan",
                  "Pull it all together. This is your go-to plan when things get hard.",
                  [("My early warning signs that a feeling is getting big:", 2),
                   ("My top 3 tools that actually work for me:", 2),
                   ("People I can reach out to (and how):", 2),
                   ("Kind, true things I can tell myself:", 2),
                   ("One habit that helps me feel steady:", 1)])
    # crisis/support page
    p, y, n = wb.page("Support", "When You Need More Help")
    y = wb.paragraph(p, y, "Some feelings are too big to handle alone - and that's not weakness, it's human. "
                           "Reaching out is a strong, smart move.")
    y = wb.subhead(p, y, "Reach out if...")
    y = wb.checklist(p, y, ["A feeling won't ease up for days, or keeps getting worse.",
                            "You're avoiding things you used to enjoy.",
                            "You have thoughts of hurting yourself or others.",
                            "You just need someone to talk to - that's reason enough."], box=False)
    y = wb.subhead(p, y, "Who I can reach out to")
    y = wb.write_lines(p, y, 3, spacing=26)
    y = wb.intro_box(p, y, "If you ever feel unsafe or think about hurting yourself, tell a trusted adult now or "
                           "contact a local emergency number or crisis/helpline in your country right away. "
                           "You deserve support.")
    _pad_pages(wb)
    path = os.path.join(OUT, filename)
    wb.save(path)
    return path


# common coping menu reused across books
COPING_MENU = [
    ("Fast resets (under 2 minutes)",
     ["Slow breathing: in for 4, out for 6, a few rounds.",
      "Cold water on your face or hands.",
      "Name 5 things you see, 4 you hear, 3 you can touch.",
      "Unclench your jaw, drop your shoulders, shake out your hands."]),
    ("Move & release",
     ["Walk, stretch, or do a few push-ups or jumping jacks.",
      "Put on a song and move to it.",
      "Squeeze and release your muscles from head to toe."]),
    ("Connect & express",
     ["Text or talk to someone you trust.",
      "Write or draw what you're feeling - no filter.",
      "Do something kind for someone else."]),
    ("Longer-term care",
     ["Keep a steady sleep routine.",
      "Limit doom-scrolling before bed.",
      "Spend time on something that gives you meaning."]),
]


# =====================================================================
# BOOK 1 — Regulate: A Teen's Guide to Managing Big Emotions
# =====================================================================
def book1():
    toc = ["Understanding Emotions", "Knowing My Patterns", "My Coping Toolkit",
           "Rewiring My Thinking", "Real-Life Scenarios", "Reflection & Plan"]
    wb = start("Regulate",
               "A Teen's Guide to Understanding and Managing Big Emotions",
               s.INDIGO, s.SUN, toc)
    wb.divider("Part 1: Understanding Emotions",
               "Emotions aren't the enemy - they're information.", mood="calm")
    t.info_page(wb, "Learn", "What Emotions Actually Do",
                ["Emotions are signals from your brain and body. Fear says 'watch out,' anger says "
                 "'something feels unfair,' sadness says 'something matters and it hurt.' None of them "
                 "are 'bad' - they're data. The skill isn't turning emotions off; it's learning to read "
                 "them and choose your response.",
                 "During the teen years your brain is literally rewiring. The emotional part develops "
                 "faster than the part that hits the brakes - which is exactly why big feelings can feel "
                 "so intense and sudden. That's normal, and it's also why practicing these skills now "
                 "makes a real difference."],
                subhead="Three quick truths",
                bullets=["A feeling is not a fact or a command.",
                         "Feelings pass - even the big ones peak and fade.",
                         "You can feel something strongly and still choose what you do."])
    s.feelings_faces_color(wb, "Vocabulary", "Naming It Precisely",
                           [("angry", "Frustrated"), ("worried", "Anxious"), ("sad", "Disappointed"),
                            ("happy", "Content"), ("surprised", "Overwhelmed"), ("calm", "Settled")])
    t.info_page(wb, "Learn", "The Feeling Wave",
                ["Emotions tend to rise, peak, and fall like a wave - usually within about 90 seconds for "
                 "the first surge, if we don't keep feeding it with our thoughts. If you can ride the first "
                 "wave without acting on it, you often make far better choices.",
                 "'Riding the wave' doesn't mean ignoring the feeling. It means noticing it, breathing "
                 "through the peak, and letting it settle before you decide what to do."],
                subhead="Riding the wave",
                bullets=["Notice: 'A wave is starting.'",
                         "Breathe slowly through the peak.",
                         "Wait for it to settle before you act or speak."])
    wb.divider("Part 2: Knowing My Patterns",
               "Self-awareness is the first tool.", mood="worried")
    t.rating_scale(wb, "Self-Check", "My Emotion Habits",
                   "Rate how true each is for you right now. Notice - don't judge.",
                   ["I can name what I'm feeling when it happens.",
                    "I notice feelings in my body before they get huge.",
                    "I pause before reacting when I'm upset.",
                    "I bounce back after a bad mood in a reasonable time.",
                    "I ask for help when a feeling is too big.",
                    "I'm kind to myself when I mess up."])
    s.body_scan(wb)
    t.mood_tracker(wb)
    wb.divider("Part 3: My Coping Toolkit",
               "Tools you can actually use in the moment.", mood="calm")
    s.breathing_exercise(wb, "Breathe", "Box Breathing", "Box Breathing",
                         ["Breathe in for 4 as you trace up.", "Hold for 4 across the top.",
                          "Breathe out for 4 down the side.", "Hold for 4 across the bottom.",
                          "Repeat until the wave settles."], shape="square")
    t.coping_menu(wb, "Toolkit", "My Coping Menu",
                  "There's no single 'right' tool. Tick the ones you want to try, and star the ones that work.",
                  COPING_MENU)
    t.stress_log(wb)
    wb.divider("Part 4: Rewiring My Thinking",
               "Change the thought, change the feeling.", mood="surprised")
    t.unhelpful_thinking(wb)
    t.thought_reframe(wb)
    wb.divider("Part 5: Real-Life Scenarios",
               "Practice choosing your response.", mood="worried")
    s.scenario_page(wb, "Scenarios", "What Would You Do? (1)",
                    ["You get a bad grade and feel like giving up on the whole subject.",
                     "A friend leaves you on read and your mind races to the worst.",
                     "You snap at a family member and feel guilty afterward."])
    s.scenario_page(wb, "Scenarios", "What Would You Do? (2)",
                    ["You feel jealous seeing others' posts and your mood drops.",
                     "You're overwhelmed by everything due this week.",
                     "Someone criticizes you in front of others."])
    return finish(wb, "01_Regulate_Teens_Guide_to_Managing_Big_Emotions.pdf")


# =====================================================================
# BOOK 2 — Under Pressure: Stress & Anxiety Coping Workbook for Teens
# =====================================================================
def book2():
    toc = ["Understanding Stress & Anxiety", "My Stress Signals", "Calming the Body",
           "Calming the Mind", "Managing Pressure", "Reflection & Plan"]
    wb = start("Under Pressure",
               "A Stress & Anxiety Coping Workbook for Teens",
               s.OCEAN, s.PEACH, toc)
    wb.divider("Part 1: Understanding Stress & Anxiety",
               "Your alarm system, explained.", mood="worried")
    t.info_page(wb, "Learn", "Stress Isn't All Bad",
                ["Stress is your body getting ready to meet a challenge - a pounding heart before a game "
                 "or a test can actually help you focus. The problem is when the alarm won't switch off, "
                 "or fires when there's no real danger. That's when stress tips into anxiety.",
                 "Anxiety is like a smoke alarm that goes off at burnt toast: the feeling is real, but the "
                 "danger often isn't as big as it feels. Learning to check 'real threat or false alarm?' is "
                 "a core skill in this book."],
                subhead="Signs the alarm is overworking",
                bullets=["Racing thoughts or constant 'what ifs.'",
                         "Trouble sleeping or relaxing.",
                         "Avoiding things because they feel scary.",
                         "Physical stuff: tight chest, stomachaches, tension."])
    t.info_page(wb, "Learn", "The Stress-Performance Sweet Spot",
                ["A little pressure sharpens you; too much overwhelms you. Picture an upside-down U: "
                 "performance rises with some stress, peaks, then drops as stress becomes too much.",
                 "The goal isn't zero stress - it's finding your sweet spot and having tools to come back "
                 "down when you tip past it."],
                subhead="Coming back to the sweet spot",
                bullets=["Slow the body first (breathing, movement).",
                         "Break big tasks into small steps.",
                         "Challenge 'what if' thoughts with facts."])
    wb.divider("Part 2: My Stress Signals",
               "Catch it early, handle it easier.", mood="worried")
    t.rating_scale(wb, "Self-Check", "My Stress & Anxiety Check",
                   "Rate how often each has been true lately.",
                   ["My mind races with worries.",
                    "I feel tension or aches in my body.",
                    "I avoid things that make me anxious.",
                    "I have trouble sleeping because of worry.",
                    "I feel on edge or irritable.",
                    "Worry gets in the way of school or friends."],
                   low="Rarely", high="Very often")
    s.feelings_thermometer(wb, kicker="Stress Meter", heading="My Stress Thermometer")
    t.stress_log(wb)
    wb.divider("Part 3: Calming the Body",
               "Settle the body and the mind follows.", mood="calm")
    s.breathing_exercise(wb, "Breathe", "4-7-8 Breathing", "4-7-8 Breathing",
                         ["Breathe in through your nose for 4.",
                          "Hold gently for 7.",
                          "Breathe out slowly through your mouth for 8.",
                          "Repeat 4 times. Great before sleep or a test."], shape="triangle")
    p, y, n = wb.page("Grounding", "5-4-3-2-1 Grounding")
    y = wb.intro_box(p, y, "When anxiety spikes, grounding pulls you out of the 'what ifs' and back to right now "
                           "using your senses. Fill it in the next time you feel anxious.")
    for label in ["5 things I can SEE", "4 things I can FEEL/TOUCH", "3 things I can HEAR",
                  "2 things I can SMELL", "1 slow BREATH"]:
        p.set_fill(*wb.accent); p.text(s.MARGIN, y, label, 12, bold=True)
        y = wb.write_lines(p, y - 14, 1, spacing=22); y -= 6
    t.coping_menu(wb, "Toolkit", "Calm-the-Body Menu",
                  "Tick tools to try; star the ones that help.", COPING_MENU[:2] + [COPING_MENU[3]])
    wb.divider("Part 4: Calming the Mind",
               "Worry thoughts aren't facts.", mood="surprised")
    t.unhelpful_thinking(wb)
    t.thought_reframe(wb)
    p2, y2, n2 = wb.page("Worry Tool", "Worry Time & the 'Control' Sort")
    y2 = wb.intro_box(p2, y2, "Two tools that shrink worry: set a short daily 'worry time' so worries don't run all "
                              "day, and sort worries into what you CAN and CAN'T control - then act only on what you can.")
    y2 = wb.subhead(p2, y2, "Things I can control")
    y2 = wb.write_lines(p2, y2, 3, spacing=25)
    y2 = wb.subhead(p2, y2, "Things I can't control (practice letting these go)")
    wb.write_lines(p2, y2, 3, spacing=25)
    wb.divider("Part 5: Managing Pressure",
               "Handle real pressures with a plan.", mood="worried")
    s.scenario_page(wb, "Scenarios", "Pressure Situations (1)",
                    ["You have three deadlines and a test in the same week.",
                     "You feel panicky before speaking or performing in front of people.",
                     "You're lying awake at night with a racing mind."])
    s.scenario_page(wb, "Scenarios", "Pressure Situations (2)",
                    ["You feel pressure to be perfect and it's exhausting.",
                     "Everyone seems to have it together except you.",
                     "A big decision is stressing you out."])
    t.action_plan(wb, "Plan", "My Anti-Stress Toolkit Plan",
                  "Build your go-to plan for stressful stretches.",
                  [("My earliest stress signals are:", 2),
                   ("Body-calming tools I'll use:", 1),
                   ("Mind-calming tools I'll use:", 1),
                   ("How I'll break big tasks down:", 2)])
    return finish(wb, "02_Under_Pressure_Stress_and_Anxiety_Coping_Workbook_for_Teens.pdf")


BUILDERS = [book1, book2]

if __name__ == "__main__":
    from sel_teen_books_3_10 import BUILDERS_3_10
    ok = True
    for b in BUILDERS + BUILDERS_3_10:
        ok &= report(b())
    print("\n" + ("ALL >=42 & VALID" if ok else "SOME FAILED"))
