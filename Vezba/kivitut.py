import kivy
try:
    kivy.require('1.9.0')
    from kivy.app import App
    from kivy.uix.button import Label

    class HelloKivy(App):
        def build(self):
            return Label(text="HelloWorld")

            hello = HelloKivy()
            hello.run()
        
except:
    print ("GUI IS TURNED ON")
