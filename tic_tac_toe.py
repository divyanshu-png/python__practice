import streamlit as st
import numpy as np

def initialize_game():
    return np.full((3,3), ''), 'X'

def check_winner(board):
    for i in range(3):
        if board[i,0]==board[i,1]== board[i,2]!=' ':
            return board[i,0]
        if board[0,i]==board[1,i]==board[2,i]!=" ":
            return board[0,i]
    if board[0,0]==board[1,1]==board[2,2]!=' ':
        return board[0,0]
    if board[0,2]==board[1,1]==board[2,0]!=" ":
        return board[0,2]
    return None

# def display_board(board):
#     for i in rangefd