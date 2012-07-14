package com.lib.udacity.simulator.view;

import java.awt.BorderLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.Rectangle;

import javax.swing.JButton;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.event.ChangeEvent;

import java.util.LinkedList;
import java.util.List;

import com.lib.udacity.simulator.Simulation;

public class ControlPanel2 extends JPanel implements ActionListener
{
	private static final long serialVersionUID = 1L;
	private Simulation simulation;

	private JButton btnGoal;
	private JTextField goalX;
	private JTextField goalY;
	
	public ControlPanel2(Simulation s)
	{
		this.simulation = s;
		
		btnGoal = new JButton("Change Goal");
		btnGoal.addActionListener(this);

	  goalX = new JTextField(35);
		goalX.setText("770");
		goalY = new JTextField(35);
		goalY.setText("570");

		this.setLayout(new BorderLayout());
		this.add(btnGoal, BorderLayout.EAST);
		this.add(goalX, BorderLayout.WEST);
    this.add(goalY,  BorderLayout.CENTER);
	}

	@Override
	public void actionPerformed(ActionEvent arg0) 
	{
		if(arg0.getSource() == btnGoal) {
			int x = Integer.parseInt(goalX.getText());
			int y = Integer.parseInt(goalY.getText());
		  System.out.print(x+" - "+y);

			simulation.setGoalX(x);
			simulation.setGoalY(y);
		}
	}
}
