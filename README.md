# chess-com-video-bot

Python script to create videos of your [Chess.com](https://www.chess.com/) games. It visits the chess.com website and logs in using your credential and navigates to your games archive and opens the first game of the archive and clicks on the auto-play button and starts screen recording the game.

## Usage

1. Clone this repository

    `git clone https://github.com/sankethsj/chess-com-video-bot.git`

2. Install necessary packages using below command

    `pip install -r requirments.txt`

3. Set the below two environment variables

    `CHESS_USERNAME=your-chess-com-username`
    
    `CHESS_PASSWORD=your-chess-com-password`
    
4. Run the script using below command

    `python main.py`
