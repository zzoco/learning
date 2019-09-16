package com.github.zzoco.learning.designpattern.ch3;

/**
 * @author nnoco
 * @since 16/09/2019
 */
public class Door implements MapSite {
    private Room room1;

    private Room room2;

    private boolean isOpen;

    public Door(Room room1, Room room2) {
        this.room1 = room1;
        this.room2 = room2;
    }

    @Override
    public void enter() {

    }

    Room otherSideFrom(Room room) {
        return (room == room1) ? room2 : room1;
    }
}
