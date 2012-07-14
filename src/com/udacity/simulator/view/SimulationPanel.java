package com.lib.udacity.simulator.view;

import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Rectangle;
import java.awt.event.MouseListener;
import java.awt.event.MouseEvent;

import javax.swing.JPanel;

import com.lib.udacity.simulator.Simulation;
import com.lib.udacity.simulator.abstracts.SimulationObject;

public class SimulationPanel extends JPanel implements MouseListener
{
	private static final long serialVersionUID = 1L;
	private Simulation simulation;
	
	private int px;
	private int py;
	private int pbx;
	private int pby;
	
	public SimulationPanel(Simulation s)
	{
		this.simulation = s;
		addMouseListener(this);
	}
	
	@Override
	public void paint(Graphics g) 
	{
		super.paint(g);
		
		//if(simulation.isRunning())
		{
			Graphics2D g2d = (Graphics2D)g;
			for(SimulationObject o : simulation)
				o.onPaint(g2d);
				
			simulation.getListener().onPaint(g2d);
		}
	}

	public void mousePressed(MouseEvent e)
	{
		int bgSpacing = simulation.world.getSpacint();
		int height = simulation.world.getHeight();
		int width = simulation.world.getWidth();
	  
		px = e.getX();
		if(px < 0)
			 px = 0;
		else if(px > width)
			 px = width;
		
		py = e.getY();
		if(py < 0)
			 py = 0;
		else if(py > height)
			 py = height;
		
		pbx = (int)(px/bgSpacing);
		pby = (int)(py/bgSpacing);
	}
	
	public void mouseReleased(MouseEvent e)
	{
		int height = simulation.world.getHeight();
		int width = simulation.world.getWidth();
		int bgSpacing = simulation.world.getSpacint();
	  
		int cx = e.getX();
		if(cx < 0)
			 cx = 0;
		else if(cx > width)
			 cx = width - bgSpacing;
		
		int cy = e.getY();
		if(cy < 0)
			 cy = 0;
		else if(cy > height)
			 cy = height - bgSpacing;
		
		int cbx = (int)(cx/bgSpacing);
		int cby = (int)(cy/bgSpacing);
	  
		if(cbx > pbx)
			 if(cby > pby)
				 simulation.world.wallMap.rects.add(new Rectangle(pbx*bgSpacing, pby*bgSpacing, (cbx-pbx)*bgSpacing, (cby-pby)*bgSpacing));
			 else
				 simulation.world.wallMap.rects.add(new Rectangle(pbx*bgSpacing, cby*bgSpacing, (cbx-pbx)*bgSpacing, (pby-cby)*bgSpacing));
		else
			 if(cby > pby)
				 simulation.world.wallMap.rects.add(new Rectangle(cbx*bgSpacing, pby*bgSpacing, (pbx-cbx)*bgSpacing, (cby-pby)*bgSpacing));
			 else
				 simulation.world.wallMap.rects.add(new Rectangle(pbx*bgSpacing, cby*bgSpacing, (pbx-cbx)*bgSpacing, (pby-cby)*bgSpacing));
		this.revalidate();
		this.repaint();
	}
	
	public void mouseEntered(MouseEvent e)
	{
	  
	}
	
	public void mouseClicked(MouseEvent e)
	{
		int height = simulation.world.getHeight();
		int width = simulation.world.getWidth();
		int bgSpacing = simulation.world.getSpacint();
		
		int x = e.getX();
		if(x < 0)
			 x = 0;
		else if(x > width)
			 x = width - bgSpacing;
		
		int y = e.getY();
		if(y < 0)
			 y = 0;
		else if(y > height)
			 y = height - bgSpacing;
		
		int bx = (int)(x/bgSpacing);
		int by = (int)(y/bgSpacing);
				
		simulation.world.wallMap.rects.add(new Rectangle(bx*bgSpacing, by*bgSpacing, 10, 10));
		this.revalidate();
		this.repaint();
	}
	
	public void mouseExited(MouseEvent e)
	{
		
	}
}
