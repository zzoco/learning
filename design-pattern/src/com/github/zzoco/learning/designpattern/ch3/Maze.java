package com.github.zzoco.learning.designpattern.ch3;

import java.util.HashMap;
import java.util.Map;

/**
 * @author nnoco
 * @since 16/09/2019
 */
public class Maze {
    private Map<Integer, Room> rooms = new HashMap<>();

    void addRoom(Room room) {
        rooms.put(room.getRoomNumber(), room);
    }

    Room getRoom(int roomNumber) {
        return rooms.get(roomNumber);
    }
}
