public class House {
    private Turtle tia;

    public House(Turtle t) {
        tia = t;
    }
    public void base(int x, int y, int length){
        tia.penUp();
        tia.moveTo(x, y);
        tia.penDown();
        tia.forward(length); //default value 100
        tia.turnRight();
        tia.forward(length);
        tia.turnRight();
        tia.forward(length);
        tia.turnRight();
        tia.forward(length);
        tia.turnRight();
    }
}
