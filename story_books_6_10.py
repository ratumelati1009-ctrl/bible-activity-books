"""
story_books_6_10.py — Social-story books 6-10, 42+ pages each.
Reuses helpers from build_story_books.py.
"""

import workbook_story as w
from build_story_books import (
    start, finish, _one_kid, _two_kids, _kid_and_adult,
)


# =====================================================================
# BOOK 6 — Waiting Patiently and Taking Turns (3-7) : story + matching game
# =====================================================================
def book6():
    toc = ["The Story: My Turn Will Come", "Waiting Feelings", "Matching Game",
           "Turtle Breathing", "What Would You Do?", "My Waiting Ideas", "My Certificate"]
    wb = start("Waiting Patiently and Taking Turns",
               "A Social Story With a Matching Game", "Ages 3-7",
               "Story + matching game", w.MINT, w.ORANGE, toc)
    wb.section("The Story", "My Turn Will Come", mood="worried")
    wb.story(_one_kid("worried"), ["Sometimes I have to WAIT.",
                                   "Waiting can feel hard. I want my turn NOW."])
    wb.story(_one_kid("worried"), ["When I wait, my body feels wiggly.",
                                   "My feelings can feel big and bubbly inside."])
    wb.story(_one_kid("calm"), ["Waiting is easier when I know my turn WILL come.",
                                "Good things are worth waiting for."])
    wb.story(_two_kids("happy", "calm"), ["Taking turns means everyone gets a chance.",
                                          "First my friend, then me. That is fair and kind."])
    wb.story(_one_kid("calm"), ["While I wait, I can keep my body busy.",
                                "I can count, hum a song, or wiggle my fingers quietly."])
    wb.story(_one_kid("calm"), ["I can take a slow breath and say, 'I can wait.'",
                                "Waiting gets easier every time I practice."])
    wb.story(_two_kids("happy", "happy"), ["And then - it is my turn!",
                                           "Waiting patiently helped me and my friend both have fun."])
    w.feelings_faces(wb, "Feelings", "How Waiting Feels",
                     [("worried", "Impatient"), ("angry", "Frustrated"), ("sad", "Bored"),
                      ("calm", "Patient"), ("happy", "Hopeful"), ("excited", "Excited")])
    w.matching(wb, "Game", "Matching Game: Waiting Helpers",
               ["Count slowly", "Hum a song", "Take a breath", "Watch and cheer"],
               ["1-2-3-4-5", "la-la-la", "in... out...", "you can do it!"],
               "Draw a line to match each waiting helper to what it looks like.")
    w.matching(wb, "Game", "Matching Game: Whose Turn?",
               ["First", "Next", "Then", "Last"],
               ["1st", "2nd", "3rd", "4th"],
               "Match the turn words to the order they come in.")
    w.breathing_card(wb, "Turtle Breathing",
                     ["Pull your head and shoulders in slowly like a shy turtle - breathe in.",
                      "Slowly poke back out - breathe out.",
                      "Go nice and slow, like a calm turtle.",
                      "Do it a few times while you wait."], shape="flower")
    w.scenario_page(wb, "Think It Through", "What Would You Do?",
                    ["You want the swing but another child is on it.",
                     "You are waiting for your turn to talk.",
                     "Dinner is not ready yet and you are hungry."])
    w.journal_page(wb, "My Ideas", "My Waiting Ideas",
                   ["Fun things I can do while I wait are...",
                    "Words I can say to myself are...",
                    "A time I waited patiently was..."])
    return finish(wb, "06_Waiting_Patiently_and_Taking_Turns.pdf",
                  "for learning to wait patiently and take turns!")


# =====================================================================
# BOOK 7 — Handling Losing and Disappointment (5-10) : scenario cards + worksheets
# =====================================================================
def book7():
    toc = ["The Story: When I Don't Win", "Disappointed Feelings", "Scenario Cards",
           "Calm-Down Breathing", "Worksheets", "My Good-Sport Plan", "My Certificate"]
    wb = start("Handling Losing and Disappointment",
               "Scenario Cards and Worksheets to Practice Being a Good Sport", "Ages 5-10",
               "Scenario cards + worksheets", w.INDIGO, w.GOLD, toc)
    wb.section("The Story", "When Things Don't Go My Way", mood="sad")
    wb.story(_one_kid("sad"), ["Sometimes I lose a game, or things don't go my way.",
                               "It feels DISAPPOINTING - like a heavy, sinking feeling."])
    wb.story(_one_kid("sad"), ["Disappointment is a real feeling, and it's okay to feel it.",
                               "Even grown-ups feel it. It does not mean anything is wrong with me."])
    wb.story(_one_kid("angry"), ["Sometimes losing makes me want to quit, cry, or get angry.",
                                 "Those big feelings make sense. But I get to choose what I do next."])
    wb.story(_one_kid("calm"), ["First, I take a slow breath and name it: 'I feel disappointed.'",
                                "Naming the feeling helps it feel a little smaller."])
    wb.story(_two_kids("calm", "happy"), ["I can be a good sport.",
                                          "I can say 'good game' and mean it, even when I lose."])
    wb.story(_one_kid("calm"), ["Losing is a chance to learn.",
                                "I can ask, 'What can I try differently next time?'"])
    wb.story(_one_kid("happy"), ["One game does not decide who I am.",
                                 "I can enjoy playing, win or lose. Trying again is what matters."])
    w.feelings_faces(wb, "Feelings", "Disappointed Feelings",
                     [("sad", "Disappointed"), ("angry", "Frustrated"), ("worried", "Discouraged"),
                      ("calm", "Calmer"), ("happy", "Proud to Try"), ("excited", "Ready Again")])
    w.cards_page(wb, "Scenario Cards", "Good-Sport Scenario Cards",
                 "Cut out and talk through each card. What is a good-sport choice?",
                 [("You lose a race", "You worked hard but came last. What now?"),
                  ("Game night loss", "You lose a board game to your sibling."),
                  ("Not picked", "You don't get chosen for the part you wanted."),
                  ("Rained out", "Your big plan gets cancelled."),
                  ("Lower score", "You got a lower grade than you hoped."),
                  ("Friend wins", "Your friend beats you at your favorite game.")], cardh=86)
    w.breathing_card(wb, "Calm-Down Breathing",
                     ["Breathe in slowly for 4.", "Breathe out slowly for 6 - longer than the in-breath.",
                      "Feel the disappointment settle a little.", "Repeat until you feel calmer."], shape="triangle")
    w.journal_page(wb, "Worksheet", "Turning a Loss Into a Lesson",
                   ["A time I felt disappointed was...",
                    "What I did with that feeling...",
                    "What I could try differently next time..."])
    w.journal_page(wb, "My Plan", "My Good-Sport Plan",
                   ["When I lose, I can say...",
                    "To calm my body I can...",
                    "One thing I am proud of, win or lose, is..."])
    return finish(wb, "07_Handling_Losing_and_Disappointment.pdf",
                  "for being a good sport and handling disappointment!")


# =====================================================================
# BOOK 8 — Making Friends and Joining a Group (5-9) : social story + conversation cards
# =====================================================================
def book8():
    toc = ["The Story: Joining In", "Friendly Faces", "Conversation Cards",
           "Friendly Words", "What Would You Do?", "My Friendship Plan", "My Certificate"]
    wb = start("Making Friends and Joining a Group",
               "A Social Story With Conversation Cards", "Ages 5-9",
               "Social story + conversation cards", w.ROSE, w.SUN, toc)
    wb.section("The Story", "How to Join In", mood="worried")
    wb.story(_one_kid("worried"), ["Sometimes I see other kids playing.",
                                   "I want to join, but I feel nervous. What if they say no?"])
    wb.story(_one_kid("calm"), ["Feeling nervous about joining in is normal.",
                                "Lots of kids feel exactly the same way."])
    wb.story(_one_kid("calm"), ["First, I watch for a moment to see what they are playing.",
                                "Then I walk over with a friendly face and a smile."])
    wb.story(_two_kids("happy", "worried"), ["I can say a friendly hello.",
                                             "'Hi! Can I play too?' or 'That looks fun - what are you playing?'"])
    wb.story(_two_kids("happy", "happy"), ["Sometimes they say yes right away.",
                                           "I join in, take turns, and follow the game they are already playing."])
    wb.story(_one_kid("worried"), ["Sometimes they say 'not right now.'",
                                   "That feels disappointing, but it is not about me. I can try again or find someone else."])
    wb.story(_two_kids("happy", "happy"), ["Being a good friend means listening, sharing, and being kind.",
                                           "Friends are made a little at a time."])
    wb.story(_one_kid("happy"), ["Every time I practice, joining in gets easier.",
                                 "I can be brave and friendly. I can make friends!"])
    w.feelings_faces(wb, "Feelings", "Friendly Feelings",
                     [("worried", "Nervous"), ("calm", "Brave"), ("happy", "Friendly"),
                      ("sad", "Left Out"), ("excited", "Excited"), ("happy", "Included")])
    w.cards_page(wb, "Conversation Cards", "Conversation Starter Cards",
                 "Cut out and practice these friendly things to say.",
                 [("Say hello", "'Hi, I'm ___. What's your name?'"),
                  ("Ask to join", "'That looks fun. Can I play too?'"),
                  ("Give a compliment", "'I really like your drawing!'"),
                  ("Ask a question", "'What are you playing?'"),
                  ("Offer to share", "'Do you want to use this with me?'"),
                  ("Invite them", "'Want to play together?'")], cardh=86)
    w.tracing_page(wb, "Words", "Friendly Words to Trace",
                   ["Can I play too?", "Hi, my name is...", "Want to play?"])
    w.scenario_page(wb, "Think It Through", "What Would You Do?",
                    ["A group is playing a game you'd like to join.",
                     "You said hi but the kid seemed shy and didn't answer.",
                     "You feel left out at recess."])
    w.journal_page(wb, "My Plan", "My Friendship Plan",
                   ["A friendly thing I can say to join in is...",
                    "If someone says 'not now,' I can...",
                    "One way I can be a good friend is..."])
    return finish(wb, "08_Making_Friends_and_Joining_a_Group.pdf",
                  "for being brave and friendly when making friends!")


# =====================================================================
# BOOK 9 — Safe Ways to Handle Big Feelings (4-8) : calm-down toolkit
# =====================================================================
def book9():
    toc = ["The Story: My Big Feelings", "Feelings Faces", "My Calm-Down Toolkit Cards",
           "Breathing Cards", "Where I Feel It", "What Would You Do?", "My Certificate"]
    wb = start("Safe Ways to Handle Big Feelings",
               "A Calm-Down Toolkit Social Story", "Ages 4-8",
               "Calm-down toolkit", w.TEAL, w.PEACH, toc)
    wb.section("The Story", "Big Feelings Are Okay", mood="worried")
    wb.story(_one_kid("worried"), ["I have BIG feelings sometimes.",
                                   "Anger, worry, sadness - they can feel huge inside me."])
    wb.story(_one_kid("worried"), ["All feelings are okay to have.",
                                   "Feelings are like waves - they get big, then they pass."])
    wb.story(_one_kid("angry"), ["But big feelings can make me want to do unsafe things,",
                                 "like hitting, yelling, or throwing. Those choices can hurt."])
    wb.story(_one_kid("calm"), ["So I have a toolkit of SAFE ways to handle big feelings.",
                                "A tool is something I can do to help my body calm down."])
    wb.story(_one_kid("calm"), ["I can breathe slowly, squeeze something soft, or take a break.",
                                "I can move my body, draw, or ask for a hug."])
    wb.story(_kid_and_adult("calm"), ["I can tell a safe grown-up how I feel.",
                                      "'I feel...' helps them help me."])
    wb.story(_one_kid("happy"), ["When I use my tools, my big feeling gets smaller.",
                                 "I stay safe, and so does everyone around me."])
    wb.story(_one_kid("happy"), ["I am learning which tools work best for ME.",
                                 "I am the boss of my body, even when feelings are big."])
    w.feelings_faces(wb, "Feelings", "My Big Feelings",
                     [("angry", "Angry"), ("worried", "Worried"), ("sad", "Sad"),
                      ("surprised", "Overwhelmed"), ("calm", "Calm"), ("happy", "Okay Again")])
    w.cards_page(wb, "Toolkit Cards", "My Calm-Down Toolkit Cards",
                 "Cut out your toolkit cards. Try each one and keep your favorites close.",
                 [("Slow Breaths", "Breathe in slow, out slower."),
                  ("Squeeze", "Squeeze a pillow or stress ball."),
                  ("Take a Break", "Go to a calm, quiet spot."),
                  ("Move", "Stomp, jump, or stretch it out."),
                  ("Draw It", "Draw or scribble your feeling."),
                  ("Ask for a Hug", "Ask a safe grown-up for a hug.")], cardh=86)
    w.breathing_card(wb, "Belly Breathing",
                     ["Put a hand on your belly.", "Breathe in slowly and feel it rise.",
                      "Breathe out slowly and feel it fall.", "Do it until your body feels calmer."], shape="square")
    p, y, n = wb.page("Body", "Where I Feel My Feelings")
    y = wb.intro_box(p, y, "Big feelings show up in our bodies. Color or mark where you feel yours. There are no "
                           "wrong answers.")
    # simple body outline
    import workbook_story as _w
    top = y - 10
    p.set_stroke(0.13, 0.14, 0.17); p.set_line_width(1.8)
    bx = 56 + 110
    p.circle(bx, top - 30, 26, fill=False, stroke=True)
    p.round_rect(bx - 40, top - 170, 80, 115, 22, fill=False, stroke=True)
    p.line(bx - 40, top - 110, bx - 78, top - 150)
    p.line(bx + 40, top - 110, bx + 78, top - 150)
    p.line(bx - 18, top - 170, bx - 30, top - 250)
    p.line(bx + 18, top - 170, bx + 30, top - 250)
    kx = bx + 130; ky = top - 20
    p.set_fill(0.13, 0.14, 0.17); p.text(kx, ky, "Color where you feel:", 11, bold=True)
    for (label, color) in [("Hot / angry", _w.CORAL), ("Fluttery / worried", _w.GOLD),
                           ("Heavy / sad", _w.SKY), ("Calm / good", _w.MINT)]:
        ky -= 30
        p.set_fill(*color); p.circle(kx + 8, ky + 3, 8, fill=True, stroke=False)
        p.set_fill(0.13, 0.14, 0.17); p.text(kx + 24, ky, label, 10.5)
    w.scenario_page(wb, "Think It Through", "What Would You Do?",
                    ["You feel so angry you want to hit something.",
                     "You feel worried and your tummy hurts.",
                     "You feel sad and want to be alone."])
    return finish(wb, "09_Safe_Ways_to_Handle_Big_Feelings.pdf",
                  "for learning safe ways to handle big feelings!")


# =====================================================================
# BOOK 10 — Solving Conflicts With Kind Words (6-10) : role-play game + workbook
# =====================================================================
def book10():
    toc = ["The Story: Working It Out", "Conflict Feelings", "Role-Play Game Cards",
           "Kind Words to Trace", "Worksheets", "My Peace Plan", "My Certificate"]
    wb = start("Solving Conflicts With Kind Words",
               "A Role-Play Game and Workbook for Peaceful Problem-Solving", "Ages 6-10",
               "Role-play game + workbook", w.BLUE, w.SUN, toc)
    wb.section("The Story", "Working It Out Together", mood="angry")
    wb.story(_two_kids("angry", "angry"), ["Sometimes I disagree with someone.",
                                           "We both want different things, and it turns into a conflict."])
    wb.story(_one_kid("angry"), ["Conflict can make me feel angry or upset.",
                                 "Those feelings are normal. Everyone has conflicts sometimes."])
    wb.story(_one_kid("calm"), ["The first step is to CALM DOWN before I talk.",
                                "I take a breath so my thinking brain can help me."])
    wb.story(_two_kids("calm", "calm"), ["Then we take turns talking AND listening.",
                                         "I use 'I feel...' words instead of blaming or yelling."])
    wb.story(_two_kids("calm", "worried"), ["I try to understand the other person too.",
                                            "'How do you feel? What do you want?' Listening helps a lot."])
    wb.story(_two_kids("calm", "calm"), ["Together we look for a fair fix.",
                                         "Maybe we share, take turns, trade, or find a new idea."])
    wb.story(_two_kids("happy", "happy"), ["Kind words solve more problems than mean words ever could.",
                                           "We worked it out, and we are still friends."])
    wb.story(_one_kid("happy"), ["If we get stuck, we can ask a grown-up to help us fix it.",
                                 "Solving problems with kind words feels good."])
    w.feelings_faces(wb, "Feelings", "Conflict Feelings",
                     [("angry", "Angry"), ("worried", "Upset"), ("sad", "Hurt"),
                      ("calm", "Calmer"), ("happy", "Understood"), ("happy", "Friends Again")])
    w.cards_page(wb, "Role-Play Game", "Role-Play Game Cards",
                 "Play the game: draw a card, act out the conflict, and solve it with kind words.",
                 [("Same toy", "You both want the same toy."),
                  ("Cutting in", "Someone says you cut in line."),
                  ("Different games", "You want different games at recess."),
                  ("Broken by accident", "A friend breaks your thing by accident."),
                  ("Both right?", "You disagree about the rules."),
                  ("Left out", "A friend feels left out by you.")], cardh=86)
    w.tracing_page(wb, "Words", "Kind Words to Trace",
                   ["I feel...", "Let's take turns.", "Can we share?"])
    w.journal_page(wb, "Worksheet", "The Peace Steps",
                   ["Step 1 - How I calm down first...",
                    "Step 2 - What I say using 'I feel...'...",
                    "Step 3 - A fair fix we could try..."])
    w.journal_page(wb, "My Plan", "My Peace Plan",
                   ["When I have a conflict, I will first...",
                    "Kind words I can use are...",
                    "If we get stuck, I can ask..."])
    return finish(wb, "10_Solving_Conflicts_With_Kind_Words.pdf",
                  "for solving conflicts with kind words!")


BUILDERS_6_10 = [book6, book7, book8, book9, book10]
