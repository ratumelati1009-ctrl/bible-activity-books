"""
sel_teen_books_3_10.py — Teen SEL books 3-10 (ages 10-19), 42+ pages each.
Reuses shared helpers from build_sel_teen_books.py.
"""

import workbook_sel as s
import workbook_sel_teen as t
from build_sel_teen_books import start, finish, COPING_MENU


# =====================================================================
# BOOK 3 — Scroll Smart: Social Media, Mood & Mental Health Workbook
# =====================================================================
def book3():
    toc = ["How Social Media Affects Mood", "My Digital Habits", "Comparison & Self-Worth",
           "Healthier Online Habits", "Real-Life Scenarios", "Reflection & Plan"]
    wb = start("Scroll Smart",
               "Social Media, Mood & Mental Health - A Workbook for Teens",
               s.SKY, s.CORAL, toc)
    wb.divider("Part 1: How Social Media Affects Mood",
               "The apps are designed to keep you scrolling.", mood="surprised")
    t.info_page(wb, "Learn", "Why It's So Hard to Put Down",
                ["Social apps are engineered to hold your attention. Likes, streaks, and endless feeds give "
                 "little hits of dopamine that keep you coming back - it's not a lack of willpower, it's "
                 "design. Knowing that puts you back in charge.",
                 "Social media isn't all bad: it connects us, informs us, and can be creative and fun. The "
                 "goal isn't to quit forever - it's to use it on purpose instead of on autopilot, and to "
                 "notice how it affects your mood."],
                subhead="Signs it's hurting more than helping",
                bullets=["You feel worse about yourself after scrolling.",
                         "You lose track of time or lose sleep.",
                         "You compare your life to everyone's highlight reel.",
                         "You feel anxious when you can't check it."])
    t.info_page(wb, "Learn", "The Highlight Reel Trap",
                ["People mostly post their best moments - the wins, the good angles, the fun. Comparing your "
                 "behind-the-scenes to someone else's highlight reel is a rigged game you can't win.",
                 "What you see is curated, filtered, and often staged. Remembering that protects your mood "
                 "when the comparison monster shows up."],
                subhead="Reality check",
                bullets=["A post is a chosen moment, not a whole life.",
                         "Filters and edits are everywhere.",
                         "Everyone has struggles they don't post."])
    wb.divider("Part 2: My Digital Habits",
               "Notice your patterns without judgment.", mood="worried")
    t.rating_scale(wb, "Self-Check", "My Social Media Check-In",
                   "Rate how true each has been lately.",
                   ["I check my phone first thing and last thing daily.",
                    "I feel worse about myself after scrolling.",
                    "I lose more time online than I meant to.",
                    "I compare myself to people I follow.",
                    "I feel anxious without my phone.",
                    "Screen time cuts into my sleep."],
                   low="Rarely", high="Very often")
    t.mood_tracker(wb, kicker="Track", heading="Mood vs. Screen-Time Tracker")
    wb.divider("Part 3: Comparison & Self-Worth",
               "Your worth isn't a number of likes.", mood="calm")
    t.unhelpful_thinking(wb)
    t.thought_reframe(wb, kicker="Reframe", heading="Reframing Comparison Thoughts")
    t.reflection_journal(wb, "Reflect", "Who Am I Offline?",
                         ["List things about you that no post could capture.",
                          "When do you feel most like yourself - and is a screen involved?"])
    wb.divider("Part 4: Healthier Online Habits",
               "Use it on purpose.", mood="calm")
    p, y, n = wb.page("Habits", "Design Your Digital Boundaries")
    y = wb.intro_box(p, y, "Small boundaries make a big difference. Tick the ones you'll try, then write your own.")
    y = wb.checklist(p, y, ["No phone for the first/last 30 minutes of the day.",
                            "Turn off non-essential notifications.",
                            "Unfollow accounts that make me feel worse.",
                            "Phone out of the bedroom at night.",
                            "Set a daily time limit on my heaviest app.",
                            "Follow accounts that inspire or teach me."], box=True)
    y = wb.subhead(p, y, "My two digital boundaries this week")
    wb.write_lines(p, y, 3, spacing=26)
    t.coping_menu(wb, "Instead", "Things to Do Instead of Scrolling",
                  "When you catch yourself reaching for the phone out of boredom or stress, try one of these.",
                  COPING_MENU)
    wb.divider("Part 5: Real-Life Scenarios",
               "Handle the tricky online moments.", mood="worried")
    s.scenario_page(wb, "Scenarios", "Online Situations (1)",
                    ["You see friends hanging out without you in a post.",
                     "A photo of you gets posted that you don't like.",
                     "You feel down comparing yourself to an influencer."])
    s.scenario_page(wb, "Scenarios", "Online Situations (2)",
                    ["Someone leaves a mean comment or DM.",
                     "You keep checking for likes and feel let down.",
                     "A group chat gets heated or exclusionary."])
    t.action_plan(wb, "Plan", "My Scroll-Smart Plan",
                  "Make your plan for a healthier relationship with your phone.",
                  [("Times/places I'll keep phone-free:", 2),
                   ("Accounts I'll unfollow or mute:", 2),
                   ("What I'll do when comparison hits:", 2),
                   ("One offline thing I want more of:", 1)])
    return finish(wb, "03_Scroll_Smart_Social_Media_Mood_and_Mental_Health_Workbook.pdf")


# =====================================================================
# BOOK 4 — Know Your Worth: Self-Esteem & Confidence Workbook
# =====================================================================
def book4():
    toc = ["Understanding Self-Esteem", "My Inner Voice", "Strengths & Identity",
           "Building Confidence", "Real-Life Scenarios", "Reflection & Plan"]
    wb = start("Know Your Worth",
               "A Self-Esteem & Confidence Workbook for Teens",
               s.PURPLE, s.GOLD, toc)
    wb.divider("Part 1: Understanding Self-Esteem",
               "Confidence is built, not born.", mood="happy")
    t.info_page(wb, "Learn", "What Self-Esteem Really Is",
                ["Self-esteem is how you value yourself. Healthy self-esteem doesn't mean thinking you're "
                 "better than everyone - it means knowing you have worth even when you fail, get rejected, "
                 "or aren't the best in the room.",
                 "Self-esteem isn't fixed. It grows through how you talk to yourself, the challenges you "
                 "take on, and the way you treat yourself when things go wrong. This book helps you build it."],
                subhead="Healthy self-esteem sounds like",
                bullets=["'I made a mistake' - not 'I am a mistake.'",
                         "'I can learn this' - not 'I'm just bad at everything.'",
                         "'I matter, even when I'm not perfect.'"])
    t.info_page(wb, "Learn", "The Inner Critic vs. the Inner Coach",
                ["Everyone has an inner voice. The inner critic tears you down: 'You're not good enough.' The "
                 "inner coach is honest but kind: 'That was hard - what can you learn?' You can't delete the "
                 "critic, but you can turn up the coach.",
                 "Talking to yourself the way you'd talk to a good friend is one of the most powerful "
                 "self-esteem skills there is."],
                subhead="Coaching yourself",
                bullets=["Would I say this to a friend? If not, don't say it to yourself.",
                         "Swap 'I can't' for 'I can't yet.'",
                         "Notice effort, not just results."])
    wb.divider("Part 2: My Inner Voice",
               "Catch the critic, coach yourself.", mood="surprised")
    t.rating_scale(wb, "Self-Check", "How I See Myself",
                   "Rate how true each feels right now.",
                   ["I like who I am, most of the time.",
                    "I can accept a compliment without brushing it off.",
                    "I treat myself kindly when I fail.",
                    "I don't need everyone's approval to feel okay.",
                    "I can name things I'm good at.",
                    "I believe I can grow and improve."])
    t.unhelpful_thinking(wb, kicker="Inner Critic", heading="How My Inner Critic Talks")
    t.thought_reframe(wb, kicker="Coach", heading="From Critic to Coach")
    wb.divider("Part 3: Strengths & Identity",
               "You are more than any one thing.", mood="happy")
    p, y, n = wb.page("Strengths", "My Strengths Inventory")
    y = wb.intro_box(p, y, "We often list our flaws easily but forget our strengths. Time to balance the scale. "
                           "Circle strengths you have, then add your own.")
    y = wb.checklist(p, y, ["Kind", "Funny", "Loyal", "Curious", "Creative", "Hard-working",
                            "Brave", "Good listener", "Honest", "Determined", "Caring", "Fair"], box=False)
    y = wb.subhead(p, y, "Three strengths I'm proud of - with an example of each")
    wb.write_lines(p, y, 4, spacing=26)
    t.reflection_journal(wb, "Identity", "The Real Me",
                         ["What do the people who love you value about you?",
                          "What are you proud of that has nothing to do with looks or grades?"])
    wb.divider("Part 4: Building Confidence",
               "Confidence grows by doing.", mood="calm")
    t.info_page(wb, "Learn", "Confidence Follows Action",
                ["We often wait to 'feel confident' before trying - but it usually works the other way. You "
                 "act (even nervously), you survive, and confidence grows. Courage comes first; confidence "
                 "follows.",
                 "Small brave steps stack up. Each one is proof to yourself that you can do hard things."],
                subhead="Building it",
                bullets=["Do one slightly-scary thing regularly.",
                         "Keep promises to yourself.",
                         "Collect evidence of times you coped."])
    t.action_plan(wb, "Practice", "My Confidence Challenge",
                  "Pick small, doable steps that stretch you a little.",
                  [("A small brave step I'll take this week:", 2),
                   ("How I'll talk to myself before and after:", 2),
                   ("Proof from my past that I can handle hard things:", 2)])
    wb.divider("Part 5: Real-Life Scenarios",
               "Confidence under pressure.", mood="worried")
    s.scenario_page(wb, "Scenarios", "Confidence Situations (1)",
                    ["You have to speak up in class or a group but feel scared.",
                     "Someone puts you down and you start to believe it.",
                     "You want to try out for something but fear failing."])
    s.scenario_page(wb, "Scenarios", "Confidence Situations (2)",
                    ["You compare yourself to a sibling or friend and feel small.",
                     "You made a mistake and want to hide.",
                     "A compliment makes you uncomfortable."])
    return finish(wb, "04_Know_Your_Worth_Self-Esteem_and_Confidence_Workbook.pdf")


# =====================================================================
# BOOK 5 — Ride the Wave: Understanding & Managing Anger for Teens
# =====================================================================
def book5():
    toc = ["Understanding Anger", "My Anger Signals & Triggers", "Cooling Down",
           "What's Under the Anger", "Real-Life Scenarios", "Reflection & Plan"]
    wb = start("Ride the Wave",
               "Understanding & Managing Anger - A Workbook for Teens",
               s.CORAL, s.GOLD, toc)
    wb.divider("Part 1: Understanding Anger",
               "Anger is normal; harm is optional.", mood="angry")
    t.info_page(wb, "Learn", "Anger Is a Messenger",
                ["Anger is a normal, healthy emotion - it often shows up when something feels unfair, when "
                 "you're hurt, or when a boundary gets crossed. Anger itself isn't the problem. What we DO "
                 "with it can be.",
                 "Managing anger doesn't mean never feeling it or stuffing it down. It means feeling it, "
                 "understanding its message, and expressing it in ways that don't damage you or others."],
                subhead="Anger often masks",
                bullets=["Hurt or embarrassment.",
                         "Fear or feeling out of control.",
                         "Feeling disrespected or unheard.",
                         "Exhaustion, hunger, or stress."])
    t.info_page(wb, "Learn", "The Anger Escalator",
                ["Anger usually builds in steps, like riding an escalator up: annoyed, frustrated, angry, "
                 "furious. The higher you go, the harder it is to think clearly. The trick is to notice the "
                 "early steps and step off before the top.",
                 "Once you're at the top (flooded), your thinking brain goes offline. That's why the best "
                 "move is often to pause and cool down BEFORE responding."],
                subhead="Stepping off early",
                bullets=["Learn your first warning signs.",
                         "Use a cool-down before you react.",
                         "Come back to the issue once you're calm."])
    wb.divider("Part 2: My Anger Signals & Triggers",
               "Know your warning signs.", mood="angry")
    s.feelings_thermometer(wb, kicker="Anger Meter", heading="My Anger Thermometer")
    s.body_scan(wb, kicker="Body", heading="Where I Feel Anger")
    t.stress_log(wb, kicker="Triggers", heading="My Anger Trigger Log")
    wb.divider("Part 3: Cooling Down",
               "Cool the body before you speak.", mood="calm")
    s.breathing_exercise(wb, "Breathe", "Cool-Down Breathing", "Slow Belly Breathing",
                         ["Breathe in slowly through your nose for 4.",
                          "Feel your belly (not chest) expand.",
                          "Breathe out for 6, longer than the in-breath.",
                          "Repeat until you step down the escalator."], shape="triangle")
    t.coping_menu(wb, "Toolkit", "Anger Cool-Down Menu",
                  "Tick tools to try in the heat of the moment; star what works.",
                  [("In the moment",
                    ["Walk away to cool off (say 'I need a minute').",
                     "Slow your breathing right down.",
                     "Count backward from 20.",
                     "Push against a wall or squeeze something."]),
                   ("Release the energy",
                    ["Go for a run or move hard for a few minutes.",
                     "Rip or scribble on scrap paper.",
                     "Blast and move to music."]),
                   ("After you cool down",
                    ["Use 'I feel...' statements instead of blame.",
                     "Fix what you can; repair if you hurt someone.",
                     "Figure out what the anger was really about."])])
    wb.divider("Part 4: What's Under the Anger",
               "Anger is often the tip of the iceberg.", mood="worried")
    t.thought_reframe(wb, kicker="Reframe", heading="Reframing Anger Thoughts")
    t.reflection_journal(wb, "Dig Deeper", "Under My Anger",
                         ["Think of a recent time you got angry. What was really underneath it?",
                          "What did you need in that moment that you weren't getting?"])
    wb.divider("Part 5: Real-Life Scenarios",
               "Practice the pause.", mood="angry")
    s.scenario_page(wb, "Scenarios", "Anger Situations (1)",
                    ["Someone blames you for something you didn't do.",
                     "A sibling takes or breaks your stuff.",
                     "You feel disrespected by a teacher or coach."])
    s.scenario_page(wb, "Scenarios", "Anger Situations (2)",
                    ["A friend spreads a rumor about you.",
                     "You lose an important game or competition.",
                     "Someone provokes you online."])
    t.action_plan(wb, "Plan", "My Anger Management Plan",
                  "Your plan for handling anger without regret.",
                  [("My earliest anger warning signs:", 2),
                   ("My go-to cool-down moves:", 1),
                   ("How I'll express anger without harm:", 2),
                   ("How I'll repair things if I slip:", 1)])
    return finish(wb, "05_Ride_the_Wave_Understanding_and_Managing_Anger_for_Teens.pdf")


# =====================================================================
# BOOK 6 — People Skills: Navigating Friendships, Conflict & Boundaries
# =====================================================================
def book6():
    toc = ["Understanding Relationships", "Communication Skills", "Boundaries",
           "Handling Conflict", "Real-Life Scenarios", "Reflection & Plan"]
    wb = start("People Skills",
               "Navigating Friendships, Conflict & Boundaries - A Teen Workbook",
               s.MINT, s.INDIGO, toc)
    wb.divider("Part 1: Understanding Relationships",
               "Good relationships are built on skills you can learn.", mood="happy")
    t.info_page(wb, "Learn", "What Makes a Healthy Friendship",
                ["Healthy friendships are two-way: respect, honesty, support, and give-and-take go both ways. "
                 "In healthy friendships you can be yourself, disagree without it ending everything, and count "
                 "on each other.",
                 "Unhealthy or one-sided friendships often leave you drained, anxious, or walking on "
                 "eggshells. Noticing the difference helps you invest in the right people."],
                subhead="Green flags vs. red flags",
                bullets=["Green: they respect your 'no' and celebrate your wins.",
                         "Green: you can be honest without fear.",
                         "Red: it's always about them, or you feel controlled.",
                         "Red: they pressure, guilt-trip, or put you down."])
    t.rating_scale(wb, "Self-Check", "How I Show Up With Others",
                   "Rate how true each is for you.",
                   ["I listen without planning my reply.",
                    "I can disagree respectfully.",
                    "I keep others' secrets and trust.",
                    "I can say 'no' when I need to.",
                    "I apologize and repair when I'm wrong.",
                    "I treat others how I want to be treated."])
    wb.divider("Part 2: Communication Skills",
               "How you say it matters.", mood="calm")
    t.info_page(wb, "Learn", "Passive, Aggressive, or Assertive?",
                ["Passive means burying your needs to keep the peace. Aggressive means pushing your needs at "
                 "others' expense. Assertive - the sweet spot - means expressing your needs honestly AND "
                 "respecting others.",
                 "Assertive communication uses calm, clear 'I' statements: 'I feel ___ when ___ because ___. "
                 "I'd like ___.' It's a skill worth practicing out loud."],
                subhead="The assertive formula",
                bullets=["Say what you feel, not just what they did wrong.",
                         "Be specific and calm.",
                         "Ask clearly for what you'd like."])
    p, y, n = wb.page("Practice", "'I' Statement Practice")
    y = wb.intro_box(p, y, "Turn blame into an 'I' statement. Fill in real situations from your life.")
    for _ in range(4):
        p.set_fill(*wb.accent); p.text(s.MARGIN, y, "I feel ___ when ___ because ___. I'd like ___.", 10.8, bold=True)
        y = wb.write_lines(p, y - 14, 2, spacing=24); y -= 8
    wb.divider("Part 3: Boundaries",
               "Boundaries protect relationships, not end them.", mood="worried")
    t.info_page(wb, "Learn", "Why Boundaries Are Healthy",
                ["A boundary is a limit that keeps you safe and respected. Saying 'no,' asking for space, or "
                 "not sharing something isn't mean - it's self-respect. People who care about you will "
                 "respect your boundaries.",
                 "You're allowed to have limits, and you don't owe everyone a long explanation. 'No' can be "
                 "a complete sentence, kindly said."],
                subhead="Boundaries can sound like",
                bullets=["'That doesn't work for me.'",
                         "'I'm not comfortable with that.'",
                         "'I need some time to myself.'"])
    t.boundaries_scripts(wb)
    wb.divider("Part 4: Handling Conflict",
               "Conflict handled well can make bonds stronger.", mood="worried")
    t.thought_reframe(wb, kicker="Reframe", heading="Reframing Conflict Thoughts")
    t.reflection_journal(wb, "Reflect", "A Conflict I'm Carrying",
                         ["Describe a conflict that's on your mind. What's your part in it?",
                          "What would a fair, respectful next step look like?"])
    wb.divider("Part 5: Real-Life Scenarios",
               "Practice people skills.", mood="worried")
    s.scenario_page(wb, "Scenarios", "Friendship Situations (1)",
                    ["A close friend keeps cancelling and you feel taken for granted.",
                     "Two friends want you to pick a side in their fight.",
                     "A friend pressures you to do something you don't want to."])
    s.scenario_page(wb, "Scenarios", "Friendship Situations (2)",
                    ["You feel left out of a group you used to belong to.",
                     "A friendship has become one-sided and draining.",
                     "You hurt a friend and need to make it right."])
    t.action_plan(wb, "Plan", "My People-Skills Plan",
                  "Your plan for healthier relationships.",
                  [("A boundary I need to set (and with whom):", 2),
                   ("An 'I' statement I want to practice:", 1),
                   ("How I'll handle conflict more calmly:", 2),
                   ("A relationship I want to invest in:", 1)])
    return finish(wb, "06_People_Skills_Friendships_Conflict_and_Boundaries.pdf")


# =====================================================================
# BOOK 7 — Bounce Back: Building Resilience & Coping Skills
# =====================================================================
def book7():
    toc = ["What Resilience Is", "My Coping Style", "Coping Toolkit",
           "Growth Mindset", "Real-Life Scenarios", "Reflection & Plan"]
    wb = start("Bounce Back",
               "Building Resilience & Coping Skills for Teens",
               s.OCEAN, s.SUN, toc)
    wb.divider("Part 1: What Resilience Is",
               "Resilience is a skill, not a personality.", mood="calm")
    t.info_page(wb, "Learn", "Bending Without Breaking",
                ["Resilience is the ability to cope with hard times and bounce back - not by never struggling, "
                 "but by adapting and recovering. Resilient people still feel pain, fear, and doubt; they've "
                 "just built skills to get through it.",
                 "The good news: resilience is learnable. Every hard thing you get through - with support and "
                 "the right tools - builds it, like a muscle."],
                subhead="Resilience is built by",
                bullets=["Strong connections with people you trust.",
                         "Coping skills you practice ahead of time.",
                         "A belief that you can grow and things can improve.",
                         "Taking care of your basics: sleep, food, movement."])
    t.rating_scale(wb, "Self-Check", "My Resilience Check",
                   "Rate how true each is right now.",
                   ["I can calm myself when I'm upset.",
                    "I have people I can lean on.",
                    "I believe hard times will pass.",
                    "I learn from setbacks instead of only dwelling.",
                    "I take care of my body's basics.",
                    "I can ask for help when I need it."])
    wb.divider("Part 2: My Coping Style",
               "Some coping helps; some just numbs.", mood="worried")
    t.info_page(wb, "Learn", "Helpful vs. Numbing Coping",
                ["When life gets hard, we all cope somehow. Helpful coping deals with the feeling or the "
                 "problem (talking, moving, planning, resting). Numbing coping just avoids it (endless "
                 "scrolling, isolating, lashing out) and often makes things worse later.",
                 "There's no shame in having some numbing habits - almost everyone does. The goal is to grow "
                 "the helpful ones so you reach for them first."],
                subhead="Ask yourself",
                bullets=["Does this help me now AND later?",
                         "Am I facing the feeling or just escaping it?",
                         "Would I suggest this to a friend?"])
    t.stress_log(wb, kicker="Log", heading="What I Do When Things Get Hard")
    wb.divider("Part 3: Coping Toolkit",
               "Build your kit before you need it.", mood="calm")
    s.breathing_exercise(wb, "Breathe", "Grounding Breath", "Star Breathing",
                         ["Trace up a point as you breathe in.",
                          "Trace down as you breathe out.",
                          "Move slowly around all five points.",
                          "Finish with one long, calm breath."], shape="star")
    t.coping_menu(wb, "Toolkit", "My Resilience Toolkit", "Tick what you'll try; star what works.", COPING_MENU)
    wb.divider("Part 4: Growth Mindset",
               "'I can't do it' vs. 'I can't do it yet.'", mood="happy")
    t.info_page(wb, "Learn", "The Power of 'Yet'",
                ["A growth mindset is believing your abilities can develop with effort and practice. A fixed "
                 "mindset says 'I'm just bad at this.' A growth mindset adds one word: 'I'm not good at this "
                 "YET.'",
                 "Setbacks stop being proof you're a failure and start being information about what to try "
                 "next. That shift builds serious resilience."],
                subhead="Growth-mindset self-talk",
                bullets=["'Mistakes help me learn.'",
                         "'This is hard, which means I'm growing.'",
                         "'I'll try a different strategy.'"])
    t.thought_reframe(wb, kicker="Reframe", heading="Turning Setbacks Into Lessons")
    wb.divider("Part 5: Real-Life Scenarios",
               "Bounce back in real life.", mood="worried")
    s.scenario_page(wb, "Scenarios", "Setback Situations (1)",
                    ["You worked hard but still failed a test.",
                     "You didn't make the team or get the role.",
                     "A friendship or relationship ended."])
    s.scenario_page(wb, "Scenarios", "Setback Situations (2)",
                    ["You're going through a big change (new school, move, family change).",
                     "You made a public mistake and feel embarrassed.",
                     "Everything feels like too much at once."])
    t.action_plan(wb, "Plan", "My Bounce-Back Plan",
                  "Your plan for getting through hard times.",
                  [("My support people (and how to reach them):", 2),
                   ("My top coping tools:", 1),
                   ("A growth-mindset phrase I'll use:", 1),
                   ("One way I'll care for my basics:", 1)])
    return finish(wb, "07_Bounce_Back_Building_Resilience_and_Coping_Skills.pdf")


# =====================================================================
# BOOK 8 — Quiet the Noise: Mindfulness & Calm for Teens
# =====================================================================
def book8():
    toc = ["What Mindfulness Is", "Noticing My Mind", "Breathing & Grounding",
           "Everyday Mindfulness", "Real-Life Scenarios", "Reflection & Plan"]
    wb = start("Quiet the Noise",
               "Mindfulness & Calm - A Practical Workbook for Teens",
               s.TEAL, s.LAVEN, toc)
    wb.divider("Part 1: What Mindfulness Is",
               "Paying attention, on purpose, without judging.", mood="calm")
    t.info_page(wb, "Learn", "Mindfulness Isn't Emptying Your Mind",
                ["Mindfulness doesn't mean stopping your thoughts or 'feeling zen' all the time. It means "
                 "noticing what's happening right now - your breath, your body, your thoughts - without "
                 "grabbing onto it or judging it.",
                 "Your mind will wander a thousand times; that's not failing. The practice is simply "
                 "noticing you've wandered and gently coming back. Over time it calms the mental noise."],
                subhead="Why bother?",
                bullets=["It lowers stress and helps you focus.",
                         "It creates a pause between feeling and reacting.",
                         "It helps you actually enjoy good moments.",
                         "It improves sleep and mood over time."])
    t.info_page(wb, "Learn", "The Busy Mind",
                ["Our minds love to time-travel: replaying the past (regret) or racing to the future (worry). "
                 "Very little stress lives in the actual present moment. Mindfulness gently brings you back "
                 "to now, where you can breathe and choose.",
                 "You don't need incense or an hour of silence. A single mindful minute counts."],
                subhead="Coming back to now",
                bullets=["Feel your feet on the floor.",
                         "Take three slow, noticed breaths.",
                         "Name what you're doing right now."])
    wb.divider("Part 2: Noticing My Mind",
               "Watch your thoughts like clouds.", mood="calm")
    t.rating_scale(wb, "Self-Check", "My Mind & Attention Check",
                   "Rate how true each has been lately.",
                   ["My mind races or won't switch off.",
                    "I get lost in worry about the future.",
                    "I replay the past a lot.",
                    "I find it hard to focus on one thing.",
                    "I miss the good moment because I'm distracted.",
                    "I struggle to relax or fall asleep."],
                   low="Rarely", high="Very often")
    t.reflection_journal(wb, "Notice", "What's on My Mind",
                         ["Do a 'brain dump': write whatever thoughts are buzzing right now.",
                          "Which of these can you set down for now, and which need action?"])
    wb.divider("Part 3: Breathing & Grounding",
               "Simple practices you can do anywhere.", mood="calm")
    s.breathing_exercise(wb, "Breathe", "Box Breathing", "Box Breathing",
                         ["Breathe in for 4 (trace up).", "Hold for 4 (across).",
                          "Out for 4 (down).", "Hold for 4 (across).", "Repeat 4-6 times."], shape="square")
    s.breathing_exercise(wb, "Breathe", "Finger Breathing", "Five-Finger Breathing",
                         ["Trace up a finger as you breathe in.",
                          "Trace down as you breathe out.",
                          "Move across all five fingers slowly.",
                          "Notice how your body feels after."], shape="star")
    p, y, n = wb.page("Grounding", "The 5 Senses Reset")
    y = wb.intro_box(p, y, "A quick way to drop into the present. Fill it in now, then use it anytime you feel scattered.")
    for label in ["5 things I can SEE", "4 things I can HEAR", "3 things I can FEEL",
                  "2 things I can SMELL", "1 thing I'm grateful for right now"]:
        p.set_fill(*wb.accent); p.text(s.MARGIN, y, label, 12, bold=True)
        y = wb.write_lines(p, y - 14, 1, spacing=22); y -= 6
    wb.divider("Part 4: Everyday Mindfulness",
               "Bring calm into ordinary moments.", mood="happy")
    p2, y2, n2 = wb.page("Practice", "Mindfulness in Daily Life")
    y2 = wb.intro_box(p2, y2, "You don't need extra time - just attention. Tick the mini-practices you'll try.")
    y2 = wb.checklist(p2, y2, ["Eat one meal slowly, actually tasting it.",
                               "Take three mindful breaths before school or bed.",
                               "Notice five things on a walk you usually ignore.",
                               "Listen to a song with full attention.",
                               "Feel the water and warmth while you shower.",
                               "Put the phone down and just be, for one minute."], box=True)
    y2 = wb.subhead(p2, y2, "The mini-practice I'll build into my day")
    wb.write_lines(p2, y2, 2, spacing=26)
    wb.divider("Part 5: Real-Life Scenarios",
               "Use calm when you need it.", mood="worried")
    s.scenario_page(wb, "Scenarios", "Calm Situations (1)",
                    ["Your mind won't stop racing at bedtime.",
                     "You feel panicky before a test or performance.",
                     "You're so distracted you can't get started."])
    s.scenario_page(wb, "Scenarios", "Calm Situations (2)",
                    ["You're overwhelmed and everything feels like too much.",
                     "You keep replaying an embarrassing moment.",
                     "You feel wound-up and can't relax."])
    t.action_plan(wb, "Plan", "My Calm Practice Plan",
                  "Make mindfulness a small daily habit.",
                  [("When I'll practice (a time that fits my day):", 1),
                   ("My go-to breathing or grounding tool:", 1),
                   ("A mindful moment I'll add to daily life:", 1),
                   ("How I'll come back when my mind wanders:", 2)])
    return finish(wb, "08_Quiet_the_Noise_Mindfulness_and_Calm_for_Teens.pdf")


# =====================================================================
# BOOK 9 — Motivated Mind: Focus, Goals & Beating Procrastination
# =====================================================================
def book9():
    toc = ["Understanding Motivation", "My Focus & Habits", "Goal-Setting",
           "Beating Procrastination", "Real-Life Scenarios", "Reflection & Plan"]
    wb = start("Motivated Mind",
               "Focus, Goals & Beating Procrastination - A Teen Workbook",
               s.INDIGO, s.LIME, toc)
    wb.divider("Part 1: Understanding Motivation",
               "Motivation follows action more than it leads it.", mood="happy")
    t.info_page(wb, "Learn", "Waiting to 'Feel Like It'",
                ["A trap many people fall into: waiting to feel motivated before starting. But motivation "
                 "often shows up AFTER you begin, not before. Starting - even badly, even for two minutes - "
                 "is usually what unlocks the momentum.",
                 "There are two kinds of motivation: outside rewards (grades, praise) and inside drivers "
                 "(curiosity, values, growth). Inside motivation lasts longer, so it helps to connect tasks "
                 "to something you actually care about."],
                subhead="Motivation myths vs. truths",
                bullets=["Myth: I need to feel motivated first. Truth: action creates motivation.",
                         "Myth: I should do it all at once. Truth: small steps beat big bursts.",
                         "Myth: I'm just lazy. Truth: usually it's fear, overwhelm, or no clear next step."])
    t.info_page(wb, "Learn", "Why We Procrastinate",
                ["Procrastination usually isn't laziness - it's often the brain avoiding a task that feels "
                 "hard, boring, unclear, or scary (fear of failing). Understanding the real reason helps you "
                 "pick the right fix.",
                 "The cure is rarely 'try harder.' It's usually 'make the first step smaller and clearer,' "
                 "or 'deal with the feeling that's making you avoid it.'"],
                subhead="Common procrastination causes",
                bullets=["The task feels too big - shrink it.",
                         "It's unclear - define the next tiny step.",
                         "Fear of doing it wrong - allow a rough draft.",
                         "Too many distractions - remove them."])
    wb.divider("Part 2: My Focus & Habits",
               "Notice what helps and what steals your focus.", mood="worried")
    t.rating_scale(wb, "Self-Check", "My Focus & Motivation Check",
                   "Rate how true each has been lately.",
                   ["I start tasks without endless delay.",
                    "I can focus without constantly checking my phone.",
                    "I break big tasks into steps.",
                    "I finish what I start.",
                    "I know why my goals matter to me.",
                    "I bounce back after an off day."])
    t.stress_log(wb, kicker="Track", heading="My Procrastination Log")
    wb.divider("Part 3: Goal-Setting",
               "Clear goals beat vague wishes.", mood="calm")
    t.info_page(wb, "Learn", "Make Goals SMART",
                ["A goal like 'do better in school' is too fuzzy to act on. SMART goals are Specific, "
                 "Measurable, Achievable, Relevant, and Time-bound - so you know exactly what to do and when "
                 "you've done it.",
                 "Break big goals into small milestones. Each small win fuels the next."],
                subhead="Fuzzy vs. SMART",
                bullets=["Fuzzy: 'Study more.'  SMART: 'Review 10 flashcards after dinner, Mon-Thu.'",
                         "Fuzzy: 'Get fit.'  SMART: 'Walk 20 minutes, 3 days this week.'"])
    t.values_goals(wb, kicker="Goals", heading="My Goal & Why It Matters")
    wb.divider("Part 4: Beating Procrastination",
               "Small steps, fewer distractions.", mood="calm")
    t.coping_menu(wb, "Toolkit", "Anti-Procrastination Toolkit",
                  "Tick strategies to try; star what works for you.",
                  [("Shrink it",
                    ["Do just the first 2 minutes.",
                     "Break the task into the smallest next step.",
                     "Lower the bar: allow a messy first attempt."]),
                   ("Focus it",
                    ["Work in short sprints (e.g. 25 min) then break.",
                     "Put your phone in another room.",
                     "Turn off notifications while you work."]),
                   ("Reward it",
                    ["Plan a small reward after finishing.",
                     "Track your streak of started tasks.",
                     "Tell someone your plan for accountability."])])
    t.thought_reframe(wb, kicker="Reframe", heading="Reframing 'I Can't Be Bothered'")
    wb.divider("Part 5: Real-Life Scenarios",
               "Get moving in real life.", mood="worried")
    s.scenario_page(wb, "Scenarios", "Motivation Situations (1)",
                    ["A big project is due and you keep putting it off.",
                     "You can't focus because your phone keeps pulling you away.",
                     "You feel overwhelmed and don't know where to start."])
    s.scenario_page(wb, "Scenarios", "Motivation Situations (2)",
                    ["You had one bad day and want to quit a goal entirely.",
                     "The task is boring but has to get done.",
                     "You're scared of doing it wrong, so you avoid it."])
    t.action_plan(wb, "Plan", "My Motivation Plan",
                  "Your plan to start, focus, and finish.",
                  [("A goal that matters to me:", 1),
                   ("The very next 2-minute step:", 1),
                   ("Distractions I'll remove:", 2),
                   ("My reward and accountability:", 1)])
    return finish(wb, "09_Motivated_Mind_Focus_Goals_and_Beating_Procrastination.pdf")


# =====================================================================
# BOOK 10 — Grounded: A Teen Journal for Mood, Stress & Self-Awareness
# =====================================================================
def book10():
    toc = ["How to Use This Journal", "Daily Check-Ins", "Weekly Reflections",
           "Feelings & Thoughts", "Growth & Gratitude", "My Plan"]
    wb = start("Grounded",
               "A Guided Teen Journal for Mood, Stress & Self-Awareness",
               s.OCEAN, s.PEACH, toc)
    wb.divider("Part 1: Getting Started",
               "Journaling makes the invisible visible.", mood="calm")
    t.info_page(wb, "Learn", "Why Journaling Helps",
                ["Writing about your thoughts and feelings sounds simple, but research shows it can lower "
                 "stress, improve mood, and help you understand yourself better. Getting a worry out of your "
                 "head and onto paper often shrinks it.",
                 "There's no right way to do this. Some days you'll write a lot, some days a line. Both count. "
                 "This journal gives you gentle prompts so you're never staring at a blank page."],
                subhead="Journaling tips",
                bullets=["Be honest - no one is grading this.",
                         "Don't worry about spelling or 'sounding deep.'",
                         "Even a few minutes helps.",
                         "Notice patterns over days and weeks."])
    t.mood_tracker(wb)
    wb.divider("Part 2: Daily Check-Ins",
               "A few minutes a day builds self-awareness.", mood="happy")
    for i in range(1, 4):
        p, y, nn = wb.page("Daily", f"Daily Check-In #{i}")
        y = wb.subhead(p, y, "Today my mood was... (and why)")
        y = wb.write_lines(p, y, 2, spacing=25)
        y = wb.subhead(p, y, "One thing that challenged me")
        y = wb.write_lines(p, y, 2, spacing=25)
        y = wb.subhead(p, y, "One thing that went okay or well")
        y = wb.write_lines(p, y, 2, spacing=25)
        y = wb.subhead(p, y, "One thing I'll try tomorrow")
        wb.write_lines(p, y, 1, spacing=25)
    wb.divider("Part 3: Weekly Reflections",
               "Zoom out and spot the patterns.", mood="calm")
    for i in range(1, 3):
        t.reflection_journal(wb, "Weekly", f"Weekly Reflection #{i}",
                             ["What was the highlight and the hardest part of my week?",
                              "What drained my energy, and what refilled it?"])
    wb.divider("Part 4: Feelings & Thoughts",
               "Understand what's going on inside.", mood="worried")
    t.unhelpful_thinking(wb)
    t.thought_reframe(wb)
    t.reflection_journal(wb, "Explore", "A Feeling I Want to Understand",
                         ["Pick a feeling that keeps showing up. When does it appear?",
                          "What might it be trying to tell you?"])
    wb.divider("Part 5: Growth & Gratitude",
               "Notice how far you've come.", mood="happy")
    s.gratitude_page(wb, kicker="Gratitude", heading="What I'm Grateful For")
    t.reflection_journal(wb, "Growth", "How I'm Changing",
                         ["What's something you handle better now than a year ago?",
                          "What kind of person are you becoming - and want to become?"])
    return finish(wb, "10_Grounded_Teen_Journal_for_Mood_Stress_and_Self-Awareness.pdf")


BUILDERS_3_10 = [book3, book4, book5, book6, book7, book8, book9, book10]
