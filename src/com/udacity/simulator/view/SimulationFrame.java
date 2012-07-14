package com.lib.udacity.simulator.view;

import java.awt.BorderLayout;

import javax.swing.JFrame;

import com.lib.udacity.simulator.Simulation;

public class SimulationFrame extends JFrame
{
	private static final long serialVersionUID = 1L;
	
	private SimulationPanel simulationPanel;
	private ControlPanel1 controlPanel1;
	private ControlPanel2 controlPanel2;

	public SimulationFrame(Simulation s)
	{
		simulationPanel = new SimulationPanel(s);
		s.setPanel(simulationPanel);
		
		controlPanel1 = new ControlPanel1(s);
		controlPanel2 = new ControlPanel2(s);
		
		setLayout( new BorderLayout() );
		add(simulationPanel, BorderLayout.CENTER);
		add(controlPanel1, BorderLayout.NORTH);
		add(controlPanel2,  BorderLayout.SOUTH);
		
		setBounds(100, 100, s.getWorld().getWidth()+20, s.getWorld().getHeight()+80);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
}
