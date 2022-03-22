from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QFont

import yaml

def construct(x, yaml_file, settings):

    with open(yaml_file, 'r') as f:
        yaml_data = yaml.load(f, Loader=yaml.SafeLoader)

    if settings in yaml_data.keys():

        settings_dict = yaml_data[settings]

        if settings_dict['type'] == 'QLabel':
            
            ##サイズの設定
            if ('height' in settings_dict.keys() and 'width' in settings_dict.keys()):

                h = settings_dict['height']
                w = settings_dict['width']

                x.setFixedSize(QSize(w, h))
            ##サイズの設定

            ##fontの設定
            font = QFont()

            if 'fontFamily' in settings_dict.keys():
                font.setFamily(settings_dict['fontFamily'])

            if 'fontPoint' in settings_dict.keys():
                font.setPointSize(settings_dict['fontPoint'])

            if 'fontBold' in settings_dict.keys():
                font.setBold(settings_dict['fontBold'])
                    
            x.setFont(font)
            ##fontの設定

            ##テキストの設定
            if 'text' in settings_dict.keys():
                x.setText(settings_dict['text'])
            ##テキストの設定

            ##アライメントの設定
            if 'alignment' in settings_dict.keys():

                alignment_str = settings_dict['alignment']

                if alignment_str == 'center':
                    x.setAlignment(Qt.AlignmentFlag.AlignCenter)
                
                elif alignment_str == 'right':
                    x.setAlignment(Qt.AlignmentFlag.AlignRight)

                elif alignment_str == 'right':
                    x.setAlignment(Qt.AlignmentFlag.AlignLeft)
            ##アライメントの設定
        
        elif settings_dict['type'] == 'QPushButton':
            
            ##サイズの設定
            if ('height' in settings_dict.keys() and 'width' in settings_dict.keys()):

                h = settings_dict['height']
                w = settings_dict['width']

                x.setFixedSize(QSize(w, h))
            ##サイズの設定

            ##fontの設定
            font = QFont()

            if 'fontFamily' in settings_dict.keys():
                font.setFamily(settings_dict['fontFamily'])

            if 'fontPoint' in settings_dict.keys():
                font.setPointSize(settings_dict['fontPoint'])

            if 'fontBold' in settings_dict.keys():
                font.setBold(settings_dict['fontBold'])
                    
            x.setFont(font)
            ##fontの設定

            ##テキストの設定
            if 'text' in settings_dict.keys():
                x.setText(settings_dict['text'])
            ##テキストの設定

    return x