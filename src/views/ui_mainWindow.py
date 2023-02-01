from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
       ############################################ UI - MAIN WINDOW ############################################
        # VENTANA PRINCIPAL
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 630)
        MainWindow.setMinimumSize(QtCore.QSize(1366, 650))
        MainWindow.setMaximumSize(QtCore.QSize(1366, 0))
        MainWindow.setStyleSheet(" font-size: 12px; font-weight: bold; font-family: time new roman")
        
        # WIDGET CONTENEDOR
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # FRAME CONTENEDOR PRINCIPAL
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(5, 0, 1355, 790))
        self.frame.setStyleSheet("background: #FEFEFE; font-size: 16px; font-weight: bold; font-family: time new roman")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        # LABEL CONTENEDORA DE IMAGEN
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 1366, 790))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setStyleSheet("background: #2b1b18")
        
        
        # CONTENEDOR SIMPLEX
        self.widgetSimplex = QtWidgets.QWidget(self.frame)
        self.widgetSimplex.setEnabled(True)
        self.widgetSimplex.setGeometry(QtCore.QRect(0, 0, 1355, 690))
        self.widgetSimplex.setStyleSheet("")
        self.widgetSimplex.setObjectName("widgetSimplex")
        self.widgetSimplex.setVisible(False)
        # CONTENEDOR PERL
        
        """self.widgetPerl = QtWidgets.QWidget(self.frame)
        self.widgetPerl.setEnabled(True)
        self.widgetPerl.setGeometry(QtCore.QRect(0, 0, 1355, 690))
        self.widgetPerl.setStyleSheet("")
        self.widgetPerl.setObjectName("widgetPerl")
        self.widgetPerl.setVisible(False)"""
        MainWindow.setCentralWidget(self.centralwidget)
        
        
        # MENÚ
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(280, 500, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuM_todo = QtWidgets.QMenu(self.menubar)
        self.menuM_todo.setObjectName("menuM_todo")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.setVisible(True)
        
        
        # STATUSBAR
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        # ACTION SIMPLEX
        self.actionSimplex = QtWidgets.QAction(MainWindow)
        self.actionSimplex.setObjectName("actionSimplex")
        # ACTION PERL
        self.actionPerl_CPM = QtWidgets.QAction(MainWindow)
        self.actionPerl_CPM.setObjectName("actionPerl_CPM")
        self.menuM_todo.addAction(self.actionSimplex)
        self.menuM_todo.addSeparator()
        self.menuM_todo.addAction(self.actionPerl_CPM)
        self.menubar.addAction(self.menuM_todo.menuAction())
        ########################################### UI - MÉTODO SIMPLEX ###########################################
        # GROUP BOX DATOS
        self.groupBoxDatos = QtWidgets.QGroupBox(self.widgetSimplex)
        self.groupBoxDatos.setGeometry(QtCore.QRect(25, 0, 400, 135))
        font = QtGui.QFont()
        font.setFamily("time new roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(70)
        self.groupBoxDatos.setFont(font)
        self.groupBoxDatos.setObjectName("groupBoxDatos")
        self.groupBoxDatos.setStyleSheet("background: #bcc1d2")
        
        # LABEL VARIABLE
        self.lblVar = QtWidgets.QLabel(self.groupBoxDatos)
        self.lblVar.setGeometry(QtCore.QRect(35, 30, 280, 20))
        self.lblVar.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("time new roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lblVar.setFont(font)
        self.lblVar.setAutoFillBackground(False)
        self.lblVar.setStyleSheet("")
        self.lblVar.setObjectName("lblVar")
        self.lblVar.setStyleSheet("font-size: 12px")
        # INPUT VARIABLE
        self.inputVar = QtWidgets.QSpinBox(self.groupBoxDatos)
        self.inputVar.setGeometry(QtCore.QRect(350, 30, 40, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.inputVar.setFont(font)
        self.inputVar.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.inputVar.setToolTipDuration(-27)
        self.inputVar.setKeyboardTracking(True)
        self.inputVar.setMinimum(2)
        self.inputVar.setObjectName("inputVar")
        
      
        # LABEL RESTRICCIONES
        self.lblRes = QtWidgets.QLabel(self.groupBoxDatos)
        self.lblRes.setGeometry(QtCore.QRect(40, 60, 300, 20))
        font = QtGui.QFont()
        font.setFamily("time new roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lblRes.setFont(font)
        self.lblRes.setStyleSheet("")
        self.lblRes.setObjectName("lblRes")
        self.lblRes.setStyleSheet("font-size: 12px")
        
        
        # INPUT RESTRICCIONES
        self.inputRes = QtWidgets.QSpinBox(self.groupBoxDatos)
        self.inputRes.setGeometry(QtCore.QRect(350, 60, 40, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.inputRes.setFont(font)
        self.inputRes.setMinimum(1)
        self.inputRes.setObjectName("inputRes")
        # BTN GENERAR
        self.btnGenerar = QtWidgets.QPushButton(self.groupBoxDatos)
        self.btnGenerar.setGeometry(QtCore.QRect(170, 90, 80, 30))
        self.btnGenerar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnGenerar.setObjectName("btnGenerar")
        self.btnGenerar.setStyleSheet("background: #3999da; color: #000000")
        self.opacity_effectGenerar = QtWidgets.QGraphicsOpacityEffect() 
        self.opacity_effectGenerar.setOpacity(1) 
        self.btnGenerar.setGraphicsEffect(self.opacity_effectGenerar)
        
        
        # GROUP BOX FUNCIÓN OBJETIVA
        self.groupBoxFuncObj = QtWidgets.QGroupBox(self.widgetSimplex)
        self.groupBoxFuncObj.setGeometry(QtCore.QRect(445, 0, 430, 135))
        font = QtGui.QFont()
        font.setFamily("time new roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxFuncObj.setFont(font)
        self.groupBoxFuncObj.setObjectName("groupBoxFuncObj")
        self.groupBoxFuncObj.setStyleSheet("background: #bcc1d2")
        
        # LABEL MAX Z
        self.lblTextMaxZ = QtWidgets.QLabel(self.groupBoxFuncObj)
        self.lblTextMaxZ.setGeometry(QtCore.QRect(20, 30, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblTextMaxZ.setFont(font)
        self.lblTextMaxZ.setObjectName("lblTextMaxZ")
        
        # TABLA FUNCIÓN OBJETIVA
        self.tableFuncObj = QtWidgets.QTableWidget(self.groupBoxFuncObj)
        self.tableFuncObj.setGeometry(QtCore.QRect(15, 60, 400, 68))
        self.tableFuncObj.setObjectName("tableFuncObj")
        self.tableFuncObj.setColumnCount(0)
        self.tableFuncObj.setRowCount(0)
        self.tableFuncObj.verticalHeader().setVisible(False)
    
        self.tableFuncObj.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignHCenter and QtCore.Qt.AlignVCenter and QtCore.Qt.AlignCenter)
        self.tableFuncObj.horizontalHeader().setDefaultSectionSize(50)
        self.tableFuncObj.horizontalHeader().setStyleSheet("color: #fff")
        
        self.tableFuncObj.setStyleSheet("border: none; font-size: 16px")
        
        
        # GROUP BOX RESTRICCIONES
        self.groupBoxRestriccion = QtWidgets.QGroupBox(self.widgetSimplex)
        self.groupBoxRestriccion.setGeometry(QtCore.QRect(890, 0, 450, 360))
        font = QtGui.QFont()
        font.setFamily("time new roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxRestriccion.setFont(font)
        self.groupBoxRestriccion.setObjectName("groupBoxRestriccion")
        self.groupBoxRestriccion.setStyleSheet("background: #bcc1d2")
        
        # TABLA RESTRICCIONES
        self.tableRestr = QtWidgets.QTableWidget(self.groupBoxRestriccion)
        self.tableRestr.setGeometry(QtCore.QRect(10, 30, 430, 320))
        self.tableRestr.setObjectName("tableRestr")
        self.tableRestr.setColumnCount(0)
        self.tableRestr.setRowCount(0)
        self.tableRestr.verticalHeader().setVisible(False)
        self.tableRestr.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignHCenter and QtCore.Qt.AlignVCenter and QtCore.Qt.AlignCenter)
        self.tableRestr.horizontalHeader().setDefaultSectionSize(50)
        self.tableRestr.horizontalHeader().setStyleSheet("color: #fff")
        self.tableRestr.setStyleSheet("border: none; font-size: 16px")
        
        
        # GROUP BOX ACCIONES
        self.groupBoxAcciones = QtWidgets.QGroupBox(self.widgetSimplex)
        self.groupBoxAcciones.setGeometry(QtCore.QRect(890, 420, 440, 181))
        font = QtGui.QFont()
        font.setFamily("time new roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxAcciones.setFont(font)
        self.groupBoxAcciones.setObjectName("groupBoxAcciones")
        
        
        # BTN CALCULAR
        self.btnCalcular = QtWidgets.QPushButton(self.groupBoxAcciones)
        self.btnCalcular.setGeometry(QtCore.QRect(35, 45, 162, 60))
        self.btnCalcular.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCalcular.setObjectName("btnCalcular")
        self.btnCalcular.setEnabled(False)
        self.btnCalcular.setStyleSheet("background: #3999da; color: #000000; font-size: 16px;")
        self.opacity_effectCalc = QtWidgets.QGraphicsOpacityEffect() 
        self.opacity_effectCalc.setOpacity(0.3) 
        self.btnCalcular.setGraphicsEffect(self.opacity_effectCalc) 
        # BTN NUEVO 
        self.btnNuevo = QtWidgets.QPushButton(self.groupBoxAcciones)
        self.btnNuevo.setGeometry(QtCore.QRect(250, 45, 162, 60))
        self.btnNuevo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnNuevo.setObjectName("btnNuevo")
        self.btnNuevo.setStyleSheet("background: #3999da; color: #000000; font-size: 16px")
        # BTN SALIR
        self.btnSalir = QtWidgets.QPushButton(self.groupBoxAcciones)
        self.btnSalir.setGeometry(QtCore.QRect(35, 110, 162, 60))
        self.btnSalir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSalir.setObjectName("btnSalir")
        self.btnSalir.setStyleSheet("background: #3999da; color: #000000; font-size: 16px")
        
        # BTN NEXT
        self.btnSimplex = QtWidgets.QPushButton(self.groupBoxAcciones)
        self.btnSimplex.setGeometry(QtCore.QRect(240, 35, 83, 50))
        self.btnSimplex.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSimplex.setObjectName("btnSalir")
        self.btnSimplex.setStyleSheet("background: #3999da; color: #000000; font-size: 14px")
        self.btnSimplex.setVisible(False)
        
        # BTN IMPRIMIR
        self.btnImprimir = QtWidgets.QPushButton(self.groupBoxAcciones)
        self.btnImprimir.setGeometry(QtCore.QRect(348, 35, 83, 50))
        self.btnImprimir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnImprimir.setObjectName("btnImprimir")
        self.btnImprimir.setEnabled(False)
        self.btnImprimir.setStyleSheet("background: #3999da; color: #000000; font-size: 14px")
        self.opacity_effectImprimir = QtWidgets.QGraphicsOpacityEffect() 
        self.opacity_effectImprimir.setOpacity(0.3) 
        self.btnImprimir.setGraphicsEffect(self.opacity_effectImprimir) 
        self.btnImprimir.setVisible(False)
        
        # BTN CALCULAR PIBOTE
        self.btnCalPibote = QtWidgets.QPushButton(self.groupBoxAcciones)
        self.btnCalPibote.setGeometry(QtCore.QRect(20, 110, 132, 50))
        self.btnCalPibote.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCalPibote.setObjectName("btnCalPibote")
        self.btnCalPibote.setEnabled(False)
        self.btnCalPibote.setStyleSheet("background: #3999da; color: #000000; font-size: 14px")
        self.opacity_effectPibote = QtWidgets.QGraphicsOpacityEffect() 
        self.opacity_effectPibote.setOpacity(0.3) 
        self.btnCalPibote.setGraphicsEffect(self.opacity_effectPibote) 
        self.btnCalPibote.setVisible(False)
        
        # BTN ANTERIROR TABLA
        self.btnPreviousTabla = QtWidgets.QPushButton(self.groupBoxAcciones)
        self.btnPreviousTabla.setGeometry(QtCore.QRect(170, 110, 122, 50))
        self.btnPreviousTabla.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnPreviousTabla.setObjectName("btnPreviousTabla")
        self.btnPreviousTabla.setEnabled(False)
        self.btnPreviousTabla.setStyleSheet("background: #3999da; color: #000000; font-size: 14px")
        self.opacity_effectAnterior = QtWidgets.QGraphicsOpacityEffect() 
        self.opacity_effectAnterior.setOpacity(0.3) 
        self.btnPreviousTabla.setGraphicsEffect(self.opacity_effectAnterior) 
        self.btnPreviousTabla.setVisible(False)
        
        # BTN SIGUIENTE TABLA
        self.btnNextTabla = QtWidgets.QPushButton(self.groupBoxAcciones)
        self.btnNextTabla.setGeometry(QtCore.QRect(250, 110, 162, 60))
        self.btnNextTabla.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnNextTabla.setObjectName("btnNextTabla")
        self.btnNextTabla.setEnabled(False)
        self.btnNextTabla.setStyleSheet("background: #3999da; color: #000000; font-size: 16px")
        self.opacity_effectNext = QtWidgets.QGraphicsOpacityEffect() 
        self.opacity_effectNext.setOpacity(0.3) 
        self.btnNextTabla.setGraphicsEffect(self.opacity_effectNext) 
        
        
        # GROUP BOX RESULTADO
        self.groupBoxResul = QtWidgets.QGroupBox(self.widgetSimplex)
        self.groupBoxResul.setGeometry(QtCore.QRect(25, 155, 850, 480))
        font = QtGui.QFont()
        font.setFamily("time new roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxResul.setFont(font)
        self.groupBoxResul.setObjectName("groupBoxResul")
        self.groupBoxResul.setStyleSheet("background: #bcc1d2")
        
        
        # LABEL FUNCION OBJETIVO
        self.lblMaxZ = QtWidgets.QTextBrowser(self.groupBoxResul)
        self.lblMaxZ.setGeometry(QtCore.QRect(20, 25, 750, 40))
        font = QtGui.QFont()
        font.setFamily("time new roman")
        font.setPointSize(12)
        font.setBold(True)
        self.lblMaxZ.setFont(font)
        self.lblMaxZ.setObjectName("lblMaxZ")
        self.lblMaxZ.setStyleSheet("border: none; font-size: 14px")
        
        # LABEL RESTRICCIONES
        self.lblRestricc = QtWidgets.QTextBrowser(self.groupBoxResul)
        self.lblRestricc.setGeometry(QtCore.QRect(20, 67, 750, 150))
        font = QtGui.QFont()
        font.setFamily("time new roman")
        font.setPointSize(12)
        font.setBold(True)
        self.lblRestricc.setFont(font)
        self.lblRestricc.setObjectName("lblRestricc")
        self.lblRestricc.setStyleSheet("border: none")
        
        # TABLA RESULTADO
        self.tableResult = QtWidgets.QTableWidget(self.groupBoxResul)
        self.tableResult.setGeometry(QtCore.QRect(20, 150, 650, 755))
        self.tableResult.setObjectName("tableResult")
        self.tableResult.setColumnCount(0)
        self.tableResult.setRowCount(0)
        self.tableResult.verticalHeader().setVisible(False)
        self.tableResult.horizontalHeader().setVisible(False)
        self.tableResult.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignHCenter and QtCore.Qt.AlignVCenter and QtCore.Qt.AlignCenter)
        self.tableResult.horizontalHeader().setDefaultSectionSize(75)
        self.tableResult.setStyleSheet("background: #3999da")
        # LABEL PIVOTE
        self.lblPibote = QtWidgets.QTextBrowser(self.groupBoxResul)
        self.lblPibote.setGeometry(QtCore.QRect(20, 778, 750, 40))
        font = QtGui.QFont()
        font.setFamily("time new roman")
        font.setPointSize(12)
        font.setBold(True)
        self.lblPibote.setFont(font)
        self.lblPibote.setObjectName("lblPibote")
        self.lblPibote.setStyleSheet("border: none; font-size: 18px")
        # GROUP BOX RESPUESTA
        self.groupBoxRespuesta = QtWidgets.QGroupBox(self.groupBoxResul)
        self.groupBoxRespuesta.setGeometry(QtCore.QRect(20, 340, 750, 130))
        font = QtGui.QFont()
        font.setFamily("time new roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxRespuesta.setFont(font)
        self.groupBoxRespuesta.setObjectName("groupBoxRespuesta")
        self.groupBoxRespuesta.setHidden(True)
        # LABEL RESPUESTA
        self.lblRespuesta = QtWidgets.QTextBrowser(self.groupBoxRespuesta)
        self.lblRespuesta.setGeometry(QtCore.QRect(50, 50, 500, 40))
        font = QtGui.QFont()
        font.setFamily("time new roman")
        font.setPointSize(12)
        font.setBold(True)
        self.lblRespuesta.setFont(font)
        self.lblRespuesta.setObjectName("lblRespuesta")
        self.lblRespuesta.setStyleSheet(" border: none; font-size: 18px")
        # LABEL TOTAL TABLAS
        self.lblTotalTable = QtWidgets.QTextBrowser(self.groupBoxRespuesta)
        self.lblTotalTable.setGeometry(QtCore.QRect(20, 80, 700, 40))
        font = QtGui.QFont()
        font.setFamily("time new roman")
        font.setPointSize(12)
        font.setBold(True)
        self.lblTotalTable.setFont(font)
        self.lblTotalTable.setObjectName("lblTotalTable")
        self.lblTotalTable.setStyleSheet("border: none; font-size: 18px")
        ########################################### UI - MÉTODO PERL ###########################################
        # GROUP BOX DATOS ACTIVIDADES
        """self.groupBoxDatosPerl = QtWidgets.QGroupBox(self.widgetPerl)
        self.groupBoxDatosPerl.setGeometry(QtCore.QRect(30, 0, 1300, 80))
        font = QtGui.QFont()
        font.setFamily("time new roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxDatosPerl.setFont(font)
        self.groupBoxDatosPerl.setObjectName("groupBoxDatosPerl")
        # LABEL ACTIVIDAD
        self.lblAct = QtWidgets.QLabel(self.groupBoxDatosPerl)
        self.lblAct.setGeometry(QtCore.QRect(40, 40, 300, 20))
        self.lblAct.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("time new roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lblAct.setFont(font)
        self.lblAct.setAutoFillBackground(False)
        self.lblAct.setStyleSheet("")
        self.lblAct.setObjectName("lblAct")
        self.lblAct.setStyleSheet("font-size: 16px")
        # INPUT ACTIVIDAD
        self.inputAct = QtWidgets.QSpinBox(self.groupBoxDatosPerl)
        self.inputAct.setGeometry(QtCore.QRect(350, 40, 40, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.inputAct.setFont(font)
        self.inputAct.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.inputAct.setToolTipDuration(-27)
        self.inputAct.setKeyboardTracking(True)
        self.inputAct.setMinimum(2)
        self.inputAct.setObjectName("inputAct")
        # BTN GENERAR
        self.btnGenerarPerl = QtWidgets.QPushButton(self.groupBoxDatosPerl)
        self.btnGenerarPerl.setGeometry(QtCore.QRect(420, 35, 80, 30))
        self.btnGenerarPerl.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnGenerarPerl.setObjectName("btnGenerarPerl")
        self.btnGenerarPerl.setStyleSheet("background: #463f57; color: #ffffff")
        self.opacity_effectGeneraPert = QtWidgets.QGraphicsOpacityEffect() 
        self.opacity_effectGeneraPert.setOpacity(1) 
        self.btnGenerarPerl.setGraphicsEffect(self.opacity_effectGeneraPert) 
        # BTN NUEVO
        self.btnNuevoPerl = QtWidgets.QPushButton(self.groupBoxDatosPerl)
        self.btnNuevoPerl.setGeometry(QtCore.QRect(1000, 35, 80, 30))
        self.btnNuevoPerl.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnNuevoPerl.setObjectName("btnNuevoPerl")
        self.btnNuevoPerl.setEnabled(False)
        self.btnNuevoPerl.setStyleSheet("background: #463f57; color: #ffffff")
        self.opacity_effectNuevoPert = QtWidgets.QGraphicsOpacityEffect() 
        self.opacity_effectNuevoPert.setOpacity(0.3) 
        self.btnNuevoPerl.setGraphicsEffect(self.opacity_effectNuevoPert) 
        # BTN GUARDAR
        self.btnGuardar = QtWidgets.QPushButton(self.groupBoxDatosPerl)
        self.btnGuardar.setGeometry(QtCore.QRect(1100, 35, 80, 30))
        self.btnGuardar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnGuardar.setObjectName("btnGuardar")
        self.btnGuardar.setEnabled(False)
        self.btnGuardar.setStyleSheet("background: #463f57; color: #ffffff")
        self.opacity_effectGuardar = QtWidgets.QGraphicsOpacityEffect() 
        self.opacity_effectGuardar.setOpacity(0.3) 
        self.btnGuardar.setGraphicsEffect(self.opacity_effectGuardar) 
        # BTN SALIR
        self.btnSalirPert = QtWidgets.QPushButton(self.groupBoxDatosPerl)
        self.btnSalirPert.setGeometry(QtCore.QRect(1200, 35, 80, 30))
        self.btnSalirPert.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSalirPert.setObjectName("btnSalirPert")
        self.btnSalirPert.setStyleSheet("background: #463f57; color: #ffffff")
        # GROUP BOX RESULTADO ACTIVIDADES
        self.groupBoxrResPerl = QtWidgets.QGroupBox(self.widgetPerl)
        self.groupBoxrResPerl.setGeometry(QtCore.QRect(30, 100, 1300, 580))
        font = QtGui.QFont()
        font.setFamily("time new roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxrResPerl.setFont(font)
        self.groupBoxrResPerl.setObjectName("groupBoxrResPerl")
        self.groupBoxrResPerl.setVisible(False)
        # TABLA ACTIVIDADES
        self.tableActividades = QtWidgets.QTableWidget(self.groupBoxrResPerl)
        self.tableActividades.setGeometry(QtCore.QRect(5, 5, 1290, 400))
        self.tableActividades.setObjectName("tableActividades")
        self.tableActividades.setColumnCount(0)
        self.tableActividades.setRowCount(0)
        self.tableActividades.verticalHeader().setVisible(False)
        self.tableActividades.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignHCenter and QtCore.Qt.AlignVCenter and QtCore.Qt.AlignCenter)
        self.tableActividades.horizontalHeader().setDefaultSectionSize(75)
        self.tableActividades.horizontalHeader().setStyleSheet("color: #fff")
        self.tableActividades.setStyleSheet("border: 1px solid #000; font-size: 16px")
        # LABEL RUTA CRÍTICA
        self.lblRutaCritica = QtWidgets.QLabel(self.groupBoxrResPerl)
        self.lblRutaCritica.setGeometry(QtCore.QRect(10, 420, 500, 30))
        self.lblRutaCritica.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("time new roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lblRutaCritica.setFont(font)
        self.lblRutaCritica.setAutoFillBackground(False)
        self.lblRutaCritica.setStyleSheet("")
        self.lblRutaCritica.setObjectName("lblRutaCritica")
        self.lblRutaCritica.setStyleSheet("font-size: 16px")
        # LABEL FECHA INICIO PROYECTO
        self.lblInicioProyecto = QtWidgets.QLabel(self.groupBoxrResPerl)
        self.lblInicioProyecto.setGeometry(QtCore.QRect(10, 460, 500, 30))
        self.lblInicioProyecto.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("time new roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lblInicioProyecto.setFont(font)
        self.lblInicioProyecto.setAutoFillBackground(False)
        self.lblInicioProyecto.setStyleSheet("")
        self.lblInicioProyecto.setObjectName("lblInicioProyecto")
        self.lblInicioProyecto.setStyleSheet("font-size: 16px")
        # LABEL FECHA FINAL PROYEXTO
        self.lblFinProyecto = QtWidgets.QLabel(self.groupBoxrResPerl)
        self.lblFinProyecto.setGeometry(QtCore.QRect(10, 500, 500, 30))
        self.lblFinProyecto.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("time new roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lblFinProyecto.setFont(font)
        self.lblFinProyecto.setAutoFillBackground(False)
        self.lblFinProyecto.setStyleSheet("")
        self.lblFinProyecto.setObjectName("lblFinProyecto")
        self.lblFinProyecto.setStyleSheet("font-size: 16px")
        # LABEL DÍAS DEL PROYECTO
        self.lblDiasProyecto = QtWidgets.QLabel(self.groupBoxrResPerl)
        self.lblDiasProyecto.setGeometry(QtCore.QRect(10, 540, 500, 30))
        self.lblDiasProyecto.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("time new roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lblDiasProyecto.setFont(font)
        self.lblDiasProyecto.setAutoFillBackground(False)
        self.lblDiasProyecto.setStyleSheet("")
        self.lblDiasProyecto.setObjectName("lblDiasProyecto")
        self.lblDiasProyecto.setStyleSheet("font-size: 16px")
        # GROUP BOX DATOS ACTIVIDADES - INGRESO
        self.groupBoxInputActv = QtWidgets.QGroupBox(self.widgetPerl)
        self.groupBoxInputActv.setGeometry(QtCore.QRect(30, 100, 1300, 580))
        font = QtGui.QFont()
        font.setFamily("time new roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxInputActv.setFont(font)
        self.groupBoxInputActv.setObjectName("groupBoxInputActv")
        self.groupBoxInputActv.setVisible(False)
        # LABEL ACTIVIDAD
        self.lblInputAct = QtWidgets.QLabel(self.groupBoxInputActv)
        self.lblInputAct.setGeometry(QtCore.QRect(500, 5, 300, 20))
        self.lblInputAct.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("time new roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lblInputAct.setFont(font)
        self.lblInputAct.setAutoFillBackground(False)
        self.lblInputAct.setStyleSheet("")
        self.lblInputAct.setObjectName("lblInputAct")
        self.lblInputAct.setStyleSheet("font-size: 16px")
        # LABEL INFORMACIÓN
        self.lblInfo = QtWidgets.QLabel(self.groupBoxInputActv)
        self.lblInfo.setGeometry(QtCore.QRect(275, 30, 800, 20))
        self.lblInfo.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("time new roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lblInfo.setFont(font)
        self.lblInfo.setAutoFillBackground(False)
        self.lblInfo.setStyleSheet("")
        self.lblInfo.setObjectName("lblInfo")
        self.lblInfo.setStyleSheet("font-size: 12px; font-style: italic")
        # TABLA ACTIVIDADES - INGRESO
        self.tableInputActividades = QtWidgets.QTableWidget(self.groupBoxInputActv)
        self.tableInputActividades.setGeometry(QtCore.QRect(254, 60, 718, 326))
        self.tableInputActividades.setObjectName("tableInputActividades")
        self.tableInputActividades.setColumnCount(0)
        self.tableInputActividades.setRowCount(0)
        self.tableInputActividades.verticalHeader().setVisible(False)
        self.tableInputActividades.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignHCenter and QtCore.Qt.AlignVCenter and QtCore.Qt.AlignCenter)
        self.tableInputActividades.horizontalHeader().setDefaultSectionSize(75)
        self.tableInputActividades.horizontalHeader().setStyleSheet("color: #fff")
        self.tableInputActividades.setStyleSheet("border: 1px solid #000; font-size: 16px")
        # BTN CALCULAR PERL
        self.btnCalcularPerl = QtWidgets.QPushButton(self.groupBoxInputActv)
        self.btnCalcularPerl.setGeometry(QtCore.QRect(600, 400, 80, 30))
        self.btnCalcularPerl.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCalcularPerl.setObjectName("btnCalcularPerl")
        self.btnCalcularPerl.setStyleSheet("background: #463f57; color: #ffffff")
        # BTN BORRAR PERL
        self.btnBorrarPerl = QtWidgets.QPushButton(self.groupBoxInputActv)
        self.btnBorrarPerl.setGeometry(QtCore.QRect(600, 440, 80, 30))
        self.btnBorrarPerl.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnBorrarPerl.setObjectName("btnBorrarPerl")
        self.btnBorrarPerl.setStyleSheet("background: #463f57; color: #ffffff")
        # GROUP BOX DIAS NO LABORABLES
        self.groupBoxDiasNoLab = QtWidgets.QGroupBox(self.groupBoxInputActv)
        self.groupBoxDiasNoLab.setGeometry(QtCore.QRect(3, 60, 240, 326))
        font = QtGui.QFont()
        font.setFamily("time new roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxDiasNoLab.setFont(font)
        self.groupBoxDiasNoLab.setObjectName("groupBoxDiasNoLab")
        # CHECKBOX DIAS
        #Lunes
        self.diaLunes = QtWidgets.QCheckBox("Lunes", self.groupBoxDiasNoLab)
        self.diaLunes.move(20,30)
        self.diaLunes.resize(100,40)
        #Martes
        self.diaMartes = QtWidgets.QCheckBox("Martes", self.groupBoxDiasNoLab)
        self.diaMartes.move(20,70)
        self.diaMartes.resize(100,40)
        #Miercoles
        self.diaMiercoles = QtWidgets.QCheckBox("Miercoles", self.groupBoxDiasNoLab)
        self.diaMiercoles.move(20,110)
        self.diaMiercoles.resize(100,40)
        #Jueves
        self.diaJueves = QtWidgets.QCheckBox("Jueves", self.groupBoxDiasNoLab)
        self.diaJueves.move(20,150)
        self.diaJueves.resize(100,40)
        #Viernes
        self.diaViernes = QtWidgets.QCheckBox("Viernes", self.groupBoxDiasNoLab)
        self.diaViernes.move(20,190)
        self.diaViernes.resize(100,40)
        #Sabado
        self.diaSabado = QtWidgets.QCheckBox("Sábado", self.groupBoxDiasNoLab)
        self.diaSabado.move(20,230)
        self.diaSabado.resize(100,40)
        #Domingo
        self.diaDomingo = QtWidgets.QCheckBox("Domingo", self.groupBoxDiasNoLab)
        self.diaDomingo.move(20,270)
        self.diaDomingo.resize(100,40)
        # GROUP BOX FECHA INICIO PROYECTO
        self.groupBoxFechInicio = QtWidgets.QGroupBox(self.groupBoxInputActv)
        self.groupBoxFechInicio.setGeometry(QtCore.QRect(980, 60, 312, 326))
        font = QtGui.QFont()
        font.setFamily("time new roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxFechInicio.setFont(font)
        self.groupBoxFechInicio.setObjectName("groupBoxFechInicio")
        # GROUP BOX CONTENDOR FECHA INICIO PROYECTO
        self.groupBoxContenedorFech = QtWidgets.QGroupBox(self.groupBoxFechInicio)
        self.groupBoxContenedorFech.setGeometry(QtCore.QRect(0, 50, 312, 200))
        font = QtGui.QFont()
        font.setFamily("time new roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxContenedorFech.setFont(font)
        self.groupBoxContenedorFech.setObjectName("groupBoxContenedorFech")
        self.groupBoxContenedorFech.setStyleSheet("background: #C1C0C0")
        # CALENDARIO
        self.calendario = QtWidgets.QCalendarWidget(self.groupBoxContenedorFech)
        self.calendario.setGeometry(0, 0, 312, 200) 
        self.calendario.setGridVisible(True)
        self.calendario.verticalHeaderFormat()
        self.calendario.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendario.setNavigationBarVisible(True)
        self.calendario.setStyleSheet("color: #000")
        self.calendario.setObjectName("calendario")"""
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        #################################### MAIN WINDOW ####################################
        MainWindow.setWindowTitle(_translate("MainWindow", "METODO SIMPLEX"))
        #self.label.setText(_translate("MainWindow", "BIENVENIDO"))
        self.menuM_todo.setTitle(_translate("MainWindow", "Método"))
        self.actionSimplex.setText(_translate("MainWindow", "Simplex"))
        """self.actionPerl_CPM.setText(_translate("MainWindow", "Perl"))"""
        #################################### UI - SIMPLEX ####################################
        self.groupBoxDatos.setTitle(_translate("MainWindow", "Datos"))
        self.lblVar.setText(_translate("MainWindow", "Ingrese el número de variables:"))
        self.lblRes.setText(_translate("MainWindow", "Ingrese el número de restricciones:"))
        self.btnGenerar.setText(_translate("MainWindow", "GENERAR"))
        self.groupBoxRestriccion.setTitle(_translate("MainWindow", "Restricciones"))
        self.lblTextMaxZ.setText(_translate("MainWindow", "MAXI Z ="))
        self.groupBoxFuncObj.setTitle(_translate("MainWindow", "Función Objetivo"))
        self.groupBoxAcciones.setTitle(_translate("MainWindow", "Acciones"))
        self.btnCalcular.setText(_translate("MainWindow", "CALCULAR"))
        self.btnCalPibote.setText(_translate("MainWindow", "CALCULAR PIVOTE"))
        self.btnPreviousTabla.setText(_translate("MainWindow", "ANTERIOR TABLA"))
        self.btnNextTabla.setText(_translate("MainWindow", "SIGUIENTE TABLA"))
        self.btnNuevo.setText(_translate("MainWindow", "Nuevo"))
        self.btnSalir.setText(_translate("MainWindow", "Salir"))
        self.btnSalir.setText(_translate("MainWindow", "Salir"))
        self.btnImprimir.setText(_translate("MainWindow", "IMPRIMIR"))
        self.groupBoxResul.setTitle(_translate("MainWindow", "Resultado"))
        self.groupBoxRespuesta.setTitle(_translate("MainWindow", "Respuesta: "))
        self.btnSimplex.setText(_translate("MainWindow", "NEXT"))
        #################################### UI - PERL ####################################
        """self.groupBoxDatosPerl.setTitle(_translate("MainWindow", "Datos"))
        self.lblAct.setText(_translate("MainWindow", "Ingrese el número de actividades:"))
        self.lblInputAct.setText(_translate("MainWindow", "Ingrese todos los datos para continuar"))
        self.lblInfo.setText(_translate("MainWindow", 'Los predecesores debe ingresarlos en mayúscula. Ej: "A" | "A-B-C". En caso de no tener predecesor ingrese "N/A".'))
        self.btnGenerarPerl.setText(_translate("MainWindow", "GENERAR"))
        self.btnNuevoPerl.setText(_translate("MainWindow", "NUEVO"))
        self.btnGuardar.setText(_translate("MainWindow", "GUARDAR"))
        self.btnSalirPert.setText(_translate("MainWindow", "SALIR"))
        self.btnCalcularPerl.setText(_translate("MainWindow", "CALCULAR"))
        self.btnBorrarPerl.setText(_translate("MainWindow", "BORRAR"))
        self.groupBoxDiasNoLab.setTitle(_translate("MainWindow", "DÍAS NO LABORABLES"))
        self.groupBoxFechInicio.setTitle(_translate("MainWindow", "FECHA INICIO"))"""

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())