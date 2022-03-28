from fpdf import FPDF, HTMLMixin
import ListaRobot
from os import system

def pdf_combate(robot, celda):
    pdf = FPDF("P", "cm", "A4")
    pdf.set_font("helvetica", "", 16)
    pdf.add_page()
    pdf.cell(19, 1, "RUTA DE EXTRACCIÓN", align="C", ln=True)
    pdf.image("grafica.png", x=0.5, w=20, h=16)
    pdf.set_font("helvetica", "", 12)
    pdf.cell(6.5, 1, "Celda negra: intransitable", align="C")
    pdf.cell(6.5, 1, "Celda blanca: camino", align="C")
    pdf.cell(6.5, 1, "Celda verde: entrada", align="C")
    pdf.cell(6.5, 1, "Celda azul: unidad civil", align="C", ln=True)
    pdf.cell(6.5, 1, "Celda gris: recurso", align="C")
    pdf.cell(6.5, 1, "Celda roja: unidad militar", align="C", ln=True)
    pdf.set_font("helvetica", "B", 14)
    pdf.cell(19, 1, "TIPO DE MISIÓN: EXTRACCIÓN DE RECURSO", align="C", ln=True)
    pdf.cell(19, 1, "RECURSO EXTRAIDO: " + str(celda.x) + ", " + str(celda.y), align="C", ln=True)
    pdf.cell(19, 1, "ROBOT UTILIZADO: " + robot.name, align="C", ln=True)
    pdf.cell(19, 1, "CAPACIDAD DE COMBATE INICIAL: " + str(ListaRobot.robot_seleccionado.capacidad), align="C", ln=True)
    pdf.cell(19, 1, "CAPACIDAD DE COMBATE FINAL: " + str(robot.capacidad), align="C", ln=True)
    pdf.output('reporte.pdf', 'F')
    system("xdg-open reporte.pdf")


def pdf_rescate(robot, celda):
    pdf = FPDF("P", "cm", "A4")
    pdf.set_font("helvetica", "", 16)
    pdf.add_page()
    pdf.cell(19, 1, "RUTA DE RESCATE", align="C", ln=True)
    pdf.image("grafica.png", x=0.5, w=20, h=16)
    pdf.set_font("helvetica", "", 12)
    pdf.cell(6.5, 1, "Celda negra: intransitable", align="C")
    pdf.cell(6.5, 1, "Celda blanca: camino", align="C")
    pdf.cell(6.5, 1, "Celda verde: entrada", align="C")
    pdf.cell(6.5, 1, "Celda azul: unidad civil", align="C", ln=True)
    pdf.cell(6.5, 1, "Celda gris: recurso", align="C")
    pdf.cell(6.5, 1, "Celda roja: unidad militar", align="C", ln=True)
    pdf.set_font("helvetica", "B", 14)
    pdf.cell(19, 1, "TIPO DE MISIÓN: RESCATE DE CIVILES", align="C", ln=True)
    pdf.cell(19, 1, "UNIDAD RESCATADA: " + str(celda.x) + ", " + str(celda.y), align="C", ln=True)
    pdf.cell(19, 1, "ROBOT UTILIZADO: " + robot.name, align="C", ln=True)
    pdf.output('reporte.pdf', 'F')
    system("xdg-open reporte.pdf")

