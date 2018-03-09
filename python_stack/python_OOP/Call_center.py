from datetime import datetime                                                   # datetime import
class Call(object):
    Num_calls = 0                                                               # Counts how many calls received
    def __init__(self, caller_name, caller_phone_number, time_of_call, reason_for_call):
        self.unique_id = Call.Num_calls                                         # unique id = Num_calls, everytime receive call, unique id will increment by 1
        Call.Num_calls += 1
        self.caller_name = caller_name
        self.caller_phone_number = caller_phone_number
        self.time_of_call = datetime.now()
        self.reason_for_call = reason_for_call
    def display(self):                                                          # Will display call's information
        print 'ID: {}'.format(self.unique_id)
        print 'Caller Name: {}'.format(self.caller_name)
        print 'Caller #: {}'.format(self.caller_phone_number)
        print 'Time of Call: {}'.format(self.time_of_call)
        print 'Reason for Call: {}'.format(self.reason_for_call)
class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue_size = len(self.calls)
    def add(self, call):                                                        # Appending call info to emtpy list
        self.calls.append({'id': call.unique_id, 'name': call.caller_name, 'number': call.caller_phone_number, 'time': call.time_of_call, 'reason': call.reason_for_call})
        self.queue_size = len(self.calls)
        return self
    def remove(self):                                                           # Pops index[0]
        self.calls.pop(0)
        return self
    def info(self):
        print '\n'+('#'* 125)+'\n'
        for call in range(len(self.calls)):                                     # Displays detailed info
            print "Caller Name: {}, Caller's Phone Number: {} Started time: {}, Reason for call: {}".format(self.calls[call]['name'], self.calls[call]['number'], self.calls[call]['time'], self.calls[call]['reason'])
        print self.queue_size
        print '\n' + '#'* 125
        return self
call1 = Call('Alex', 3162262266, '6pm', 'No internet')
call2 = Call('Tina', 3162265522, '7pm', 'No internet')
call3 = Call('Chien', 3162268822, '7pm', 'No internet')
call4 = Call('Batt', 3162299922, '8pm', 'No internet')
# call1.display()
CallCenter().add(call2).add(call1).add(call3).add(call4).remove().info()
