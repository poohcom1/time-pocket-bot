#http://masudakoji.github.io/2015/05/23/generate-timetable-using-matplotlib/en/
#!usr/bin/env python
#coding: utf-8
import matplotlib.pyplot as plt
from schedule_manager import *




# Event data: [[Day, Start (hr), Start (min), duration (min), Name]]
def time_table(event_data: list, title="Schedule", 
                sections=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'], 
                colors=['pink', 'lightgreen', 'lightblue', 'wheat', 'salmon'],
                start_hour = 0, end_hour=24
                ):

    fig = plt.figure(figsize=(10, 5.89))

    for event in event_data:
        room = event[0]-0.48
        start = event[1]+event[2]/60
        end = start+event[3]/60
        eventName = event[4]

        # plot event
        plt.fill_between([room, room+0.96], [start, start], [end, end],
                         color=colors[int(event[0]-1)], edgecolor='k', linewidth=0.5)
        # plot beginning time
        plt.text(room+0.02, start+0.05,
                 '{0}:{1:0>2}'.format(int(event[1]), int(event[2])), va='top', fontsize=7)
        # plot event name
        plt.text(room+0.48, (start+end)*0.5, eventName,
                 ha='center', va='center', fontsize=11)

    # Set Axis
    ax = fig.add_subplot(111)
    ax.yaxis.grid()
    ax.set_xlim(0.5, len(sections)+0.5)
    ax.set_ylim(end_hour, start_hour)
    ax.set_xticks(range(1, len(sections)+1))
    ax.set_xticklabels(sections)
    ax.set_ylabel('Time')

    # Set Second Axis
    ax2 = ax.twiny().twinx()
    ax2.set_xlim(ax.get_xlim())
    ax2.set_ylim(ax.get_ylim())
    ax2.set_xticks(ax.get_xticks())
    ax2.set_xticklabels(sections)
    ax2.set_ylabel('Time')

    plt.title(title, y=1.07)
    plt.savefig('{0}.png'.format(title), dpi=200)

