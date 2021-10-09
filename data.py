from whaaaaat import style_from_dict, Token

Property_Data = [
    {
        "Position" : 0,
        "Name": "Go",
        "SubText" : "<---------",
        "Type" : 'Start'
    },
    {
        "Position" : 1,
        "Name" : "Central",
        "Type" : "Property",
        "Price": 800,
        "Rent" : 90
    },
    {
        "Position" : 2,
        "Name" : "Wan Chai",
        "Type" : "Property",
        "Price": 700,
        "Rent" : 65
    },
    {
        "Position" : 3,
        "Name" : "Income Tax",
        "SubText" : "Pay 10%",
        "Type" : "IncomeTax",
        'Tax' : 10
    },
    {
        "Position" : 4,
        "Name" : "Stanley",
        "Type" : "Property",
        "Price": 600,
        "Rent" : 60
    },
    {
        "Position" : 5,
        "Name" : "In Jail",
        "SubText" : "Just Visiting",
        "Type" : "Jail",
        'Fine' : 150,
        'Turn' : 3
    },
        {
        "Position" : 6,
        "Name" : "Shek O",
        "Type" : "Property",
        "Price": 400,
        "Rent" : 10
    },
    {
        "Position" : 7,
        "Name" : "Mong Kok",
        "Type" : "Property",
        "Price": 500,
        "Rent" : 40
    },
    {
        "Position" : 8,
        "Name" : "Chance",
        "Type" : "Chance",
        "SubText" : "?",
        "min" : -300,
        "max" : 200
    },
    {
        "Position" : 9,
        "Name" : "Tsing Yi",
        "Type" : "Property",
        "Price": 400,
        "Rent" : 15
    },
    {
        "Position" : 10,
        "Name" : "Free",
        "SubText" : "Parking",
        "Type" : "FreeParking",
    },
    {
        "Position" : 11,
        "Name" : "Shatin",
        "Type" : "Property",
        "Price": 700,
        "Rent" : 75
    },
    {
        "Position" : 12,
        "Name" : "Chance",
        "Type" : "Chance",
        "SubText" : "?",
        "min" : -300,
        "max" : 200
    },
    {
        "Position" : 13,
        "Name" : "Tuen Mun",
        "Type" : "Property",
        "Price": 400,
        "Rent" : 20
    },
    {
        "Position" : 14,
        "Name" : "Tai Po",
        "Type" : "Property",
        "Price": 500,
        "Rent" : 25
    },
    {
        "Position" : 15,
        "Name" : "Go To Jail",
        "Type" : "GoToJail",
        "JailPosition" : 5,
        'Fine' : 150,
        'Turn' : 3
    },
    {
        "Position" : 16,
        "Name" : "Sai Kung",
        "Type" : "Property",
        "Price": 400,
        "Rent" : 10
    },
    {
        "Position" : 17,
        "Name" : "Yuen Long",
        "Type" : "Property",
        "Price": 400,
        "Rent" : 25
    },
    {
        "Position" : 18,
        "Name" : "Chance",
        "Type" : "Chance",
        "SubText" : "?",
        "min" : -300,
        "max" : 200
    },
    {
        "Position" : 19,
        "Name" : "Tai O",
        "Type" : "Property",
        "Price": 600,
        "Rent" : 25
    },
]

# whaaaaat style
style = style_from_dict({
    Token.Separator: '#6C6C6C',
    Token.QuestionMark: '#FF9D00 bold',
    Token.Selected: '#5F819D',
    Token.Pointer: '#FF9D00 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#5F819D bold',
    Token.Question: '',
})

# in main
AskHowManyPlayer = [
    {
        'type': 'list',
        'name': 'ans',
        'message': 'How Many Players ? (Use Arrow Key)',
        'choices': [
            '2',
            '3',
            '4',
            '5',
            '6'
        ]
    },
]

# in menu
questions = [
    {
        'type': 'list',
        'name': 'select',
        'message': 'Menu ',
        'choices': [
            'New Game',
            'Continue',
            'Check Game Rule',
            'Exit'
        ]
    },
]

# in menu
gameRuleBack = [
    {
        'type': 'list',
        'name': 'choice',
        'message': '',
        'choices': [
            'Back'
        ]
    },
]

# in Block
enter_RollDice = [
    {
        'type': 'list',
        'name': 'ans',
        'message': '',
        'choices': [
            'Roll !',
            'Save Game'
        ]
    }
]

enter_Property = [
    {
        'type': 'list',
        'name': 'ans',
        'message': '',
        'choices': [
            #'Buy !',
            #'Pass !',
            #'Save Game'
        ]
    }
]