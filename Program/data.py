from whaaaaat import style_from_dict, Token
from enum import Enum

START_MONEY = 1500
SALARY = 1500
MAX_TURN = 100
DICE = [[1,2,3], [1,2,4], [1,3,4], [2,3,4]]

class BoardColor(Enum):
    BG = "\x1b[6;37;40m"
    END ='\x1b[0m'        # reset
    P1 = '\x1b[6;31;40m'
    P2 = '\x1b[6;32;40m'
    P3 = '\x1b[6;33;40m'
    P4 = '\x1b[6;34;40m'
    P5 = '\x1b[6;35;40m'
    P6 = '\x1b[6;36;40m'


property_data = [
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
ask_how_many_player = [
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
game_rule_back = [
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
no_effect_block = [
    {
        'type': 'list',
        'name': 'ans',
        'message': 'This block has no effect, Pass or Save Game ?',
        'choices': [
            'Pass !',
            'Save Game !'
        ]
    } 
]

enter_roll_dice = [
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

enter_property = [
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

enter_jail = [
    {
        'type': 'list',
        'name': 'ans',
        'message': '',
        'choices': [
            'Roll dice twice !',
            'Pay the fine !',
            'Save Game'
        ]
    }
]

game_logo = [
    '  __  __                               _',
    " |  \/  | ___  _ __   ___  _ __   ___ | |_   _  ",
    " | |\/| |/ _ \| '_ \ / _ \| '_ \ / _ \| | | | | ",
    " | |  | | (_) | | | | (_) | |_) | (_) | | |_| | ",
    " |_|  |_|\___/|_| |_|\___/| .__/ \___/|_|\__, | ",
    "                          |_|            |___/  "
]


rule = [
    'MOVING AROUND THE BOARD',
    'A maximum of 6, minimum of 2 players are required to play The Monopoly Game.',
    '''On your turn, you roll the dice and move your token forward (clockwise around the edge of the board) the same number of spaces as the sum of the dice you rolled''',
    'You must then follow the instructions of whatever space your token lands on.',
    'Rule 1: If you land on GO or pass over it while moving your token, you collect $1500.',
    'Rule 2: If you land on Free Parking, nothing bad (or good) happens to you - it\'s just a "free" resting space, you can save your game here.',
    'Rule 3: If you land on Income Tax, you must calculate 10% of the value of everything you own and pay that much money to the Bank.',
    'Rule 4: If you land on Chance, you may earn money or lost money',
    'Rule 5: If you land on a property that no player owns, you may buy it from the Bank at the price printed on the board. Or you may also pass or save the game.',
    'Rule 6: If you land on a property another player owns, you must pay them the rent that is printed on the board.',
    'Rule 7: If you land on a Go to Jail, you must go to In Jail',
    '',
    'In JAIL',
    'You can Roll dice twice or Pay the fine',
    'If you roll a double for your turn, you get to leave Jail and move your token as normal. However, even though you rolled doubles, you don\'t get another turn.',
    'Pay a fine of $150 to the Bank to leave Jail and move forward according to your roll. If you don\'t roll doubles for three turns in a row, you must pay $150 to bank.',
    '',
    'END OF THE GAME',
    'If your money less than 0, you are bankrupt!',
    'If the turn is less than 100:',
    'After all but one of the players have been eliminated, the last remaining player wins.',
    'If the turn is 100:',
    'The players who have the most money will wins.'
    ]