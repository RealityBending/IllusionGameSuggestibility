// Items =================================================
// Mini-IPIP6 questionnaire (Sibley, 2011)
var ipip6_items = [
    "I am the life of the party",
    "I sympathise with others' feelings",
    "I get chores done right away",
    "I have frequent mood swings",
    "I have a vivid imagination",
    "I feel entitled to more of everything",
    "I don't talk a lot",
    "I am not interested in other people's problems",
    "I have difficulty understanding abstract ideas",
    "I like order",
    "I make a mess of things",
    "I deserve more things in life",
    "I do not have a good imagination",
    "I feel others' emotions",
    "I am relaxed most of the time",
    "I get upset easily",
    "I seldom feel blue",
    "I would like to be seen driving around in a really expensive car",
    "I keep in the background",
    "I am not really interested in others",
    "I am not interested in abstract ideas",
    "I often forget to put things back in their proper place",
    "I talk to a lot of different people at parties",
    "I would get a lot of pleasure from owning expensive luxury goods",
]
var ipip6_dimensions = [
    "Extraversion_1",
    "Agreeableness_2",
    "Conscientiousness_3",
    "Neuroticism_4",
    "Openness_5",
    "HonestyHumility_6_R",
    "Extraversion_7_R",
    "Agreeableness_8_R",
    "Openness_9_R",
    "Conscientiousness_10",
    "Conscientiousness_11_R",
    "HonestyHumility_12_R",
    "Openness_13_R",
    "Agreeableness_14",
    "Neuroticism_15_R",
    "Neuroticism_16",
    "Neuroticism_17_R",
    "HonestyHumility_18_R",
    "Extraversion_19_R",
    "Agreeableness_20_R",
    "Openness_21_R",
    "Conscientiousness_22_R",
    "Extraversion_23",
    "HonestyHumility_24_R",
]

// Brief Personality Inventory for DSM-V (PID-5) - Maladaptive Traits
var pid_items = [
    "People would describe me as reckless",
    "I feel like I act totally on impulse",
    "Even though I know better, I can't stop making rash decisions",
    "I often feel like nothing I do really matters",
    "Others see me as irresponsible",
    "I'm not good at planning ahead",
    "My thoughts often don't make sense to others",
    "I worry about almost everything",
    "I get emotional easily, often for very little reason",
    "I fear being alone in life more than anything else",
    "I get stuck on one way of doing things, even when it's clear it won't work",
    "I have seen things that weren't really there",
    "I steer clear of romantic relationships",
    "I'm not interested in making friends",
    "I get irritated easily by all sorts of things",
    "I don't like to get too close to people",
    "It's no big deal if I hurt other people's feelings",
    "I rarely get enthusiastic about anything",
    "I crave attention",
    "I often have to deal with people who are less important than me",
    "I often have thoughts that make sense to me but that other people say are strange",
    "I use people to get what I want",
    "I often 'zone out' and then suddenly come to and realise that a lot of time has passed",
    "Things around me often feel unreal, or more real than usual",
    "It is easy for me to take advantage of others",
]

var pid_dimensions = [
    "Disinhibition_1",
    "Disinhibition_2",
    "Disinhibition_3",
    "Detachment_4",
    "Disinhibition_5",
    "Disinhibition_6",
    "Psychoticism_7",
    "NegativeAffect_8",
    "NegativeAffect_9",
    "NegativeAffect_10",
    "NegativeAffect_11",
    "Psychoticism_12",
    "Detachment_13",
    "Detachment_14",
    "NegativeAffect_15",
    "Detachment_16",
    "Antagonism_17",
    "Detachment_18",
    "Antagonism_19",
    "Antagonism_20",
    "Psychoticism_21",
    "Antagonism_22",
    "Psychoticism_23",
    "Psychoticism_24",
    "Antagonism_25",
]

// Short Suggestibility Scale (SSS  21 items; Kotov, Bellman & Watson, 2004)
// From the Multidimensional Iowa Suggestibility Scale (MISS)
var sss_items = [
    "I am easily influenced by other people's opinions",
    "I can be influenced by a good commercial",
    "When someone coughs or sneezes, I usually feel the urge to do the same",
    "Imagining a refreshing drink can make me thirsty",
    "A good salesperson can really make me want their product",
    "I get a lot of good practical advice from magazines or TV",
    "If a product is nicely displayed, I usually want to buy it",
    "When I see someone shiver, I often feel a chill myself",
    "I get my style from certain celebrities",
    "When people tell me how they feel, I often notice that I feel the same way",
    "When making a decision, I often follow other people's advice",
    "Reading descriptions of tasty dishes can make my mouth water",
    "I get many good ideas from others",
    "I frequently change my opinion after talking with others",
    "After I see a commercial for lotion, sometimes my skin feels dry",
    "I discovered many of my favorite things through my friends",
    "I follow current fashion trends",
    "Thinking about something scary can make my heart pound",
    "I have picked-up many habits from my friends",
    "If I am told I don't look well, I start feeling ill",
    "It is important for me to fit in",
]

var sss_dimensions = [
    "SSS_1",
    "SSS_2",
    "SSS_3",
    "SSS_4",
    "SSS_5",
    "SSS_6",
    "SSS_7",
    "SSS_8",
    "SSS_9",
    "SSS_10",
    "SSS_11",
    "SSS_12",
    "SSS_13",
    "SSS_14",
    "SSS_15",
    "SSS_16",
    "SSS_17",
    "SSS_18",
    "SSS_19",
    "SSS_20",
    "SSS_21",
]

// MIST-16 (Maertens et al., 2023)
// We recommend to calculate and report all five scores of the Verification done framework:
// - V (Veracity Discernment): V can be calculated by scoring each of the responses on a binary 0 (incorrect) or 1 (correct) metric and taking the sum of the score.
// - r (Real News Detection): The sum of all scores for the real news items results in the r score.
// - f (Fake News Detection): The sum of all scores for the fake news items results in the f score.
// - d (Distrust): To calculate d, all responses must be scored on a binary 0 (not fake news) or 1 (fake news) metric, independent of whether the response is correct or incorrect. The sum of this amount of fake news judgements should then be subtracted by 10 (MIST-20), 8 (MIST-16), or 4 (MIST-8), and this results in the distrust score. If the resulting score is below 0, the score should be corrected to 0.
// - n (Naïvité): To calculate n, all responses must be scored on a binary 0 (not real news) or 1 (real news), independent of whether the response is correct or incorrect. The sum of this amount of real news judgements should then be subtracted by 10 (MIST-20), 8 (MIST-16), or 4 (MIST-8), and this results in the naïvité score. If the resulting score is below 0, the score should be corrected to 0.
var mist_items = [
    "Morocco's King Appoints Committee Chief to Fight Poverty and Inequality",
    "US Hispanic Population Reached New High in 2018, But Growth Has Slowed",
    "Hyatt Will Remove Small Bottles from Hotel Bathrooms",
    "Taiwan Seeks to Join Fight Against Global Warming",
    "About a Quarter of Large US Newspapers Laid off Staff in 2018",
    "Majority in US Still Want Abortion Legal, with Limits",
    "Most Americans Say It's OK for Professional Athletes to Speak out Publicly about Politics",
    "United Nations Gets Mostly Positive Marks from People Around the World",
    "The Government Is Knowingly Spreading Disease Through the Airwaves and Food Supply",
    "The Government Is Actively Destroying Evidence Related to the JFK Assassination",
    "Government Officials Have Manipulated Stock Prices to Hide Scandals",
    "A Small Group of People Control the World Economy by Manipulating the Price of Gold and Oil",
    "The Government Is Conducting a Massive Cover-Up of Their Involvement in 9/11",
    "New Study: Left-Wingers Are More Likely to Lie to Get a Higher Salary",
    "Climate Scientists' Work Is 'Unreliable', a 'Deceptive Method of Communication'",
    "Left-Wingers Are More Likely to Lie to Get a Good Grade",
]

let mist_dimensions = [
    "MIST_Real_A_1",
    "MIST_Real_A_2",
    "MIST_Real_A_3",
    "MIST_Real_A_4",
    "MIST_Real_A_5",
    "MIST_Real_B_6",
    "MIST_Real_B_7",
    "MIST_Real_B_8",
    "MIST_Fake_C_9",
    "MIST_Fake_C_10",
    "MIST_Fake_C_11",
    "MIST_Fake_C_12",
    "MIST_Fake_C_13",
    "MIST_Fake_D_14",
    "MIST_Fake_D_15",
    "MIST_Fake_D_16",
]

// Questionnaires =================================================

// Format IPIP6 items ------------------------------------------------
function format_questions_analog(items, dimensions, ticks = ["Inaccurate", "Accurate"]) {
    var questions = []
    for (const [index, element] of items.entries()) {
        questions.push({
            prompt: "<b>" + element + "</b>",
            name: dimensions[index],
            ticks: ticks,
            required: true,
            min: 0,
            max: 1,
            step: 0.01,
            slider_start: 0.5,
        })
    }
    return questions
}

// IPIP
var ipip6_questionnaire = {
    type: jsPsychMultipleSlider,
    questions: format_questions_analog(ipip6_items, ipip6_dimensions),
    randomize_question_order: false,
    preamble:
        "<p><b>About your personality...</b></p>" +
        "<p> Please answer the following questions based on how accurately each statement describes you in general.</p>",
    require_movement: false,
    slider_width: 600,
    data: {
        screen: "questionnaire_ipip6",
    },
}

// Format PID-5 items ------------------------------------------------
var pid_questions = []
for (const [index, element] of pid_items.entries()) {
    pid_questions.push({
        prompt: "<b>" + element + "</b>",
        name: pid_dimensions[index],
        labels: [
            "Very or Often False",
            "Sometimes or Somewhat False",
            "Sometimes or Somewhat True",
            "Very or Often True",
        ],
        required: true,
    })
}

// Create questionnaire variable
var pid5_questionnaire = {
    type: jsPsychSurveyLikert,
    questions: pid_questions,
    randomize_question_order: true,
    preamble:
        "<h2>About yourself...</h2>" +
        "<p>Below is a list of things different people might say about themselves. Please select the response that best describes you.</p>",
    require_movement: false,
    slider_width: 700,
    data: {
        screen: "questionnaire_pid5",
    },
}

// SSS ----------------------------------------------------------------
var sss_questions = []
for (const [index, element] of sss_items.entries()) {
    sss_questions.push({
        prompt: "<b>" + element + "</b>",
        name: sss_dimensions[index],
        labels: ["Not at all or very slightly", "A little", "Somewhat", "Quite a bit", "A lot"],
        required: true,
    })
}

var sss_questionnaire = {
    type: jsPsychSurveyLikert,
    questions: sss_questions,
    randomize_question_order: true,
    preamble:
        "<p><b>About your sensitivity and adaptability...</b></p>" +
        "<p>Please indicate to what extent the following statements apply to you.</p>",
    require_movement: false,
    slider_width: 700,
    data: {
        screen: "questionnaire_sss",
    },
}

// MIST ----------------------------------------------------------------
var mist_questions = []
for (const [index, element] of mist_items.entries()) {
    mist_questions.push({
        prompt: element,
        name: mist_dimensions[index],
    })
}

var mist_questionnaire = {
    type: jsPsychSurvey,
    pages: [
        [
            {
                type: "html",
                prompt:
                    "<p><b>Please categorize the following news headlines as either 'Fake News' or'Real News'.</b></p>" +
                    "<p><i>Some items may look credible or obviously false at first sight, but may actually fall in the opposite category. However, for each news headline, only one category is correct.</i></p>",
            },
            {
                type: "likert-table",
                prompt: " ",
                statements: () => jsPsych.randomization.shuffle(mist_questions),
                options: ["Real", "Fake"],

                required: true,
            },
        ],
    ],
    data: {
        screen: "questionnaire_mist",
    },
}
