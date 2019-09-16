package com.github.zzoco.learning.designpattern.ch3;

/**
 * @author nnoco
 * @since 16/09/2019
 */
public class Room implements MapSite {
    private int roomNumber;

    private MapSite[] sides = new MapSite[4];

    public Room(int roomNumber) {
        this.roomNumber = roomNumber;
    }

    @Override
    public void enter() {

    }

    public void setSide(Direction direction, MapSite side) {
        sides[direction.ordinal()] = side;
    }

    public MapSite getSide(Direction direction) {
        return sides[direction.ordinal()];
    }

    public int getRoomNumber() {
        return roomNumber;
    }
}
