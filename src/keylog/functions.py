'''
Created on 27 oct. 2012

@author: Lois Aubree
'''
def OnMouseEvent(event):
    '''
    print('MessageName:',event.MessageName)
    print('Message:',event.Message)
    print('Time:',event.Time)
    print('Window:',event.Window)
    print('WindowName:',event.WindowName)
    print('Position:',event.Position)
    print('Wheel:',event.Wheel)
    print('Injected:',event.Injected)
    print('---')
    '''
    
    tableKey = []
    tableKey.append(event.MessageName)
    print(tableKey)
    # return True to pass the event to other handlers
    # return False to stop the event from propagating
    return True

def OnKeyboardEvent(event):
    '''
    print('MessageName:',event.MessageName)
    print('Message:',event.Message)
    print('Time:',event.Time)
    print('Window:',event.Window)
    print('WindowName:',event.WindowName)
    print('Ascii:', event.Ascii, chr(event.Ascii))
    print('Key:', event.Key)
    print('KeyID:', event.KeyID)
    print('ScanCode:', event.ScanCode)
    print('Extended:', event.Extended)
    print('Injected:', event.Injected)
    print('Alt', event.Alt)
    print('Transition', event.Transition)
    print('---')
    '''
    return True