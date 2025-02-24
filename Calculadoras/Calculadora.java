package Calculadoras;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Calculadora extends JFrame {
    private JTextField txtNum1;
    private JTextField txtNum2;
    private JTextField txtTotal;
    private JButton btnSumar;
    private JButton btnRestar;
    private JButton btnMultiplicar;
    private JButton btnDividir;
    private JButton btnBorrar;

    public Calculadora() {
        setSize(400, 330);
        setLocationRelativeTo(null);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JPanel panel = new JPanel();
        panel.setLayout(null);

        // Etiquetas y campos de texto
        JLabel lblNum1 = new JLabel("Número 1");
        lblNum1.setBounds(20, 20, 80, 20);
        panel.add(lblNum1);

        txtNum1 = new JTextField();
        txtNum1.setBounds(120, 20, 100, 20);
        panel.add(txtNum1);

        JLabel lblNum2 = new JLabel("Número 2");
        lblNum2.setBounds(20, 50, 80, 20);
        panel.add(lblNum2);

        txtNum2 = new JTextField();
        txtNum2.setBounds(120, 50, 100, 20);
        panel.add(txtNum2);

        JLabel lblTotal = new JLabel("Total");
        lblTotal.setBounds(20, 80, 80, 20);
        panel.add(lblTotal);

        txtTotal = new JTextField();
        txtTotal.setBounds(120, 80, 100, 20);
        txtTotal.setEditable(false); // Hacer el campo de solo lectura
        panel.add(txtTotal);

        // Botones
        btnSumar = new JButton("Sumar");
        btnSumar.setBounds(20, 120, 80, 30);
        panel.add(btnSumar);

        btnRestar = new JButton("Restar");
        btnRestar.setBounds(120, 120, 80, 30);
        panel.add(btnRestar);

        btnMultiplicar = new JButton("Multiplicar");
        btnMultiplicar.setBounds(20, 160, 100, 30);
        panel.add(btnMultiplicar);

        btnDividir = new JButton("Dividir");
        btnDividir.setBounds(140, 160, 80, 30);
        panel.add(btnDividir);

        btnBorrar = new JButton("Borrar");
        btnBorrar.setBounds(20, 200, 80, 30);
        panel.add(btnBorrar);

        // Acciones de los botones
        btnSumar.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                try {
                    int num1 = Integer.parseInt(txtNum1.getText());
                    int num2 = Integer.parseInt(txtNum2.getText());
                    int resultado = num1 + num2;
                    txtTotal.setText(String.valueOf(resultado));
                } catch (NumberFormatException ex) {
                    txtTotal.setText("Error");
                }
            }
        });

        btnRestar.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                try {
                    int num1 = Integer.parseInt(txtNum1.getText());
                    int num2 = Integer.parseInt(txtNum2.getText());
                    int resultado = num1 - num2;
                    txtTotal.setText(String.valueOf(resultado));
                } catch (NumberFormatException ex) {
                    txtTotal.setText("Error");
                }
            }
        });

        btnMultiplicar.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                try {
                    int num1 = Integer.parseInt(txtNum1.getText());
                    int num2 = Integer.parseInt(txtNum2.getText());
                    int resultado = num1 * num2;
                    txtTotal.setText(String.valueOf(resultado));
                } catch (NumberFormatException ex) {
                    txtTotal.setText("Error");
                }
            }
        });

        btnDividir.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                try {
                    int num1 = Integer.parseInt(txtNum1.getText());
                    int num2 = Integer.parseInt(txtNum2.getText());
                    if (num2 == 0) {
                        txtTotal.setText("Error: Div/0");
                    } else {
                        double resultado = (double) num1 / num2;
                        txtTotal.setText(String.valueOf(resultado));
                    }
                } catch (NumberFormatException ex) {
                    txtTotal.setText("Error");
                }
            }
        });

        btnBorrar.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                txtNum1.setText("");
                txtNum2.setText("");
                txtTotal.setText("");
            }
        });

        add(panel);
    }

    public static void main(String[] args) {
        Calculadora calculadora = new Calculadora();
        calculadora.setVisible(true);
    }
}