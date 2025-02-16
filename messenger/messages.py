########################################################################
# COMPONENT:
#    MESSAGES
# Author:
#    Br. Helfrich, Kyle Mueller, Nate Duncan, Clark Mulvey
# Summary: 
#    This class stores the notion of a collection of messages
########################################################################

import control, message

##################################################
# MESSAGES
# The collection of high-tech messages
##################################################
class Messages:

    ##################################################
    # MESSAGES CONSTRUCTOR
    # Read a file to fill the messages
    ##################################################
    def __init__(self, filename):
        self._messages = []
        self._read_messages(filename)

    ##################################################
    # MESSAGES :: DISPLAY
    # Display the list of messages
    ################################################## 
    def display(self, subject_control):
        for m in self._messages:
            m.display_properties(subject_control)

    ##################################################
    # MESSAGES :: SHOW
    # Show a single message
    ################################################## 
    def show(self, id, subject_control):
        for m in self._messages:
            if m.get_id() == id:
                m.display_text(subject_control)
                return True
        return False

    ##################################################
    # MESSAGES :: UPDATE
    # Update a single message
    ################################################## 
    def update(self, id, subject_control, text):
        for m in self._messages:
            if m.get_id() == id:
                m.update_text(subject_control, text)

    ##################################################
    # MESSAGES :: REMOVE
    # Remove a single message
    ################################################## 
    def remove(self, id, subject_control):
        for m in self._messages:
            if m.get_id() == id:
                m.clear(subject_control)

    ##################################################
    # MESSAGES :: ADD
    # Add a new message
    ################################################## 
    def add(self, text, author, date, text_control):
        m = message.Message(text, author, date, text_control)
        self._messages.append(m)

    ##################################################
    # MESSAGES :: READ MESSAGES
    # Read messages from a file
    ################################################## 
    def _read_messages(self, filename):
        try:
            with open(filename, "r") as f:
                for line in f:
                    text_control, author, date, text = line.split('|')
                    self.add(text.rstrip('\r\n'), author, date, control.Control[text_control]) 

        except FileNotFoundError:
            print(f"ERROR! Unable to open file \"{filename}\"")
            return
