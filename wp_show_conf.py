#!/usr/bin/env python

# example entry.py

import gtk
import gobject
import os




class wp_show_conf():
    
    def setit(self,widget,dummy):
        path = self.filechooserbutton.get_filename()
        timeout = self.spin_button.get_value_as_int()
        enabled = str(self.check.get_active()).lower()
        depth = self.depth_select.get_value_as_int()
        request='./install '+path+' '+str(timeout)+' '+enabled+' '+str(depth)
        os.system(request)

    def __init__(self):
        # create a new window
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_title("Gnome 3 Wallpaper Slideshow")
        window.connect("delete_event", lambda w,e: gtk.main_quit())

        vbox = gtk.VBox(False, 0)
        window.add(vbox)
        vbox.show()
        
        artwork = gtk.VBox()
        fileimage = 'artwork.png'
        image = gtk.Image()
        image.set_from_file(fileimage)
        artwork.pack_start(image, True, True, 0)
        vbox.pack_start(artwork,True,True,1)
        artwork.show()
        image.show()

        table = gtk.Table(3,2)
        table.set_border_width(5)
        vbox.pack_start(table,True,True,1)

        label = gtk.Label(' Path : ')
        label.set_alignment(0, 0.5)
        table.attach(label, 0, 1, 0, 1, gtk.FILL,gtk.FILL | gtk.EXPAND, 0, 0)
        label.show()

        self.filechooserbutton = gtk.FileChooserButton('Browse')
        self.filechooserbutton.set_current_folder('~/Pictures')
        self.filechooserbutton.set_tooltip_text('Browse to the folder containing your wallpapers')
        table.attach(self.filechooserbutton, 1, 2, 0, 1, gtk.FILL,gtk.FILL | gtk.EXPAND, 0, 0)
        self.filechooserbutton.set_action(gtk.FILE_CHOOSER_ACTION_SELECT_FOLDER)
        self.filechooserbutton.show()

        label = gtk.Label(' Timeout : ')
        label.set_alignment(0, 0.5)
        table.attach(label, 0, 1, 1, 2, gtk.FILL,gtk.FILL | gtk.EXPAND, 0, 0)
        label.show()

        adjustment = gtk.Adjustment(100,10,1000,5,10)
        self.spin_button = gtk.SpinButton(adjustment)
        self.spin_button.set_numeric(True)
        self.spin_button.set_tooltip_text('Time between Switch')
        table.attach(self.spin_button, 1, 2, 1, 2, gtk.FILL,gtk.FILL | gtk.EXPAND, 0, 0)
        self.spin_button.show()

        label = gtk.Label(' Depth : ')
        label.set_alignment(0, 0.5)
        table.attach(label, 0, 1, 2, 3, gtk.FILL,gtk.FILL | gtk.EXPAND, 0, 0)
        label.show()

        adjustment1 = gtk.Adjustment(3,1,10,1,1)
        self.depth_select = gtk.SpinButton(adjustment1)
        self.depth_select.set_numeric(True)
        self.depth_select.set_tooltip_text('Level to which the sub-folder must be scanned')
        table.attach(self.depth_select, 1, 2, 2, 3, gtk.FILL,gtk.FILL | gtk.EXPAND, 0, 0)
        self.depth_select.show()
        
        self.check = gtk.CheckButton("Enable")
        vbox.pack_start(self.check, False, True, 0)
        self.check.set_tooltip_text('Enable or disable the Slideshow')
        
        self.check.set_active(True)
        self.check.show()


        hbox = gtk.HBox(True)
        vbox.pack_end(hbox, False, True, 0)
        hbox.show()


        button = gtk.Button(stock=gtk.STOCK_CLOSE)
        button.connect("clicked", lambda w: gtk.main_quit())
        hbox.pack_start(button, False, True, 0)
        button.set_flags(gtk.CAN_DEFAULT)
        button.grab_default()
        button.show()

        button = gtk.Button(stock=gtk.STOCK_OK)
        button.connect("clicked", self.setit,None)
        hbox.pack_start(button, False, True, 0)
        button.show()

        table.show()
        window.show()


def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    wp_show_conf()
    main()
