package gui;

import java.awt.Dimension;


import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JPanel;

public class RayTracerIU {
	static final String COMANDO_SALIR = "SALIR";
	static final String COMANDO_GENERAR = "GENERAR";
	static final String COMANDO_LIMPIAR = "LIMPIAR";
    static final String COMANDO_GUARDAR = "GUARDAR";
	
	private JFrame ventana;
	private ControlVentana control;
    public JLabel labelImagen;
	
	public RayTracerIU() {
		ventana = new JFrame("Ray Tracer");
		ventana.setSize(new Dimension(620, 501));
		ventana.getContentPane().setLayout(null);
		ventana.setLocationRelativeTo(null);
		ventana.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		control = new ControlVentana(this);
		
		setMenuBar();
		setControl();
		setPanelImagen();
		
		ventana.setVisible(true);
	}
	
	private void setMenuBar() {
		JMenuBar menuBar = new JMenuBar();
		ventana.setJMenuBar(menuBar);
		
		JMenu menuArchivo = new JMenu("Archivo");
		menuBar.add(menuArchivo);
		
		JMenuItem itemGuardar = new JMenuItem("Guardar");
		menuArchivo.add(itemGuardar);
		
		JMenuItem salirItem = new JMenuItem("Salir");
		salirItem.setActionCommand(COMANDO_SALIR);
		salirItem.addActionListener(control);
		menuArchivo.add(salirItem);
	}
	
	private void setControl() {
		JButton botonGenerarImagen = new JButton("Generar");
		botonGenerarImagen.setBounds(159, 404, 89, 28);
		botonGenerarImagen.setActionCommand(COMANDO_GENERAR);
		botonGenerarImagen.addActionListener(control);
		ventana.getContentPane().add(botonGenerarImagen);
		
		JButton botonLimpiarImagen = new JButton("Limpiar");
		botonLimpiarImagen.setBounds(365, 404, 90, 28);
		botonLimpiarImagen.addActionListener(control);
		ventana.getContentPane().add(botonLimpiarImagen);
	}
	
	private void setPanelImagen() {
		JPanel panel = new JPanel();
		panel.setBounds(12, 12, 580, 380);
		labelImagen = new JLabel();//new ImageIcon(Toolkit.getDefaultToolkit().getImage(dir)));
		panel.add(labelImagen);
		ventana.getContentPane().add(panel);
	}
}