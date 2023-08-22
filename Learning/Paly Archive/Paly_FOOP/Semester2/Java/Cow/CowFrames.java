import java.awt.Color;
import java.awt.Graphics;

import javax.swing.JFrame;

public class CowFrames extends JFrame {
	private final Color BISQUE = new Color(0xcdb79e);
	private final Color CHARTRUSE = new Color(0x7FFF00);
	public CowFrames () {
		init();
	}
	
	public void init() {
		setSize(700,600);
		setBackground(Color.WHITE);
		repaint();
	}
//draw a cow
	public void paint(Graphics g) {
		g.setColor(BISQUE);
		//g.setColor(CHARTRUSE);
		g.setColor(Color.BLUE);
		g.fillRect(0, 0, 700, 200);
		g.setColor(Color.GREEN);
		g.fillRect(0, 200, 700, 400);
		g.setColor(Color.BLACK);
		g.fillOval(350, 100, 200, 100);
		g.setColor(Color.WHITE);
		g.fillOval(355, 90, 35, 60);
		g.fillOval(450, 110, 30, 30);
		g.fillOval(410, 110, 30, 30);
		g.fillOval(435, 140, 30, 30);
	}
}