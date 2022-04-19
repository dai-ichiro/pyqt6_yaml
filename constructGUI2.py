from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QLabel, QPushButton, QSlider, QFrame
from PyQt6.QtGui import QFont

import yaml

class Label(QLabel):
    def __init__(self, fname = "", settings = ""):
        super().__init__()

        if not fname == "":
            with open(fname, 'r') as f:
                yaml_data = yaml.load(f, Loader=yaml.SafeLoader)
            
            settings_dict = yaml_data.get(settings)

            if settings_dict is not None:

                match settings_dict:
                    case {'height': height, 'width': width}:
                        self.setFixedSize(QSize(width, height))
                
                font = QFont()
                match settings_dict:
                    case {'fontFamily': fontFamily}:
                        font.setFamily(fontFamily)
                match settings_dict:
                    case {'fontPoint': fontPoint}:
                        font.setPointSize(fontPoint)
                match settings_dict:
                    case {'fontBold': fontBold}:
                        font.setBold(fontBold)
                self.setFont(font)

                match settings_dict:
                    case {'text': text}:
                        self.setText(text)            

                match settings_dict.get('alignment'):
                    case 'center':
                        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    case 'right':
                        self.setAlignment(Qt.AlignmentFlag.AlignRight)
                    case 'left':
                        self.setAlignment(Qt.AlignmentFlag.AlignLeft)

                match settings_dict:
                    case {'linewidth': linewidth}:
                        self.setLineWidth(linewidth)

                match settings_dict:
                    case {'shape': 'box', 'shadow': 'plain'}:
                        self.setFrameStyle(QFrame.Shape.Box.value | QFrame.Shadow.Plain.value)
                    case {'shape': 'box', 'shadow': 'raised'}:
                        self.setFrameStyle(QFrame.Shape.Box.value | QFrame.Shadow.Raised.value)
                    case {'shape': 'box', 'shadow': 'sunken'}:
                        self.setFrameStyle(QFrame.Shape.Box.value | QFrame.Shadow.Sunken.value)
                    case {'shape': 'panel', 'shadow': 'plain'}:
                        self.setFrameStyle(QFrame.Shape.Panel.value | QFrame.Shadow.Plain.value)
                    case {'shape': 'panel', 'shadow': 'raised'}:
                        self.setFrameStyle(QFrame.Shape.Panel.value | QFrame.Shadow.Raised.value)
                    case {'shape': 'panel', 'shadow': 'sunken'}:
                        self.setFrameStyle(QFrame.Shape.Panel.value | QFrame.Shadow.Sunken.value)

                color_list = []
                match settings_dict:
                    case {'color': color}:
                        color_list.append('color: %s'%color)
                match settings_dict:
                    case {'background-color': background_color}:
                        color_list.append('background-color: %s'%background_color)
                if len(color_list) > 0:
                    self.setStyleSheet(';'.join(color_list))

class PushButton(QPushButton):
    def __init__(self, fname = "", settings = ""):
        super().__init__()

        if not fname == "":
            with open(fname, 'r') as f:
                yaml_data = yaml.load(f, Loader=yaml.SafeLoader)
            
            settings_dict = yaml_data.get(settings)

            if settings_dict is not None:

                match settings_dict:
                    case {'height': height, 'width': width}:
                        self.setFixedSize(QSize(width, height))
                
                font = QFont()
                match settings_dict:
                    case {'fontFamily': fontFamily}:
                        font.setFamily(fontFamily)
                match settings_dict:
                    case {'fontPoint': fontPoint}:
                        font.setPointSize(fontPoint)
                match settings_dict:
                    case {'fontBold': fontBold}:
                        font.setBold(fontBold)
                self.setFont(font)

                match settings_dict:
                    case {'text': text}:
                        self.setText(text)            

class Slider(QSlider):
    def __init__(self, fname = "", settings = ""):
        super().__init__()
        
        if not fname == "":
            with open(fname, 'r') as f:
                yaml_data = yaml.load(f, Loader=yaml.SafeLoader)

            settings_dict = yaml_data.get(settings)

            if settings_dict is not None:

                match settings_dict:
                    case {'height': height, 'width': width}:
                        self.setFixedSize(QSize(width, height))
        
                match settings_dict.get('orientation'):
                    case 'h':
                        self.setOrientation(Qt.Orientation.Horizontal)
                    case 'v':
                        self.setOrientation(Qt.Orientation.Vertical)

                match settings_dict:
                    case {'max': max}:                    
                        self.setMaximum(max)

                match settings_dict:
                    case {'min': min}:                    
                        self.setMinimum(min)
                
                match settings_dict:
                    case {'default': default}:
                        self.setValue(default)

                match settings_dict.get('tickposition'): 
                    case 'both':
                        self.setTickPosition(QSlider.TickPosition.TicksBothSides)
                    case 'above':
                        self.setTickPosition(QSlider.TickPosition.TicksAbove)
                    case 'below':
                        self.setTickPosition(QSlider.TickPosition.TicksBelow)
                    case 'left':
                        self.setTickPosition(QSlider.TickPosition.TicksLeft)
                    case 'right':
                        self.setTickPosition(QSlider.TickPosition.TicksRight)

