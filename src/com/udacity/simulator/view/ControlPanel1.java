package com.lib.udacity.simulator.view;

import java.awt.BorderLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.Rectangle;

import javax.swing.JButton;
import javax.swing.JPanel;
import javax.swing.JSlider;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;

import java.util.LinkedList;
import java.util.List;

import com.lib.udacity.simulator.Simulation;

public class ControlPanel1 extends JPanel implements ActionListener,  ChangeListener
{
	private static final long serialVersionUID = 1L;
	private Simulation simulation;

	private JButton btnStart;
	private JSlider speed;
	
	public ControlPanel1(Simulation s)
	{
		this.simulation = s;
		
		btnStart = new JButton("Pause");
		btnStart.addActionListener(this);

		speed = new JSlider(0,  100);
		speed.addChangeListener(this);
		speed.setValue(70);

		this.setLayout(new BorderLayout());
		this.add(btnStart, BorderLayout.EAST);
		this.add(speed, BorderLayout.CENTER);
	}

	@Override
	public void actionPerformed(ActionEvent arg0) 
	{
		if(arg0.getSource() == btnStart) {
			 if(simulation.isRunning())
			 {
				simulation.setRunning(false);
				btnStart.setText("Start");
			 }
			 else
			 {
				simulation.setRunning(true);
				if( simulation.start() )
					 btnStart.setText("Pause");
			 }

			 simulation.visual.revalidate();
	  	 simulation.visual.repaint();
		}
/*		else if(arg0.getSource() == btnClear) {
			 simulation.world.wallMap.rects = new LinkedList<Rectangle>();
			 int height = simulation.world.getHeight();
			 int width = simulation.world.getWidth();
			 int bgSpacing = simulation.world.getSpacint();
			 
			 simulation.world.wallMap.rects.add(new Rectangle(0, 0, width, bgSpacing));
			 simulation.world.wallMap.rects.add(new Rectangle(0, 0, bgSpacing, height));
			 simulation.world.wallMap.rects.add(new Rectangle(0, height-bgSpacing, width, bgSpacing));
			 simulation.world.wallMap.rects.add(new Rectangle(width-bgSpacing, 0, bgSpacing, height));
			 
			 simulation.visual.revalidate();
			 simulation.visual.repaint();
		}*/
	}

	@Override
	public void stateChanged(ChangeEvent arg0)
	{
		simulation.setTimeDelay(101 - speed.getValue());
	}
}
