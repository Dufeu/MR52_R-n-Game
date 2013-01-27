'''
Created on 9 dec. 2012

@author: Lois Aubree
'''
from PyQt4 import QtGui,QtCore
import os

class mrKeyboardGraphicsView(QtGui.QGraphicsView):
    
    
    def __init__(self):
        QtGui.QGraphicsView.__init__(self)
        self.sceneKeyboard = QtGui.QGraphicsScene(self)
        self.setScene(self.sceneKeyboard)
        self.KeyboardImage = QtGui.QPixmap()
        self.KeyboardImage.load('image/keyboard.png')
        self.sceneKeyboard.addPixmap(self.KeyboardImage)
        self.setMinimumSize(self.KeyboardImage.width()+20,self.KeyboardImage.height()+20)
        self.key_width = 27  
        self.pen = QtGui.QPen(QtCore.Qt.NoPen)
        self.brush = QtGui.QBrush(QtGui.QColor(255,0,0))
        
        """ NUM KEY """
        tmpX = 31
        tmpY = 56
        self.un_rect = QtCore.QRectF(tmpX,tmpY,self.key_width,self.key_width)
        self.deux_rect = QtCore.QRectF(tmpX+self.key_width*1,tmpY,self.key_width,self.key_width)
        self.trois_rect = QtCore.QRectF(tmpX+self.key_width*2,tmpY,self.key_width,self.key_width)
        self.quatre_rect = QtCore.QRectF(tmpX+self.key_width*3,tmpY,self.key_width,self.key_width)
        self.cinq_rect = QtCore.QRectF(tmpX+self.key_width*4,tmpY,self.key_width,self.key_width)
        self.six_rect = QtCore.QRectF(tmpX+self.key_width*5,tmpY,self.key_width,self.key_width)
        self.sept_rect = QtCore.QRectF(tmpX+self.key_width*6,tmpY,self.key_width,self.key_width)
        self.huit_rect = QtCore.QRectF(tmpX+self.key_width*7,tmpY,self.key_width,self.key_width)
        self.neuf_rect = QtCore.QRectF(tmpX+self.key_width*8,tmpY,self.key_width,self.key_width)
        self.zero_rect = QtCore.QRectF(tmpX+self.key_width*9,tmpY,self.key_width,self.key_width)
        
        """self.sceneKeyboard.addRect(self.un_rect)
        self.sceneKeyboard.addRect(self.deux_rect)
        self.sceneKeyboard.addRect(self.trois_rect)
        self.sceneKeyboard.addRect(self.quatre_rect)
        self.sceneKeyboard.addRect(self.cinq_rect)
        self.sceneKeyboard.addRect(self.six_rect)
        self.sceneKeyboard.addRect(self.sept_rect)
        self.sceneKeyboard.addRect(self.huit_rect)
        self.sceneKeyboard.addRect(self.neuf_rect)
        self.sceneKeyboard.addRect(self.zero_rect)"""
        
        """ FIRST KEY """
        tmpX = 43
        tmpY = 84
        self.a_rect = QtCore.QRectF(tmpX,tmpY,self.key_width,self.key_width)
        self.z_rect = QtCore.QRectF(tmpX+self.key_width*1,tmpY,self.key_width,self.key_width)
        self.e_rect = QtCore.QRectF(tmpX+self.key_width*2,tmpY,self.key_width,self.key_width)
        self.r_rect = QtCore.QRectF(tmpX+self.key_width*3,tmpY,self.key_width,self.key_width)
        self.t_rect = QtCore.QRectF(tmpX+self.key_width*4,tmpY,self.key_width,self.key_width)
        self.y_rect = QtCore.QRectF(tmpX+self.key_width*5,tmpY,self.key_width,self.key_width)
        self.u_rect = QtCore.QRectF(tmpX+self.key_width*6,tmpY,self.key_width,self.key_width)
        self.i_rect = QtCore.QRectF(tmpX+self.key_width*7,tmpY,self.key_width,self.key_width)
        self.o_rect = QtCore.QRectF(tmpX+self.key_width*8,tmpY,self.key_width,self.key_width)
        self.p_rect = QtCore.QRectF(tmpX+self.key_width*9,tmpY,self.key_width,self.key_width)
        
        """self.sceneKeyboard.addRect(self.a_rect)
        self.sceneKeyboard.addRect(self.z_rect)
        self.sceneKeyboard.addRect(self.e_rect)
        self.sceneKeyboard.addRect(self.r_rect)
        self.sceneKeyboard.addRect(self.t_rect)
        self.sceneKeyboard.addRect(self.y_rect)
        self.sceneKeyboard.addRect(self.u_rect)
        self.sceneKeyboard.addRect(self.i_rect)
        self.sceneKeyboard.addRect(self.o_rect)
        self.sceneKeyboard.addRect(self.p_rect)"""
        
        """ SECOND STAGE KEY """
        tmpX = 51
        tmpY = 112
        self.q_rect = QtCore.QRectF(tmpX,tmpY,self.key_width,self.key_width)
        self.s_rect = QtCore.QRectF(tmpX+self.key_width*1,tmpY,self.key_width,self.key_width)
        self.d_rect = QtCore.QRectF(tmpX+self.key_width*2,tmpY,self.key_width,self.key_width)
        self.f_rect = QtCore.QRectF(tmpX+self.key_width*3,tmpY,self.key_width,self.key_width)
        self.g_rect = QtCore.QRectF(tmpX+self.key_width*4,tmpY,self.key_width,self.key_width)
        self.h_rect = QtCore.QRectF(tmpX+self.key_width*5,tmpY,self.key_width,self.key_width)
        self.j_rect = QtCore.QRectF(tmpX+self.key_width*6,tmpY,self.key_width,self.key_width)
        self.k_rect = QtCore.QRectF(tmpX+self.key_width*7,tmpY,self.key_width,self.key_width)
        self.l_rect = QtCore.QRectF(tmpX+self.key_width*8,tmpY,self.key_width,self.key_width)
        self.m_rect = QtCore.QRectF(tmpX+self.key_width*9,tmpY,self.key_width,self.key_width)
        
        """self.sceneKeyboard.addRect(self.q_rect)
        self.sceneKeyboard.addRect(self.s_rect)
        self.sceneKeyboard.addRect(self.d_rect)
        self.sceneKeyboard.addRect(self.f_rect)
        self.sceneKeyboard.addRect(self.g_rect)
        self.sceneKeyboard.addRect(self.h_rect)
        self.sceneKeyboard.addRect(self.j_rect)
        self.sceneKeyboard.addRect(self.k_rect)
        self.sceneKeyboard.addRect(self.l_rect)
        self.sceneKeyboard.addRect(self.m_rect)"""
        
        """ THIRD STAGE KEY """
        tmpX = 70
        tmpY = 140
        self.w_rect = QtCore.QRectF(tmpX,tmpY,self.key_width,self.key_width)
        self.x_rect = QtCore.QRectF(tmpX+self.key_width*1,tmpY,self.key_width,self.key_width)
        self.c_rect = QtCore.QRectF(tmpX+self.key_width*2,tmpY,self.key_width,self.key_width)
        self.v_rect = QtCore.QRectF(tmpX+self.key_width*3,tmpY,self.key_width,self.key_width)
        self.b_rect = QtCore.QRectF(tmpX+self.key_width*4,tmpY,self.key_width,self.key_width)
        self.n_rect = QtCore.QRectF(tmpX+self.key_width*5,tmpY,self.key_width,self.key_width)
        self.intero_rect = QtCore.QRectF(tmpX+self.key_width*6,tmpY,self.key_width,self.key_width)
        self.point_rect = QtCore.QRectF(tmpX+self.key_width*7,tmpY,self.key_width,self.key_width)
        self.slash_rect = QtCore.QRectF(tmpX+self.key_width*8,tmpY,self.key_width,self.key_width)
        self.exclam_rect = QtCore.QRectF(tmpX+self.key_width*9,tmpY,self.key_width,self.key_width)
        
        """self.sceneKeyboard.addRect(self.w_rect)
        self.sceneKeyboard.addRect(self.x_rect)
        self.sceneKeyboard.addRect(self.c_rect)
        self.sceneKeyboard.addRect(self.v_rect)
        self.sceneKeyboard.addRect(self.b_rect)
        self.sceneKeyboard.addRect(self.n_rect)
        self.sceneKeyboard.addRect(self.intero_rect)
        self.sceneKeyboard.addRect(self.point_rect)
        self.sceneKeyboard.addRect(self.slash_rect)
        self.sceneKeyboard.addRect(self.exclam_rect)"""
        
        """ FX STAGE KEY """
        tmpX = 50
        tmpY = 5
        self.f1_rect = QtCore.QRectF(tmpX,tmpY,self.key_width,self.key_width)
        self.f2_rect = QtCore.QRectF(tmpX+self.key_width*1,tmpY,self.key_width,self.key_width)
        self.f3_rect = QtCore.QRectF(tmpX+self.key_width*2,tmpY,self.key_width,self.key_width)
        self.f4_rect = QtCore.QRectF(tmpX+self.key_width*3,tmpY,self.key_width,self.key_width)
        tmpX = 174
        self.f5_rect = QtCore.QRectF(tmpX,tmpY,self.key_width,self.key_width)
        self.f6_rect = QtCore.QRectF(tmpX+self.key_width*1,tmpY,self.key_width,self.key_width)
        self.f7_rect = QtCore.QRectF(tmpX+self.key_width*2,tmpY,self.key_width,self.key_width)
        self.f8_rect = QtCore.QRectF(tmpX+self.key_width*3,tmpY,self.key_width,self.key_width)
        
        tmpX = 297
        self.f9_rect = QtCore.QRectF(tmpX,tmpY,self.key_width,self.key_width)
        self.f10_rect = QtCore.QRectF(tmpX+self.key_width*1,tmpY,self.key_width,self.key_width)
        self.f11_rect = QtCore.QRectF(tmpX+self.key_width*2,tmpY,self.key_width,self.key_width)
        self.f12_rect = QtCore.QRectF(tmpX+self.key_width*3,tmpY,self.key_width,self.key_width)
        
        """self.sceneKeyboard.addRect(self.f1_rect)
        self.sceneKeyboard.addRect(self.f2_rect)
        self.sceneKeyboard.addRect(self.f3_rect)
        self.sceneKeyboard.addRect(self.f4_rect)
        self.sceneKeyboard.addRect(self.f5_rect)
        self.sceneKeyboard.addRect(self.f6_rect)
        self.sceneKeyboard.addRect(self.f7_rect)
        self.sceneKeyboard.addRect(self.f8_rect)
        self.sceneKeyboard.addRect(self.f9_rect)
        self.sceneKeyboard.addRect(self.f10_rect)
        self.sceneKeyboard.addRect(self.f11_rect)
        self.sceneKeyboard.addRect(self.f12_rect)"""
        
        
        
        """SPECIAL KEY """
        tmpX = 420
        tmpY = 5
        self.imp_rect = QtCore.QRectF(tmpX,tmpY,self.key_width,self.key_width)
        self.scroll_rect = QtCore.QRectF(tmpX+self.key_width*1,tmpY,self.key_width,self.key_width)
        self.pause_rect = QtCore.QRectF(tmpX+self.key_width*2,tmpY,self.key_width,self.key_width)
               
        """self.sceneKeyboard.addRect(self.imp_rect)
        self.sceneKeyboard.addRect(self.scroll_rect)
        self.sceneKeyboard.addRect(self.pause_rect)"""
        
        tmpY = 56
        self.inser_rect = QtCore.QRectF(tmpX,tmpY,self.key_width,self.key_width)
        self.home_rect = QtCore.QRectF(tmpX+self.key_width*1,tmpY,self.key_width,self.key_width)
        self.pUp_rect = QtCore.QRectF(tmpX+self.key_width*2,tmpY,self.key_width,self.key_width)
               
        """self.sceneKeyboard.addRect(self.inser_rect)
        self.sceneKeyboard.addRect(self.home_rect)
        self.sceneKeyboard.addRect(self.pUp_rect)"""
        
        tmpY = 84
        self.del_rect = QtCore.QRectF(tmpX,tmpY,self.key_width,self.key_width)
        self.end_rect = QtCore.QRectF(tmpX+self.key_width*1,tmpY,self.key_width,self.key_width)
        self.pDown_rect = QtCore.QRectF(tmpX+self.key_width*2,tmpY,self.key_width,self.key_width)
               
        """self.sceneKeyboard.addRect(self.del_rect)
        self.sceneKeyboard.addRect(self.end_rect)
        self.sceneKeyboard.addRect(self.pDown_rect)"""
        
        tmpY = 139
        tmpX = 447
        self.up_rect = QtCore.QRectF(tmpX,tmpY,self.key_width,self.key_width)
        """self.sceneKeyboard.addRect(self.up_rect)"""
        
        tmpX = 420
        tmpY = 167
        self.left_rect = QtCore.QRectF(tmpX,tmpY,self.key_width,self.key_width)
        self.down_rect = QtCore.QRectF(tmpX+self.key_width*1,tmpY,self.key_width,self.key_width)
        self.right_rect = QtCore.QRectF(tmpX+self.key_width*2,tmpY,self.key_width,self.key_width)
               
        """self.sceneKeyboard.addRect(self.right_rect)
        self.sceneKeyboard.addRect(self.down_rect)
        self.sceneKeyboard.addRect(self.left_rect)
        """
        self.space_rect = QtCore.QRectF(114,tmpY,147,self.key_width)
        self.lCtrl_rect = QtCore.QRectF(5,tmpY,39,self.key_width)
        self.lWin_rect = QtCore.QRectF(45,tmpY,34,self.key_width)
        self.lAlt_rect = QtCore.QRectF(79,tmpY,34,self.key_width)
        
        self.rAlt_rect = QtCore.QRectF(261,tmpY,34,self.key_width)
        self.rWin_rect = QtCore.QRectF(295,tmpY,35,self.key_width)
        self.op_rect = QtCore.QRectF(330,tmpY,35,self.key_width)
        self.rCtrl_rect = QtCore.QRectF(365,tmpY,39,self.key_width)
        
        tmpY = 140
        tmpX = 340
        
        self.rShift_rect = QtCore.QRectF(tmpX,tmpY,64,self.key_width)
        
        tmpX = 5
        self.lShift_rect = QtCore.QRectF(tmpX,tmpY,64,self.key_width)
        tmpY = 112
        self.cap_rect = QtCore.QRectF(tmpX,tmpY,47,self.key_width)
        
        
        tmpX = 348
        self.enter_rect = QtCore.QRectF(tmpX,tmpY,56,self.key_width)
        
        tmpY = 56
        tmpX = 353
        self.back_rect = QtCore.QRectF(tmpX,tmpY,52,self.key_width)
        
        tmpY = 84
        tmpX = 5
        self.tab_rect = QtCore.QRectF(tmpX,tmpY,38,self.key_width)
        
        tmpY = 5
        tmpX = 5
        self.esc_rect = QtCore.QRectF(tmpX,tmpY,self.key_width,self.key_width)
        
        """self.sceneKeyboard.addRect(self.space_rect)
        self.sceneKeyboard.addRect(self.lCtrl_rect)
        self.sceneKeyboard.addRect(self.lWin_rect)
        self.sceneKeyboard.addRect(self.lAlt_rect)
        self.sceneKeyboard.addRect(self.lShift_rect)
        self.sceneKeyboard.addRect(self.rAlt_rect)
        self.sceneKeyboard.addRect(self.rWin_rect)
        self.sceneKeyboard.addRect(self.op_rect)
        self.sceneKeyboard.addRect(self.rCtrl_rect)
        self.sceneKeyboard.addRect(self.rShift_rect)
        self.sceneKeyboard.addRect(self.cap_rect)
        self.sceneKeyboard.addRect(self.enter_rect)
        self.sceneKeyboard.addRect(self.back_rect)
        self.sceneKeyboard.addRect(self.tab_rect)
        self.sceneKeyboard.addRect(self.esc_rect)"""
        
        self.table_key={'A': self.a_rect, 'Z': self.z_rect, 'E':self.e_rect, 'R': self.r_rect, 'T':self.t_rect,'Y':self.y_rect,'U': self.u_rect,
                   'I':self.i_rect,'O':self.o_rect,'P':self.p_rect,'Q':self.q_rect,'S':self.s_rect,'D':self.d_rect,'F':self.f_rect,'G':self.g_rect,'H':self.h_rect,'J':self.j_rect,'K':self.k_rect,'L':self.l_rect,
                   'M':self.m_rect,'W':self.w_rect,'X':self.x_rect,'C':self.c_rect,'V':self.v_rect,'B':self.b_rect,'N':self.n_rect, 'Space':self.space_rect,
                   'Lcontrol':self.lCtrl_rect,'Rcontrol':self.rCtrl_rect,'Tab':self.tab_rect,'Lwin':self.lWin_rect,'Lshift':self.lShift_rect,'Rshift':self.rShift_rect,
                   'Up':self.up_rect,'Down':self.down_rect,'Right':self.right_rect,'Left':self.left_rect,'Return':self.enter_rect,'Back':self.back_rect,'Delete':self.del_rect,
                   'F1':self.f1_rect,'F2':self.f2_rect,'F3':self.f3_rect,'F4':self.f4_rect,'F5':self.f5_rect,'F6':self.f6_rect,'F7':self.f7_rect,'F8':self.f8_rect,'F9':self.f9_rect,
                   'F10':self.f10_rect,'F11':self.f11_rect,'F12':self.f12_rect,'1':self.un_rect,'2':self.deux_rect,'3':self.trois_rect,'4':self.quatre_rect,'5':self.cinq_rect,'6':self.six_rect,
                   '7':self.sept_rect,'8':self.huit_rect,'9':self.neuf_rect,'0':self.zero_rect,'Escape':self.esc_rect}
    
    def updateKeyBoardView(self,tableKey):
        self.sceneKeyboard.clear()
        self.sceneKeyboard.addPixmap(self.KeyboardImage)
        self.setMinimumSize(self.KeyboardImage.width()+20,self.KeyboardImage.height()+20)
        maximum = 0
        for key in tableKey:
            if key[1] > maximum:
                maximum = key[1]
        for key in tableKey:
            self.sceneKeyboard.addRect(self.table_key[key[0]],self.pen,self.getBrushColor(key[1], maximum))
    
    
    def getBrushColor(self,value,max):
        color = (510*value)/max
        if color-255 > 0:
            blue = 255
            green = color-255
        else:
            blue = color
            green = 0  
        return QtGui.QBrush(QtGui.QColor(255-green,255,255-blue,150))