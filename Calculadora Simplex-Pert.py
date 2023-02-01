from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
from src.simplex import Simplex
#from src.perl import Perl
from src.views.ui_mainWindow import Ui_MainWindow
import sys, os

class MainWindow(QMainWindow):
    # Constructor
    def __init__(self):
        
        super(MainWindow, self).__init__()
        
        self.ui = Ui_MainWindow()
       
        self.ui.setupUi(self)
       
        # Resolver Ruta
  
        def resolver_ruta(ruta_relativa):
            if hasattr(sys, "_MEIPASS"):
                return os.path.join(sys._MEIPASS, ruta_relativa)
            return os.path.join(os.path.abspath("."), ruta_relativa)
        
        # Icono ventana
        self.icoMain = resolver_ruta("C:/Users/santi/OneDrive/Documentos/deterministicos/calculadora-metodo-simplex-master/calculadora-metodo-simplex-master/src/assets/mayor.jpg")
        self.icoError = resolver_ruta("C:/Users/santi/OneDrive/Documentos/deterministicos/calculadora-metodo-simplex-master/calculadora-metodo-simplex-master/src/assets/cancelar.ico")
        self.icoSucess = resolver_ruta("C:/Users/santi/OneDrive/Documentos/deterministicos/calculadora-metodo-simplex-master/calculadora-metodo-simplex-master/src/assets/check.ico")
        self.setWindowIcon(QIcon(self.icoMain))

        # Imagenes
        self.img = resolver_ruta("C:/Users/santi/OneDrive/Documentos/deterministicos/calculadora-metodo-simplex-master/calculadora-metodo-simplex-master/src/assets/INICIO2.png")
        pixmap = QPixmap(self.img)
        self.ui.label.setPixmap(pixmap)
        self.ui.label.setAlignment(Qt.AlignCenter)
        
        # Eventos
        #self.ui.actionSimplex.triggered.connect(self.showSimplexUI)
        self.showSimplexUI()

    # Método: Muestra la interfaz del método simplex  
    def showSimplexUI(self):
        #self.ui.widgetPerl.setVisible(False)
        self.ui.widgetSimplex.setVisible(True)
        self.simplex = Simplex(self.ui, self.icoError, self.icoSucess, self.icoMain)
        self.simplex.deleteData()

  
    
# Inicia la aplicación
if __name__ == '__main__':    
    #app = QApplication([])
   # app.setStyle(QStyleFactory.create('Fusion'))
    mi_App = MainWindow()
    mi_App.show()
    #sys.exit(app.exec_())