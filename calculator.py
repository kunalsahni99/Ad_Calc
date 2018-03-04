# coding=utf-8

from kivy.app import App
from kivy.uix.button import Button
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.uix.scrollview import ScrollView
from kivymd.theming import ThemeManager

from sympy.parsing.sympy_parser import parse_expr,standard_transformations,implicit_multiplication_application, convert_equals_signs
from sympy import N, sympify, diff, integrate, symbols,simplify,factor, Matrix
from sympy import *
import os
os.environ['dbg'] = '0'
from sympy import plot
from kivymd.textfields import MDTextField
from kivymd.dialog import MDDialog
from kivymd.label import MDLabel
from kivy.core.window import Window
from kivy.logger import Logger

try:
    print('try import sympy')
    import sympy.simplify
    print('sympy import successful')

except:
    import zipfile
    zip_ref = zipfile.ZipFile('unittest.zip', 'r')
    zip_ref.extractall('./')
    zip_ref.close()

transformations = (standard_transformations + (implicit_multiplication_application, convert_equals_signs))

x = sympy.symbols('x')

calc = """
#:import Toolbar kivymd.toolbar.Toolbar
#:import ThemeManager kivymd.theming.ThemeManager
#:import MDNavigationDrawer kivymd.navigationdrawer.MDNavigationDrawer
#:import NavigationLayout kivymd.navigationdrawer.NavigationLayout
#:import NavigationDrawerDivider kivymd.navigationdrawer.NavigationDrawerDivider
#:import NavigationDrawerToolbar kivymd.navigationdrawer.NavigationDrawerToolbar
#:import NavigationDrawerSubheader kivymd.navigationdrawer.NavigationDrawerSubheader
#:import MDCheckbox kivymd.selectioncontrols.MDCheckbox
#:import MDSwitch kivymd.selectioncontrols.MDSwitch
#:import MDList kivymd.list.MDList
#:import OneLineListItem kivymd.list.OneLineListItem
#:import TwoLineListItem kivymd.list.TwoLineListItem
#:import ThreeLineListItem kivymd.list.ThreeLineListItem
#:import OneLineAvatarListItem kivymd.list.OneLineAvatarListItem
#:import OneLineIconListItem kivymd.list.OneLineIconListItem
#:import OneLineAvatarIconListItem kivymd.list.OneLineAvatarIconListItem
#:import MDTextField kivymd.textfields.MDTextField
#:import MDSpinner kivymd.spinner.MDSpinner
#:import MDCard kivymd.card.MDCard
#:import MDSeparator kivymd.card.MDSeparator
#:import MDDropdownMenu kivymd.menu.MDDropdownMenu
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import colors kivymd.color_definitions.colors
#:import SmartTile kivymd.grid.SmartTile
#:import MDSlider kivymd.slider.MDSlider
#:import MDTabbedPanel kivymd.tabs.MDTabbedPanel
#:import MDTab kivymd.tabs.MDTab
#:import MDProgressBar kivymd.progressbar.MDProgressBar
#:import MDAccordion kivymd.accordion.MDAccordion
#:import MDAccordionItem kivymd.accordion.MDAccordionItem
#:import MDAccordionSubItem kivymd.accordion.MDAccordionSubItem
#:import MDThemePicker kivymd.theme_picker.MDThemePicker
#:import MDBottomNavigation kivymd.tabs.MDBottomNavigation
#:import MDBottomNavigationItem kivymd.tabs.MDBottomNavigationItem
 
NavigationLayout:
    id: nav_layout
    MDNavigationDrawer
        id: nav_drawer
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: 'Calculator'
            on_release: main_manager.current = 'calc'
        
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: 'Matrix'
            on_release: main_manager.current = 'matrix'
            
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: 'Limit'
            on_release: main_manager.current = 'limit'
            
    BoxLayout:
        orientation: "vertical"
        ScreenManager:
            id: main_manager
            Screen:
                name: 'calc'
                BoxLayout:
                    orientation: 'vertical'
                    BoxLayout:
                        orientation: 'vertical'
                        BoxLayout:
                            orientation:'vertical'
                            size:(dp(40),dp(50))
                            size_hint:(None,None)
                            pos_hint:{'right': 1}
                            MDLabel:
                                text:'A/B'
                            MDSwitch:
                                id:fractog
                                
                        MDTextField:
                            id: out
                            text: "0"
                            font_style: "Title"
                            font_size: 40
                            align: "right"
                            padding: (20,0)
                            mulitiline: True
            
                        MDLabel:
                            bg_color: (0,0,0)    
                            size_hint: (1,0.15)
                            id: real_time_update
                            font_name: 'Hack-Regular'
                            padding: (20,0)
                            text: '0'
                            multiline: True
                            halign: 'center'
                
                    ScreenManager:
                        id: screenmngr
                        Screen:
                            name: "buttons"
                            GridLayout:
                                cols: 3
                                GridLayout:
                                    cols: 3
                                    MDFlatButton:
                                        size_hint: (1,1)
                                        on_press: out.text+="7"
                                        MDLabel:
                                            text: "7"
                                            font_size: 20
                                            halign: "center"
                                    
                                    MDFlatButton:       
                                        size_hint: (1,1)
                                        on_press: out.text+="8"
                                        MDLabel:
                                            text: "8"
                                            font_size: 20
                                            halign: "center"
                                            
                                    MDFlatButton:       
                                        size_hint: (1,1)
                                        on_press: out.text+="9"
                                        MDLabel:
                                            text: "9"
                                            font_size: 20
                                            halign: "center"
                                            
                                    MDFlatButton:       
                                        size_hint: (1,1)
                                        on_press: out.text+="4"
                                        MDLabel:
                                            text: "4"
                                            font_size: 20
                                            halign: "center"
                
                                    MDFlatButton:       
                                        size_hint: (1,1)
                                        on_press: out.text+="5"
                                        MDLabel:
                                            text: "5"
                                            font_size: 20
                                            halign: "center"
                                            
                                    MDFlatButton:       
                                        size_hint: (1,1)
                                        on_press: out.text+="6"
                                        MDLabel:
                                            text: "6"
                                            font_size: 20
                                            halign: "center"
                                            
                                    MDFlatButton:       
                                        size_hint: (1,1)
                                        on_press: out.text+="1"
                                        MDLabel:
                                            text: "1"
                                            font_size: 20
                                            halign: "center"
                
                                    MDFlatButton:       
                                        size_hint: (1,1)
                                        on_press: out.text+="2"
                                        MDLabel:
                                            text: "2"
                                            font_size: 20
                                            halign: "center"
                                            
                                    MDFlatButton:       
                                        size_hint: (1,1)
                                        on_press: out.text+="3"
                                        MDLabel:
                                            text: "3"
                                            font_size: 20
                                            halign: "center"
                                            
                                    MDFlatButton:       
                                        size_hint: (1,1)
                                        on_press: out.text+="."
                                        MDLabel:
                                            text: "."
                                            font_size: 20
                                            halign: "center"
                
                                    MDFlatButton:       
                                        size_hint: (1,1)
                                        on_press: out.text+="0"
                                        MDLabel:
                                            text: "0"
                                            font_size: 20
                                            halign: "center"
                
                                    MDFlatButton:       
                                        id: equal_but
                                        size_hint: (1,1)
                                        MDLabel:
                                            text: "="
                                            font_size: 20
                                            halign: "center"
                                            
                                            
                                GridLayout:
                                    cols: 1
                                    size_hint: (0.2, 0.15)
                                    MDFlatButton:
                                        size_hint: (0,0.1)
                                        id: cancel_but
                                        text: "DEL"
                                        halign: 'center'
                                        
                                    MDFlatButton:
                                        size_hint: (0.01,0.1)
                                        id: plus
                                        text: "+"
                                        on_press: out.text+="+"
                                        halign: 'center'
                                        
                                    MDFlatButton:
                                        size_hint: (0.01,0.1)
                                        id: minus
                                        text: "-"
                                        on_press: out.text+="-"
                                        halign: 'center'
                                        
                                    MDFlatButton:
                                        size_hint: (0.01,0.1)
                                        id: multiply
                                        text: "*"
                                        on_press: out.text+="*"
                                        halign: 'center'
                                        
                                    MDFlatButton:
                                        size_hint: (0.01,0.1)
                                        id: divide
                                        text: "÷"
                                        on_press: out.text+="/"
                                        halign: 'center'
                                        
                                MDIconButton:
                                    id: arrow
                                    size_hint: (0.1,1)
                                    icon: "arrow-right"
                                    on_press: screenmngr.current="trigo"
                                    on_press:
                                        screenmngr.transition.direction: "right"
                                        screenmngr.current: "trigo"
                                        
                                                                 
                        Screen:
                            name: "trigo"
                            GridLayout:
                                cols: 3
                                MDIconButton:
                                    size_hint: (0.2,1)
                                    icon: "arrow-left"
                                    on_press: screenmngr.current= "buttons"
                                    on_press:
                                        screenmngr.transition.direction: "left"
                                        screenmngr.current: "buttons"
                                        
                                
                                GridLayout:
                                    id: basic_buts
                                    cols: 1
                                    size_hint_x: 0.2
                                    MDFlatButton:
                                        on_press: out.text+="("
                                        size_hint: (0.1,0.1)
                                        MDLabel:
                                            text: "("
                                            font_size: 20
                                            halign: 'center'
                                            
                                    MDFlatButton:
                                        on_press: out.text+=")"
                                        size_hint: (0.1,0.1)
                                        MDLabel:
                                            text: ")"
                                            font_size: 20
                                            halign: 'center'
                                            
                                    MDFlatButton:
                                        on_press: out.text+="x"
                                        size_hint: (0.1,0.1)
                                        MDLabel:
                                            text: "x"
                                            font_size: 20
                                            halign: 'center'
                                            
                                    MDFlatButton:
                                        on_press: out.text+="pi"
                                        size_hint: (0.1,0.1)
                                        MDLabel:
                                            text: "π"
                                            font_size: 20
                                            halign: 'center'
                                            
                                ScrollView:
                                    do_scroll_x: False
                                    GridLayout:
                                        id: functions_but
                                        size_hint: (1,None)
                                        height: Window.height
                                        cols: 3
                                        
                                        
                                        MDFlatButton:
                                            id: inv
                                            size_hint: (1,1)
                                            on_press: screenmngr.current = "inv_trigo"
                                            on_press:
                                                screenmngr.transition.direction: "right"
                                                screenmngr.current = "inv_trigo"
                                            MDLabel:
                                                text: "INV"
                                                font_size: 20
                                                halign: "center"
                                            
                                        MDFlatButton:
                                            on_press: out.text += 'sin('
                                            size_hint: (1,1)
                                            MDLabel:
                                                text: 'sin'
                                                font_size: 20
                                                halign: 'center'
                                                
                                        MDFlatButton:
                                            on_press: out.text += 'cos('
                                            size_hint: (1,1)
                                            MDLabel:
                                                text: 'cos'
                                                font_size: 20
                                                halign: 'center'
                                                
                                        MDFlatButton:
                                            on_press: out.text += 'tan('
                                            size_hint: (1,1)
                                            MDLabel:
                                                text: 'tan'
                                                font_size: 20
                                                halign: 'center'
                                                
                                        MDFlatButton:
                                            on_press: out.text += '!'
                                            size_hint: (1,1)
                                            MDLabel:
                                                text: 'x!'
                                                font_size: 20
                                                halign: 'center'    
                                    
                                        MDFlatButton:
                                            on_press: out.text += '1/'
                                            size_hint: (1,1)
                                            MDLabel:
                                                text: '1/x'
                                                font_size: 20
                                                halign: 'center'
                                                
                                        MDFlatButton:
                                            on_press: out.text += '**'
                                            size_hint: (1,1)
                                            MDLabel:
                                                text: 'x^y'
                                                font_size: 20
                                                halign: 'center'
                                                
                                        MDFlatButton:
                                            on_press: out.text += 'e**('
                                            size_hint: (1,1)
                                            MDLabel:
                                                text: 'e^'
                                                font_size: 20
                                                halign: 'center'
                                                
                                        MDFlatButton:
                                            on_press: out.text += 'log('
                                            size_hint: (1,1)          
                                            MDLabel: 
                                                text: 'log'
                                                font_size: 20
                                                halign: 'center'
                        
                        Screen:
                            name: "inv_trigo"
                            ScrollView:
                                do_scroll_x: False
                                GridLayout:
                                    id: inv_tri
                                    cols: 3
                                    MDFlatButton:
                                        id: back
                                        size_hint: (1,1)
                                        on_press: screenmngr.current = "trigo"
                                        on_press:
                                            screenmngr.transition.direction = "left"
                                            screenmngr.current = "trigo"
                                        MDLabel:
                                            text: "Back"
                                            font_size: 20
                                            halign: "center"
                                        
                                    MDFlatButton:
                                        on_press: out.text += "asin("
                                        size_hint: (1,1)
                                        MDLabel:
                                            text: "asin"
                                            font_size: 20
                                            halign: "center"
                                        
                                    MDFlatButton:
                                        on_press: out.text += "acos("
                                        size_hint: (1,1)
                                        MDLabel:
                                            text: "acos"
                                            font_size: 20
                                            halign: "center"
                                        
                                    MDFlatButton:
                                        on_press: out.text += "atan("
                                        size_hint: (1,1)
                                        MDLabel:
                                            text: "atan"
                                            font_size: 20
                                            halign: "center"
                                    
                                    MDFlatButton:
                                        id: differentiate
                                        size_hint: (1,1)
                                        MDLabel:
                                            text: "d/dx"
                                            font_size: 20
                                            halign: "center"
                                            
                                    MDFlatButton:
                                        id: integrate
                                        size_hint: (1,1)
                                        MDLabel:
                                            text: "∫"
                                            font_size: 20
                                            halign: "center"
                                            
                                    MDFlatButton:
                                        id: simplify
                                        size_hint: (1,1)
                                        MDLabel:
                                            text: "Simplify"
                                            font_size: 20
                                            halign: "center"
                                    
                                    MDFlatButton:
                                        id: factorise
                                        size_hint: (1,1)
                                        MDLabel:
                                            text: "Factorise"
                                            font_size: 20
                                            halign: "center"
                                
                                    MDFlatButton:
                                        id: expand
                                        size_hint: (1,1)
                                        MDLabel:
                                            text: "Expand"
                                            font_size: 20
                                            halign: "center"
                                            
                                    MDFlatButton:
                                        id: solve
                                        size_hint: (1,1)
                                        MDLabel:
                                            text: 'Solve'
                                            font_size: 20
                                            halign: 'center'
            
            Screen:
                name: 'matrix'
                BoxLayout:
                    orientation: 'vertical'
                    BoxLayout:
                        size_hint_y: 0.1
                        Spinner:
                            id: Matrix_menu
                            text: 'Operations'
                            values: ('A + B', 'A - B', 'A * B', 'RREF of A', 'RREF of B', 'Inverse of A', 'Inverse of B')
                            
                        MDRaisedButton:
                            id: rref
                            size_hint: (0.2,1)
                            text: 'Do it!'
                            md_bg_color: app.theme_cls.accent_color
                            background_palette: 'Red'
                            
                    BoxLayout:
                        orientation: 'vertical'
                        spacing: 10
                        MDCard:
                            size_hint: (0.8,0.8)
                            pos_hint: {'center_x' : 0.5, 'center_y' : 0.5}
                            BoxLayout:
                                padding: 30        
                                orientation: 'vertical'
                                BoxLayout:
                                    size_hint_y: 0.4
                                    MDTextField:
                                        id: row
                                        hint_text: 'Rows'
                                        required: True
                                        helper_text_mode: 'on_error'
                                        font_size: 30
                                    
                                    MDTextField:
                                        id: col
                                        hint_text: 'Columns'
                                        required: True
                                        helper_text_mode: 'on_error'
                                        font_size: 30    
                                ScrollView:
                                    GridLayout:
                                        size_hint_y: None
                                        id: matrix_grid
                                        
                        MDCard:
                            size_hint: (0.8,0.8)
                            pos_hint: {'center_x' : 0.5, 'center_y' : 0.5}
                            BoxLayout:
                                padding: 30
                                orientation: 'vertical'
                                BoxLayout:
                                    size_hint_y: 0.4
                                    MDTextField:
                                        id: row2
                                        hint_text: 'Rows'
                                        required: True
                                        helper_text_mode: 'on_error'
                                        font_size: 30
                                        
                                    MDTextField:
                                        id: col2
                                        hint_text: 'Columns'
                                        required: True
                                        helper_text_mode: 'on_error'
                                        font_size: 30
                                        
                                ScrollView:
                                    GridLayout:
                                        size_hint_y: None
                                        id: matrix_grid_2


            Screen:
                name: 'limit'
                BoxLayout:
                    orientation: 'vertical'
                    Toolbar:
                        id: toolbar
                        title: 'Limit'
                        md_bg_color: app.theme_cls.primary_color
                        background_palette: 'Primary'
                        background_hue: '500'
                    
                    BoxLayout:
                        orientation: 'vertical'
                        size_hint_y: 0.1
                        MDTextField:
                            id: f(x)
                            hint_text: 'f(x)'
                            required: True
                            helper_text_mode: 'on_error'
                            font_size: 20
                            pos_hint: {'top' : 0.8}

                        
                        MDTextField:
                            id: X0
                            hint_text: 'X0'
                            required: True
                            helper_text_mode: 'on_error'
                            font_size: 20
                            pos_hint: {'top' : 0.8}
                            
                        MDTextField:
                            id: sign
                            hint_text: 'sign'
                            font_size: 20    
                            pos_hint: {'top' : 0.8}
                            
                    BoxLayout:
                        size_hint_y: 0.1
                        MDLabel:
                            bg_color: (0,0,0)
                            size_hint: (1,1)
                            id: real_time_update_2
                            font_name: 'Hack-Regular'
                            padding: (20,0)
                            text: '0'
                            multiline: True
                            halign: 'center'
                            
                        MDRaisedButton:
                            id: do_it
                            text: 'Do it!'
                            md_bg_color: app.theme_cls.accent_color
                            background_palette: 'Red' 
                            pos_hint: {'right' : 0.8}
  
                        
"""

class mainapp(BoxLayout):
    def __init__(self,**kwargs):
        BoxLayout.__init__(self,**kwargs)
        self.orientation= "vertical"
        self.numpad= Builder.load_string(calc)
        self.add_widget(self.numpad)

        #Buttons
        self.out = self.numpad.ids['out']
        self.rout = self.numpad.ids['real_time_update']
        self.rout_2 = self.numpad.ids['real_time_update_2']
        self.delbutton = self.numpad.ids['cancel_but']
        self.equalbutton = self.numpad.ids['equal_but']
        self.differnbutton = self.numpad.ids['differentiate']
        self.integrabutton = self.numpad.ids['integrate']
        self.simplifybutton = self.numpad.ids['simplify']
        self.factorisebutton = self.numpad.ids['factorise']
        self.expandbutton = self.numpad.ids['expand']
        self.fractog = self.numpad.ids['fractog']
        self.solvebutton = self.numpad.ids['solve']



        #Binds
        self.delbutton.bind(on_release=self.delholdclr, on_press=self.delbut)
        self.equalbutton.bind(on_release=self.equal_call)
        self.differnbutton.bind(on_release = self.differentiate)
        self.integrabutton.bind(on_release = self.integral)
        self.simplifybutton.bind(on_release = self.simplify)
        self.factorisebutton.bind(on_release = self.factorise)
        self.expandbutton.bind(on_release = self.expand)
        self.out.bind(text = self.rout_update)
        self.rout_2.bind(text = self.rout_update)
        self.fractog.bind(active=self.rout_update)
        self.solvebutton.bind(on_release = self.solver)

        #Clock
        Clock.schedule_interval(self.outputloop, 0)

        # Coloring
        self.numpad.ids['arrow'].md_bg_color = (0.1,0,0,0.1)

        for x in self.numpad.ids['basic_buts'].children:
            x.md_bg_color = (1,0,0,0.2)

        for x in self.numpad.ids['functions_but'].children:
            x.md_bg_color = (0.1,0,0,0.2)

        self.numpad.ids['inv'].md_bg_color = (0,0.5,0.5,0.2)

        for x in self.numpad.ids['inv_tri'].children:
            x.md_bg_color = (0,0.5,0.5,0.2)

        self.numpad.ids['back'].md_bg_color = (0.1,0,0,0.2)

        # init() of matrix
        self.mat_init()

        # init() of limit
        self.limit_init()

        # extras
        self.pretex = '..'
        self.expr = 0
    def outputloop(self,dt):
        tex = self.out.text
        if tex == '':
            tex = '0'

        elif len(tex) > 1 and tex[:1] == '0':
            tex = tex[1:]
        self.out.text = tex


    def delbut(self,ins):
        tex=self.out.text
        tex=tex[:-1]
        self.out.text=tex
        Clock.schedule_once(self.clearall,1)

    def clearall(self,ins):
        self.out.text='0'

    def delholdclr(self,ins):
        Clock.unschedule(self.clearall)

    def equal_call(self, ins, out = None):
        if out == None:
            self.ou = self.out
        else:
            self.ou = out
        special_expr = False
        final_expr_str = self.out.text.replace('^', '**')
        try:
            expr = sympy.N(parse_expr(final_expr_str, transformations=transformations))
            try:
                expr = float(expr)
            except:
                pass


            if expr != expr.doit():
                self.out.text = str(expr.doit())
                spx = str(expr)+" = "+str(expr.doit())
                special_expr = 'Eq('+str(expr)+', '+str(expr.doit())+')'
                if sympy.sympify(special_expr) == True:
                    special_expr = False
                print("special expr",special_expr)
                self.out.text = str(expr.doit())
            self.expr = expr
        except Exception as e:
            print(e)
            expr = final_expr_str
        try:
            tex = str(eval(str(expr)))
        except:
            tex = expr
        if out == None:
            self.ou.text = str(tex).replace('**','^')
        else:
            self.ou.text = str(tex)
            if special_expr:
                self.ou.text = special_expr
        self.out.text = self.out.text.replace('**','^')


    def equalcall_old(self,ins, out = None):
        try:
            expr = N(parse_expr(self.out.text, transformations = transformations, evaluate = True))
            tex = str(expr)
            self.out.text = tex
        except:
            pass
    def rout_update(self,*args):
        exprg=self.expgen()
        if exprg!=False:
            newtext=sympy.pretty(self.expgen())
            self.rout.text=newtext

    def differentiate(self, ins):
        try:
            expr = self.expgen()
            diff_expr = diff(expr, x)
            self.finaloutstr(diff_expr)

        except Exception as e:
            print(e)

    def integral(self, ins):
        try:
            expr = self.expgen()
            int_expr = integrate(expr, x)
            self.finaloutstr(int_expr)

        except Exception as e:
            print(e)

    def simplify(self, ins):
        try:
            expr = self.expgen()
            simplified_expr = simplify(expr)
            self.finaloutstr(simplified_expr)

        except Exception as e:
            print(e)

    def factorise(self, ins):
        try:
            expr = self.expgen()
            simplified_expr = sympy.factor(expr)
            self.finaloutstr(simplified_expr)

        except Exception as e:
            print(e)

    def expand(self, ins):
        try:
            expr = self.expgen()
            expand_expr = sympy.expand(expr)
            self.finaloutstr(expand_expr)

        except Exception as e:
            print(e)
            print(self.rout.text)

    def expgen(self):
        try:
            final_expr_str = self.out.text.replace('^', '**')
            if  not self.fractog.active:
                expr = N(parse_expr(final_expr_str, transformations = transformations))
            else:
                expr = (parse_expr(final_expr_str, transformations = transformations))

            print("Generated Expr ",expr)
            return expr

        except Exception as e:
            print("Expression generated Error! \n",e)
            return False
    def finaloutstr(self, expr):
        tmps = str(expr)
        tmps.replace('**', '^').replace('(pi/180)', u'\u00b0')
        print(tmps)
        self.out.text = tmps
        self.equalcall(None)

    def solver(self, *args):
        try:
            expr = self.expgen()
            Logger.info(expr)
            eq = sympy.Eq(expr, 0, evaluate = False)
            finalcc = '\n\nExpression : \n' + sympy.pretty(eq)

            for symbol in list(expr.atoms(sympy.Symbol)):
                Logger.info(symbol)
                os.environ['dbg'] = '1'

                solved = sympy.solveset(eq, symbol)
                os.environ['dbg'] = '0'

                Logger.info(solved)
                solved_pretty = sympy.pretty(solved, use_unicode = True, num_columns = 4000)
                top_content = '\n \n Solution for ' + str(symbol) + ':\n\n'
                finalc = (top_content + solved_pretty)
                try:
                    finalc.encode('utf-8')
                except:
                    pass
                finally:
                    print(finalc)
                print('creating button')
                finalcc += finalc
            self.make_dialog('Solve', finalcc)
            print('button created')

        except Exception as e:
            print(e)

    def make_dialog(self, title, finalc):
        content = Button(text = finalc, padding = (0,0), font_name = 'Hack-Regular', halign = 'left', size_hint = (None, None),
                         color = [0,0,0,1], background_normal = './transparent.png', background_down = './transparent.png')
        content.bind(size = lambda x, y: Logger.info(y))
        content.bind(texture_size = lambda obj, t: content.setter('size')(obj, t))
        bx = ScrollView(size_hint = (1,None), size = (Window.width * 0.7, Window.height * 0.6))
        bx.add_widget(content)
        bx.bind(size = lambda obj, x: Logger.info(x))
        self.dialog = MDDialog(title = title, content = bx, size_hint = (0.8,0.8))
        self.dialog.add_action_button('Dismiss', lambda *args: self.dialog.dismiss())
        self.dialog.open()

    ## MATRIX

    def mat_init(self):
        self.rows = self.numpad.ids['row']
        self.rows_2 = self.numpad.ids['row2']
        self.columns = self.numpad.ids['col']
        self.columns_2 = self.numpad.ids['col2']
        self.matrixgrid = self.numpad.ids['matrix_grid']
        self.matrixgrid2 = self.numpad.ids['matrix_grid_2']
        self.rrefbut = self.numpad.ids['rref']
        self.matrixmenu = self.numpad.ids['Matrix_menu']


        self.rrefbut.bind(on_release = self.rref_call)
        self.rows.bind(on_release = self.matup1)
        self.columns.bind(on_release = self.matup1)
        self.rows_2.bind(on_release = self.matup2)
        self.columns_2.bind(on_release = self.matup2)
        self.matupdate(1)
        self.matupdate(no = 2)

        self.matrixgrid.bind(minimum_height = self.matrixgrid.setter('height'))
        self.matrixgrid2.bind(minimum_height = self.matrixgrid2.setter('height'))

        self.matrix1 = self.matrix2 = None

    def matup1(self, *args):
        self.matupdate(1)

    def matup2(self, *args):
        self.matupdate(no = 2)

    def matupdate(self, no, *args):
        try:
            if no == 1:
                self.matrixgrid.cols = int(self.columns.text)
                self.matgridform(rows = int(self.rows.text), cols = int(self.columns.text), matgrid = self.matrixgrid)

            elif no == 2:
                self.matrixgrid2.cols = int(self.columns_2.text)
                self.matgridform(rows = int(self.rows_2.text), cols = int(self.columns_2.text), matgrid = self.matrixgrid2)

        except:
            pass

    def matgridform(self, rows, cols, matgrid):
        try:
            if len(matgrid.children) > rows * cols:
                for x in range((len(matgrid.children)) - rows * cols):
                    matgrid.remove_widget(matgrid.children[-1])

            else:
                for x in range(rows * cols - (len(matgrid.children))):
                    matgrid.add_widget(self.matblock())

        except Exception as e:
            print(e)

    def matblock(self):
        b = MDTextField(text = '0', hint_text = '0', padding_x = 20)
        b.bind(text = self.checktext)

        return b

    def checktext(self, obj, text):
        if text == '':
            obj.text = '0'

        elif len(text) > 1 and text[:1] == '0':
            obj.text = text[1:]

    def make_matrix(self, cols, matgrid, mat):
        try:
            mat_list = []
            tmpl = []
            for x in matgrid.children:
                print(x.text)
                tmpl.append(parse_expr(str(x.text), transformations = transformations))
            tmpl = tmpl[::-1]
            Logger.info(tmpl)
            try:
                mat_list = [tmpl[i:i  + cols] for i in xrange(0, len(tmpl), cols)]
                print(mat_list)

            except:
                mat_list = [tmpl[i:i + cols] for  i in range(0, len(tmpl), cols)]
                print(mat_list)

            mat = sympy.Matrix(mat_list)
            Logger.info(mat_list)
            print(mat_list)
            return mat

        except Exception as e:
            Logger.error(e)
            print(e)
            return False

    def rref_call(self, matno = 1, *args):
        if matno == 2:
            matrix = self.matrix2
            matgrid = self.matrixgrid2
            cols = int(self.columns_2.text)

        else:
            matrix = self.matrix1
            matgrid = self.matrixgrid
            cols = int(self.columns.text)

        for x in matgrid.children:
            print(x.text)

        matrix = self.make_matrix(cols = cols, matgrid = matgrid, mat = matrix)
        print(matrix)
        if matrix == None or matrix == False:
            return

        rref = matrix.rref()[0]
        count = 0
        for x in matgrid.children:
            count -= 1
            x.text = str(rref[count])

        self.make_dialog(title = 'RREF', finalc = sympy.pretty(sympy.Eq(matrix, rref, evaluate = False), use_unicode = True))

    ## LIMIT

    def limit_init(self):
        self.func = self.numpad.ids['f(x)']
        self.x0 = self.numpad.ids['X0']
        self.Sign = self.numpad.ids['sign']
        self.doit = self.numpad.ids['do_it']

        # Binds
        




class Calculator(App):
    theme_cls=ThemeManager()
    def build(self):
        return mainapp()

if __name__=="__main__":
    Calculator().run()
