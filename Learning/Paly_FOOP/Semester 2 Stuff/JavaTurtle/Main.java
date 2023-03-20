import javax.swing.*;
import java.awt.event.*;
import java.util.*;
import java.awt.*;

public class Main {
  public static void main(String[] args) {  
    World world = new World(300,300);
     
    Turtle tia = new Turtle(world);
    //house
    tia.penUp();
    tia.moveTo(60, 260);
    tia.penDown();
    tia.forward(); //default value 100
    tia.turnRight();
    tia.forward(200);
    tia.turnRight();
    tia.forward(100);
    tia.turnRight();
    tia.forward(200);
    tia.turnRight();
    //roof
    tia.penUp();
    tia.forward(100);
    tia.turn(45);
    tia.penDown();
    tia.forward(141);
    tia.turn(90);
    tia.forward(143);
    tia.turn(45);


  
    world.setVisible(true);
  }
}
