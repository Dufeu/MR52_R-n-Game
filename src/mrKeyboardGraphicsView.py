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
        
        self.sceneKeyboard.addRect(self.un_rect)
        self.sceneKeyboard.addRect(self.deux_rect)
        self.sceneKeyboard.addRect(self.trois_rect)
        self.sceneKeyboard.addRect(self.quatre_rect)
        self.sceneKeyboard.addRect(self.cinq_rect)
        self.sceneKeyboard.addRect(self.six_rect)
        self.sceneKeyboard.addRect(self.sept_rect)
        self.sceneKeyboard.addRect(self.huit_rect)
        self.sceneKeyboard.addRect(self.neuf_rect)
        self.sceneKeyboard.addRect(self.zero_rect)
        
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
        
        self.sceneKeyboard.addRect(self.a_rect)
        self.sceneKeyboard.addRect(self.z_rect)
        self.sceneKeyboard.addRect(self.e_rect)
        self.sceneKeyboard.addRect(self.r_rect)
        self.sceneKeyboard.addRect(self.t_rect)
        self.sceneKeyboard.addRect(self.y_rect)
        self.sceneKeyboard.addRect(self.u_rect)
        self.sceneKeyboard.addRect(self.i_rect)
        self.sceneKeyboard.addRect(self.o_rect)
        self.sceneKeyboard.addRect(self.p_rect)
        
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
        
        self.sceneKeyboard.addRect(self.q_rect)
        self.sceneKeyboard.addRect(self.s_rect)
        self.sceneKeyboard.addRect(self.d_rect)
        self.sceneKeyboard.addRect(self.f_rect)
        self.sceneKeyboard.addRect(self.g_rect)
        self.sceneKeyboard.addRect(self.h_rect)
        self.sceneKeyboard.addRect(self.j_rect)
        self.sceneKeyboard.addRect(self.k_rect)
        self.sceneKeyboard.addRect(self.l_rect)
        self.sceneKeyboard.addRect(self.m_rect)
        
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
        
        self.sceneKeyboard.addRect(self.w_rect)
        self.sceneKeyboard.addRect(self.x_rect)
        self.sceneKeyboard.addRect(self.c_rect)
        self.sceneKeyboard.addRect(self.v_rect)
        self.sceneKeyboard.addRect(self.b_rect)
        self.sceneKeyboard.addRect(self.n_rect)
        self.sceneKeyboard.addRect(self.intero_rect)
        self.sceneKeyboard.addRect(self.point_rect)
        self.sceneKeyboard.addRect(self.slash_rect)
        self.sceneKeyboard.addRect(self.exclam_rect)
        
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
        
        self.sceneKeyboard.addRect(self.f1_rect)
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
        self.sceneKeyboard.addRect(self.f12_rect)
        
        
        
        """SPECIAL KEY """
        tmpX = 420
        tmpY = 5
        self.imp_rect = QtCore.QRectF(tmpX,tmpY,self.key_width,self.key_width)
        self.scroll_rect = QtCore.QRectF(tmpX+self.key_width*1,tmpY,self.key_width,self.key_width)
        self.pause_rect = QtCore.QRectF(tmpX+self.key_width*2,tmpY,self.key_width,self.key_width)
               
        self.sceneKeyboard.addRect(self.imp_rect)
        self.sceneKeyboard.addRect(self.scroll_rect)
        self.sceneKeyboard.addRect(self.pause_rect)
        
        tmpY = 56
        self.inser_rect = QtCore.QRectF(tmpX,tmpY,self.key_width,self.key_width)
        self.home_rect = QtCore.QRectF(tmpX+self.key_width*1,tmpY,self.key_width,self.key_width)
        self.pUp_rect = QtCore.QRectF(tmpX+self.key_width*2,tmpY,self.key_width,self.key_width)
               
        self.sceneKeyboard.addRect(self.inser_rect)
        self.sceneKeyboard.addRect(self.home_rect)
        self.sceneKeyboard.addRect(self.pUp_rect)
        
        tmpY = 84
        self.del_rect = QtCore.QRectF(tmpX,tmpY,self.key_width,self.key_width)
        self.end_rect = QtCore.QRectF(tmpX+self.key_width*1,tmpY,self.key_width,self.key_width)
        self.pDown_rect = QtCore.QRectF(tmpX+self.key_width*2,tmpY,self.key_width,self.key_width)
               
        self.sceneKeyboard.addRect(self.del_rect)
        self.sceneKeyboard.addRect(self.end_rect)
        self.sceneKeyboard.addRect(self.pDown_rect)
        
        tmpY = 139
        tmpX = 447
        self.up_rect = QtCore.QRectF(tmpX,tmpY,self.key_width,self.key_width)
        self.sceneKeyboard.addRect(self.up_rect)
        
        tmpX = 420
        tmpY = 167
        self.right_rect = QtCore.QRectF(tmpX,tmpY,self.key_width,self.key_width)
        self.down_rect = QtCore.QRectF(tmpX+self.key_width*1,tmpY,self.key_width,self.key_width)
        self.left_rect = QtCore.QRectF(tmpX+self.key_width*2,tmpY,self.key_width,self.key_width)
               
        self.sceneKeyboard.addRect(self.right_rect)
        self.sceneKeyboard.addRect(self.down_rect)
        self.sceneKeyboard.addRect(self.left_rect)
        
        
        
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
        
        tmpX = 347
        self.enter_rect = QtCore.QRectF(tmpX,tmpY,57,self.key_width)
        
        tmpX = 320
        self.back_rect = QtCore.QRectF(tmpX,tmpY,57,self.key_width)
        
        self.sceneKeyboard.addRect(self.space_rect)
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
        