Public Class Form1
    Dim numerouno As Double
    Dim numerodos As Double
    Dim total As Double
    Dim operacion As Integer

    Private Sub btn0_Click(sender As Object, e As EventArgs) Handles btn0.Click
        TextBox2.Text = TextBox2.Text & "0"
    End Sub

    Private Sub btn1_Click(sender As Object, e As EventArgs) Handles btn1.Click
        TextBox2.Text = TextBox2.Text & "1"
    End Sub

    ' Repetir para los botones 2 al 9...

    Private Sub btnPunto_Click(sender As Object, e As EventArgs) Handles btnPunto.Click
        TextBox2.Text = TextBox2.Text & "."
        btnPunto.Enabled = False
    End Sub

    Private Sub btnSuma_Click(sender As Object, e As EventArgs) Handles btnSuma.Click
        numerouno = Val(TextBox2.Text)
        TextBox2.Clear()
        operacion = 1 ' 1 para suma
    End Sub

    Private Sub btnResta_Click(sender As Object, e As EventArgs) Handles btnResta.Click
        numerouno = Val(TextBox2.Text)
        TextBox2.Clear()
        operacion = 2 ' 2 para resta
    End Sub

    Private Sub btnMultiplicacion_Click(sender As Object, e As EventArgs) Handles btnMultiplicacion.Click
        numerouno = Val(TextBox2.Text)
        TextBox2.Clear()
        operacion = 3 ' 3 para multiplicación
    End Sub

    Private Sub btnDivision_Click(sender As Object, e As EventArgs) Handles btnDivision.Click
        numerouno = Val(TextBox2.Text)
        TextBox2.Clear()
        operacion = 4 ' 4 para división
    End Sub

    Private Sub btnIgual_Click(sender As Object, e As EventArgs) Handles btnIgual.Click
        numerodos = Val(TextBox2.Text)
        Select Case operacion
            Case 1
                total = numerouno + numerodos
            Case 2
                total = numerouno - numerodos
            Case 3
                total = numerouno * numerodos
            Case 4
                If numerodos <> 0 Then
                    total = numerouno / numerodos
                Else
                    TextBox2.Text = "Error"
                    Return
                End If
        End Select
        TextBox2.Text = total
    End Sub

    Private Sub btnBorrar_Click(sender As Object, e As EventArgs) Handles btnBorrar.Click
        TextBox2.Clear()
        btnPunto.Enabled = True
    End Sub
End Class