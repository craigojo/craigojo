
'''
page 34 example
'''
class Time:
    """Represents the time of day.
    attributes: hour, minute, second
    """

    def __init__(self, hour = 0, minute = 0, second = 0):
        self.seconds = second
        self.seconds +=60 * minute
        self.seconds += 60 * 60 * hour
        self.seconds = self.seconds % (24 * 60 * 60)

    def __str__(self):
        minutes, seconds = divmod(self.seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return(f"{hours:02d}:{minutes:02d}:{seconds:02d}")




    def time_to_int(self):
        return self.seconds
    

    def is_after(self, time):
        return self.time_to_int() > time.time_to_int()
        # if self.hour > time.hour:
        #     return True
        # elif self.hour == time.hour:
        #     if self.minute  > time.minute:
        #         return True
        #     elif self.minute == time.minute:
        #         return self.second > time.second
        # return False


    def increment(self, seconds):
        self.seconds += seconds
        self.seconds = self.seconds % (24 * 60 * 60)

t = Time(7, 12, 8)
s = Time(8, 9, 15)

t.increment(10)
print(t)
t.increment(60)
print(t)
t.increment(60*60)
print(t)








# class Time:
#     """Represents the time of day.
#     attributes: hour, minute, second
#     """

#     def __init__(self, hour = 0, minute = 0, second = 0):
#         self.hour = hour
#         self.minute = minute
#         self.second = second

#     def __str__(self):

#         return(f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}")

#     def time_to_int(self):
#         minutes = self.hour * 60 + self.minute
#         seconds = minutes * 60 + self.second
#         return seconds
    

#     def is_after(self, time):
#         return self.time_to_int() > time.time_to_int()
#         # if self.hour > time.hour:
#         #     return True
#         # elif self.hour == time.hour:
#         #     if self.minute  > time.minute:
#         #         return True
#         #     elif self.minute == time.minute:
#         #         return self.second > time.second
#         # return False


#     def increment(self, seconds):
#         self.second += seconds
#         while self.second >= 60:
#             self.minute += 1
#             self.second -= 60
#         while self.minute >= 60:
#             self.hour += 1
#             self.minute -= 60
#         self.hour = self.hour % 24

# t = Time(7, 12, 8)
# s = Time(8, 9, 15)

# t.increment(10)
# print(t)
# t.increment(60)
# print(t)
# t.increment(60*60)
# print(t)


# print(t.is_after(s))
# print(s.is_after(t))

# def int_to_time(seconds):
#     t = Time()
#     minutes, t.second = divmod(seconds, 60)
#     t.hour, t.minute = divmod(minutes, 60)
#     return t

# t = Time(12)
# print(t)


# t = int_to_time(1000)
# print(t)
# print(t.time_to_int())





# '''
# example 2 page 34
# '''
# class Time:
#     """Represents the time of day.
#     attributes: hour, minute, second
#     """

#     def __init__(self, hour = 0, minute = 0, second = 0):
#         self.hour = hour
#         self.minute = minute
#         self.second = second

#     def __str__(self):

#         return(f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}")

#     def time_to_int(self):
#         minutes = self.hour * 60 + self.minute
#         seconds = minutes * 60 + self.second
#         return seconds
    

#     def is_after(self, time):
#         return self.time_to_int() > time.time_to_int()
#         # if self.hour > time.hour:
#         #     return True
#         # elif self.hour == time.hour:
#         #     if self.minute  > time.minute:
#         #         return True
#         #     elif self.minute == time.minute:
#         #         return self.second > time.second
#         # return False

# t = Time(7, 12, 8)
# s = Time(8, 9, 15)
# print(t.is_after(s))
# print(s.is_after(t))

# def int_to_time(seconds):
#     t = Time()
#     minutes, t.second = divmod(seconds, 60)
#     t.hour, t.minute = divmod(minutes, 60)
#     return t

# t = Time(12)
# print(t)


# t = int_to_time(1000)
# print(t)
# print(t.time_to_int())





# '''
# EXAMPLE 1 page 34
# '''

# class Time:
#     """Represents the time of day.
#     attributes: hour, minute, second
#     """

#     def __init__(self, hour = 0, minute = 0, second = 0):
#         self.hour = hour
#         self.minute = minute
#         self.second = second

#     def __str__(self):

#         return(f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}")

#     def time_to_int(self):
#         minutes = self.hour * 60 + self.minute
#         seconds = minutes * 60 + self.second
#         return seconds



# def int_to_time(seconds):

#     minutes, second = divmod(seconds, 60)
#     hour, minute = divmod(minutes, 60)
#     return Time(hour, minute, second)

# t = Time(12)
# print(t)


# t = int_to_time(1000)
# print(t)
# print(t.time_to_int())






# class Time:
#     """Represents the time of day.
#     attributes: hour, minute, second
#     """

#     def __init__(self, hour = 0, minute = 0, second = 0):
#         self.hour = hour
#         self.minute = minute
#         self.second = second

#     def print_time(self):

#         print(f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}")

#     def time_to_int(self):
#         minutes = self.hour * 60 + self.minute
#         seconds = minutes * 60 + self.second
#         return seconds



# def int_to_time(seconds):

#     minutes, second = divmod(seconds, 60)
#     hour, minute = divmod(minutes, 60)
#     return Time(hour, minute, second)

# t = Time(12)
# t.print_time()


# t = int_to_time(1000)
# t.print_time()
# print(t.time_to_int())
























# class Time:
#     """Represents the time of day.
#     attributes: hour, minute, second
#     """
#     def print_time(self):
#         """Prints the time in HH:mm:ss format
#     """
    

#         print(f"{self.hour}:{self.minute}:{self.second}")
#         # print('%.2d:%.2d:%.2d' %
#         # (self.hour, self.minute, self.second))


#     # inside class Time:
#     def time_to_int(self):
#         minutes = self.hour * 60 + self.minute
#         seconds = minutes * 60 + self.second
#         return seconds

# t = Time()
# t.hour = 12
# t.minute = 29
# t.second = 18
# t.print_time()



# def int_to_time(seconds):
#     time = Time()
#     minutes, time.second = divmod(seconds, 60)
#     time.hour, time.minute = divmod(minutes, 60)
#     return time




# t = int_to_time(1000)
# t.print_time()
# print(t.time_to_int())



# class Time:
#     """Represents the time of day.
#     attributes: hour, minute, second
#     """
#     def print_time(self):
#         """Prints the time in HH:mm:ss format"""
#         print(f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}")

#     @staticmethod
#     def int_to_time(seconds):
#         time = Time()
#         minutes, time.second = divmod(seconds, 60)
#         time.hour, time.minute = divmod(minutes, 60)
#         return time

#     def time_to_int(self):
#         minutes = self.hour * 60 + self.minute
#         seconds = minutes * 60 + self.second
#         return seconds

# t = Time()
# t.hour = 12
# t.minute = 29
# t.second = 18
# t.print_time()

# t = Time.int_to_time(1000)
# t.print_time()
# print(t.time_to_int())


