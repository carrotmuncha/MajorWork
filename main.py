import sqlite3  # Importing the sqlite3 library for database operations

from kivy.core.window import Window  # Importing the Window module from Kivy for window-related operations

from kivy.lang import Builder  # Importing the Builder module from Kivy for loading UI definitions

from kivy.properties import StringProperty,  NumericProperty  # Importing property types from Kivy

from kivy.uix.screenmanager import Screen  # Importing the Screen class from Kivy for managing screens
from kivy.uix.label import Label
from kivymd.uix.boxlayout import MDBoxLayout

from kivymd.app import MDApp  # Importing the MDApp class from KivyMD for creating the application
from kivymd.uix.button import MDFlatButton  # Importing the MDFlatButton class from KivyMD for creating flat buttons
from kivymd.uix.dialog import MDDialog  # Importing the MDDialog class from KivyMD for creating dialogs

KV = '''
# Kivy language string defining the UI layout

# The screen manager to alternate between screens
ScreenManager:
    LoginScreen:
    RegisterScreen:
    AdminScreen:
    UserScreen:
    CarSizeScreen:
    DetailsScreen:
    LeaseTermScreen:
    ExtrasScreen
    LeaseCalculatorScreen:
    LeaseHistoryScreen:
    HelpScreen:
    
#The code to define the Login Screen
<LoginScreen>:
    # Definition of the LoginScreen class
    name: 'login'

    # Username input field
    MDTextField:
        id: username
        hint_text: 'Username'
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        size_hint_x: None
        width: 300

    # Password input field
    MDTextField:
        id: password
        hint_text: 'Password'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint_x: None
        width: 300
        password: True

    # Login button
    MDRoundFlatIconButton:
        icon: 'login'
        text: 'Login'
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        on_release: app.login(username.text, password.text)
            
    # Register button
    MDRoundFlatIconButton:
        icon: 'plus-circle-outline'
        text: 'Enrol'
        pos_hint: {'center_x': 0.5, 'center_y': 0.32}
        on_release: root.manager.current = 'register'

#The code to define the Register Screen
<RegisterScreen>:
    # Definition of the RegisterScreen class
    name: 'register'

    # Username input field
    MDTextField:
        id: reg_username
        hint_text: 'Enter a Username:'
        max_text_length: 24
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        size_hint_x: None
        width: 300

    # Password input field
    MDTextField:
        id: reg_password
        hint_text: 'Enter a password:'
        max_text_length: 16
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint_x: None
        width: 300
        password: True

    # Register button
    MDRoundFlatIconButton:
        text: 'Register'
        icon: 'account-plus'
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        on_release: app.register(reg_username.text, reg_password.text)

    # Back to Login button
    MDRoundFlatIconButton:
        text: 'Back to Login'
        icon: 'keyboard-return'
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        on_release: root.manager.current = 'login'

#The code to define the Admin Screen
<AdminScreen>:
    # Definition of the AdminScreen class
    name: 'admin'

    # Welcome label
    MDLabel:
        text: 'Welcome, Admin!'
        halign: 'center'

    # Logout button
    MDFlatButton:
        text: 'Logout'
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        on_release: root.manager.current = 'login'

#The code to define the User (Home Page) Screen
<UserScreen>:
    # Definition of the UserScreen class
    name: 'user'

    # Top app bar layout
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'

        # Top app bar
        MDTopAppBar:
            title: "Easy Peasy Leasy"
            md_bg_color: app.theme_cls.primary_color  
            specific_text_color: 1, 1, 1, 1  # Set text color to white
            left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

        MDScreen:
            
            MDNavigationDrawer:
                id: nav_drawer
                radius: (0, 16, 16, 0)
    
                BoxLayout:
                    orientation: 'vertical'
    
                    # Header
                    MDLabel:
                        text: app.username
                        font_style: 'H6'
                        size_hint_y: None
                        height: self.texture_size[1]
                        padding_y: '15dp'
    
                    # Menu options
                    ScrollView:
                        MDList:
                            OneLineAvatarListItem:
                                on_press:
                                    nav_drawer.set_state("close")
                                    root.manager.current = 'help'
                                text: 'Help'
                                IconLeftWidget:
                                    icon: 'help'
                                    on_press:
                                        nav_drawer.set_state("close")
                                        root.manager.current = 'help'
                                    
                            OneLineAvatarListItem:
                                on_press:
                                    nav_drawer.set_state("close")
                                    root.manager.current = 'lease_history'
                                text: 'Check Previous Leases'
                                IconLeftWidget:
                                    icon: 'history'
                                    on_press:
                                        nav_drawer.set_state("close")
                                        root.manager.current = 'lease_history'
                                    
                            OneLineAvatarListItem:
                                on_press:
                                    nav_drawer.set_state("close")
                                    app.logout()
                                text: 'Logout'
                                IconLeftWidget:
                                    icon: 'logout'
                                    on_press:
                                        nav_drawer.set_state("close")
                                        app.logout()
            
            MDSmartTile:
                radius: 24
                box_radius: [0, 0, 24, 24]
                box_color: 1, 1, 1, .2
                source: 'images/smalll.jpeg'
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: None, None
                size: "320dp", "320dp"
                on_release: root.manager.current = 'car_size'
        
                MDIconButton:
                    icon: "plus"
                    theme_icon_color: "Custom"
                    icon_color: 1, 0, 0, 1
                    pos_hint: {"center_y": .5}
                    on_release: root.manager.current = 'car_size'
        
                MDLabel:
                    text: "Create New Lease"
                    bold: True
                    color: 0, 0, 0, 1
                
<CarSizeScreen>:
    name: 'car_size'
    # Top app bar layout
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'

        # Top app bar
        MDTopAppBar:
            title: "Car Size"
            md_bg_color: app.theme_cls.primary_color  
            specific_text_color: 1, 1, 1, 1  # Set text color to white
            left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

        MDScreen:
            
            MDNavigationDrawer:
                id: nav_drawer
    
                BoxLayout:
                    orientation: 'vertical'
    
                    # Header
                    MDLabel:
                        text: app.username
                        font_style: 'H6'
                        size_hint_y: None
                        height: self.texture_size[1]
                        padding_y: '15dp'
    
                    # Menu options
                    MDScrollView:
                    
                        MDList:
                        
                            OneLineAvatarListItem:
                                on_press:
                                    nav_drawer.set_state("close")
                                    root.manager.current = 'user'
                                text: 'Home'
                                IconLeftWidget:
                                    icon: 'home'
                                    on_press:
                                        nav_drawer.set_state("close")
                                        root.manager.current = 'user'
                                    
                            OneLineAvatarListItem:
                                on_press:
                                    nav_drawer.set_state("close")
                                    root.manager.current = 'help'
                                text: 'Help'
                                IconLeftWidget:
                                    icon: 'help'
                                    on_press:
                                        nav_drawer.set_state("close")
                                        root.manager.current = 'help'
        
    MDBoxLayout:
        orientation: 'horizontal'
        spacing: dp(10)
        
        MDScreen:
                
            MDSmartTile:
                radius: 24
                box_radius: [0, 0, 24, 24]
                box_color: 0.5, 0.5, 0.5, 0.1
                source: 'images/vehicle-2.png'
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: None, None
                size: "250dp", "250dp"
                car_size_factor: 1.3
                on_press: root.car_size_factor = self.car_size_factor
                on_release: root.manager.current = 'details'
        
                MDIconButton:
                    icon: "car-hatchback"
                    theme_icon_color: "Custom"
                    icon_color: 0, 0, 0, 1
                    pos_hint: {"center_y": .5}
                    on_press: root.car_size_factor = self.car_size_factor
                    on_release: root.manager.current = 'details'
                    
                MDLabel:
                    text: "Small"
                    bold: True
                    color: 0, 0, 0, 1
    
        MDScreen:
                
            MDSmartTile:
                radius: 24
                box_radius: [0, 0, 24, 24]
                box_color: 0.5, 0.5, 0.5, 0.1
                source: 'images/vehicle-3.png'
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: None, None
                size: "250dp", "250dp"
                car_size_factor: 1.5
                on_press: root.car_size_factor = self.car_size_factor
                on_release: root.manager.current = 'details'
        
                MDIconButton:
                    icon: "car-convertible"
                    theme_icon_color: "Custom"
                    icon_color: 0, 0, 0, 1
                    pos_hint: {"center_y": .5}
                    on_press: root.car_size_factor = self.car_size_factor
                    on_release: root.manager.current = 'details'
                    
                MDLabel:
                    text: "Medium"
                    bold: True
                    color: 0, 0, 0, 1
    
        MDScreen:
        
            MDSmartTile:
                radius: 24
                box_radius: [0, 0, 24, 24]
                box_color: 0.5, 0.5, 0.5, 0.1
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: None, None
                size: "250dp", "250dp"
                source: 'images/vehicle-8.png'
                car_size_factor: 1.7
                on_press: root.car_size_factor = self.car_size_factor
                on_release: root.manager.current = 'details'
        
                MDIconButton:
                    icon: "car-estate"
                    theme_icon_color: "Custom"
                    icon_color: 0, 0, 0, 1
                    pos_hint: {"center_y": .5}
                    on_press: root.car_size_factor = self.car_size_factor
                    on_release: root.manager.current = 'details'
                    
                MDLabel:
                    text: "Large"
                    bold: True
                    color: 0, 0, 0, 1


<DetailsScreen>:
    name: 'details'
    
     # Top app bar layout
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'

        # Top app bar
        MDTopAppBar:
            title: "Details"
            md_bg_color: app.theme_cls.primary_color  
            specific_text_color: 1, 1, 1, 1  # Set text color to white
            left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

        MDScreen:
            
            MDNavigationDrawer:
                id: nav_drawer
    
                BoxLayout:
                    orientation: 'vertical'
    
                    # Header
                    MDLabel:
                        text: app.username
                        font_style: 'H6'
                        size_hint_y: None
                        height: self.texture_size[1]
                        padding_y: '15dp'
    
                    # Menu options
                    MDScrollView:
                    
                        MDList:
                        
                            OneLineAvatarListItem:
                                on_press:
                                    nav_drawer.set_state("close")
                                    root.manager.current = 'user'
                                text: 'Home'
                                IconLeftWidget:
                                    icon: 'home'
                                    on_press:
                                        nav_drawer.set_state("close")
                                        root.manager.current = 'user'
                                    
                            OneLineAvatarListItem:
                                on_press:
                                    nav_drawer.set_state("close")
                                    root.manager.current = 'help'
                                text: 'Help'
                                IconLeftWidget:
                                    icon: 'help'
                                    on_press:
                                        nav_drawer.set_state("close")
                                        root.manager.current = 'help'

    # Salary label
    MDLabel:
        text: f'Total Taxable Income: ${int(salary_slider.value)}'
        theme_text_color: 'Primary'
        size_hint_y: None
        height: '48dp'
        pos_hint: {'center_x': 0.52, 'center_y': 0.85}
        font_style: 'Button'

    # Salary slider
    MDSlider:
        id: salary_slider
        min: 18000
        max: 1000000
        step: 1
        value: 90000
        orientation: 'horizontal'
        size_hint_y: None
        height: '48dp'
        pos_hint: {'center_x': 0.5, 'center_y': 0.75}
        hint: True
        hint_bg_color: "white"
        hint_text_color: "black"

    # Driveaway Car Price label
    MDLabel:
        text: f'Driveaway Car Price: ${int(car_price_slider.value)}'
        theme_text_color: 'Primary'
        size_hint_y: None
        height: '48dp'
        pos_hint: {'center_x': 0.52, 'center_y': 0.55}
        font_style: 'Button'

    # Driveaway Car Price slider
    MDSlider:
        id: car_price_slider
        min: 10000
        max: 200000
        step: 100
        value: 70000
        orientation: 'horizontal'
        size_hint_y: None
        height: '48dp'
        pos_hint: {'center_x': 0.5, 'center_y': 0.45 }
        hint: True
        hint_bg_color: "white"
        hint_text_color: "black"

    # Annual KMs label
    MDLabel:
        text: f'Avg. Annual KMs: {int(annual_kms_slider.value)} km'
        theme_text_color: 'Primary'
        size_hint_y: None
        height: '48dp'
        pos_hint: {'center_x': 0.52, 'center_y': 0.25}
        font_style: 'Button'

    # Annual KMs slider
    MDSlider:
        id: annual_kms_slider
        min: 0
        max: 50000
        step: 10
        value: 15000
        orientation: 'horizontal'
        size_hint_y: None
        height: '48dp'
        pos_hint: {'center_x': 0.5, 'center_y': 0.15}
        hint: True
        hint_bg_color: "white"
        hint_text_color: "black"
                
    MDRoundFlatIconButton:
        text: "Next -> Lease Term"
        icon: "format-list-numbered"
        text_color: "black"
        pos_hint: {'center_x': 0.5, 'center_y': 0.05}
        on_release: root.manager.current = 'lease_term'
        

<LeaseTermScreen>:
    name: 'lease_term'
    
    MDBoxLayout:
        orientation: 'vertical'

        # Top app bar
        MDTopAppBar:
            title: "Lease Term and Frequency"
            md_bg_color: app.theme_cls.primary_color  
            specific_text_color: 1, 1, 1, 1  # Set text color to white
            left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

        MDScreen:
            
            MDNavigationDrawer:
                id: nav_drawer
    
                BoxLayout:
                    orientation: 'vertical'
    
                    # Header
                    MDLabel:
                        text: app.username
                        font_style: 'H6'
                        size_hint_y: None
                        height: self.texture_size[1]
                        padding_y: '15dp'
    
                    # Menu options
                    ScrollView:
                    
                        MDList:
                        
                            OneLineAvatarListItem:
                                on_press:
                                    nav_drawer.set_state("close")
                                    root.manager.current = 'user'
                                text: 'Home'
                                IconLeftWidget:
                                    icon: 'home'
                                    on_press:
                                        nav_drawer.set_state("close")
                                        root.manager.current = 'user'
                                    
                            OneLineAvatarListItem:
                                on_press:
                                    nav_drawer.set_state("close")
                                    root.manager.current = 'help'
                                text: 'Help'
                                IconLeftWidget:
                                    icon: 'help'
                                    on_press:
                                        nav_drawer.set_state("close")
                                        root.manager.current = 'help'

    # Lease Term label
    MDLabel:
        text: f'Term Length: {int(term_slider.value)} years'
        theme_text_color: 'Primary'
        size_hint_y: None
        height: '48dp'
        pos_hint: {'center_x': 0.52, 'center_y': 0.675}
        font_style: 'Button'

    # Salary slider
    MDSlider:
        id: term_slider
        min: 1
        max: 5
        step: 1
        value: 3
        orientation: 'horizontal'
        size_hint_y: None
        height: '48dp'
        pos_hint: {'center_x': 0.5, 'center_y': 0.60}
        hint: True
        hint_bg_color: "white"
        hint_text_color: "black"
    
    MDFloatLayout:
        
        MDLabel:
            text: "Bi-Monthly"
            theme_text_color: 'Primary'
            size_hint_y: None
            height: '48dp'
            pos_hint: {'center_x': 0.847, 'center_y': 0.37}
            font_style: 'Button'
            
        Check:
            active: True
            pos_hint: {'center_x': 0.4, 'center_y': 0.30}
    
        MDLabel:
            text: "Monthly"
            theme_text_color: 'Primary'
            size_hint_y: None
            height: '48dp'
            pos_hint: {'center_x': 1.065, 'center_y': 0.37}
            font_style: 'Button'
    
        Check:
            pos_hint: {'center_x': 0.6, 'center_y': .30}
    
    MDRoundFlatIconButton:
        text: "Next -> Add-Ons"
        icon: "basket-plus-outline"
        text_color: "black"
        pos_hint: {'center_x': 0.5, 'center_y': 0.05}
        on_release:
            root.manager.current = 'extras'
        

<ExtrasScreen>:
    name: 'extras'
    
    MDBoxLayout:
        orientation: 'vertical'

        # Top app bar
        MDTopAppBar:
            title: "Add-Ons"
            md_bg_color: app.theme_cls.primary_color  
            specific_text_color: 1, 1, 1, 1  # Set text color to white
            left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

        MDScreen:
            
            MDNavigationDrawer:
                id: nav_drawer
    
                BoxLayout:
                    orientation: 'vertical'
    
                    # Header
                    MDLabel:
                        text: app.username
                        font_style: 'H6'
                        size_hint_y: None
                        height: self.texture_size[1]
                        padding_y: '15dp'
    
                    # Menu options
                    ScrollView:
                    
                        MDList:
                        
                            OneLineAvatarListItem:
                                on_press:
                                    nav_drawer.set_state("close")
                                    root.manager.current = 'user'
                                text: 'Home'
                                IconLeftWidget:
                                    icon: 'home'
                                    on_press:
                                        nav_drawer.set_state("close")
                                        root.manager.current = 'user'
                                    
                            OneLineAvatarListItem:
                                on_press:
                                    nav_drawer.set_state("close")
                                    root.manager.current = 'help'
                                text: 'Help'
                                IconLeftWidget:
                                    icon: 'help'
                                    on_press:
                                        nav_drawer.set_state("close")
                                        root.manager.current = 'help'
                                        
            
        MDBoxLayout:
            orientation: "horizontal"
            padding: "100dp"

            MDLabel:
                text: "Fuel"
                theme_text_color: 'Primary'
                size_hint_y: None
                height: '48dp'

            MDSwitch:
                id: fuel_switch
                icon_active: "check"
                icon_active_color: "white"

        MDBoxLayout:
            orientation: "horizontal"
            padding: "100dp"

            MDLabel:
                text: "Tyres"
                theme_text_color: 'Primary'
                size_hint_y: None
                height: '48dp'

            MDSwitch:
                id: tyres_switch
                icon_active: "check"
                icon_active_color: "white"

        MDBoxLayout:
            orientation: "horizontal"
            padding: "100dp"

            MDLabel:
                text: "Registration"
                theme_text_color: 'Primary'
                size_hint_y: None
                height: '48dp'

            MDSwitch:
                id: registration_switch
                icon_active: "check"
                icon_active_color: "white"

        MDBoxLayout:
            orientation: "horizontal"
            padding: "100dp"

            MDLabel:
                text: "Maintenance"
                theme_text_color: 'Primary'
                size_hint_y: None
                height: '48dp'

            MDSwitch:
                id: maintenance_switch
                icon_active: "check"
                icon_active_color: "white"

        MDBoxLayout:
            orientation: "horizontal"
            padding: "100dp"

            MDLabel:
                text: "Roadside Assist"
                theme_text_color: 'Primary'
                size_hint_y: None
                height: '48dp'

            MDSwitch:
                id: roadside_assist_switch
                icon_active: "check"
                icon_active_color: "white"
    
    MDRoundFlatIconButton:
        text: "Next -> Summary"
        icon: "file-document-multiple-outline"
        text_color: "black"
        pos_hint: {'center_x': 0.5, 'center_y': 0.05}
        on_release: root.manager.current = 'lease_calculator'
    
    
#The code to define the Calculator Screen
<LeaseCalculatorScreen>:
    # Definition of the LeaseCalculatorScreen class
    name: 'lease_calculator'
    
    MDBoxLayout:
        orientation: 'vertical'

        # Top app bar
        MDTopAppBar:
            title: "Summary"
            md_bg_color: app.theme_cls.primary_color  
            specific_text_color: 1, 1, 1, 1  # Set text color to white
            left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

        MDScreen:
            
            MDNavigationDrawer:
                id: nav_drawer
    
                BoxLayout:
                    orientation: 'vertical'
    
                    # Header
                    MDLabel:
                        text: app.username
                        font_style: 'H6'
                        size_hint_y: None
                        height: self.texture_size[1]
                        padding_y: '15dp'
    
                    # Menu options
                    ScrollView:
                    
                        MDList:
                        
                            OneLineAvatarListItem:
                                on_press:
                                    nav_drawer.set_state("close")
                                    root.manager.current = 'user'
                                text: 'Home'
                                IconLeftWidget:
                                    icon: 'home'
                                    on_press:
                                        nav_drawer.set_state("close")
                                        root.manager.current = 'user'
                                    
                            OneLineAvatarListItem:
                                on_press:
                                    nav_drawer.set_state("close")
                                    root.manager.current = 'help'
                                text: 'Help'
                                IconLeftWidget:
                                    icon: 'help'
                                    on_press:
                                        nav_drawer.set_state("close")
                                        root.manager.current = 'help'
                                        
        # Calculate Lease button
        MDRaisedButton:
            text: 'Calculate Lease'
            pos_hint: {'center_x': 0.5}
            on_release: app.on_calculate_lease()


# The code to define Lease History screen
<LeaseHistoryScreen>:
    name: 'lease_history'
    # Top app bar layout
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'

        # Top app bar
        MDTopAppBar:
            title: "Previous Leases"
            md_bg_color: app.theme_cls.primary_color  
            specific_text_color: 1, 1, 1, 1  # Set text color to white
            left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

        MDScreen:
            
            MDNavigationDrawer:
                id: nav_drawer
    
                BoxLayout:
                    orientation: 'vertical'
    
                    # Header
                    MDLabel:
                        text: app.username
                        font_style: 'H6'
                        size_hint_y: None
                        height: self.texture_size[1]
                        padding_y: '15dp'
    
                    # Menu options
                    ScrollView:
                    
                        MDList:
                        
                            OneLineAvatarListItem:
                                on_press:
                                    nav_drawer.set_state("close")
                                    root.manager.current = 'user'
                                text: 'Home'
                                IconLeftWidget:
                                    icon: 'home'
                                    on_press:
                                        nav_drawer.set_state("close")
                                        root.manager.current = 'user'
                                    
                            OneLineAvatarListItem:
                                on_press:
                                    nav_drawer.set_state("close")
                                    root.manager.current = 'help'
                                text: 'Help'
                                IconLeftWidget:
                                    icon: 'help'
                                    on_press:
                                        nav_drawer.set_state("close")
                                        root.manager.current = 'help'
       
<HelpScreen>:
    name: 'help'
    
    # The code to define Lease History screen
<LeaseHistoryScreen>:
    name: 'lease_history'
    # Top app bar layout
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'

        # Top app bar
        MDTopAppBar:
            title: "Previous Leases"
            md_bg_color: app.theme_cls.primary_color  
            specific_text_color: 1, 1, 1, 1  # Set text color to white
            left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

        MDScreen:
            
            MDNavigationDrawer:
                id: nav_drawer
    
                BoxLayout:
                    orientation: 'vertical'
    
                    # Header
                    MDLabel:
                        text: app.username
                        font_style: 'H6'
                        size_hint_y: None
                        height: self.texture_size[1]
                        padding_y: '15dp'
    
                    # Menu options
                    ScrollView:
                    
                        MDList:
                        
                            OneLineAvatarListItem:
                                on_press:
                                    nav_drawer.set_state("close")
                                    root.manager.current = 'user'
                                text: 'Home'
                                IconLeftWidget:
                                    icon: 'home'
                                    on_press:
                                        nav_drawer.set_state("close")
                                        root.manager.current = 'user'
    MDLabel:
        text: ""
     
<CheckItem>
    adaptive_height: True

    MDCheckbox:
        size_hint: None, None
        size: "48dp", "48dp"
        group: root.group

    MDLabel:
        text: root.text
        adaptive_height: True
        theme_text_color: "Custom"
        text_color: "#B2B6AE"
        pos_hint: {"center_y": .5}
        
<Check@MDCheckbox>:
    group: 'group'
    size_hint: None, None
    size: dp(48), dp(48)
'''

# Screen classes


class LoginScreen(Screen):
    pass


class RegisterScreen(Screen):
    pass


class AdminScreen(Screen):
    pass


class CarSizeScreen(Screen):
    pass


class DetailsScreen(Screen):
    pass


class LeaseTermScreen(Screen):
    pass


class ExtrasScreen(Screen):
    pass


class LeaseHistoryScreen(Screen):
    pass


class UserScreen(Screen):
    pass


class HelpScreen(Screen):
    pass


class LeaseCalculatorScreen(Screen):
    car_size = StringProperty('')
    car_size_factor = 1


class CheckItem(MDBoxLayout):
    text = StringProperty()
    group = StringProperty()


# Initialize the database
def init_database():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Create the 'users' table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (username TEXT PRIMARY KEY NOT NULL, password TEXT NOT NULL);''')
    # Create the 'lease' table if it doesn't exist
    # Create the 'lease' table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS leases
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      username TEXT NOT NULL, 
                      car_size TEXT, 
                      cost REAL, 
                      incidentals TEXT, 
                      lease_term INT, 
                      frequency TEXT,
                      timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL);''')
    conn.commit()
    conn.close()


def insert_lease(username, car_size, cost, incidentals, lease_term, frequency):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO leases (username, car_size, cost, incidentals, lease_term, frequency) VALUES (?, ?, ?, ?, ?, ?)",
                   (username, car_size, cost, incidentals, lease_term, frequency))
    conn.commit()
    conn.close()


# Validate the user credentials
def validate_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Check if the username and password match the records in the 'users' table
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        return True
    else:
        return False


# Show an alert dialog
def show_alert_dialog(message):
    dialog = MDDialog(
        title="Notice",
        text=message,
        size_hint=(0.8, 1),
        buttons=[
            MDFlatButton(
                text="OK", on_release=lambda x: dialog.dismiss()
            ),
        ],
    )
    dialog.open()


# LeaseCalculator class for lease calculations
class LeaseCalculator:
    def __init__(self, car_price, annual_kms, lease_term, payment_frequency, car_size, salary, fuel, tyres, maintenance, registration, roadside_assist):
        self.car_price = car_price
        self.annual_kms = annual_kms
        self.lease_term = lease_term
        self.payment_frequency = payment_frequency
        self.car_size = car_size
        self.salary = salary
        self.fuel = fuel
        self.tyres = tyres
        self.maintenance = maintenance
        self.registration = registration
        self.roadside_assist = roadside_assist

    def calculate_extras(self, fuel, tyres, maintenance, car_size, annual_kms, lease_term):
        extras_cost = 0
        fuel = self.root.ids.fuel_switch.active
        tyres = self.root.ids.tyres_switch.active
        maintenance = self.root.ids.maintenance_switch.active
        registration = self.root.ids.registration_switch.active
        roadside_assist = self.root.ids.roadside_assist_switch.active

        # Define average cost of tyre by car size
        average_tyre_costs = {
            "small": 150,  # Example value for small car
            "medium": 200,  # Example value for medium car
            "large": 250  # Example value for large car
        }

        # Define average fuel usage in litres per 100kms by car size
        average_fuel_usage = {
            "small": 7,  # Example value for small car
            "medium": 10,  # Example value for medium car
            "large": 14  # Example value for large car
        }

        # Define average service cost by car size
        average_service_cost = {
            "small": 300,  # Example value for small car
            "medium": 400,  # Example value for medium car
            "large": 450  # Example value for large car
        }

        # Calculate fuel budget
        if fuel:
            fuel_budget = (average_fuel_usage[car_size] * (annual_kms / 100) * 2.0)
            extras_cost += fuel_budget

        # Calculate tyre budget
        if tyres:
            sets_of_tyres_required = (annual_kms * lease_term) / 35000
            cost_of_set = average_tyre_costs[car_size] * 4
            tyre_budget = (sets_of_tyres_required * cost_of_set) / lease_term
            extras_cost += tyre_budget

        # Calculate maintenance budget
        if maintenance:
            maintenance_budget = average_service_cost[car_size] * (annual_kms / 15000)
            extras_cost += maintenance_budget

        if registration:
            extras_cost += 100

        if roadside_assist:
            extras_cost += 100

        return extras_cost

    def calculate(self):
        # Residual Value based on lease term (in months)
        residual_percentages = {12: 65.63, 24: 56.25, 36: 46.88, 48: 37.5, 60: 28.13}
        residual_value = self.finance_amount * (residual_percentages[self.lease_term] / 100)
        extras_cost = self.calculate_extras(self.fuel, self.tyres, self.maintenance, self.car_size, self.annual_kms,
                                            self.lease_term)

        # Number of payments
        num_payments = 0
        if self.payment_frequency == "Monthly":
            num_payments = self.lease_term * 12
        elif self.payment_frequency == "Fortnightly":
            num_payments = self.lease_term * 26

        # Lease Payment
        lease_payment = ((self.finance_amount - residual_value + self.extras) / num_payments) + extras_cost / num_payments

        # Total lease cost
        total_lease_cost = lease_payment * num_payments + residual_value

        # Total tax savings
        total_tax_savings = self.calculate_tax_savings(lease_payment, num_payments)

        return lease_payment, total_lease_cost, total_tax_savings

    def calculate_tax_savings(self, lease_payment, num_payments):
        total_payment = lease_payment * num_payments
        taxable_income = self.salary - total_payment

        # Tax brackets
        tax_brackets = [
            (18200, 0, 0),
            (45000, 0.19, 18200),
            (120000, 0.325, 45000),
            (180000, 0.37, 120000),
            (float('inf'), 0.45, 180000)
        ]

        # Calculate tax
        tax = 0
        base_tax = [0, 5092, 29467, 51667]
        for i, bracket in enumerate(tax_brackets):
            if taxable_income <= bracket[0]:
                break
            additional_tax = (min(taxable_income, bracket[0]) - bracket[2]) * bracket[1]
            tax += additional_tax if i > 0 else 0
        if i > 0:
            tax += base_tax[i - 1]

        # Calculate tax on salary without lease payments
        original_tax = 0
        for i, bracket in enumerate(tax_brackets):
            if self.salary <= bracket[0]:
                break
            additional_tax = (min(self.salary, bracket[0]) - bracket[2]) * bracket[1]
            original_tax += additional_tax if i > 0 else 0
        if i > 0:
            original_tax += base_tax[i - 1]

        # Calculate tax savings
        tax_savings = original_tax - tax
        return tax_savings


# LeaseApp class for the main application
class LeaseApp(MDApp):
    payment_frequency = StringProperty("")
    username = StringProperty("")
    lease_term = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)
        init_database()  # Initialize the database when the app starts

    def logout(self):
        # Clear user data
        self.username = ""
        # Redirect to login screen
        self.root.current = 'login'

    def build(self):
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = "Light"

        Window.clearcolor = (1, 1, 1, 1)

        return self.screen

    # Login function for handling login logic
    def login(self, username, password):
        if username == 'admin' and password == 'admin':
            self.root.current = 'admin'
        elif validate_user(username, password):
            self.username = username
            self.root.current = 'user'
        else:
            show_alert_dialog("Invalid username or password")

    # Register function for handling user registration
    def register(self, username, password):
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            show_alert_dialog("Registration successful!")
            self.root.current = 'login'
        except sqlite3.IntegrityError:
            show_alert_dialog("Username already exists")
        finally:
            conn.close()

    # Set the car size factor
    def set_car_size_factor(self, factor):
        self.root.get_screen('lease_calculator').car_size_factor = factor

    # Set the lease term
    def set_lease_term(self, text_item):
        self.root.get_screen("lease_calculator").ids.lease_term_dropdown.text = text_item

    # Set the payment frequency
    def set_payment_frequency(self, text_item):
        self.payment_frequency = text_item

    # Event handler for calculating the lease
    def on_calculate_lease(self):
        username = self.username

        # Accessing the screens
        car_size_screen = self.root.get_screen('car_size')
        details_screen = self.root.get_screen('details')
        extras_screen = self.root.get_screen('extras')
        lease_calculator_screen = self.root.get_screen('lease_calculator')

        # Extracting information from sliders
        car_price = details_screen.ids.car_price_slider.value
        annual_kms = details_screen.ids.annual_kms_slider.value

        # Extracting information from extras screen
        include_fuel = extras_screen.ids.fuel_switch.active
        include_tyres = extras_screen.ids.tyres_switch.active
        include_maintenance = extras_screen.ids.maintenance_switch.active
        include_registration = extras_screen.ids.registration_switch.active
        include_roadside_assist = extras_screen.ids.roadside_assist_switch.active

        # Extracting lease term and payment frequency
        lease_term = lease_calculator_screen.ids.lease_term_dropdown.text
        payment_frequency = lease_calculator_screen.ids.payment_frequency.text  # assuming you have set ids for the checkboxes

        # Calculating the lease
        lease_payment = self.calculate_lease(
            car_price=car_price,
            annual_kms=annual_kms,
            lease_term=lease_term,
            payment_frequency=payment_frequency,
            include_fuel=include_fuel,
            include_tyres=include_tyres,
            include_maintenance=include_maintenance,
            include_registration=include_registration,
            include_roadside_assist=include_roadside_assist
        )

        # Updating the result label
        lease_calculator_screen.ids.result_label.text = (
            f"Lease payment: ${lease_payment:.2f}"
        )

        # Inserting the lease into the database
        insert_lease(username, car_size, lease_payment, 'No incidentals', lease_term, payment_frequency)

    # Function for checking previous leases
    def check_previous_leases(self, *args):
        self.update_lease_history(self.username)
        self.root.current = 'lease_history'

    def update_lease_history(self, username):
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM leases WHERE username = ?", (username,))
        leases = cursor.fetchall()

        lease_history_screen = self.root.get_screen('lease_history')
        lease_history_screen.ids.scroll.clear_widgets()

        for lease in leases:
            lease_info = f"Car Size: {lease[1]}, Cost: {lease[2]}, Incidentals: {lease[3]}, Lease Term: {lease[4]}, Frequency: {lease[5]}"
            lease_history_screen.ids.scroll.add_widget(Label(text=lease_info))

        conn.close()


# Run the app
if __name__ == '__main__':
    LeaseApp().run()
