from typing import List
import Config
from Player import *
from Block import *



class GameBoard:
    def __init__(self, players : List[Player], blocks):
        self.turn = 1
        self.players = players
        self.blocks = blocks
        self.setCurrentPlayer(players[0])
        self.jailList = []

    def setCurrentPlayer(self, player : Player):
        self.currentPlayer = player

    #print text 
    def p_Text(self):
        string = ''
        MAX = 6
        for i in range(len(self.players)):
            if i == max:
                break
            string += ('P' + str(i+1)+ " "+Config.BoardColor[f'P{i+1}'].value + '♣' + Config.BoardColor.END.value +"   ")

        for i in range(MAX-len(self.players)):
            string += "       "
        return string

    def p_turn_Text(self):
        string = ''
        if self.turn < 10:
            string += str(self.turn) + '  ' 
        elif self.turn < 100:
            string += str(self.turn) + ' '
        else:
            string += str(self.turn)

        return string

    def p_chess_Text(self):
        currentNo = self.currentPlayer.playerNumber
        string = Config.BoardColor[f'P{currentNo}'].value + '♣' + Config.BoardColor.END.value
        return string

    # set turn, for loading save
    def setRound(self,num):
        self.turn = num

    # add turn by 1
    def addRound(self):
        self.turn += 1
        # if turn > max, end game
        if self.turn >= Config.MAX_TURN:
            #END GAME
            #TODO
            print("END GAME")


    # sort player by money
    def sort_ranking(self):
        return sorted(self.players, key=lambda x: x.money, reverse=True)

    def check_Rank(self, rankedPlayer : List[Player], pos):
        rank = []
        lastRank = 1
        for index, player in enumerate(rankedPlayer):
            if index == 0:
                rank.append(lastRank)
                continue
            else:
                if player.money == rankedPlayer[index-1].money:
                    rank.append(lastRank)
                else:
                    lastRank += 1
                    rank.append(lastRank)

        try:
            moneyStr = str(rankedPlayer[pos].money)

            while len(moneyStr) < 11:
                moneyStr += ' '
            n = str(rankedPlayer[pos].playerNumber)

            return str(rank[pos]) + ' │ P' + n + " " + Config.BoardColor[f'P{str(n)}'].value + '♣' +Config.BoardColor.END.value + ' │ $'+ moneyStr
        except:
            return '- │      │             '

    # def test_jailList(self):
    #     a = Player(1,1500,1)
    #     a.jailLeft = 2

    #     b = Player(2,1340,1)
    #     b.jailLeft = 3

    #     self.jailList.append(a)
    #     self.jailList.append(b)

    def print_jail_list(self, pos):
        # test
        # if not self.jailList:
        #     self.test_jailList()

        if self.jailList:
            try:
                n = self.jailList[pos].playerNumber
                return 'P' + str(n) + ' ' + Config.BoardColor[f'P{str(n)}'].value + '♣' +Config.BoardColor.END.value + ' │ ' + str(self.jailList[pos].jailLeft)+ ' Turn(s) Left '
            except:
                return '     │                '
        else:
            return '     │                '

    def p_owner(self,block):
        if block.owner == 'None':
            return 'None'
        else:
            return 'P' + str(block.owner.playerNumber) + '  '

    def p_chess(self, position,pNum):
        try:
            for player in self.players:
                if player.playerNumber == pNum and player.position == position:
                    return Config.BoardColor[f'P{str(pNum)}'].value + '♣' + Config.BoardColor.END.value
            return ' '
        except:
            return ' '

    def print_board(self):
        rankedPlayer = self.sort_ranking()

        print(f"╔════════════════════╦════════════════════╦════════════════════╦════════════════════╦════════════════════╦════════════════════╗")
        print(f"║                    ║                    ║                    ║                    ║                    ║                    ║")
        print(f"║ {self.p_chess(10,1)}                {self.p_chess(10,4)} ║ {self.p_chess(11,1)}    {self.blocks[11].name}      {self.p_chess(11,4)} ║ {self.p_chess(12,1)}                {self.p_chess(12,4)} ║ {self.p_chess(13,1)}    {self.blocks[13].name}    {self.p_chess(13,4)} ║ {self.p_chess(14,1)}    {self.blocks[14].name}      {self.p_chess(14,4)} ║ {self.p_chess(15,1)}                {self.p_chess(15,4)} ║")
        print(f"║                    ║                    ║       {self.blocks[12].name}       ║                    ║                    ║                    ║")
        print(f"║ {self.p_chess(10,2)}     {self.blocks[10].name}       {self.p_chess(10,5)} ║ {self.p_chess(11,2)}    HKD:{self.blocks[11].price}     {self.p_chess(11,5)} ║ {self.p_chess(12,2)}                {self.p_chess(12,5)} ║ {self.p_chess(13,2)}    HKD:{self.blocks[13].price}     {self.p_chess(13,5)} ║ {self.p_chess(14,2)}    HKD:{self.blocks[14].price}     {self.p_chess(14,5)} ║ {self.p_chess(15,2)}   {self.blocks[15].name}   {self.p_chess(15,5)} ║")
        print(f"║      {self.blocks[10].subText}       ║      Rent:{self.blocks[11].rent}       ║         {self.blocks[12].subText}          ║      Rent:{self.blocks[13].rent}       ║      Rent:{self.blocks[14].rent}       ║                    ║")
        print(f"║ {self.p_chess(10,3)}                {self.p_chess(10,6)} ║ {self.p_chess(11,3)}                {self.p_chess(11,6)} ║ {self.p_chess(12,3)}                {self.p_chess(12,6)} ║ {self.p_chess(13,3)}                {self.p_chess(13,6)} ║ {self.p_chess(14,3)}                {self.p_chess(14,6)} ║ {self.p_chess(15,3)}                {self.p_chess(15,6)} ║")
        print(f"║                    ║    Owner: {self.p_owner(self.blocks[11])}     ║                    ║    Owner: {self.p_owner(self.blocks[13])}     ║    Owner: {self.p_owner(self.blocks[14])}     ║                    ║")
        print(f"╠════════════════════╬════════════════════╩════════════════════╩════════════════════╩════════════════════╬════════════════════╣")
        print(f"║                    ║                                                                                   ║                    ║")
        print(f"║ {self.p_chess(9,1)}   {self.blocks[9].name}     {self.p_chess(9,4)} ║                                                                                   ║ {self.p_chess(16,1)}    {self.blocks[16].name}    {self.p_chess(16,4)} ║")
        print(f"║                    ║                                                                                   ║                    ║")
        print(f"║ {self.p_chess(9,2)}    HKD:{self.blocks[9].price}     {self.p_chess(9,5)} ║                                                                                   ║ {self.p_chess(16,2)}    HKD:{self.blocks[16].price}     {self.p_chess(16,5)} ║")
        print(f"║      Rent:{self.blocks[9].rent}       ║                         ┌──────────────────────────┐                              ║      Rent:{self.blocks[16].rent}       ║")
        print(f"║ {self.p_chess(9,3)}                {self.p_chess(9,6)} ║                         │ This Round : Player {self.currentPlayer.playerNumber}  {self.p_chess_Text()} │                              ║ {self.p_chess(16,3)}                {self.p_chess(16,6)} ║")
        print(f"║    Owner: {self.p_owner(self.blocks[9])}     ║                         │                          │                              ║    Owner: {self.p_owner(self.blocks[16])}     ║")
        print(f"╠════════════════════╣                         │     Turn: {self.p_turn_Text()}/100        │                              ╠════════════════════╣")
        print(f"║                    ║                         └──────────────────────────┘                              ║                    ║")
        print(f"║ {self.p_chess(8,1)}                {self.p_chess(8,4)} ║                                                                                   ║ {self.p_chess(17,1)}   {self.blocks[17].name}    {self.p_chess(17,4)} ║")
        print(f"║       {self.blocks[8].name}       ║      ┌────────────────────────────┐               ┌───────────────────────┐       ║                    ║")
        print(f"║ {self.p_chess(8,2)}                {self.p_chess(8,5)} ║      │         Ranking:           │               │        In Jail        │       ║ {self.p_chess(17,2)}    HKD:{self.blocks[17].price}     {self.p_chess(17,5)} ║")
        print(f"║         {self.blocks[8].subText}          ║      ├───────┬──────┬─────────────┤               ├──────┬────────────────┤       ║      Rent:{self.blocks[17].rent}       ║")
        print(f"║ {self.p_chess(8,3)}                {self.p_chess(8,6)} ║      │  No.{self.check_Rank(rankedPlayer,0)}│               │ {self.print_jail_list(0)}│       ║ {self.p_chess(17,3)}                {self.p_chess(17,6)} ║")
        print(f"║                    ║      │  No.{self.check_Rank(rankedPlayer,1)}│               │ {self.print_jail_list(1)}│       ║    Owner: {self.p_owner(self.blocks[17])}     ║")
        print(f"╠════════════════════╣      │  No.{self.check_Rank(rankedPlayer,2)}│               │ {self.print_jail_list(2)}│       ╠════════════════════╣")
        print(f"║                    ║      │  No.{self.check_Rank(rankedPlayer,3)}│               │ {self.print_jail_list(3)}│       ║                    ║")
        print(f"║ {self.p_chess(7,1)}   {self.blocks[7].name}     {self.p_chess(7,4)} ║      │  No.{self.check_Rank(rankedPlayer,4)}│               │ {self.print_jail_list(4)}│       ║ {self.p_chess(18,1)}                {self.p_chess(18,4)} ║")
        print(f"║                    ║      │  No.{self.check_Rank(rankedPlayer,5)}│               │ {self.print_jail_list(5)}│       ║       {self.blocks[18].name}       ║")
        print(f"║ {self.p_chess(7,2)}    HKD:{self.blocks[7].price}     {self.p_chess(7,5)} ║      └───────┴──────┴─────────────┘               └──────┴────────────────┘       ║ {self.p_chess(18,2)}                {self.p_chess(18,5)} ║")
        print(f"║      Rent:{self.blocks[7].rent}       ║                                                                                   ║         {self.blocks[18].subText}          ║")
        print(f"║ {self.p_chess(7,3)}                {self.p_chess(7,6)} ║                                                                                   ║ {self.p_chess(18,3)}                {self.p_chess(18,6)} ║")
        print(f"║    Owner: {self.p_owner(self.blocks[7])}     ║                                                                                   ║                    ║")
        print(f"╠════════════════════╣                                                                                   ╠════════════════════╣")
        print(f"║                    ║                                                                                   ║                    ║")
        print(f"║ {self.p_chess(6,1)}    {self.blocks[6].name}      {self.p_chess(6,4)} ║                                                                                   ║ {self.p_chess(19,1)}     {self.blocks[19].name}      {self.p_chess(19,4)} ║")
        print(f"║                    ║                      {self.p_Text()}                   ║                    ║")
        print(f"║ {self.p_chess(6,2)}    HKD:{self.blocks[6].price}     {self.p_chess(6,5)} ║                                                                                   ║ {self.p_chess(19,2)}    HKD:{self.blocks[19].price}     {self.p_chess(19,5)} ║")
        print(f"║      Rent:{self.blocks[6].rent}       ║                                                                                   ║      Rent:{self.blocks[19].rent}       ║")
        print(f"║ {self.p_chess(6,3)}                {self.p_chess(6,6)} ║                                                                                   ║ {self.p_chess(19,3)}                {self.p_chess(19,6)} ║")
        print(f"║    Owner: {self.p_owner(self.blocks[6])}     ║                                                                                   ║    Owner: {self.p_owner(self.blocks[19])}     ║")
        print(f"╠════════════════════╬════════════════════╦════════════════════╦════════════════════╦════════════════════╬════════════════════╣")
        print(f"║                    ║                    ║                    ║                    ║                    ║                    ║")
        print(f"║ {self.p_chess(5,1)}   ┌───────┐    {self.p_chess(5,4)} ║ {self.p_chess(4,1)}    {self.blocks[4].name}     {self.p_chess(4,4)} ║ {self.p_chess(3,1)}   {self.blocks[3].name}   {self.p_chess(3,4)} ║ {self.p_chess(2,1)}   {self.blocks[2].name}     {self.p_chess(2,4)} ║ {self.p_chess(1,1)}    {self.blocks[1].name}     {self.p_chess(1,4)} ║ {self.p_chess(0,1)} (Salary:${Config.SALARY}) {self.p_chess(0,4)} ║")
        print(f"║     │{self.blocks[5].name}│      ║                    ║                    ║                    ║                    ║                    ║")
        print(f"║ {self.p_chess(5,2)}   └───────┘    {self.p_chess(5,5)} ║ {self.p_chess(4,2)}    HKD:{self.blocks[4].price}     {self.p_chess(4,5)} ║ {self.p_chess(3,2)}    {self.blocks[3].subText}     {self.p_chess(3,5)} ║ {self.p_chess(2,2)}   HKD:{self.blocks[2].price}      {self.p_chess(2,5)} ║ {self.p_chess(1,2)}    HKD:{self.blocks[1].price}     {self.p_chess(1,5)} ║ {self.p_chess(0,2)}       {self.blocks[0].name}       {self.p_chess(0,5)} ║")
        print(f"║   {self.blocks[5].subText}    ║      Rent:{self.blocks[4].rent}       ║                    ║     Rent:{self.blocks[2].rent}        ║      Rent:{self.blocks[1].rent}       ║                    ║")
        print(f"║ {self.p_chess(5,3)}                {self.p_chess(5,6)} ║ {self.p_chess(4,3)}                {self.p_chess(4,6)} ║ {self.p_chess(3,3)}                {self.p_chess(3,6)} ║ {self.p_chess(2,3)}                {self.p_chess(2,6)} ║ {self.p_chess(1,3)}                {self.p_chess(1,6)} ║ {self.p_chess(0,3)}   {self.blocks[0].subText}   {self.p_chess(0,6)} ║")
        print(f"║                    ║    Owner: {self.p_owner(self.blocks[4])}     ║                    ║    Owner: {self.p_owner(self.blocks[2])}     ║    Owner: {self.p_owner(self.blocks[1])}     ║                    ║")
        print(f"╚════════════════════╩════════════════════╩════════════════════╩════════════════════╩════════════════════╩════════════════════╝")

    def run(self):

        while self.turn < MAX_TURN:
            self.print_board()
            pos = self.currentPlayer.position
            self.blocks[pos].activateBlockEffect(self.currentPlayer, self)

            #Add turn
            #self.turn += 1
            #Next Player
            #get next player
            currentPlayerNo = self.currentPlayer.playerNumber
            count = 0
            while True:
                newNo = currentPlayerNo + 1
                count += 1
                
                #if out of bound, reset to first player
                try:
                    found = False
                    for player in self.players:
                        if player.playerNumber == newNo:
                            nextPlayer = player
                            found = True
                            break
                    
                    if not found:
                        self.turn += 1
                        nextPlayer = self.players[0]

                except:
                    self.turn += 1
                    nextPlayer = self.players[0]

                if nextPlayer.isAlive():
                    self.currentPlayer = nextPlayer
                    break

                #if all dead
                if count >= len(self.players):
                    print("END GAME")
                    exit()
            
            
