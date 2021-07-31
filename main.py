import numpy as np
from scipy.optimize import minimize
import pandas as pd
import csv

import KazuhaCharacter
import KazuhaSkills
import EnemyCharacter
import ExportData
import Weapon

# USER INPUT
inputParametersChar = ['Kazuha', '90']
inputParametersEnemy = ['Hilichurl','90']
inputWeaponName = 'BlackcliffPole'
inputWeaponNameList = "BlackcliffSlasher,PrototypeArchaic,Rainslasher,RoyalGreatsword,SerpentSpine,TheBell,WhiteBlind,SacrificialGreatsword,Snow-TombedStarsilver,FavoniusGreatsword,LithicBlade,SkywardPride,Wolf'sGravestone,TheUnforged,SongOfBrokenPines,SkyriderGreatsword"

# first initialize the character / weapon / skill classes [new class]
kazuha = KazuhaCharacter.Kazuha(inputParametersChar)
weapon = Weapon.Weapon(inputWeaponName)
kazuhaSkills = KazuhaSkills.KazuhaSkills(inputParametersChar[0])

# then choose to optimize substats or not [new class]

# then export data for either one or more weapons [new class]





